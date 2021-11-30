import serial.serialutil

from src.chafonrfid.base import CommandRunner, ReaderCommand
from src.chafonrfid.command import G2_TAG_INVENTORY
from src.chafonrfid.response import G2_TAG_INVENTORY_STATUS_MORE_FRAMES
from src.chafonrfid.transport_serial import SerialTransport
from src.chafonrfid.uhfreader18 import G2InventoryResponseFrame as G2InventoryResponseFrame18


class Chafonrfid(object):

    def __init__(self, device='/dev/ttyUSB0'):
        self.error = None
        self.device = device

    def open_port(self, ):
        try:
            result = SerialTransport(self.device)
        except serial.serialutil.SerialException:
            result = None
        return result

    def get_tid(self):
        get_inventory_uhfreader18 = ReaderCommand(G2_TAG_INVENTORY, data=[4, 2])

        transport = self.open_port()
        if transport is None:
            self.error = "olvasási hiba"
            return None

        runner = CommandRunner(transport)

        transport.write(get_inventory_uhfreader18.serialize())
        inventory_status = None
        while inventory_status is None or inventory_status == G2_TAG_INVENTORY_STATUS_MORE_FRAMES:
            g2_response = G2InventoryResponseFrame18(transport.read_frame())
            inventory_status = g2_response.result_status
            result = []
            for tag in g2_response.get_tag():
                result.append(tag.epc.hex())
        transport.close()
        if len(result) == 1:
            return result[0]
        elif len(result) > 1:
            self.error = "Több chip!"
            return None
        else:
            return None

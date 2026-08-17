from PyQt6.QtGui import QFont

from src.chafonrfid.Chafonrfid import Chafonrfid


class RfidReaderMixin:
    def _readTid(self, comm_port, set_status):
        chafonrfid = Chafonrfid(comm_port)
        rfid = chafonrfid.get_tid()
        if chafonrfid.error is not None:
            set_status(chafonrfid.error)
        else:
            set_status(None)
        return rfid


class ResizeFontMixin:
    def _resizeFont(self, divisor=40, default_size=14):
        width = self.rect().width() // divisor
        if width > default_size:
            return QFont('', width)
        return QFont('', default_size)

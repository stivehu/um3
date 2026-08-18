import atexit

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QFont

from src.chafonrfid.Chafonrfid import Chafonrfid

# ApplicationWindow.closeEvent a Python beépített exit()-jét hívja, ami a
# Qt-t megkerülve azonnal leállítja az interpretert -- ilyenkor egy még futó
# RfidReadWorker QThread-et a leállási sorrend "élve" érhet, és a Qt ezt
# végzetes hibaként ("QThread: Destroyed while thread is still running")
# abort()-tal bünteti. Az atexit garantáltan lefut a leállás előtt, itt
# várjuk meg a még futó worker(eke)t, függetlenül attól, hogy melyik ablak
# closeEvent-je (ha egyáltalán) hívódott meg.
_active_workers = []


def _wait_for_active_workers():
    for worker in list(_active_workers):
        if worker.isRunning():
            worker.wait(6000)


atexit.register(_wait_for_active_workers)


class RfidReadWorker(QThread):
    """A Chafonrfid.get_tid() blokkoló soros olvasását futtatja háttérszálon.

    A soros port timeoutja (SerialTransport, timeout=5s) miatt egy olvasás
    (esp. több frame-es válasz esetén) több másodpercig is elhúzódhat; ha ez
    a GUI szálon fut, a teljes ablak lefagy erre az időre, és a közben
    beérkező kattintások Qt-sorba kerülve a fagyás feloldódásakor egyszerre,
    duplán sülnek el (lásd docs/ARCHITECTURE.md).
    """
    read_finished = pyqtSignal(object, object)

    def __init__(self, comm_port, parent=None):
        super().__init__(parent)
        self.__comm_port = comm_port

    def run(self):
        try:
            chafonrfid = Chafonrfid(self.__comm_port)
            rfid = chafonrfid.get_tid()
            error = chafonrfid.error
        except Exception as exc:
            rfid = None
            error = str(exc)
        self.read_finished.emit(rfid, error)


class RfidReaderMixin:
    def _readTid(self, comm_port, set_status):
        chafonrfid = Chafonrfid(comm_port)
        rfid = chafonrfid.get_tid()
        if chafonrfid.error is not None:
            set_status(chafonrfid.error)
        else:
            set_status(None)
        return rfid

    def _readTidAsync(self, comm_port, on_result):
        """Nem blokkoló változat: a hardveres olvasást háttérszálon futtatja,
        és a `on_result(rfid, error)` callback-et a GUI szálon hívja meg,
        amint elkészült. A visszaadott worker-t a hívónak életben kell
        tartania (pl. self-attribútumban), amíg be nem fejeződik."""
        worker = RfidReadWorker(comm_port)
        _active_workers.append(worker)

        def _unregister():
            if worker in _active_workers:
                _active_workers.remove(worker)

        worker.finished.connect(_unregister)
        worker.read_finished.connect(on_result)
        worker.finished.connect(worker.deleteLater)
        worker.start()
        return worker


class ResizeFontMixin:
    def _resizeFont(self, divisor=40, default_size=14):
        width = self.rect().width() // divisor
        if width > default_size:
            return QFont('', width)
        return QFont('', default_size)

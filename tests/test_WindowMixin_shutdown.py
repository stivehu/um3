import os
import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_active_worker_survives_python_exit_during_close(tmp_path):
    # ApplicationWindow.closeEvent a beépített exit()-et hívja, ami a Qt-t
    # megkerülve azonnal leállítja az interpretert. Ha ilyenkor egy
    # RfidReadWorker (QThread) még fut, és a Python az utolsó referenciáját
    # elveszti a leállás közben, a Qt "QThread: Destroyed while thread is
    # still running" végzetes hibával elhasal (SIGABRT). A WindowMixin
    # modulszintű _active_workers regisztere + atexit hook ezt hivatott
    # megelőzni azzal, hogy a worker-t a befejezéséig életben tartja.
    # Ezt csak külön processzben lehet valósághűen tesztelni (a folyamat
    # tényleges leállása a lényeg), ezért subprocess-ben futtatjuk.
    script = tmp_path / "repro.py"
    script.write_text(textwrap.dedent("""
        import os
        import sys
        import time

        os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

        from PyQt6.QtCore import QThread, QTimer, pyqtSignal
        from PyQt6.QtWidgets import QApplication, QWidget

        from src.controller.WindowMixin import _active_workers


        class SlowWorker(QThread):
            read_finished = pyqtSignal(object, object)

            def run(self):
                time.sleep(1.5)
                self.read_finished.emit("ABCDEF", None)


        class Win(QWidget):
            def __init__(self):
                super().__init__()
                self.worker = SlowWorker()
                _active_workers.append(self.worker)
                self.worker.finished.connect(
                    lambda: _active_workers.remove(self.worker) if self.worker in _active_workers else None)
                self.worker.start()

            def closeEvent(self, event):
                exit()


        app = QApplication(sys.argv)
        w = Win()
        w.show()
        QTimer.singleShot(200, w.close)
        sys.exit(app.exec())
    """))

    env = dict(os.environ, PYTHONPATH=str(REPO_ROOT))
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        timeout=15,
        cwd=str(REPO_ROOT),
        env=env,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Destroyed while thread" not in result.stderr

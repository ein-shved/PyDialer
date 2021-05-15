# Python Dialer entry point

import sys
from PyQt5.QtGui import QGuiApplication

from . import MainWindow

app = QGuiApplication(sys.argv)
w = MainWindow.MainWindow()
w.show()
sys.exit(app.exec_())

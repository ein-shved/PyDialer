import os

from PySide2.QtCore import Slot
from PySide2.QtCore import QUrl, QObject
from PySide2.QtQuick import QQuickView


class MainWindow(QQuickView):
    def __init__(self, parent = None):
        super().__init__(parent)
        qml_file = os.path.join(os.path.dirname(__file__),"MainWindow.qml")

        self.rootContext().setContextProperty("pWidth", 200)
        self.rootContext().setContextProperty("pHeight", 100)
        self.rootContext().setContextProperty("self", self)

        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

    @Slot()
    def answer(self):
        print("Answer!")

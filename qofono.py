import readline
import code
import threading
import sys

from QOfono import QOfonoManager, QOfonoModem, QOfonoVoiceCallManager
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import SIGNAL, QObject, Signal, Slot

# Example script. Demonstrates workability of qOfono binding on python.
# Run this script, it automatically initiates and connects to first available
# modem. Run then
#
#   >>> self.dialer.dial("<phone number>")
#
# To initialize call.

class TestShell(threading.Thread):
    def __init__(self, app, dialer):
        threading.Thread.__init__(self)
        self.app = app
        self.dialer = dialer

    def run(self):
        variables = globals().copy()
        variables.update(locals())
        shell = code.InteractiveConsole(variables)
        shell.interact()
        self.app.exit()

class Dialer(QObject):
    __dial = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.modem = None
        self.manager = QOfonoManager(self)
        for m in self.manager.modems():
            self.onModemAdded(modem)
        self.callman = QOfonoVoiceCallManager(self)

        self.manager.connect(SIGNAL("modemAdded()"), self.onModemUpdated)
        self.manager.connect(SIGNAL("modemRemoved()"), self.onModemUpdated)
        self.__dial.connect(self.callman.dial)

    def onModemUpdated(self):
        modems = self.manager.modems()
        if (self.modem):
            for m in modems:
                if m == self.modem.modemPath():
                    return
        self.prepareModem(modems[0])

    def prepareModem(self, path):
        self.modem = QOfonoModem(path, self)
        print ("Modem registered:", self.modem.name())
        self.callman.setModemPath(path)

    def dial(self, phoneNumber, calleridHide = "default"):
        self.__dial.emit(phoneNumber, calleridHide)

app = QApplication(sys.argv)
d = Dialer()

shell = TestShell(app, d)
shell.start()

app.exec_()
shell.join()

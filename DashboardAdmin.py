import sys
from PyQt5 import QtCore, QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from FrmMatakuliah import WindowMatakuliah

qtcreator_file  = "dashboard_admin.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowDashboardAdmin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        self.actionExit.triggered.connect(self.app_exit)
        self.actionMatakuliah_2.triggered.connect(self.app_matakuliah)        

    def app_exit(self):
        sys.exit()

    def app_matakuliah(self):
        winmatakuliah.setWindowModality(QtCore.Qt.ApplicationModal)
        winmatakuliah.show()  

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboardAdmin()
    winmatakuliah = WindowMatakuliah()
    window.showFullScreen()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboardAdmin()
    winmatakuliah = WindowMatakuliah() 
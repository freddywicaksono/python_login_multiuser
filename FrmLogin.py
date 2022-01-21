import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from DashboardAdmin import WindowDashboardAdmin
from DashboardOperator import WindowDashboardOperator
from Users import Users as Login

qtcreator_file  = "login.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowLogin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnSubmit.clicked.connect(self.app_login) # ketika klik tombol submit

    def app_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        valid = usr.Validasi(username,password)
        role = usr.rolename.strip() # ketika login berhasil maka variabel role berisi 'admin' atau 'operator'
        if(valid==True): # Login berhasil
            window.hide()
            self.messagebox("Info","Login Berhasil")
            if(role=='admin'):
                self.messagebox("Info","Anda Login sebagai Admin")
                winadmin.showFullScreen()
            if(role=='operator'):
                self.messagebox("Info","Anda Login sebagai Operator")
                winop.showFullScreen()
        else: # login gagal
            self.messagebox("Info","Maaf login gagal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin() # Create Instance Object Form Login
    winadmin = WindowDashboardAdmin() # load Instance object window dashboard admin
    winop = WindowDashboardOperator() # load Instance object window dashboard operator
    window.show() # Tampilkan form Login
    usr = Login() # create Instance Object User
    sys.exit(app.exec_())
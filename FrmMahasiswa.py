import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from Mahasiswa import Mahasiswa

qtcreator_file  = "mahasiswa.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowMahasiswa(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNIM.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            mhs = Mahasiswa()

            # Get all 
            result = mhs.getAllData()

            self.gridMahasiswa.setHorizontalHeaderLabels(['ID', 'NIM', 'Nama', 'Jenis Kelamin', 'Prodi'])
            self.gridMahasiswa.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridMahasiswa.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridMahasiswa.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nim=self.txtNIM.text()           
            mhs = Mahasiswa()
            # search process
            result = mhs.getByNIM(nim)           
            a = mhs.affected
            if(a!=0):
                self.txtNama.setText(mhs.nama.strip())
                
                self.cboProdi.setCurrentText(mhs.kode_prodi.strip())
                #self.messagebox("test2", mhs.kode_prodi)
                if(result[3]=="L"):
                    self.optLaki.setChecked(True)
                    self.optPerempuan.setChecked(False)
                else:
                    self.optLaki.setChecked(False)
                    self.optPerempuan.setChecked(True)

                
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            mhs = Mahasiswa()
            nim=self.txtNIM.text()
            nama=self.txtNama.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"

            kode_prodi=self.cboProdi.currentText()
            
            if(self.edit_mode==False):   
                mhs.nim = nim
                mhs.nama = nama
                mhs.jk = jk
                mhs.kode_prodi = kode_prodi
                a = mhs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Mahasiswa Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Mahasiswa Gagal Tersimpan")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mhs.nama = nama
                mhs.jk = jk
                mhs.kode_prodi = kode_prodi
                a = mhs.updateByNIM(nim)
                if(a>0):
                    self.messagebox("SUKSES", "Data Mahasiswa Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Mahasiswa Gagal Diperbarui")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            mhs = Mahasiswa()
            nim=self.txtNIM.text()
                       
            if(self.edit_mode==True):
                a = mhs.deleteByNIM(nim)
                if(a>0):
                    self.messagebox("SUKSES", "Data Mahasiswa Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Mahasiswa Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtNIM.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.cboProdi.setCurrentText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowMahasiswa()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowMahasiswa()
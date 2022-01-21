from db import DBConnection as mydb

class Mahasiswa:

    def __init__(self):
        self.__id=None
        self.__nim=None
        self.__nama=None
        self.__jk=None
        self.__kode_prodi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "NIM:" + self.__nim + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Kode Prodi:" + self.__kode_prodi
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__jk, self.__kode_prodi)
        sql="INSERT INTO mahasiswa (nim, nama, jk, kode_prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__jk, self.__kode_prodi, id)
        sql="UPDATE mahasiswa SET nim = %s, nama = %s, jk=%s, kode_prodi=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__kode_prodi, nim)
        sql="UPDATE mahasiswa SET nama = %s, jk=%s, kode_prodi=%s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nim):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE nim='" + str(nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nim = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__kode_prodi = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__jk = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result

import hashlib
from db import DBConnection as mydb
class Users:
    def __init__(self):
        self.__iduser= None
        self.__username= None
        self.__password= None
        self.__rolename= None
        self.__info = None
        self.__loginvalid = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def iduser(self):
        return self.__iduser
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
    
    @property
    def rolename(self):
        return self.__rolename

    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
    
    @property
    def loginvalid(self):
        return self.__loginvalid

    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value
        
    def Validasi(self, username, password):
        a=str(username)
        b=a.strip()
        pwd=str(password).strip().encode()
        c = hashlib.md5(pwd)
        c2=c.hexdigest()

        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + b + "' and password='" + c2 + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__username = self.result[1]
            self.__password = self.result[2]
            self.__rolename = self.result[3]
            self.affected = self.conn.cursor.rowcount
            # val = [True,self.__rolename]
            self.__loginvalid = True
        else:
            self.__username = ''                  
            self.__password = ''                  
            self.__rolename = ''                  
            self.affected = 0
            # val = [False,""]
            self.__loginvalid = False
        self.conn.disconnect
        return self.__loginvalid

'''A = Users()
B = A.Validasi('admin','123')
print(B)'''

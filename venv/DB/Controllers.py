import sys
import json
from flask import jsonify,make_response
import dbapidemo.venv.DB.config as Config
import pymysql


def covertStr(val):
    return "\"" + val + "\""


class SQL:
    connection = None

    def connectDB(self):
        try:
            self.connection = pymysql.connect(host=Config.data["host"], user=Config.data["user"],
                                              passwd=Config.data["passwd"], database=Config.data["database"])
            print("connect thanh cong")
        except:
            print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra.")
            print("turn on xmapp")
            print("connect that bai");

    def setCursor(self):
        try:
            if self.connection != None:
                return self.connection.cursor()
            else:
                print("self.connection chưa khởi tạo , call method connectDB()")
                return None
        except:
            print("error here setCursor")
            return None

    # admin or user
    def getListAcount(self , val , tableName="acount"):
        if self.connection != None:
            cursor = self.setCursor()
            if cursor != None:
                try:
                    if val["admin"] == 1:
                        tableName  = "acount_admin"
                    # sql = "SELECT * FROM " + tableName + " WHERE username = " + "\"" + str(val["email"]) + "\"" + " AND password = " + "\"" + str(val["password"]) + "\"" + ";"
                    sql = "SELECT * FROM " + tableName + " WHERE username = " + covertStr(val["email"]) + " AND password = " + covertStr(val["password"]) + ";"
                    print(sql)
                    cursor.execute(sql)

                    return cursor.fetchall()

                except:
                    return
            else:
                return
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    # save account user
    def saveRegister(self, data, tableName='acount'):
        if self.connection != None:
            cursor = self.setCursor()
            if cursor != None:
                sql = "INSERT INTO " + tableName + " (username , password) " + "VALUES(%s , %s)"
                cursor.execute(sql , (data["tk"] , data["mk"]))
                self.connection.commit()
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def getHomePage(self, tableName='homepage'):
        if self.connection != None:
            cursor = self.setCursor()
            if cursor != None:
                try:

                    sql = "SELECT * FROM " + tableName + ";"

                    print(sql)
                    cursor.execute(sql)
                    lists = cursor.fetchall()
                    listProducts = []

                    for list in lists:
                        text = {
                            'id': list[0],
                            'tilte': list[1],
                            'name': list[2],
                            'noidung': list[3],
                            'image': list[4]
                        }

                        listProducts.append(text)
                    return listProducts
                except:
                    print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra. getHomePage")
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")


    def getDetailHome(self, id):
        if self.connection != None:
            cursor = self.setCursor();
            if cursor != None:
                sql = "SELECT * FROM homepage WHERE id=" + id + ";"
                cursor.execute(sql)
                lists = cursor.fetchall()
                listProducts = []
                for list in lists:
                    text = {
                        'id': list[0],
                        'tilte':list[1],
                        'name': list[2],
                        'noidung': list[3],
                        'image': list[4]
                    }
                    listProducts.append(text)
                return listProducts
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def getProduts(self, tableName='cook'):
        if self.connection != None:
            cursor = self.setCursor();
            if cursor != None:
                sql = "SELECT * FROM " + tableName + ";"
                cursor.execute(sql)
                lists = cursor.fetchall()
                listProducts = []
                for list in lists:
                    text = {
                        'id': list[0],
                        'name':list[1],
                        'nguyenlieu': list[2],
                        'soche': list[3],
                        'image': list[5]
                    }
                    listProducts.append(text)
                return listProducts
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def getDetail(self, id):
        if self.connection != None:
            cursor = self.setCursor();
            if cursor != None:
                sql = "SELECT * FROM cook WHERE id=" + id + ";"
                cursor.execute(sql)
                lists = cursor.fetchall()
                listProducts = []
                for list in lists:
                    text = {
                        'id': list[0],
                        'video': list[6],
                        'name':list[1],
                        'nguyenlieu': list[2],
                        'soche': list[3],
                        'thuchien': list[4]
                    }
                    listProducts.append(text)
                return listProducts
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def getProdutsVanHoa(self, tableName='cultural'):
        if self.connection != None:
            cursor = self.setCursor();
            if cursor != None:
                sql = "SELECT * FROM " + tableName + ";"
                cursor.execute(sql)
                lists = cursor.fetchall()
                listProducts = []
                for list in lists:
                    text = {
                        'id': list[0],
                        'ten':list[1],
                        'tacgia': list[2],
                        'noidung': list[3],
                        'image': list[4]
                    }
                    listProducts.append(text)
                return listProducts
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def getDetailCultural(self, id):
        if self.connection != None:
            cursor = self.setCursor();
            if cursor != None:
                sql = "SELECT * FROM cultural WHERE id=" + id + ";"
                cursor.execute(sql)
                lists = cursor.fetchall()
                listProducts = []
                for list in lists:
                    text = {
                        'id': list[0],
                        'ten':list[1],
                        'tacgia': list[2],
                        'noidung': list[3],
                        'image': list[4]
                    }
                    listProducts.append(text)
                return listProducts
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def saveAmThuc2(self, id, nguyenlieu, tenmon, soche, img, author, state):
        try:
            if self.connection != None:
                cursor = self.setCursor()
                if cursor != None:
                    try:
                        sql = "INSERT INTO writecook (id ,tenmon, nguyenlieu ,soche , img  , state , tag, IDuser) " + "VALUES (%s , %s, %s ,%s , %s, %s , %s , %s);"
                        cursor.execute(sql, (id, tenmon, nguyenlieu, soche, img,state, 'amthuc', str(author)))
                        self.connection.commit()

                    except:
                        print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra. at saveAmThuc")
                else:
                    print("cursor is None")
            else:
                print("self.connection chưa khởi tạo , call method connectDB()")
        except:
            print("error here saveAmThuc")

    def saveVanHoa(self, id, tenbai, noidung, img, author, state):
        try:
            if self.connection != None:
                cursor = self.setCursor()
                if cursor != None:
                    try:
                        sql = "INSERT INTO writevanhoa (id ,tenbai, noidung, img , state , tag, IDuser) " + "VALUES (%s , %s, %s , %s, %s , %s , %s);"

                        cursor.execute(sql, (id, tenbai, noidung, img,state, 'vanhoa',str(author)))
                        self.connection.commit()

                    except:
                        print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra. at saveVanHoa")
                else:
                    print("cursor is None")
            else:
                print("self.connection chưa khởi tạo , call method connectDB()")
        except:
            print("error here saveVanHoa")


    def getListByAuthor(self, val):
        global tableName

        try:
            if self.connection != None:
                cursor = self.setCursor()
                if cursor != None:
                    try:
                        if val["tag"] == "vanhoa":
                            tableName = "writevanhoa"
                        elif val["tag"] == "amthuc":
                            tableName = "writecook"
                        print(val)
                        if val["author"] == None:
                            sql ="select * from " + tableName +  " ORDER BY state asc , IDuser asc;"
                        else:
                            sql = "select * from " + tableName + " where IDuser = " + covertStr(val["author"]) + " ORDER BY state asc , IDuser asc;"
                        print(sql)
                        cursor.execute(sql)
                        return cursor.fetchall()
                    except:
                        print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra at getListByAuthor")
                else:
                    print("cursor is None")
            else:
                print("self.connection chưa khởi tạo , call method connectDB()")
        except:
            print("error here getListByAuthor")

    def deleteId(self, val):
        global tableName
        try:
            if self.connection != None:
                cursor = self.setCursor()
                if cursor != None:
                    try:
                        if val["tag"] == "vanhoa":
                            tableName = "writevanhoa"
                        elif val["tag"] == "amthuc":
                            tableName = "writecook"
                        sql = "delete from " + tableName + " where id = " + covertStr(val["id"]) + ";"
                        cursor.execute(sql)
                        self.connection.commit()
                    except:
                        print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra at getListByAuthor")
                else:
                    print("cursor is None")
            else:
                print("self.connection chưa khởi tạo , call method connectDB()")
        except:
            print("error here getListByAuthor")


 # ----------------------------------------bài đăng user----------------------------------
    def getUser_Cook(self):
        if self.connection != None:
            cursor = self.setCursor()
            if cursor != None:
                try:
                    sql = "SELECT * FROM writecook WHERE state = 1 ;"

                    cursor.execute(sql)

                    lists = cursor.fetchall()
                    listProducts = []

                    for list in lists:

                        text = {
                            'id': list[0],
                            'tenmon': list[1],
                            'nguyenlieu': list[2],
                            'soche': list[3],
                            'image': list[4],
                            'author': list[5]
                        }

                        listProducts.append(text)
                    return listProducts
                except Exception:
                    print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra. getUser_Cook")
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

    def getUser_Cultural(self):
        if self.connection != None:
            cursor = self.setCursor()
            if cursor != None:
                try:
                    sql = "SELECT * FROM writevanhoa WHERE state = 1 ;"
                    print(sql)
                    cursor.execute(sql)
                    lists = cursor.fetchall()
                    listProducts = []
                    for list in lists:

                        name = "SELECT username FROM acount WHERE ID = " + str(list[6]) + ";"
                        cursor.execute(name)
                        listss = cursor.fetchall()
                        name = listss[0][0]

                        text = {
                            'id': list[0],
                            'tenbai': list[1],
                            'noidung': list[2],
                            'image': list[3],
                            'author': name,
                        }
                        listProducts.append(text)
                    return listProducts
                except:
                    print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra. getUser_Cook")
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")



    def getID(self, username):
        if self.connection != None:
            table = "acount"
            if username == 'admin':
                table = "acount_admin"

            cursor = self.setCursor()
            if cursor != None:
                try:
                    sql = "SELECT * FROM "+ table+ " WHERE username = '" + str(username)+"';"

                    cursor.execute(sql)
                    lists = cursor.fetchall()
                    if lists:
                       return lists[0][0]

                    return -1
                except:
                    print("Có ngoại lệ ", sys.exc_info()[0], " xảy ra. getUser_Cook")
            else:
                print("cursor is None")
        else:
            print("self.connection chưa khởi tạo , call method connectDB()")

import sys

import DB.config as Config
import pymysql


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
		if self.connection != None:
			return self.connection.cursor()
		else:
			print("self.connection chưa khởi tạo , call method connectDB()")
			return None

	# admin or user
	def getListAcount(self, tableName='admin'):
		if self.connection != None:
			cursor = self.setCursor();
			if cursor != None:
				sql = "SELECT * FROM " + " acount_" + tableName + ";"
				cursor.execute(sql)
				return cursor.fetchall()
			else:
				print("cursor is None")
		else:
			print("self.connection chưa khởi tạo , call method connectDB()")

	# save account user
	def saveRegister(self, data, tableName='user'):
		if self.connection != None:
			cursor = self.setCursor();
			if cursor != None:
				sql = "INSERT INTO " + tableName + " (tk , mk) " + "VALUES(%s , %s)"

				cursor.execute(sql , (data["tk"] , data["mk"]))
				self.connection.commit();
			else:
				print("cursor is None")
		else:
			print("self.connection chưa khởi tạo , call method connectDB()")

import mysql.connector
import sqlite3
info = {
	"server_name": "localhost",
	"user": "root",
	"password": "root",
	"dbn": "delunch"
}

class database:
	def __init__(self):
		# self.conn = mysql.connector.connect(user=info["server_name"],
		# 									password=info["password"],
		# 									host=info["server_name"],
		# 									database= info["dbn"])
		self.conn = sqlite3.connect("database.db", check_same_thread=False)
		# self.database = info["dbn"]
		self.cursor = self.conn.cursor()


	def __del__(self):
		self.cursor.close()
		self.conn.close()
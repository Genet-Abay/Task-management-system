import mysql.connector

class db_connection:
    
    def __init__(self, host='localhost', user='root', pw='admin', dbname='testdb'):     
        self.host = host
        self.dbname=dbname
        self.username = user
        self.password = pw

    def connect_db(self):
       self.mydb = mysql.connector.connect(
       host=self.host,
       user= self.username,
       password=self.password,
       database=self.dbname
        )
       
    def get_cursor(self):
       cursor = self.mydb.cursor()
       return cursor
       

conn = db_connection()
conn.connect_db()
mycursor = conn.get_cursor()

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 




# Creating database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# Adding table to the database
# mycursor.execute("CREATE TABLE user (name VARCHAR(255) NOT NULL, user_id VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, PRIMARY KEY(user_id))")
# mycursor.execute("CREATE TABLE task (user_id VARCHAR(255) NOT NULL,  task_name VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, date_set DATE NOT NULL, due_date DATE, priority VARCHAR(255), PRIMARY KEY(user_id))")

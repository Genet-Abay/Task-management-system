from multipledispatch import dispatch

class user:
    def __init__(self, Name, UserId, address, email, password):
        self.username = Name
        self.userId = UserId
        self.userpw = password
        self.useraddress = address
        self.useremail = email

    def add_user(self, db, db_cursor):    
        """
        add user to database if it is not already registered
        """    
        u = self.get_user(db_cursor)
        if db_cursor.rowcount == 0:
            insert_statement = "INSERT INTO testdb (name, userid, address, email) VALUES (%s, %s, %s, %s)"
            val = (self.username, self.userId,self.useraddress, self.useremail) #("Harry", "Harry_21", "Belgium", "harry@gmail.com")
            db_cursor.execute(insert_statement, val)
            db.commit()
        else:
            print("User is already in the data base or user_id and or email_id already taken by another user")

    def delete_user(self, db, db_cursor):
        """
        delete a given user if exists
        """
        u = self.get_user(db_cursor)
        if db_cursor.rowcount == 0:
            del_query = "DELETE FROM testdb WHERE user_id = %s"
            id=self.userId
            db_cursor.execute(del_query, id)
            db.commit()

    def get_user(self, db_cursor):
        """
        search for a user with a givne user id
        """
        query_select = "SELECT user_id FROM testdb WHERE user_id = %s"
        id=self.userId
        db_cursor.execute(query_select, id)
        user = db_cursor.fetchall()
        return user
    
    def update_user(self, db, db_cursor):
        """
        updates the user information for a given user with given id
        """
        u = self.get_user(db_cursor)
        if db_cursor.rowcount == 0:
            update_query = "UPDATE testdb SET name = %s, address=%s, email=%s, WHERE user_id = %s"
            update_values =  (self.username,self.useraddress, self.useremail, self.userId)
            db_cursor.execute(update_query, update_values)
            db.commit()





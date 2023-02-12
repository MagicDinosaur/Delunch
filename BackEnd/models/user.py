from models.database import database

dbm = database()

def get_user_by_id(id):
    dbm.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    return dbm.cursor.fetchone()

def get_user_by_email(email):
    dbm.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    return dbm.cursor.fetchone()

def make_adoption(id , child_id):
    dbm.cursor.execute("INSERT INTO adoption (id, child_id) VALUES (%s, %s)", (id,child_id))
    dbm.conn.commit()
    return dbm.cursor.lastrowid

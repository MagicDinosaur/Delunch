
from models.database import  database

dbm = database()

def get_child_list(page, limit):
    #add check adoption
    query = "SELECT * FROM children sort by view_count asc LIMIT %s, %s"
    dbm.cursor.execute(query, ((page-1)*limit, limit))
    records = dbm.cursor.fetchall()
    return records


def get_child_by_id(id):
    dbm.cursor.execute("SELECT * FROM children WHERE id = %s", (id,))
    return dbm.cursor.fetchone()
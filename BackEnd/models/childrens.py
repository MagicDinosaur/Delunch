
from models.database import  database

dbm = database()

def get_child_list(page, limit):
    #add check adoption
    query = "SELECT * FROM children sort by view_count asc LIMIT {page},{limit}".format(page=page, limit=limit)
    dbm.cursor.execute(query, ((page-1)*limit, limit))
    records = dbm.cursor.fetchall()
    return records


def get_child_by_id(id):
    dbm.cursor.execute("SELECT * FROM childrens WHERE id = {id}".format(id=id))
    records = dbm.cursor.fetchone()
    data = {
        "id": records[0],
        "name": records[1],
        "age": records[2],
        "grade": records[3],
        "description": records[4],
        "adopted" : "true" if records[5] else "false",
    }
    return data
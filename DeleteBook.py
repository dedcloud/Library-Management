#program to delete book from library

def remove(db,cursor,bookID):
    cursor.execute("delete from Library where id="+bookID)
    db.commit()

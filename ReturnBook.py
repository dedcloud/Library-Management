#program to return the book

def return_book(db,cursor,id):
    date = dt.now.strftime("%x")
    time = dt.now.strftime("%X")

    sql = "update Records set Status=%s,returningDate=%s,returningTime=%s"
    vals = ("Returned",date,time)

    cursor.execute(sql,vals)
    db.commit()
    return "rows count",cursor.rowcount

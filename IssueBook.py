#programm to issue books
from datetime import datetime as dt

def issue(db,cursor,id,issuedBy,bookName,pub,writer):
    date = dt.now().strftime("%x")
    time = dt.now().strftime("%X")

    #id,issuedBy,bookName,publisher,writer,dateOfIssueing,time
    sql = "insert into Records(id,issuedBy,bookName,Publisher,Writer,issueingDate,issueingTime) values(%d,%s,%s,%s,%s,%s,%s)"
    vals = (id,issuedBy,bookName,pub,writer,date,time)

    cursor.execute(sql,vals)
    db.commit()
    return "rows count",cursor.rowcount

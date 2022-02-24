#Programm for Adding Book(s)
from datetime import datetime as dt

def add(db,cursor,bookName,publisher,writer):
    date = dt.now().strftime("%x")
    time = dt.now().strftime("%X")
    day = dt.now().strftime("%A")
    month = dt.now().strftime("%B")
    timezone = dt.now().strftime("%Z")

    #id(auto_increment),bookName,publisher,writer,date,time,day,month,timezone
    sql = "insert into Library(bookName,Publisher,Writer,Date,Time,Day,Month,Timezone) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (bookName,publisher,writer,date,time,day,month,timezone)

    cursor.execute(sql,vals)
    db.commit()
    return "rows count",cursor.rowcount

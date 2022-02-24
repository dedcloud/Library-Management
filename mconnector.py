import mysql.connector as connector

db = connector.connect(host="localhost",
                       user="root",
                       password="knight",
                       database="Knight"
                      )
cursor = db.cursor()


cursor.execute("create table if not exists Library (id int primary key auto_increment,bookName varchar(512),Publisher varchar(256),Writer varchar(256),Date varchar(32),Time varchar(64),Day varchar(16),Month varchar(16),Timezone varchar(16))")
cursor.execute("create table if not exists Records (id int primary key,issuedBy varchar(128),bookName varchar(256),Publisher varchar(256),Writer varchar(256), issueingDate varchar(32), issuingTime varchar(64) )")


from AddBook import add 
from ViewBooks import display
from DeleteBook import remove
from IssueBook import issue
from ReturnBook import return_book


print("""
×××××××××××××××××××××××××××××××××××
                                  ¦
》Library Management Project      ¦
》                                ¦
》1 《 View Available Books       ¦
》2 《 Add New Book               ¦
》3 《 Issue a Book               ¦
》4 《 Return Book                ¦
》5 《 Delete Book from Library   ¦
》0 《 Exit                       ¦
                                  ¦
—¯—_—¯-----¯-_-––¯-_-_-¯¯-_-_-_-¯-¯
""")


def inval_i():
     print("{Invalid Input}")

def inp(func="add"):
     if func == "issue":
         id = input("》Book ID《《")
         issuer = input("》Issuer Name《《")

         cursor.execute("select bookName,Publisher,Writer from Library where id = "+id)
         res = cursor.fetchone()
         return (id,issuer)+res

     else:
         bookName = input("》Book Name《《")
         pub = input("》Publisher《《")
         writer = input("》Writer《《")

         return bookName,pub,writer

i = None

while i != 0:
    try:
        i = int(input("》》》"))
    except:
        inval_i()
        continue

    if i == 1 :
        display(cursor,"Library")

    elif i == 2:
        bookName,pub,writer = inp()
        add(db,cursor,bookName,pub,writer)

    elif i == 3:
        bookId,issuer,bookName,pub,writer = inp("issue")
        issue(db,cursor,bookId,issuer,bookName,pub,writer)

    elif i == 4:
        try:
            id = int(input("》ID《《"))
        except:
            inval_i()
        if id in display(cursor,"Records"):
            return_book(db,cursor,id)
        else:
            print("ID not found ")

    elif i == 5:
        bookID = input("》Book ID《《")
        remove(db,cursor,bookID)

    elif i == 0:
        print("\nThank you .")

    else:
        inval_i()
        continue

#a = add(db,cursor,"Intermediate Algebra with early functions and graphing","Addison-Wesley","Margeret L. Lial")
#print(a)

#programm to display list of available books in library

def display(cursor,table):
    cursor.execute("select * from "+table)
    results = cursor.fetchall()

    for i in results:
        for j in i:
            print("¦",j,end="")
        print("¦")

    return results[0]

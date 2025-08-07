from database import get_connection
from prettytable import PrettyTable

def view():
    mycon, mycur = get_connection()
    print(" VIEW ")
    print("\t1. View List of all books")
    print("\t2. View List of available books")
    while True:
        a=input('Enter your choice number(1/2) : ')
        if a=='1' or a=='2':
            break
        elif a.isdigit()==False:
            print("Invalid choice ! Enter a numeric choice")
        else:
            print("Invalid choice ! ")
    ach=int(a)
    if ach==1:
        mycur.execute("select * from book_info")
        bdata=mycur.fetchall()
        tb=PrettyTable(['BookID','Bookname','Status','Author','Publisher','Cost','Genre'])
        for i in range(len(bdata)):
            tb.add_row(bdata[i])
        print(tb)
    elif ach==2:
        mycur.execute("select * from available_books")
        adata=mycur.fetchall()
        ta=PrettyTable(['BookID','Bookname','Author','Publisher'])
        for i in range(len(adata)):
            ta.add_row(adata[i])
        print(ta)
        

        
    

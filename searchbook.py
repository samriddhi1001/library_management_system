import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="lms")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()
from prettytable import PrettyTable

def searchbook():
    print(" SEARCH BOOK")
    print("\t1.Search Book by Book Name")
    print("\t2.Search Book by Author Name")
    print("\t3.Search Book by Genre")
    while True:
        a=input('Enter your choice number(1/2/3) : ')
        if a=='1' or a=='2' or a=='3':
            break
        elif a.isdigit()==False:
            print("Invalid choice ! Enter a numeric choice")
        else:
            print("Invalid choice ! ")
    ach=int(a)
    if ach==1:
        book=input("Enter the name of the book : ")        
        mycur.execute("select * from book_info where bookname like '%{}%'".format(book))
        bdata=mycur.fetchall()
        tb=PrettyTable(['BookID','Bookname','Status','Author','Publisher','Cost','Genre'])
        for i in range(len(bdata)):
            tb.add_row(bdata[i])
        print(tb)
    elif ach==2:
        ath=input("Enter the name of the author : ")        
        mycur.execute("select * from book_info where author like '%{}%'".format(ath))
        adata=mycur.fetchall()
        tb=PrettyTable(['BookID','Bookname','Status','Author','Publisher','Cost','Genre'])
        for i in range(len(adata)):
            tb.add_row(adata[i])
        print(tb)
    elif ach==3:
        gen=input("Enter the name of the book genre : ")        
        mycur.execute("select * from book_info where genre like '%{}%'".format(gen))
        gdata=mycur.fetchall()
        tb=PrettyTable(['BookID','Bookname','Status','Author','Publisher','Cost','Genre'])
        for i in range(len(gdata)):
            tb.add_row(gdata[i])
        print(tb)
    


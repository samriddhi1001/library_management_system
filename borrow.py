import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="lms")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()

from datetime import date

def choice(n):
    while True:
        a=input('Enter your Choice Number : ')
        if a.isdigit()==False:
            print("Invalid choice ! Enter a Natural Number")
        elif a>"0" and eval(a)<(n+1) and eval(a)%1==0:
            break
        elif eval(a)>=(n+1):
            print("Invalid Choice ! Enter a Natural Number less than",n+1)
        else:
            print("Invalid choice ! ")
    return(int(a))
            
def borrowbook():
    mycur.execute("select * from book_info")
    bdata=mycur.fetchall()
    mycur.execute("select * from student_info")
    data=mycur.fetchall()
    mycur.execute("select * from teacher_info")
    tdata=mycur.fetchall()
    mycur.execute("select * from borrowed_books")
    bbooks=mycur.fetchall()
    mycur.execute("select * from tborrowed_books")
    tbbooks=mycur.fetchall()
    print(" BORROW ")
    print("\t1. Borrow book for student")
    print("\t2. Borrow book for teacher")
    ch=choice(2)
    if ch==1:
       s=True
       adnos=[]
       badn=[]
       for i in range(len(bbooks)):
           badn.append(bbooks[i][7])
       for i in range(len(data)):
            adnos.append(data[i][0])      
       while s == True:
            adn=input("Enter 8 digit Admission Number: ")
            if int(adn) not in adnos:
                 print("Admission Number doesn't exist ! ")
            elif int(adn) in badn:
                 print("Student has already borrowed a book ! ")
            else :
                 s =False
        
       while True:
            if adn.isdigit()==False:
                print("Admission Number can only have digits !")
                adn=input("Enter 8 digit Admission Number : ")
            elif len(adn)!=8:
                print("Admission Number must have 8 digits !")
                adn=input("Enter 8 digit Admission Number : ")
            else:
                break
       adno=int(adn)
       
       mycur.execute("select name, grade, sec from student_info where adno={}".format(adno))
       sdata=mycur.fetchall()
       n,g,s=sdata[0]
       
       
       q=True
       bnos=[]
       for i in range(len(bdata)):
            bnos.append(bdata[i][0])
       bks=[]
       for i in range(len(bbooks)):
            bks.append(bbooks[i][0])
       bkt=[]     
       for i in range(len(tbbooks)):
           bkt.append(tbbooks[i][0])
       
       while q == True:
                bdn=input("Enter 4 digit Book id : ")
                if int(bdn) not in bnos:
                     print("Book ID doesn't exist ! ")
                elif int(bdn) in bks:
                     print("Book already borrowed ! Enter a new BookID")
                elif int(bdn) in bkt:
                     print("Book already borrowed ! Enter a new BookID")
                else :
                     q =False
            
       while True:
                if bdn.isdigit()==False:
                    print("Book id can only have digits")
                    bdn=input("Enter 4 digit Book id : ")
                elif len(bdn)!=4:
                    print("Book id must have 4 digits")
                    bdn=input("Enter 4 digit id : ")
                else:
                    break
       bno=int(bdn)

       mycur.execute("select bookname from book_info where bookid={}".format(bno))
       ndata=mycur.fetchall()
       bname=ndata[0][0]

       d=str(date.today())
       mycur.execute("select adddate('{}', interval 14 day)".format(d))
       da=mycur.fetchall()
       dd=da[0][0]
    
       mycur.execute("update book_info set status='borrowed' where bookid={}".format(bno))
       mycur.execute("insert into borrowed_books values({}, '{}', '{}', {}, '{}', '{}', '{}', {})".format(bno, bname, n, g, s, d, dd, adno))
       mycur.execute("delete from available_books where bookid={}".format(bno))
       mycon.commit()
       print("Book borrowed successfully ! ")

    elif ch==2:
       mycur.execute("select * from teacher_info")
       tdata=mycur.fetchall()
       s=True
       tnos=[]
       btid=[]
       for i in range(len(tbbooks)):
           btid.append(tbbooks[i][5])
       for i in range(len(tdata)):
            tnos.append(tdata[i][0])      
       while s == True:
            tdn=input("Enter 5 digit TeacherID : ")
            if int(tdn) not in tnos:
                 print("TeacherID doesn't exist ! ")
            elif int(tdn) in btid:
                 print("Teacher has already borrowed a book ! ")
            else :
                 s =False
        
       while True:
            if tdn.isdigit()==False:
                print("TeacherID can only have digits")
                tdn=input("Enter 5 digit TeacherID : ")
            elif len(tdn)!=5:
                print("TeacherID must have 5 digits")
                tdn=input("Enter 5 digit TeacherID : ")
            else:
                break
       tdno=int(tdn)
       
       mycur.execute("select name from teacher_info where thid={}".format(tdno))
       tdata=mycur.fetchall()
       tn=tdata[0][0]
       
       q=True
       bnos=[]
       for i in range(len(bdata)):
            bnos.append(bdata[i][0])
       bks=[]
       for i in range(len(bbooks)):
            bks.append(bbooks[i][0])
       bkt=[]     
       for i in range(len(tbbooks)):
           bkt.append(tbbooks[i][0])
           
       while q == True:
                bdn=input("Enter 4 digit Book id : ")
                if int(bdn) not in bnos:
                     print("Book ID doesn't exist ! ")
                elif int(bdn) in bks:
                     print("Book already borrowed ! Enter a new BookID")
                elif int(bdn) in bkt:
                     print("Book already borrowed ! Enter a new BookID")     
                else :
                     q =False
            
       while True:
                if bdn.isdigit()==False: 
                    print("Book id can only have digits !")
                    bdn=input("Enter 4 digit Book id : ")
                elif len(bdn)!=4:
                    print("Book id must have 4 digits !")
                    bdn=input("Enter 4 digit id : ")
                else:
                    break
       bno=int(bdn)

       mycur.execute("select bookname from book_info where bookid={}".format(bno))
       ndata=mycur.fetchall()
       bname=ndata[0][0]

       d=str(date.today())
       mycur.execute("select adddate('{}', interval 14 day)".format(d))
       da=mycur.fetchall()
       dd=da[0][0]
    
       mycur.execute("update book_info set status='borrowed' where bookid={}".format(bno))
       mycur.execute("insert into tborrowed_books values({}, '{}', '{}','{}', '{}', {})".format(bno, bname, tn, d, dd, tdno))
       mycur.execute("delete from available_books where bookid={}".format(bno))
       mycon.commit()
       print("Book borrowed successfully ! ")
        






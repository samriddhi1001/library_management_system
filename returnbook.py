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
            print("Invalid choice ! Enter an Natural Number")
        elif a>"0" and eval(a)<(n+1) and eval(a)%1==0:
            break
        elif eval(a)>(n+1):
            print("Invalid Choice ! Enter a Natural Number less than",n+1)
        else:
            print("Invalid choice ! ")
    return(int(a))
            
def returnbook():
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
    print(" RETURN")
    print("\t1. Return book for student")
    print("\t2. Return book for teacher")
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
            adn=input("Enter 8 digit admission id : ")
            if int(adn) not in adnos:
                 print("Admission number doesn't exist ! ")
            elif int(adn) not in badn:
                 print("Student has not borrowed a book ! ")
            else :
                 s =False
        
       while True:
            if adn.isdigit()==False:
                print("Admission id can only have digits")
                adn=input("Enter 8 digit admission id : ")
            elif len(adn)!=8:
                print("Admission id must have 8 digits")
                adn=input("Enter 8 digit admission id : ")
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
       
       while True:
                bdn=input("Enter 4 digit Book id : ")
                if int(bdn) not in bnos:
                     print("Book ID doesn't exist ! ")
                elif int(bdn) not in bks and int(bdn) not in bkt :
                     print("Book not borrowed ! Enter a new BookID")
                else :
                     break
        
            
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

       mycur.execute("select duedate from borrowed_books where bookid={}".format(bno))
       l=mycur.fetchall()
       v=l[0][0]

       d=str(date.today())

       mycur.execute("select datediff('{}','{}')".format(d,v))
       diff=mycur.fetchall()
       dif=diff[0][0]
       
       if dif<0 or dif==0:
           print("No fine")
       elif dif>0 and dif<=5:
           print("Pay fine - 20 Rs")
       elif dif>5 and dif<=10:
           print("Pay fine - 50 Rs")
       elif dif>10:
           f=((dif-10)*10)+100
           print("Pay fine -",f," Rs")
           
        
       mycur.execute("select bookname,author,publisher from book_info where bookid={}".format(bno))
       ndata=mycur.fetchall()
       bname,a,p=ndata[0]
    
       mycur.execute("update book_info set status='available' where bookid={}".format(bno))
       mycur.execute("insert into available_books values({}, '{}', '{}',  '{}')".format(bno, bname,a,p))
       mycur.execute("delete from borrowed_books where bookid={}".format(bno))
       mycon.commit()
       print("Book returned successfully ! ")

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
            elif int(tdn) not in btid:
                 print("Teacher has not borrowed a book ! ")
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
                elif int(bdn) not in bks and int(bdn) not in bkt:
                     print("Book not borrowed ! Enter a new BookID")     
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

       mycur.execute("select duedate from tborrowed_books where bookid={}".format(bno))
       l=mycur.fetchall()
       v=l[0][0]

       d=str(date.today())

       mycur.execute("select datediff('{}','{}')".format(d,v))
       diff=mycur.fetchall()
       dif=diff[0][0]
       
       if dif<0 or dif==0:
           print("No fine")
       elif dif>0 and dif<=5:
           print("Pay fine - 20 Rs")
       elif dif>5 and dif<=10:
           print("Pay fine - 50 Rs")
       elif dif>10:
           f=((dif-10)*10)+100
           print("Pay fine -",f," Rs")
           

       mycur.execute("select bookname,author,publisher from book_info where bookid={}".format(bno))
       ndata=mycur.fetchall()
       bname,a,p=ndata[0]
    
       mycur.execute("update book_info set status='available' where bookid={}".format(bno))
       mycur.execute("insert into available_books values({}, '{}', '{}',  '{}')".format(bno, bname,a,p))
       mycur.execute("delete from tborrowed_books where bookid={}".format(bno))
       mycon.commit()
       print("Book returned successfully ! ")
      


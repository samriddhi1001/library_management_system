import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="lms")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()

from prettytable import PrettyTable

def admin_view(bdata, adata, cdata, ddata):
    print(" VIEW BOOK DETAILS")
    print("\t1. View List of all books")
    print("\t2. View List of available books")
    print("\t3. View borrowed book details")
    
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
        tb=PrettyTable(['BookID','Bookname','Status','Author','Publisher','Cost','Genre'])
        for i in range(len(bdata)):
            tb.add_row(bdata[i])
        print(tb)
    elif ach==2:
        ta=PrettyTable(['BookID','Bookname','Author','Publisher'])
        for i in range(len(adata)):
            ta.add_row(adata[i])
        print(ta)
    elif ach==3:

         print("\t\t1. View borrowed books by students")
         print("\t\t2. View borrowed books by teachers")
         while True:
             c=input('Enter your choice number(1/2) : ')
             if c=='1' or c=='2' :
                 break
             elif c.isdigit()==False:
                print("Invalid choice ! Enter a numeric choice")
             else:
                 print("Invalid choice ! ")

         ch=int(c)
          
         if ch==1:
              tc=PrettyTable(['BookID','Bookname','Student Name','Grade','Section','Borrowed Date','Due Date','Student AdmissionID'])
              for i in range(len(cdata)):
                  tc.add_row(cdata[i])
              print(tc)
         elif ch==2:
              td=PrettyTable(['BookID','Bookname','Teacher Name','Borrowed Date','Due Date','TeacherID'])
              for i in range(len(ddata)):
                  td.add_row(ddata[i])
              print(td)       

        
        


def admin_viewdetails():
    print(" VIEW USER DETAILS")
    print("\t1. View details of students")
    print("\t2. View details of teachers")
    print("\t3. View details of admin")
    
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
        mycur.execute("select * from student_info order by grade")
        edata=mycur.fetchall()
        tb=PrettyTable(['Admission Number','Name','Userid','Password','Grade','Section'])
        for i in range(len(edata)):
            tb.add_row(edata[i])
        print(tb)
    elif ach==2:
        mycur.execute("select * from teacher_info order by name")
        fdata=mycur.fetchall()
        ta=PrettyTable(['Teacher ID ','Name','Userid','Password'])
        for i in range(len(fdata)):
            ta.add_row(fdata[i])
        print(ta)
    elif ach==3:
        mycur.execute("select * from admin_info")
        gdata=mycur.fetchall()
        tc=PrettyTable(['Admin ID ','Name','Userid','Password'])
        for i in range(len(gdata)):
            tc.add_row(gdata[i])
        print(tc)
            



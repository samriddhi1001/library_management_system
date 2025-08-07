import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="lms")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()
mycur.execute("select * from student_info")
data=mycur.fetchall()
mycur.execute("select * from teacher_info")
tdata=mycur.fetchall()
mycur.execute("select * from admin_info")
adata=mycur.fetchall()

from searchbook import *
from view import *
from adview import *
from modify import *
from addbook import *
from borrow import *
from returnbook import *
from lib_newaccount import *

while True:
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("                                                  LIBRARY MANAGEMENT SYSTEM                                               ")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print('1.Login for Student')
    print('2.Login for Teacher')
    print('3.Login for Admin')
    print('4.Create new Account')
    print('5.QUIT')

    while True:
        a=input('Enter your choice number(1/2/3/4/5): ')
        if a=='1' or a=='2' or a=='3' or a=='4' or a=='5':
            break
        elif a.isdigit()==False:
            print("Invalid choice ! Enter a numeric choice")
        else:
            print("Invalid choice ! ")
    ach=int(a)
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    if ach==1:
        usid=[]
        for i in range(len(data)):
            usid.append(data[i][2])
        while True:
            uid=input("Enter UserID : ")    
            if uid in usid:
                break
            else:
                print("Invalid USER ID!!!")
                
        mycur.execute("select password from student_info where userid='{}'".format(uid))
        pa=mycur.fetchall()
       
        while True:
            p=input("Enter Password : ")    
            if p==pa[0][0]:
                break
            else:
                print("Invalid Password!!!")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        while True:
            print(' MAIN MENU ')
            print('1. View')
            print('2. Search')
            print('3. Logout')
            

            while True:
                aa=input('Enter your choice number(1/2/3): ')
                if aa=='1' or aa=='2' or aa=='3':
                    break
                elif a.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    print("Invalid choice ! ")
            ach=int(aa)
            print("-----------------------------------------------------------------------------------------------------------------------------------")

            if ach==1:
                view()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            elif ach==2:
                searchbook()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            elif ach==3:
                break

    elif ach==2:
        
        usid=[]
        for i in range(len(tdata)):
            usid.append(tdata[i][2])
        uid=''
        while True:
            uid=input("Enter UserID : ")    
            if uid in usid:
                break
            else:
                print("Invalid USER ID!!!")
                
        mycur.execute("select password from teacher_info where userid='{}'".format(uid))
        pa=mycur.fetchall()
        p=''
        while True:
            p=input("Enter Password : ")    
            if p==pa[0][0]:
                break
            else:
                print("Invalid Password!!!")
        print("-----------------------------------------------------------------------------------------------------------------------------------")

        while True:
            print(" MAIN MENU ")
            print('1. View')
            print('2. Search')
            print('3. Logout')

            while True:
                aa=input('Enter your choice number(1/2/3): ')
                if aa=='1' or aa=='2' or aa=='3':
                    break
                elif a.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    print("Invalid choice ! ")
            ach=int(aa)
            print("-----------------------------------------------------------------------------------------------------------------------------------")
    
            if ach==1:
                view()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            elif ach==2:
                searchbook()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            elif ach==3:
                break

    elif ach==3:
        usid=[]
        for i in range(len(adata)):
            usid.append(adata[i][2])
        uid=''
        while True:
            uid=input("Enter UserID : ")    
            if uid in usid:
                break
            else:
                print("Invalid USER ID!!!")
                
        mycur.execute("select password from admin_info where userid='{}'".format(uid))
        pa=mycur.fetchall()
        p=''
        while True:
            p=input("Enter Password : ")    
            if p==pa[0][0]:
                break
            else:
                print("Invalid Password!!!")
        print("-----------------------------------------------------------------------------------------------------------------------------------")

        while True:
            print(" MAIN MENU ")
            print('1. View book details')
            print('2. View user details')
            print('3. Modify')
            print('4. Search')
            print('5. Add book')
            print('6. Borrow')
            print('7. Return')
            print('8. Logout')

            while True:
                aa=input('Enter your choice number(1/2/3/4/5/6/7/8): ')
                if aa=='1' or aa=='2' or aa=='3' or aa=='4' or aa=='5' or aa=='6' or aa=='7' or aa=='8':
                    break
                elif a.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    print("Invalid choice ! ")
            aach=int(aa)
            print("-----------------------------------------------------------------------------------------------------------------------------------")
    
            if aach==1:
                mycur.execute("select * from book_info")
                bdata=mycur.fetchall()
                mycur.execute("select * from available_books")
                adata=mycur.fetchall()
                mycur.execute("select * from borrowed_books")
                cdata=mycur.fetchall()
                mycur.execute("select * from tborrowed_books")
                ddata=mycur.fetchall()
                admin_view(bdata, adata, cdata, ddata)  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==2:
                admin_viewdetails()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==3:
                modify()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==4:
                searchbook()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==5:
                add_book()  #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==6:
                borrowbook()    #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==7:
                returnbook()   #needs to be imported
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            if aach==8:
                break
    elif ach==4:
        new_account()
        print("-----------------------------------------------------------------------------------------------------------------------------------")
    elif ach==5:
        break

import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="lms")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()

    
def modify():
    print(" MODIFY")
    print("\t1. Modify student details")
    print("\t2. Modify teacher details ")
    print("\t3. Modify admin details")
    print("\t4. Modify book details")
    
    while True:
        a=input('Enter your choice number(1/2/3/4) : ')
        if a=='1' or a=='2' or a=='3' or a=='4':
            break
        elif a.isdigit()==False:
            print("Invalid choice ! Enter a numeric choice")
        else:
            print("Invalid choice ! ")

    abc=int(a)
    if abc==1:
       mycur.execute("select * from student_info")
       data=mycur.fetchall()
       mycur.execute("select * from borrowed_books")
       sb=mycur.fetchall()
       print("\t\t1. Change Name")
       print("\t\t2. Change Grade")
       print("\t\t3. Change Section")
       print("\t\t4. Change UserID")
       print("\t\t5. Change Password")
       print("\t\t6. Delete Account")
    
       while True:
            b=input('Enter your choice number(1/2/3/4/5/6) : ')
            if b=='1' or b=='2' or b=='3' or b=='4' or b=='5' or b=='6':
                break
            elif b.isdigit()==False:
                print("Invalid choice ! Enter a numeric choice")
            else:
                print("Invalid choice ! ")
       ba=int(b)

       s=True
       adnos=[]
       for i in range(len(data)):
            adnos.append(data[i][0])
       sbb=[]
       for i in range(len(sb)):
            sbb.append(sb[i][7])
       while s == True:
            adn=input("Enter 8 digit Admission Number : ")
            if int(adn) not in adnos:
                 print("Admission Number doesn't exist ! ")
            elif int(adn) in sbb:
                 print("Student has borrowed a book, changes cannot be made!")
            else :
                 s =False
        
       while True:
            if adn.isdigit()==False:
                print("Admission Number can only have digits !")
                adn=input("Enter 8 digit Admission Number : ")
            elif len(adn)!=8:
                print("Admission Number must have 8 digits ! ")
                adn=input("Enter 8 digit Admission Number : ")
            else:
                break
       adno=int(adn)
                


       if ba==1:
            fname=input("Enter new student first name : ")
            while True:
                if fname.isalpha()==False:
                    print("First name can only consist of alphabets !")
                    fname=input("Enter first name : ")
                elif len(fname.strip())<3:
                    print("First name cannot have less than 3 characters !")
                    fname=input("Enter new student first name : ")
                else:
                    break
            fname=fname.strip()
            lname=input("Enter new student last name : ")
            while True:
                if lname.isalpha()==False:
                    print("Last name can only consist of alphabets !")
                    lname=input("Enter new student last name : ")
                else:
                    break
            lname=lname.strip()
            sname=fname+' '+lname
            mycur.execute("update student_info set name='{}' where adno={}".format(sname, adno))
            mycon.commit()
            print("Student Name changed successfully ! ")
            
       elif ba==2:
            g=input("Enter new student grade : ")
            while True:
                if g.isdigit()==False:
                    print("Grade cannot have negative numbers / alphabets / decimal numbers !")
                    g=input("Enter your grade : ")
                elif int(g)>12 :
                      print("Invalid grade ! Grade cannot be greater than 12 !")
                      g=input("Enter your grade : ")
                elif int(g)<1:
                    print("Invalid grade ! Grade cannot be less than 1 !")
                    g=input("Enter your grade : ")
                elif int(g)<0:
                    print("Invalid grade ! Grade cannot be less than 1 !")
                    g=input("Enter new student grade : ")
                else:
                    break
            grade=int(g)
            mycur.execute("update student_info set grade={} where adno={}".format(grade, adno))
            mycon.commit()
            print("Student Grade changed successfully ! ")

       elif ba==3:
            sec=input("Enter new student section : ")
            while True:
                if len(sec)>1:
                    print("Invalid input ! Section should have only 1 character")
                    sec=input("Enter your section : ")
                elif sec.isalpha()==False:
                    print("Invalid input ! Section should be an alphabet only")
                    sec=input("Enter new student section : ")
                else:
                    break
            sec=sec.strip()
            mycur.execute("update student_info set sec='{}' where adno={}".format(sec, adno))
            mycon.commit()
            print("Student Section changed successfully ! ")

       elif ba==4:
            users=[]
            for i in range(len(data)):
                users.append(data[i][2])
            while True:
                u = input('Enter new UserID (max 10 characters) : ')
                if len(u)>10:
                    print("Input has more than 10 characters !")
                elif u in users:
                     print("UserID already exists ! ENTER a NEW user ID")
                elif len(u)>10:
                    print("Input has more than 10 characters !")
                else :
                     break      
            
            u=u.strip()
            mycur.execute("update student_info set userid='{}' where adno={}".format(u, adno))
            mycon.commit()
            print("Student UserID changed successfully ! ")

       elif ba==5:
           while True:       
                pswd=input("Enter password (max 10 characters) : ")
                if len(pswd)>10:
                    print("Input has more than 10 characters !")
                else:
                    break
           pswd=pswd.strip()
           mycur.execute("update student_info set password='{}' where adno={}".format(pswd, adno))
           mycon.commit()
           print("Student Password changed successfully ! ")

       elif ba==6:
           mycur.execute("delete from student_info where adno={}".format(adno))
           mycon.commit()
           print("Student records deleted successfully")

       #teacher    
    elif abc==2:
           mycur.execute("select * from teacher_info")
           tdata=mycur.fetchall()
           mycur.execute("select * from tborrowed_books")
           tb=mycur.fetchall()
           print("\t\t1. Change Name")
           print("\t\t2. Change UserID")
           print("\t\t3. Change Password")
           print("\t\t4. Delete Account")
        

           while True:
                b=input('Enter your choice number(1/2/3/4) : ')
                if b=='1' or b=='2' or b=='3' or b=='4':
                    break
                elif b.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    print("Invalid choice ! ")
           ba=int(b)

           s=True
           tdnos=[]
           for i in range(len(tdata)):
                tdnos.append(tdata[i][0])
           tbb=[]
           for i in range(len(tb)):
               tbb.append(tb[i][5])
           while s == True:
                tdn=input("Enter 5 digit TeacherID : ")
                if int(tdn) not in tdnos:
                     print("TeacherID doesn't exist ! ")
                elif int(tdn) in tbb:
                     print("Teacher has borrowed a book, cannot make changes")
                else :
                     s =False
            
           while True:
                if tdn.isdigit()==False:
                    print("TeacherID can only have digits !")
                    tdn=input("Enter 5 digit TeacherID : ")
                elif len(tdn)!=5:
                    print("TeacherID must have 5 digits !")
                    tdn=input("Enter 5 digit TeacherID : ")
                else:
                    break
           tdno=int(tdn)       


           if ba==1:
                fname=input("Enter new Teacher first name : ")
                while True:
                    if fname.isalpha()==False:
                        print("First name can only consist of alphabets !")
                        fname=input("Enter first name : ")
                    elif len(fname.strip())<3:
                        print("First name cannot have less than 3 characters !")
                        fname=input("Enter new Teacher first name : ")
                    else:
                        break
                fname=fname.strip()
                lname=input("Enter new Teacher last name : ")
                while True:
                    if lname.isalpha()==False:
                        print("Last name can only consist of alphabets !")
                        lname=input("Enter new Teacher last name : ")
                    else:
                        break
                lname=lname.strip()
                sname=fname+' '+lname
                mycur.execute("update teacher_info set name='{}' where thid={}".format(sname, tdno))
                mycon.commit()
                print("Teacher Name changed successfully ! ")           
           
           elif ba==2:
                users=[]
                for i in range(len(tdata)):
                    users.append(tdata[i][2])
                while True:
                    u = input('Enter new UserID (max 10 characters) : ')
                    if len(u)>10:
                        print("Input has more than 10 characters !")
                    elif u in users:
                         print("UserID already exists ! ENTER a NEW user ID")
                    elif len(u)>10:
                        print("Input has more than 10 characters !")
                    else :
                         break
                u=u.strip()
                mycur.execute("update teacher_info set userid='{}' where thid={}".format(u,tdno))
                mycon.commit()
                print("Teacher UserID changed successfully ! ")

           elif ba==3:
               while True:       
                    pswd=input("Enter password (max 10 characters) : ")
                    if len(pswd)>10:
                        print("Input has more than 10 characters !")
                    else:
                        break
               pswd=pswd.strip()
               mycur.execute("update teacher_info set password='{}' where thid={}".format(pswd, tdno))
               mycon.commit()
               print("Teacher Password changed successfully ! ")

           elif ba==4:
               mycur.execute("delete from teacher_info where thid={}".format(tdno))
               mycon.commit()
               print("Teacher records deleted successfully")
      #Admin 
    elif abc==3:
           mycur.execute("select * from admin_info")
           adata=mycur.fetchall()
           print("\t\t1. Change Name")
           print("\t\t2. Change UserID")
           print("\t\t3. Change Password")
           print("\t\t4. Delete Account")       

           while True:
                b=input('Enter your choice number(1/2/3/4) : ')
                if b=='1' or b=='2' or b=='3' or b=='4':
                    break
                elif b.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    print("Invalid choice ! ")
           ba=int(b)

           s=True
           addnos=[]
           for i in range(len(adata)):
                addnos.append(adata[i][0])      
           while s == True:
                addn=input("Enter 3 digit AdminID : ")
                if int(addn) not in addnos:
                     print("AdminID doesn't exist ! ")
                else :
                     s =False
            
           while True:
                if addn.isdigit()==False:
                    print("AdminID can only have digits !")
                    addn=input("Enter 3 digit AdminID : ")
                elif len(addn)!=3:
                    print("AdminID must have 3 digits !")
                    addn=input("Enter 3 digit AdminID : ")
                else:
                    break
           addno=int(addn)                


           if ba==1:
                fname=input("Enter new Admin first name : ")
                while True:
                    if fname.isalpha()==False:
                        print("First name can only consist of alphabets !")
                        fname=input("Enter first name : ")
                    elif len(fname.strip())<3:
                        print("First name cannot have less than 3 characters !")
                        fname=input("Enter new Admin first name : ")
                    else:
                        break
                fname=fname.strip()
                lname=input("Enter new Admin last name : ")
                while True:
                    if lname.isalpha()==False:
                        print("Last name can only consist of alphabets !")
                        lname=input("Enter new Admin last name : ")
                    else:
                        break
                lname=lname.strip()
                sname=fname+' '+lname
                mycur.execute("update admin_info set name='{}' where adno={}".format(sname, addno))
                mycon.commit()
                print("Admin Name changed successfully ! ")           
           
           elif ba==2:
                users=[]
                for i in range(len(adata)):
                    users.append(adata[i][2])
                while True:
                    u = input('Enter new UserID (max 10 characters) : ')
                    if len(u)>10:
                        print("Input has more than 10 characters !")
                    elif u in users:
                         print("UserID already exists ! ENTER a NEW user ID")
                    elif len(u)>10:
                        print("Input has more than 10 characters !")
                    else :
                         break
                u=u.strip()
                mycur.execute("update admin_info set userid='{}' where adno={}".format(u,addno))
                mycon.commit()
                print("Admin UserID changed successfully ! ")

           elif ba==3:
               while True:       
                    pswd=input("Enter password (max 10 characters) : ")
                    if len(pswd)>10:
                        print("Input has more than 10 characters !")
                    else:
                        break
               pswd=pswd.strip()
               mycur.execute("update admin_info set password='{}' where adno={}".format(pswd, addno))
               mycon.commit()
               print("Admin Password changed successfully ! ")

           elif ba==4:
               mycur.execute("delete from admin_info where adno={}".format(addno))
               mycon.commit()
               print("Admin records deleted successfully")

    #book modify
    if abc==4:
        mycur.execute("select * from book_info")
        bdata=mycur.fetchall()
        mycur.execute("select * from borrowed_books")
        bbdata=mycur.fetchall()
        mycur.execute("select * from tborrowed_books")
        teacher=mycur.fetchall()
        print("\t\t1.Change Book Name")
        print("\t\t2.Change Author Name")
        print("\t\t3.Change Publisher Name")
        print("\t\t4.Change Cost")
        print("\t\t5.Change Genre")
        print("\t\t6.Delete Book")

        while True:
                b=input('Enter your choice number(1/2/3/4/5/6) : ')
                if b=='1' or b=='2' or b=='3' or b=='4' or b=='5' or b=='6':
                    break
                elif b.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    print("Invalid choice ! ")
        ba=int(b)

        s=True
        bnos=[]
        bd=[]
        td=[]
        for i in range(len(bbdata)):
            bd.append(bbdata[i][0])
        for i in range(len(bdata)):
            bnos.append(bdata[i][0])
        for i in range(len(teacher)):
            td.append(teacher[i][0])
            
        while s == True:
                bdn=input("Enter 4 digit Book ID : ")
                if int(bdn) not in bnos:
                     print("Book ID doesn't exist ! ")
                elif int(bdn) in bd:
                     print("Book has been borrowed ! Cannot make changes !")
                elif int(bdn) in td:
                     print("Book has been borrowed ! Cannot make changes !")
                else :
                     s =False
            
        while True:
                if bdn.isdigit()==False:
                    print("Book ID can only have digits !")
                    bdn=input("Enter 4 digit Book ID : ")
                elif len(bdn)!=4:
                    print("Book ID must have 4 digits !")
                    bdn=input("Enter 4 digit Book ID : ")
                else:
                    break
        bno=int(bdn)
        
        if ba==1:
            while True:
                bname=input("Enter New Book Name : ")
                if len(bname.strip())>50:
                    print("Book Name Cannot exceed 50 characters !")
                else:
                    break
            bname=bname.strip()
            mycur.execute("update book_info set bookname='{}' where bookid={}".format(bname,bno))
            mycon.commit()
            mycur.execute("update available_books set bookname='{}' where bookid={}".format(bname,bno))
            mycon.commit()
            print("Book Name Successfully Changed!")
        elif ba==2:
            while True:
                aname=input("Enter New Author Name : ")
                if len(aname.strip())>50:
                    print("Author Name Cannot exceed 50 characters !")
                else:
                    break
            aname=aname.strip()
            mycur.execute("update book_info set author='{}' where bookid={}".format(aname,bno))
            mycon.commit()
            mycur.execute("update available_books set author='{}' where bookid={}".format(aname,bno))
            mycon.commit()
            print("Author Name Successfully Changed!")
        elif ba==3:
            while True:
                pname=input("Enter New Publisher Name : ")
                if len(pname.strip())>50:
                    print("Publisher Name Cannot exceed 50 characters !")
                else:
                    break
            pname=pname.strip()
            mycur.execute("update book_info set publisher='{}' where bookid={}".format(pname,bno))
            mycon.commit()
            mycur.execute("update available_books set publisher='{}' where bookid={}".format(pname,bno))
            mycon.commit()
            print("Publisher Name Successfully Changed !")
        elif ba==4:
            while True:
                cname=input("Enter New Book Cost : ")
                if cname.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    break
            cname=cname.strip()
            c=int(cname)
            mycur.execute("update book_info set cost={} where bookid={}".format(c,bno))
            mycon.commit()
            print("Book Cost Successfully Changed!")
        elif ba==5:
            while True:
                gname=input("Enter New Book Genre : ")
                if len(gname.strip())>30:
                    print("Book Genre Cannot exceed 30 characters !")
                else:
                    break
            gname=gname.strip()
            mycur.execute("update book_info set genre='{}' where bookid={}".format(gname,bno))
            mycon.commit()
            print("Book Genre Successfully Changed!")
        elif ba==6:
               mycur.execute("delete from book_info where bookid={}".format(bno))
               mycon.commit()
               mycur.execute("delete from available_books where bookid={}".format(bno))
               mycon.commit()
               print("Book records deleted successfully!")   
            


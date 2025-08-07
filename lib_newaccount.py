import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="LMS")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()

def new_account():
    mycur.execute("select * from student_info")
    data=mycur.fetchall()
    mycur.execute("select * from teacher_info")
    tdata=mycur.fetchall()
    mycur.execute("select * from admin_info")
    adata=mycur.fetchall()
    print('Create new account for:')
    print('\t1.Student')
    print('\t2.Teacher')
    print('\t3.Admin')
    
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
        s=True
        adnos=[]
        for i in range(len(data)):
            adnos.append(data[i][0])      
        while s == True:
            adno=input("Enter 8 digit Admission Number : ")
            if int(adno) in adnos:
                 print("Admission Number already exists ! ")
            else :
                 s =False
        
        while True:
            if adno.isdigit()==False:
                print("Admission Number can only have digits !")
                adno=input("Enter 8 digit Admission Number : ")
            elif len(adno)!=8:
                print("Admission Number must have 8 digits !")
                adno=input("Enter 8 digit Admission Number : ")
            else:
                break
            
        fname=input("Enter your first name : ")
        while True:
            if fname.isalpha()==False:
                print("First name can only consist of alphabets !")
                fname=input("Enter your first name : ")
            elif len(fname.strip())<3:
                print("First name cannot have less than 3 characters !")
                fname=input("Enter your first name : ")
            else:
                break
        fname=fname.strip()
            
        lname=input("Enter your last name : ")
        while True:
            if lname.isalpha()==False:
                print("Last name can only consist of alphabets !")
                lname=input("Enter your last name : ")
            else:
                break
        lname=lname.strip()
        sname=fname+' '+lname
                
        us=True
        users=[]
        for i in range(len(data)):
            users.append(data[i][2])      
        while us == True:
            u = input('Enter UserID (max 10 characters) : ')
            if u in users:
                 print("UserID already exists ! ENTER a NEW user ID")
            elif len(u)>10:
                print("Input has more than 10 characters !")
            else :
                 us =False
        u=u.strip()

        while True:       
            pswd=input("Enter password (max 10 characters) : ")
            if len(pswd)>10:
                print("Input has more than 10 characters !")
            else:
                break
        pswd=pswd.strip()
        
        g=input("Enter your grade : ")
        while True:
            if g.isdigit()==False:
                print("Grade cannot have negative numbers / alphabets / decimal numbers/ special characters")
                g=input("Enter your grade : ")
            elif int(g)>12 :
                  print("Invalid grade ! Grade cannot be greater than 12")
                  g=input("Enter your grade : ")
            elif int(g)<1:
                print("Invalid grade ! Grade cannot be less than 1")
                g=input("Enter your grade : ")
            elif int(g)<0:
                print("Invalid grade ! Grade cannot be less than 1")
                g=input("Enter your grade : ")
            else:
                break
        grade=int(g)
            
        sec=input("Enter your section : ")
        while True:
            if len(sec)>1:
                print("Invalid input ! Section should have only 1 character")
                sec=input("Enter your section : ")
            elif sec.isalpha()==False:
                print("Invalid input ! Section should be an alphabet only")
                sec=input("Enter your section : ")
            else:
                break
        sec=sec.strip()
        
        mycur.execute("insert into student_info(adno, name, userid, password, grade, sec) values({}, '{}', '{}', '{}', {}, '{}')".format(int(adno), sname, u, pswd, int(g), sec))
        mycon.commit()
        print("Student account created successfully ! ")
        
    elif ach==2:
        x=True
        tids=[]
        for i in range(len(tdata)):
            tids.append(tdata[i][0])      
        while x == True:
            tid=input("Enter 5 digit TeacherID : ")
            if int(tid) in tids:
                 print("TeacherID already exists ! ")
            else :
                 x =False
        while True:
            if tid.isdigit()==False:
                print("TeacherID can only have digits !")
                tid=input("Enter 5 digit TeacherID : ")
            elif len(tid)!=5:
                print("TeacherID must have 5 digits !")
                tid=input("Enter 5 digit TeacherID : ")
            else:
                break
            
        tfname=input("Enter your first name : ")
        while True:
            if tfname.isalpha()==False:
                print("First name can only consist of alphabets !")
                tfname=input("Enter your first name : ")
            elif len(tfname.strip())<2:
                print("First name cannot have less than 3 characters !")
                fname=input("Enter your first name : ")
            else:
                break
        tfname=tfname.strip()
            
        tlname=input("Enter your last name : ")
        while True:
            if tlname.isalpha()==False:
                print("Last name can only consist of alphabets !")
                tlname=input("Enter your last name : ")
            else:
                break
        tlname=tlname.strip()
        tname=tfname+' '+tlname
                
        tus=True
        tusers=[]
        for i in range(len(tdata)):
            tusers.append(tdata[i][2])      
        while tus == True:
            tu = input('Enter UserID (max 10 characters) : ')
            if tu in tusers:
                 print("UserID already exists ! ENTER a NEW user ID")
            elif len(tu)>10:
               print("Input has more than 10 characters !")
            else :
                 tus =False
        tu=tu.strip()

        while True:
            tpswd=input("Enter password (max 10 characters) : ")
            if len(tpswd)>10:
                print("Input has more than 10 characters !")
            else:
                break
        tpswd=tpswd.strip()

        mycur.execute("insert into teacher_info(thid, name, userid, password) values({}, '{}', '{}', '{}')".format(int(tid), tname, tu, tpswd))
        mycon.commit()
        print("Teacher account successfully created ! ")

    elif ach==3:
        adpswd='adminpassword'
        while True:
            adp=input("Enter admin password : ")
            if adp!=adpswd:
                print("Wrong password ! Unauthorized user")
            else:
                break

        y=True
        adnos=[]
        for i in range(len(adata)):
            adnos.append(adata[i][0])      
        while y == True:
            adno=input("Enter 3 digit AdminID : ")
            if int(adno) in adnos:
                 print("AdminID already exists ! ")
            else :
                 y =False
        while True:
            if adno.isdigit()==False:
                print("AdminID can only have digits !")
                adno=input("Enter 3 digit AdminID : ")
            elif len(adno)!=3:
                print("AdminID must have 3 digits !")
                adno=input("Enter 3 digit AdminID : ")
            else:
                break
            
        afname=input("Enter your first name : ")
        while True:
            if afname.isalpha()==False:
                print("First name can only consist of alphabets !")
                afname=input("Enter your first name : ")
            elif len(afname.strip())<2:
                print("First name cannot have less than 3 characters !")
                aname=input("Enter your first name : ")
            else:
                break
        afname=afname.strip()
            
        alname=input("Enter your last name : ")
        while True:
            if alname.isalpha()==False:
                print("Last name can only consist of alphabets !")
                alname=input("Enter your last name : ")
            else:
                break
        alname=alname.strip()
        aname=afname+' '+alname
        
        ausers=[]
        aus=True
        for i in range(len(adata)):
            ausers.append(adata[i][2])      
        while aus == True:
            au = input('Enter UserID (max 10 characters) : ')
            if au in ausers:
                 print("UserID already exists ! ENTER a NEW user ID")
            elif len(au)>10:
                print("Input has more than 10 characters !")
            else :
                 aus =False
        au=au.strip()

        while True:
            apswd=input("Enter password (max 10 characters) : ")
            if len(apswd)>10:
                print("Input has more than 10 characters !")
            else:
                break
        apswd=apswd.strip()

        mycur.execute("insert into admin_info(adno, name, userid, password) values({}, '{}', '{}', '{}')".format(int(adno), aname, au, apswd))
        mycon.commit()
    
        print("Admin account successfully created ! ")
             

            
            
            
        

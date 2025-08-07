import mysql.connector as ctr
mycon=ctr.connect(host="localhost",user="root",password="Risa@1010",database="lms")
if mycon.is_connected()==False:
    print("Not connected")
mycur=mycon.cursor()

def add_book():
        mycur.execute("select * from book_info")
        bdata=mycur.fetchall()
        s=True
        bnos=[]
        for i in range(len(bdata)):
            bnos.append(bdata[i][0])      
        while s == True:
                bdn=input("Enter 4 digit Book id : ")
                if int(bdn) in bnos:
                     print("Book ID Already exists ! ")
                else :
                     s =False
            
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
        
        while True:
                bname=input("Enter New Book Name : ")
                if len(bname.strip())>50:
                    print("Book Name Cannot exceed 50 characters !")
                else:
                    break
        bname=bname.strip()

        while True:
                aname=input("Enter New Author Name : ")
                if len(aname.strip())>50:
                    print("Author Name Cannot exceed 50 characters !")
                else:
                    break
        aname=aname.strip()

        while True:
                pname=input("Enter New Publisher Name : ")
                if len(pname.strip())>50:
                    print("Publisher Name Cannot exceed 50 characters !")
                else:
                    break
        pname=pname.strip()

        while True:
                cname=input("Enter New Book Cost : ")
                if cname.isdigit()==False:
                    print("Invalid choice ! Enter a numeric choice")
                else:
                    break
        cname=cname.strip()
        c=int(cname)

        while True:
                gname=input("Enter New Book Genre : ")
                if len(gname.strip())>30:
                    print("Book Genre Cannot exceed 30 characters !")
                else:
                    break
        gname=gname.strip()
        mycur.execute("insert into book_info values({},'{}','available','{}','{}',{},'{}')".format(bno,bname,aname,pname,c,gname))
        mycon.commit()
        mycur.execute("insert into available_books values({},'{}','{}','{}')".format(bno,bname,aname,pname))
        mycon.commit()
        print("Book Successfully Added!")


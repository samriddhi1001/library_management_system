from database import get_connection

mycon, mycur = get_connection()

#tables:
#student info for admin
stuinfo="create table if not exists student_info(adno int not null, name varchar(20) not null,userid varchar(10) primary key, password varchar(10) not null,grade int not null, sec varchar(20) not null)"
#teacher info
teacherinfo="create table if not exists teacher_info(thid int not null, name varchar(30) not null, userid varchar(10) primary key,password varchar(10) not null);"
#admin info        
admininfo="create table if not exists admin_info(adno int not null, name varchar(30) not null, userid varchar(10) primary key,password varchar(10) not null)"
#books info
booksinfo="create table if not exists book_info(bookid int primary key, bookname varchar(50) not null,status varchar(30) not null, author varchar(50), publisher varchar(50), cost int, genre varchar(50))"
#student borrowed books
borrowedbooks="create table if not exists borrowed_books(bookid int primary key, bookname varchar(50) not null, studentname varchar(50) not null,grade int not null, sec varchar(20) not null, bdate date, duedate date not null, adno int not null)"
#teachers borrowed books
tborrowedbooks="create table if not exists borrowed_books(bookid int primary key, bookname varchar(50) not null, teachername varchar(50) not null, bdate date, duedate date not null, tid int not null)"
#available books
availbooks="create table if not exists available_books(bookid int primary key, bookname varchar(50) not null,author varchar(50) not null, publisher varchar(50) not null)"

mycur.execute(stuinfo)
mycur.execute(teacherinfo)
mycur.execute(admininfo)
mycur.execute(booksinfo)
mycur.execute(borrowedbooks)
mycur.execute(tborrowedbooks)
mycur.execute(availbooks)

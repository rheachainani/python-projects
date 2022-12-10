from tkinter import *
import mysql.connector as sq

def open_lib():
	lib = Tk()
	lib.title('School Library')
	lib.geometry('1000x500')
	lib.configure(bg='#008080')
	l1 = Label(lib, text='Welcome to School Library !', font=('Times new roman',12), fg='white', bg='#008080')
	l1.place(x=20,y=20)
	myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
	cursor = myc.cursor()

	def view_books():
		frame = LabelFrame(lib, text='List of Books',padx=15,pady=15, bg='light blue')
		frame.place(x=250,y=50)
		cursor.execute('select * from books')
		i=0
		for book in cursor:
			for j in range(len(book)):
				e = Entry(frame, width=23, bg='pink', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, book[j])
			i=i+1

	def add_stu():
		def submit():
			sname1 = sname.get()
			stuid1 = stuid.get()
			bid1 = bid.get()
			try:
				sql = "insert into students(stuid,sname,bid) values (%s,%s,%s)"
				val = (stuid1,sname1,bid1)
				cursor.execute(sql,val)
				messagebox.showinfo('Information','Record added succesfully !')
				update = 'update books set qty=qty-1 where bookid="%s"' %(bid1)
				cursor.execute(update)
				myc.commit()
			except Exception as e:
				messagebox.showerror('Error',e)
				myc.rollback()
				myc.close()
		add = Tk()
		add.title('Add Student Record')
		add.geometry('350x300')
		add.configure(bg='#476b6b')
		global stuid
		global sname
		global bid
		stuid_label = Label(add, text='Student ID',bg='light blue')
		stuid_label.place(x=50,y=50)
		sname_label = Label(add, text='Student Name',bg='light blue')
		sname_label.place(x=50,y=100)
		bid_label = Label(add, text='Book ID',bg='light blue')
		bid_label.place(x=50,y=150)
		stuid = Entry(add, width=25,bg='light blue')
		stuid.place(x=150,y=50)
		sname = Entry(add, width=25,bg='light blue')
		sname.place(x=150,y=100)
		bid = Entry(add, width=25,bg='light blue')
		bid.place(x=150,y=150)
		submit_btn = Button(add, text='Add Student Record', command=submit,bg='light blue')
		submit_btn.place(x=100,y=200)

	def view_books():
		frame = LabelFrame(lib, text='List of Books',padx=15,pady=15, bg='light blue')
		frame.place(x=300,y=50)
		cursor.execute('select * from books')
		i=0
		for book in cursor:
			for j in range(len(book)):
				e = Entry(frame, width=23, bg='#8080ff', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, book[j])
			i=i+1

	def view_stu1():
		stu = Tk()
		stu.title('Issued')
		cursor.execute('select students.stuid,students.sname,books.bname from students,books where students.status="issued" and students.bid=books.bookid')
		i=0
		for book in cursor:
			for j in range(len(book)):
				e = Entry(stu, width=23, bg='#d699ff', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, book[j])
			i=i+1

	def view_stu2():
		stu = Tk()
		stu.title('Returned')
		cursor.execute('select students.stuid,students.sname,books.bname from students,books where students.status="returned" and students.bid=books.bookid')
		i=0
		for book in cursor:
			for j in range(len(book)):
				e = Entry(stu, width=23, bg='#d699ff', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, book[j])
			i=i+1

	def return_book():
		def submit():
			stu = estu.get()
			book = ebook.get()
			try:
				returnb = "update students set status='Returned' where bid='%s' and stuid='%s'" %(book,stu)
				cursor.execute(returnb)
				update = 'update books set qty=qty+1 where bookid="%s"' %(book)
				cursor.execute(update)
				myc.commit()
				messagebox.showinfo('Information','Book Returned !')
			except Exception as e:
				messagebox.showerror('Error',e)
				myc.rollback()
				myc.close()
		global ebook 
		global estu 
		ret = Tk()
		ret.title('Return Book')
		ret.geometry('400x300')
		ret.configure(bg='#ac3939')
		lstu = Label(ret, text='Enter Student ID',bg='light blue')
		lstu.place(x=50,y=50)
		estu = Entry(ret, width=25,bg='light blue')
		estu.place(x=150,y=50)
		lbook = Label(ret, text='Enter Book ID',bg='light blue')
		lbook.place(x=50,y=100)
		ebook = Entry(ret, width=25,bg='light blue')
		ebook.place(x=150,y=100)
		b = Button(ret, text='Return Book',command=submit,bg='light blue')
		b.place(x=150,y=200)

	b1 = Button(lib, text = 'View list of books',command=view_books,bg='light blue')
	b1.place(x=70,y=100)
	b2 = Button(lib, text = 'Enter student record',command=add_stu,bg='light blue')
	b2.place(x=70,y=150)
	b3 = Button(lib, text = 'Update - Return Book',command=return_book,bg='light blue')
	b3.place(x=70,y=200)
	b4 = Button(lib, text = 'View list of students - Issued',command=view_stu1,bg='light blue')
	b4.place(x=70,y=250)
	b5 = Button(lib, text = 'View list of students - Returned',command=view_stu2,bg='light blue')
	b5.place(x=70,y=300)
	exitb = Button(lib, text='Exit',width=15, command=lib.destroy, bg='light blue')
	exitb.place(x=70,y=350)

def act():
	act = Tk()
	act.title('Activities and Events')
	act.geometry('400x400')
	act.configure(bg='#cc7a00')
	label1 = Label(act,text='Welcome to Activities and Events Section !',bg='#cc7a00',font=('Times new roman',12))
	label1.place(x=20,y=20)

	def up():
		up = Tk()
		up.title('Upcoming Events')
		myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
		cursor = myc.cursor()
		cursor.execute('select curdate()')
		today = cursor.fetchone()
		upc = "select event,catagory,evdate from events where evdate >= '%s'" %(today)
		cursor.execute(upc)
		i=0
		for ev in cursor:
			for j in range(len(ev)):
				e = Entry(up, width=23, bg='#d699ff', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, ev[j])
			i=i+1

	def past():
		past = Tk()
		past.title('Past Events')
		myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
		cursor = myc.cursor()
		cursor.execute('select curdate()')
		today = cursor.fetchone()
		pev = "select event,catagory,evdate from events where evdate < '%s'" %(today)
		cursor.execute(pev)
		i=0
		for pastev in cursor:
			for j in range(len(pastev)):
				e = Entry(past, width=23, bg='#d699ff', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, pastev[j])
			i=i+1

	def achieve():
		ach = Tk()
		ach.title('School Achievements')
		myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
		cursor = myc.cursor()
		cursor.execute('select event,winner from events where winner is not null')
		i=0
		for win in cursor:
			for j in range(len(win)):
				e = Entry(ach, width=23, bg='#d699ff', font=('Times New Roman',8))
				e.grid(row=i, column=j)
				e.insert(END, win[j])
			i=i+1

	b1 = Button(act,text='View Upcoming Events',width=35,bg='#ffad33',command=up).place(x=70,y=70)
	b2 = Button(act,text='View Past Events',width=35,bg='#ffad33',command=past).place(x=70,y=110)
	b3 = Button(act,text='School Achievements',width=35,bg='#ffad33',command=achieve).place(x=70,y=150)
	b3 = Button(act,text='Exit',width=35,bg='#ffad33',command=act.destroy).place(x=70,y=230)

def main_page():
	root = Tk()
	root.title('Mini Management System')
	root.geometry('550x230')
	root.configure(bg='#666699')
	frame1 = LabelFrame(root, bg='#b3b3cc', padx=55, pady=25)
	frame1.grid(row=1,column=1)
	b1 = Button(frame1, text="Library",command=open_lib,bg='light blue')
	b1.pack()
	frame2 = LabelFrame(root, bg='#b3b3cc', padx=28, pady=25)
	frame2.grid(row=2,column=0)
	b2 = Button(frame2, text="Activities and Events",bg='light blue',command=act)
	b2.pack()
	exitf = LabelFrame(root, bg='light blue', padx=45, pady=25)
	exitf.grid(row=2,column=2)
	exitb = Button(exitf, text='Exit',width=10, command=root.destroy,bg='#b3b3cc')
	exitb.pack()
	
def check():
	if E1.get()=='school' and E2.get()=='abc123':
		main_page()
		login.destroy()
	else:
		messagebox.showerror('Error','Invalid Credentials')

login = Tk()
login.geometry('550x200')
login.configure(bg='#339966')
login.title('Password Authentication')

L = Label(login, text='Please enter the correct user id and password in order to login into the system', font=('Times New Roman',12),bg='#339966')
L.place(x=20,y=20)

L1 = Label(login, text='Enter UserID ',bg='#339966')
L1.place(x=20,y=70)

E1 = Entry(login, width=25, bg='#8cd9b3')
E1.place(x=150,y=70)

L2 = Label(login, text='Enter Password ',bg='#339966')
L2.place(x=20,y=100)

E2 = Entry(login, width=25, bg='#8cd9b3', show='*')
E2.place(x=150,y=100)

B1 = Button(login, text='Log In', bg='#8cd9b3', command=check)
B1.place(x=180,y=150)


login.mainloop()

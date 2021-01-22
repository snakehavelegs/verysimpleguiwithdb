from tkinter import *
import sqlite3
from tkinter import messagebox
import time
#clickfunction
def newwindow():
	global data
	data= Tk()
	data.title('Users')
	data.geometry('200x450')
	datausers= Label(data, text= recorded).grid(row=5, column=0)
	data.mainloop()


def myShowall():
	conn= sqlite3.connect('data.db')
	c= conn.cursor()
	c.execute("SELECT *, oid FROM users")
	records= c.fetchall()
	global recorded
	recorded= ''
	for record in records:
		recorded+= str(record) + '\n'
	conn.commit()
	conn.close()
	e.delete(0,END)
	newwindow()

def myAdd(name):
	conn= sqlite3.connect('data.db')
	c= conn.cursor()
	c.execute("INSERT INTO users VALUES (?)", (name,))
	conn.commit()
	conn.close()

def myClick():
	user = e.get()
	response = messagebox.askquestion('Confirm that?')
	if response == 'yes':
		myAdd(user)
	else:
		print('nonie')
		e.delete(0, END)

def myDelete():
	conn= sqlite3.connect('data.db')
	c= conn.cursor()
	c.execute("DELETE FROM users WHERE oid= " + e.get())
	conn.commit()
	conn.close()
	e.delete(0, END)




	

#GUI
root = Tk()
root.title('JoinIN')
root.geometry('400x300')



#time
def clock():

	hour = time.strftime('%H')
	minute= time.strftime('%M')
	seconds= time.strftime('%S')
	myclock.config(text= hour + ":" + minute + ":" + seconds)
	myclock.after(1000, clock)
#Label
myLabel = Label(root, text= "\n\n\n\n\nHello! Provide Your name.")
myLabel.grid(row=0, column=0)
myclock= Label(root, text='New text')
myclock.grid(row=4, column=2)

#Entry
e = Entry(root, width = 50)
e.grid(row=1, column=0, pady=2, padx= 20)

#Buttons
myButton_next = Button(root, text= 'Next', command= myClick)
myButton_next.grid(row=2, column=0, columnspan=2)
myButton_delete = Button(root, text= 'Delete', command= myDelete)
myButton_delete.grid(row= 3, column= 0, columnspan=1)
myButton_showall = Button(root, text= 'Show all', command= myShowall)
myButton_showall.grid(row= 4, column=0, columnspan=2)


clock()
root.mainloop()
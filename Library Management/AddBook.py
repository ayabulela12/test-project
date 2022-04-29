from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import mysql.connector

def connection():
    conn = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)

cur = con.cursor() 

# function register book
def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo('Error', "Can't add book to database")

    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()



def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, cur, con, bookTable, root
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass="root"
    mydatabase = "mydb"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    #enter the table name here
    bookTable = "books" #book table

    #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #book ID
    lb1 = Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for book Id
    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    #title
    lb2 = Label(LabelFrame, text="Title: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    #entry for title
    bookInfo2 = Entry(LabelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #author
    lb3 = Label(LabelFrame, text="Author: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry for author
    bookInfo3 = Entry(LabelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #Status
    lb4 = Label(LabelFrame, text="Status: ", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    #entry for status
    bookInfo4 = Entry(LabelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg="#d1ccc0", fg="black", command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Quit", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()



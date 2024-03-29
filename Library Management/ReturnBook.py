from tkinter import *
from PIL import ImageTk,Image 
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *


mypass = "Polarbear" 
mydatabase="mydb" 

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)


cur = con.cursor()

allBid = []  

def ReturnBook():
    global submitBtn, quitBtn, LabelFrame, lb1, Canvas1, bookInfo1, root, status

    bid = bookInfo1.get()
    extractBid = "select bid from "+issueTable

    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False
        
        else:
            messagebox.showinfo("Error", "Book Id is not Present")

    except:
        messagebox.showinfo("Error", "Can't Fetch the book Id")

    #remove that book from issueTable
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"

    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'available' where bid='"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(updateStatus)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book returned successfully")

        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book id")
            root.destroy()
            return

    except:
        messagebox.showinfo("Search Error", "the valur youentered is wrong, try again!")

    allBid.clear()
    root.destroy()

def returnBook():
    global root, con, cur, labelFrame, submitBtn, quitBtn, Canvas1, bookInfo1, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="pink")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg="black", fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #book id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit Button
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=Return)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
#End

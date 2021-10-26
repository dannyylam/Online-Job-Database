'''
CISP71 Python
CRUD GUI SQLite3 Project
Online Jobs Database
by Danny Lam
11/20/20
'''


from tkinter import *
#import for message boxes
import tkinter.messagebox as mb
#import for Treeview
import tkinter.ttk as ttk
#import combobox
from tkinter.ttk import Combobox

#import database class db.py
from db import Database

#create a path variable
path = '/Users/dannylam/Documents/School/CISP71 - Python/PROJECT/Online_Jobs_Database/'
#create an object of database class
db = Database(path+'Jobs.db')

#create a window object
root = Tk()

#add title for window
root.title('ONLINE JOBS DATABASE')
label_title = Label(root,
                        text="ONLINE JOBS DATABASE",
                        font=("Helvetica",28))

#size of window
root.geometry('800x600+350+150')

#function to load(refresh) the databasae
def load_data():
    for row in tvJob.get_children():
        tvJob.delete(row)
    for row in db.fetch():
        JobID = row[1]
        Position = row[2]
        Company = row[3]
        Location = row[4]
        Experience = row[5]
        Salary = row[6]
        tvJob.insert("", 'end', text=JobID,
                        values=(JobID,Position,Company,Location,Experience,Salary))

#declare function to validate the inputs
def validate_entry():
    if entry_position.get() == '':
        mb.showinfo('Information', 'Please Enter Job Position')
        entry_position.focus_set()
        return

    if entry_company.get() == '':
        mb.showinfo('Information', 'Please Enter Company Name')
        entry_company.focus_set()
        return

    if entry_location.get() == '':
        mb.showinfo('Information', 'Please Enter Job Location')
        entry_location.focus_set()
        return

    if cb_experience.get() == '':
        mb.showinfo('Information', 'Please Enter Job Experience')
        cb_experience.focus_set()
        return

    if entry_salary.get() == '':
        mb.showinfo('Information', 'Please Enter Salary Amount')
        entry_salary.focus_set()
        return


#declare functions for button events
def input_job():
    validate_entry()
    #call db.insert method from database class
    db.insert(entry_jobID.get(), 
                entry_position.get(), 
                entry_company.get(), 
                entry_location.get(), 
                cb_experience.get(), 
                entry_salary.get())
    #call function to clear text
    clear_form()
    #call function to reload updated data
    load_data()

def update_job():
    validate_entry()
    #call db.update method from database class
    db.update(entry_jobID.get(), 
                entry_position.get(), 
                entry_company.get(), 
                entry_location.get(), 
                cb_experience.get(), 
                entry_salary.get())
    #call function to clear text
    clear_form()
    #call function to reload updated data
    load_data()

def delete_job():
    if entry_jobID.get()=='':
        mb.showinfo('Information', 'Select a job listing to delete')
        return
    MsgBox = mb.askquestion('Delete Job', 'Are you sure you want to deleted selected job listing?', icon='warning')
    if MsgBox == 'yes':
        #call db.remove method from database class
        db.remove(entry_jobID.get())
        #call function to clear text
        clear_form()
        #call function to reload updated data
        load_data()

def clear_form():
    entry_jobID.delete(0, END)
    entry_position.delete(0, END)
    entry_company.delete(0, END)
    entry_location.delete(0, END)
    cb_experience.delete(0, END)
    entry_salary.delete(0, END)

def exit():
    MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
    if MsgBox == 'yes':
        #closes application
        root.destroy()

def show_search_record():
    return

def show_selected_record(event):
    clear_form()
    for selection in tvJob.selection():
        item = tvJob.item(selection)
        global job_id
        job_id,position,company,location,experience,salary = item['values'][0:6]
        entry_jobID.insert(0,job_id)
        #disable editing the jobID
        #entry_jobID.configure(state='disabled')
        entry_position.insert(0,position)
        entry_company.insert(0,company)
        entry_location.insert(0,location)
        cb_experience.insert(0,experience)
        entry_salary.insert(0,salary)
    return job_id


#create labels for each field
label_jobID = Label(root,
                        text="JobID",
                        font=("Helvetica",14))

label_position = Label(root,
                        text="Position",
                        font=("Helvetica",14))
            
label_company = Label(root,
                        text="Company",
                        font=("Helvetica",14))

label_location = Label(root,
                        text="Location",
                        font=("Helvetica",14))

label_experience = Label(root,
                        text="Experience",
                        font=("Helvetica",14))

label_salary = Label(root,
                        text="Salary",
                        font=("Helvetica",14))


#create entry box
entry_jobID = Entry(root)
entry_position = Entry(root)
entry_company = Entry(root)
entry_location = Entry(root)
#entry_experience = Entry(root)
entry_salary = Entry(root)

#create combobox for job experience
experience = ('Internship', 'Entry level', 'Associate', 'Senior', 'Executive')
cb_experience = Combobox(root, values=experience)


#create buttons
button_input = Button(root,
                        text="Register",
                        font=("Helvetica",14),
                        command=input_job)

button_update = Button(root,
                        text="Update",
                        font=("Helvetica",14),
                        command=update_job)

button_delete = Button(root,
                        text="Delete",
                        font=("Helvetica",14),
                        command=delete_job)

button_clear = Button(root,
                        text="Clear",
                        font=("Helvetica",14),
                        command=clear_form)

button_showAll = Button(root,
                        text="Show All",
                        font=("Helvetica",14),
                        command=load_data)

button_exit = Button(root,
                        text="Exit",
                        font=("Helvetica",14),
                        command=exit)                        

#CREATE A TREEVIEW

#specify a tuple colum
columns = ('#1','#2','#3','#4','#5','#6')

#create treeview specify the columns
tvJob = ttk.Treeview(root,show='headings',height='5', columns=columns)

#specify heading corresponding columns
tvJob.heading('#1', text='JobID', anchor='center')
tvJob.column('#1', width=30,anchor='center', stretch=False)

tvJob.heading('#2', text='Position', anchor='center')
tvJob.column('#2', width=100,anchor='center', stretch=True)

tvJob.heading('#3', text='Company', anchor='center')
tvJob.column('#3', width=60,anchor='center', stretch=True)

tvJob.heading('#4', text='Location', anchor='center')
tvJob.column('#4', width=60,anchor='center', stretch=True)

tvJob.heading('#5', text='Experience', anchor='center')
tvJob.column('#5', width=50,anchor='center', stretch=True)

tvJob.heading('#6', text='Salary', anchor='center')
tvJob.column('#6', width=50,anchor='center', stretch=True)


#create a vertical scrollbar for treeview
vsb = ttk.Scrollbar(root, orient=VERTICAL, command=tvJob.yview)
#place the vsb
vsb.place(x=93 + 640 + 1, y=309, height=180 + 15)
#configure treeview that it will use the vsb for y-axis scrollbar
tvJob.configure(yscroll=vsb.set)


#create a horizontal scrollbar
hsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=tvJob.xview)
#place the hsb
hsb.place(x=52, y=300+200+5, width=620 + 62)
#configure treeview that it will use the vsb for y-axis scrollbar
tvJob.configure(xscroll=hsb.set)

#bind treeview to the function show_selected_record
tvJob.bind('<<TreeviewSelect>>', show_selected_record)

#place the labels on window
label_title.place(x=200,y=20,height=27,width=400)
label_jobID.place(x=10,y=80,height=23,width=200)
label_position.place(x=10,y=130,height=23,width=200)
label_company.place(x=10,y=180,height=23,width=200)
label_location.place(x=350,y=80,height=23,width=200)
label_experience.place(x=350,y=130,height=23,width=200)
label_salary.place(x=350,y=180,height=23,width=200)

#place entry widents on window
entry_jobID.place(x=150,y=80,height=30,width=186)
entry_position.place(x=150,y=130,height=30,width=186)
entry_company.place(x=150,y=180,height=30,width=186)
entry_location.place(x=490,y=80,height=30,width=186)
#entry_experience.place(x=320,y=180,height=21,width=186)
cb_experience.place(x=490,y=130,height=30,width=186)
entry_salary.place(x=490,y=180,height=30,width=186)

#place the buttons
button_input.place(x=150,y=245,height=25,width=75)
button_update.place(x=250,y=245,height=25,width=75)
button_delete.place(x=350,y=245,height=25,width=75)
button_clear.place(x=450,y=245,height=25,width=75)
button_showAll.place(x=550,y=245,height=25,width=75)
button_exit.place(x=350,y=550,height=28,width=75)

#place treeview widget
tvJob.place(x=50,y=290,height=230,width=700)

#load data in table when application starts
load_data()

#start the program
root.mainloop()
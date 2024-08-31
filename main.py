import tkinter
from tkinter import *

#screen
root = Tk()
root.title("To-do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file=open("tasklist.txt",'w')
        file.close()

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete(ANCHOR)


#icon
Image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False, Image_icon)

#Top bar
Top_image = PhotoImage(file="images/topbar.png")
Label(root, image=Top_image).pack()

dock_image = PhotoImage(file="images/dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30,y=25)

note_image = PhotoImage(file="images/task.png")
Label(root, image=note_image, bg="#32405b"). place(x=340,y=25)

heading = Label(root, text="ALL TASK", font =("Arial 20 bold"), fg="white", bg="#32405b") 
heading.place(x=130,y=20)

#main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()


btn = Button(frame, text="ADD", font="arial 20 bold", width =6, bg ='#5a95ff', fg="#fff", bd=0, command= addTask)
btn.place(x=300,y=7)

#listbox
frame1 = Frame(root, bd=3, width=700, height=200, bg ="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font="arial 12", width=40, height=16,bg ="#32405b",fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scroll = Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

openTaskFile()

#delete

Delete_icon = PhotoImage(file="images/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


root.mainloop()

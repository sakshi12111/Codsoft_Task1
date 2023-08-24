import tkinter #for GUI 
from tkinter import messagebox
from tkinter import ttk
import pickle

root=tkinter.Tk()
root.title("Today's Work")
root.geometry("550x450")
root.configure(bg="black")

text = tkinter.Label(text="TODAY'S TASKS",font=("Comic Sans MS",20,"bold"),bg="black",fg="white")
text.place(x=70,y=120)
text.pack()

def add_task():
    task=enter_task.get()
    if task!="":
        listbox_tasks.insert(tkinter.END,task)
        enter_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="WARNING!",message="Please enter a valid task.")

def delete_task():
    try:
      task_name=listbox_tasks.curselection()[0]
      listbox_tasks.delete(task_name)
    except:
        tkinter.messagebox.showwarning(title="WARNING!",message="Please select a particular task.")


def load_task():
    try:
       tasks=pickle.load(open("tasks.txt","rb"))
       for task in tasks:
           listbox_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="WARNING!",message="Cannot find any tasks!")
def save_task():
    tasks=listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks,open("tasks.txt","wb"))

frame_task=tkinter.Frame(root,bg="#1183e6")
frame_task.pack(padx=10,pady=20)

listbox_tasks=tkinter.Listbox(frame_task,height=10,width=50,bg="grey",font=("Comic Sans MS",10,"bold"),fg="white")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar=tkinter.Scrollbar(frame_task,bg="lightgrey")
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
enter_task=tkinter.Entry(root,width=50,font=("Comic Sans MS",8,"bold"))
enter_task.pack()

button_add_task=tkinter.Button(root,text="ADD TASK",width=35,bg="#1183e6",font=("Comic Sans MS",8,"bold"),command=add_task)
button_add_task.pack(pady=3)

button_del_task=tkinter.Button(root,text="TASK COMPLETED",width=35,bg="#01f733",font=("Comic Sans MS",8,"bold"),command=delete_task)
button_del_task.pack(pady=3)

button_load_task=tkinter.Button(root,text="LOAD TASK",width=35,bg="#1183e6",font=("Comic Sans MS",8,"bold"),command=load_task)
button_load_task.pack(pady=3)

button_save_task=tkinter.Button(root,text="SAVE TASK",width=35,bg="#1183e6",font=("Comic Sans MS",8,"bold"),borderwidth=5,border="2",command=save_task)
button_save_task.pack(pady=3)


root.mainloop()
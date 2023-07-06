from textblob import TextBlob
from tkinter import *
def spell_check():
    get_data=Enter1.get()
    read=TextBlob(get_data)
    corrected=read.correct()
    Enter2.delete(0,END)
    Enter2.insert(0,corrected)

def tkinter1():
    global Enter1,Enter2
    win=Tk()
    win.geometry("500x400")
    win.resizable(False,False)
    win.title("Spell_Checker")
    win.config(bg="blue")
    
    label1=Label(win,text="Incorrect Spelling" ,font=("Time New Roman",20,"bold"),bg="blue",fg="yellow")
    label1.place(x=100,y=10,width=300,height=50)
     
    Enter1=Entry(win,font=("Time New Roman",20),bg="white",fg="black")
    Enter1.place(x=50,width=400,height=50,y=70)
    
    
    label2=Label(win,text="Corrected Spelling",font=("Time New Roman",20,"bold"),bg="blue",fg="yellow")
    label2.place(x=100,width=300,height=50,y=130)
    
    Enter2=Entry(win,font=("Time New Roman",20),bg="white",fg="black")
    Enter2.place(x=50,width=400,height=50,y=190)
    
    button=Button(win,text="Submit&Correct",font=("Time New Roman",20,"bold"),fg="black",bg="yellow" ,command=spell_check)
    button.place(x=100,width=300,height=50,y=270)
    
    win.mainloop()  
tkinter1()

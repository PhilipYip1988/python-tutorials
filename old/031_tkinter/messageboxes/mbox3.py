from tkinter import Tk, Frame, Label, Button
from tkinter.constants import NSEW
from tkinter import messagebox

tk = Tk()
tk.title("Message Box")

def showinfo():
    showinforesponse = messagebox.showinfo("Information", "This is an information messagebox.")
    global responselabel
    responselabel.forget()
    responselabel = Label(tk, text=showinforesponse)
    responselabel.grid(row=2, columnspan=3, sticky=NSEW)

def showwarning():
    showwarningresponse = messagebox.showwarning("Warning", "This is a warning messagebox")
    global responselabel
    responselabel.forget()
    responselabel = Label(tk, text=showwarningresponse)
    responselabel.grid(row=2, columnspan=3, sticky=NSEW)

def showerror():
    showerrorresponse = messagebox.showerror("Error", "This is an error messagebox")
    global responselabel
    responselabel.forget()
    responselabel = Label(tk, text=showerrorresponse)
    responselabel.grid(row=2, columnspan=3, sticky=NSEW)

def askquestion():
    askquestionresponse = messagebox.askquestion("Question", "Is this a question box?")
    global responselabel
    responselabel.forget()
    responselabel = Label(tk, text=askquestionresponse)
    responselabel.grid(row=2, columnspan=3, sticky=NSEW)

def askokcancel():
    askokcancelresponse = messagebox.askokcancel("Ask Ok Cancel", "Is this an ok cancel box?")
    global responselabel
    responselabel.forget()
    responselabel = Label(tk, text=askokcancelresponse)
    responselabel.grid(row=2, columnspan=3, sticky=NSEW)

def askyesno():
    yesnoresponse = messagebox.askyesno("Ask Yes No", "Is this a yes no box?")
    global responselabel
    responselabel.forget()
    if(yesnoresponse == 1):
        responselabel = Label(tk, text="You Accepted Your Mission!")
        responselabel.grid(row=2, columnspan=3, sticky=NSEW)
    else:
        responselabel = Label(tk, text="You Aborted Your Mission!")
        responselabel.grid(row=2, columnspan=3, sticky=NSEW)

button1 = Button(tk, text="Information", command=showinfo)
button1.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

button2 = Button(tk, text="Warning", command=showwarning)
button2.grid(row=0, column=1, padx=10, pady=10, sticky=NSEW)

button3 = Button(tk, text="Error", command=showerror)
button3.grid(row=0, column=2, padx=10, pady=10, sticky=NSEW)

button4 = Button(tk, text="Ask Question", command=askquestion)
button4.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

button5 = Button(tk, text="Ask Ok Cancel", command=askokcancel)
button5.grid(row=1, column=1, padx=10, pady=10, sticky=NSEW)

button6 = Button(tk, text="Ask Yes No", command=askyesno)
button6.grid(row=1, column=2, padx=10, pady=10, sticky=NSEW)

responselabel = Label(tk, text="Click a Message Box to View Changes")
responselabel.grid(row=2, columnspan=3, sticky=NSEW)

tk.mainloop()
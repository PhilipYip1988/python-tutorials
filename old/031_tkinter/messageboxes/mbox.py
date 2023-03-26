from tkinter import Tk, Frame, Label, Button
from tkinter.constants import NSEW
from tkinter import messagebox

tk = Tk()
tk.title("Message Box")

def showinfo():
    messagebox.showinfo("Information", "This is an information messagebox.")

def showwarning():
    messagebox.showwarning("Warning", "This is a warning messagebox")

def showerror():
    messagebox.showerror("Error", "This is an error messagebox")

def askquestion():
    messagebox.askquestion("Question", "Is this a question box?")

def askokcancel():
    messagebox.askokcancel("Ask Ok Cancel", "Is this an ok cancel box?")

def askyesno():
    messagebox.askyesno("Ask Yes No", "Is this a yes no box?")


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

tk.mainloop()
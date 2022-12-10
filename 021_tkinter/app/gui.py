from tkinter import Tk, Frame, Label, Button
from tkinter.constants import NSEW, CENTER
from PIL import Image, ImageTk
import glob
from itertools import cycle

tk = Tk()
tk.title("Image Viewer")
tk.geometry("800x600")

image_files = glob.glob('.\images\*.png')
images = {}

for idx, img_file in enumerate(image_files):
    img = Image.open(img_file)
    img.thumbnail((400, 300))
    tkimg = ImageTk.PhotoImage(img)
    images["img"+str(idx)] = tkimg

img_inc = cycle(images.keys())

imgframe = Frame(master=tk, width=400, height=300, background="#73bda0")
imgframe.place(relx=0.5, rely=0.5, anchor=CENTER)

imglabel = Label(master=imgframe, image=images[next(img_inc)])
imglabel.pack_propagate(False)
imglabel.pack()

def next_image():
    global imglabel
    global img_inc
    imglabel.pack_forget()
    imglabel = Label(master=imgframe, image=images[next(img_inc)])
    imglabel.pack_propagate(False)
    imglabel.pack()
    return None

def back_image():
    global imglabel
    global img_inc
    imglabel.pack_forget()
    for key in range(len(images)-2):
        next(img_inc)
    imglabel = Label(master=imgframe, image=images[next(img_inc)])
    imglabel.pack_propagate(False)
    imglabel.pack()
    return None

backbutton = Button(master=tk, text="◀", padx=20, pady=20,
                    background="#0067C0", foreground="#FFFFFF",
                    activebackground="#FFFFFF", activeforeground="#0067C0",
                    command=back_image)
backbutton.place(relx=0.1, rely=0.9, anchor=CENTER)

forwardbutton = Button(master=tk, text="▶", padx=20, pady=20,
                      background="#0067C0", foreground="#FFFFFF",
                      activebackground="#FFFFFF", activeforeground="#0067C0",
                      command=next_image)
forwardbutton.place(relx=0.9, rely=0.9, anchor=CENTER)

tk.mainloop()
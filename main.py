from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
import socket

#network initialization
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
host_ip =
s.connect((host_ip, port))

windowText = """"""

name = "Anonymous"

window = Tk()
window.title("Fortune Client")
text_area = scrolledtext.ScrolledText(window, wrap=WORD, width=95, height=10, font=("Times New Roman", 15))

image1 = Image.open("logofortune.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

label1.place(x=0, y=0)


text_area.grid(column=0, columnspan=14, pady=65, padx=10)
text_area.configure(state='disabled')

e = Entry(window, width=35, borderwidth=5)
e.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_enter():
    global windowText
    windowText = "" + windowText + "\n" + name + ": " + e.get()
    text_area.configure(state='normal')
    text_area.delete("1.0", "end")
    text_area.insert(END, windowText)
    text_area.configure(state='disabled')
    e.delete(0, END)

button_enter = Button(window, text="Enter", padx=91, pady=20, command=button_enter)
button_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)

# Put the buttons on the screen
button_clear.grid(row=4, column=5, columnspan=2)
button_enter.grid(row=4, column=7, columnspan=2)

window.mainloop()

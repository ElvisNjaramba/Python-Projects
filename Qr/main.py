import qrcode
from tkinter import *

root = Tk()
root.title('Qr code')
root.geometry("1000x550")
root.config(bg='red')
root.resizable(False, False)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/"+ str(name)+".png")

    global Image
    Image = PhotoImage(file="Qrcode/"+ str(name)+".png")
    Image_view.config(image=Image)

Image_view = Label(root, bg="#AE2321")
Image_view.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="Title", fg="white", bg="#AE2321", font=15).place(x=50, y=170)
title = Entry(root, width=13, font="arial 14")
title.place(x=50, y=200)

Label(root, text="Entry", fg="white", bg="#AE2321", font=15).place(x=50, y=270)
entry = Entry(root, width=28, font="arial 14")
entry.place(x=50, y=300)

Button(root, text="Generate", command=generate ).place(x=50, y=350)

root.mainloop()


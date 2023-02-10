import tkinter as tk
from tkinter import messagebox


class MYGUI:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('500x500')

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="close", command=self.on_delete)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="close instantly", command=exit)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message")
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.root, text="Show Messagebox", font=('arial', 16), variable=self.check_state)
        self.checkbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='submit', command=self.message)
        self.button.pack(pady=10, padx=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_delete)
        self.root.mainloop()

    def message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))

        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.message()

    def on_delete(self):
        if messagebox.askyesno(title="Quit", message="Are you sure you want to quit?? "):
            self.root.destroy()

MYGUI()
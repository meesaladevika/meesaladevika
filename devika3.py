import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

root = tk.Tk()
root.title("Simple Text Editor")

btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.pack()

text = tk.Text(root, width=40, height=10)
text.pack()

root.mainloop()

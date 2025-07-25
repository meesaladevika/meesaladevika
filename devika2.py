import tkinter as tk

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack()

listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack(pady=10)

root.mainloop()

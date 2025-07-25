import tkinter as tk
from tkinter import ttk, messagebox

class StudentDataListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data List")
        self.root.geometry("600x400")

        # Variables
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.class_var = tk.StringVar()

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Student ID").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.id_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Name").grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.name_var).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.age_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Class").grid(row=1, column=2, padx=5, pady=5)
        tk.Entry(input_frame, textvariable=self.class_var).grid(row=1, column=3, padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Student", command=self.add_student).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_student).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).grid(row=0, column=2, padx=10)

        # Treeview (Table)
        columns = ("id", "name", "age", "class")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="extended")
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100 if col != "name" else 180)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def add_student(self):
        sid = self.id_var.get().strip()
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        cls = self.class_var.get().strip()

        if not sid or not name or not age or not cls:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        # Optional: check if ID already exists in the tree
        for child in self.tree.get_children():
            if self.tree.item(child)["values"][0] == sid:
                messagebox.showerror("Duplicate ID", "Student ID already exists!")
                return

        self.tree.insert("", tk.END, values=(sid, name, age, cls))
        self.clear_fields()

    def delete_student(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "No student selected!")
            return
        for item in selected_items:
            self.tree.delete(item)

    def clear_fields(self):
        self.id_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.class_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDataListApp(root)
    root.mainloop()

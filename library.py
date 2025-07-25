import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

CSV_FILE = "library.csv"

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System with CSV")
        self.books = []

        # UI setup
        input_frame = tk.Frame(root, pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(input_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(input_frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(input_frame)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(root, pady=10)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Book", width=15, command=self.add_book).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Search by Title", width=15, command=self.search_book).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Show All Books", width=15, command=self.show_books).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Delete Selected", width=15, command=self.delete_book).grid(row=0, column=3, padx=10)

        self.tree = ttk.Treeview(root, columns=("Title", "Author", "Year"), show="headings")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Year", text="Year")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Load books from CSV on start
        self.load_books()
        self.show_books()

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()

        if not title or not author or not year:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        if not year.isdigit():
            messagebox.showwarning("Input Error", "Year must be a number")
            return

        self.books.append({"Title": title, "Author": author, "Year": year})
        self.save_books()
        self.clear_entries()
        self.show_books()
        messagebox.showinfo("Success", f"'{title}' added successfully.")

    def show_books(self, books=None):
        for item in self.tree.get_children():
            self.tree.delete(item)

        books_to_show = books if books is not None else self.books

        for book in books_to_show:
            self.tree.insert("", tk.END, values=(book["Title"], book["Author"], book["Year"]))

    def search_book(self):
        search_term = self.title_entry.get().strip().lower()
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter a title to search")
            return

        filtered = [book for book in self.books if search_term in book["Title"].lower()]
        if filtered:
            self.show_books(filtered)
        else:
            messagebox.showinfo("No Results", "No books found with that title.")

    def delete_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a book to delete")
            return

        values = self.tree.item(selected_item)["values"]
        title = values[0]

        self.books = [book for book in self.books if book["Title"] != title]
        self.save_books()
        self.show_books()
        messagebox.showinfo("Deleted", f"'{title}' has been deleted.")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

    def save_books(self):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Year"])
            writer.writeheader()
            writer.writerows(self.books)

    def load_books(self):
        if not os.path.exists(CSV_FILE):
            return
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.books = list(reader)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = LibraryApp(root)
    root.mainloop()

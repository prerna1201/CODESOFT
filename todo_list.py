# CODSOFT Internship Task 1 - GUI To-Do List
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")
task_entry = tk.Entry(root, width=25)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

root.mainloop()` `
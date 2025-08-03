""" Project: Task Scheduler """

import tkinter as tk
from tkinter import ttk
import json

def load_tasks(file_path = "part-08/task.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_tasks(tasks, file_path = "part-08/task.json"):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent = 4)

# load tasks into listbox
def update_task_list(tasks):
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task['completed'] else "✕"
        task_listbox.insert(tk.END, f"{task['title']} (Due: {task['due_date']}) [{status}]")

def add_task():
    title = title_entry.get()
    due_date = date_entry.get()
    
    if title and due_date:
        tasks.append({"title": title, "due_date": due_date, "completed": False})
        save_tasks(tasks)
        update_task_list(tasks)
        title_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        print("Task added successfully!")

def mark_task_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks[selected_index[0]]['completed'] = True
        save_tasks(tasks)
        update_task_list(tasks)

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks.pop(selected_index[0])
        save_tasks(tasks)
        update_task_list(tasks)
        print("Task deleted!")

# main window
root = tk.Tk()
root.title("Task Scheduler")
root.geometry("600x600")

# entry for the task title
title_label = tk.Label(root, text = "Task Title:")
title_label.pack(pady= 5)

title_entry = tk.Entry(root, width= 40)
title_entry.pack(pady= 5)

# entry for the due date
date_label = tk.Label(root, text = "Due Date (YYYY-MM-DD):")
date_label.pack(pady= 5)

date_entry = tk.Entry(root, width= 40)
date_entry.pack(pady= 5)

# button to add task
add_button = tk.Button(root, text = "Add task", command = add_task)
add_button.pack(pady= 10)

# task listbox
task_listbox = tk.Listbox(root, width = 50, height= 10)
task_listbox.pack(pady = 10)

complete_button = tk.Button(root, text = "Mark as Completed", command= mark_task_completed)
complete_button.pack(pady = 5)

delete_button = tk.Button(root, text = "Delete Task", command= delete_task)
delete_button.pack(pady = 5)

tasks = load_tasks()
update_task_list(tasks)

# run the application
root.mainloop()
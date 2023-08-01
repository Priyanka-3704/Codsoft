#import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task = task_entry.get()
    priority = priority_scale.get()
    if task:
        lb.insert(tk.END, f"{task} - Priority: {priority}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

def delete_task():
    selected_index = lb.curselection()
    if selected_index:
        lb.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed_task():
    selected_index = lb.curselection()
    if selected_index:
        index = selected_index[0]
        task = lb.get(index)
        if not task.endswith(" (Completed)"):
            lb.delete(index)
            lb.insert(index, task + " (Completed)")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

ws = tk.Tk()
ws.geometry('500x450+500+200')
ws.title('Attractive To-Do List')

# Create a canvas to simulate the frame-like container
canvas = tk.Canvas(ws, bg='#E1F5FE', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas)
frame.pack(pady=10)

lb = tk.Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 16),
    bd=0,
    fg='#000000',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    bg='#FFFFFF'  # white background for the listbox
)
lb.pack(side=tk.LEFT, fill=tk.BOTH)


task_list = [ ]

for item in task_list:
    lb.insert(tk.END, item)

sb = tk.Scrollbar(frame)
sb.pack(side=tk.RIGHT, fill=tk.Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

task_entry = tk.Entry(
    ws,
    font=('Arial', 24),
    bg='#FFFFFF'  # Light color background for the task entry box
)
task_entry.pack(pady=20)

priority_label = tk.Label(
    ws,
    text="Priority:",
    font=('Times', 14), 
    fg='#000000',  # BLACK text color
    background='#FFFFFF'  # white background for the label
)
priority_label.pack()

priority_scale = tk.Scale(
    ws,
    from_=1,
    to=10,
    orient=tk.HORIZONTAL,
    font=('Arial', 14),
    length=200,
    resolution=1,
    sliderlength=20,
    bg='#FFFFFF'  # Light color background for the priority scale
)

priority_scale.pack()

button_frame = ttk.Frame(ws)
button_frame.pack(pady=20)

add_btn = tk.Button(
    button_frame,
    text='Add Task',
    font=('Arial', 14),
    bg='#4CAF50',
    fg='#FFFFFF',
    padx=20,
    pady=10,
    command=add_task
)
add_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

del_btn = tk.Button(
    button_frame,
    text='Delete Task',
    font=('Arial', 14),
    bg='#FF5733',
    fg='#FFFFFF',
    padx=20,
    pady=10,
    command=delete_task
)
del_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

complete_btn = tk.Button(
    button_frame,
    text='Mark as Completed',
    font=('Arial', 14),
    bg='#FFAC33',
    fg='#FFFFFF',
    padx=20,
    pady=10,
    command=mark_completed_task
)
complete_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

ws.mainloop()

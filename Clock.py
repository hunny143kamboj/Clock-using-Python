import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, font=("Helvetica", 48), bg="red", fg="white")
label.pack(padx=20, pady=20)

update_time()

root.mainloop()

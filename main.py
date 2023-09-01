import tkinter as tk
import time


def my_time():
    time_string = time.strftime("%H:%M:%S %p")
    label.config(text=time_string)
    label.after(1000, my_time)


root = tk.Tk()
root.title("Clock")
root.minsize(width=10, height=10)
root.config(bg="black", padx=40, pady=20)

label = tk.Label(root, font=("Times New Roman", 36, "bold"), bg="black", fg="white")
label.pack()

# button = tk.Button(root, text="time", command=label_update)
# button.pack()

my_time()

root.mainloop()

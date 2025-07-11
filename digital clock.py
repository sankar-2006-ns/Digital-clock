from tkinter import *
from time import strftime

# Create the main window
root = Tk()
root.title("Digital Clock")

# Function to update time
def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)

# Label to display the clock
label = Label(root, font=('Arial', 50), background='black', foreground='cyan')
label.pack(anchor='center')

time()
root.mainloop()

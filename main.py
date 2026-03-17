import calendar
import tkinter as tk
from tkinter import messagebox

def show_calendar():
    try:
        year=int(year_entry.get())
        month=int(month_entry.get())

        if month<1 or month>12:
            messagebox.showerror("Error", "Please enter a valid month in numbers.")
            return
        
        result= calendar.month(year,month)
        output_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for year and month.")

# Window
root = tk.Tk()
root.title("CALENDAR APP")
# Input
tk.Label(root,text="Enter the year:").pack()
year_entry=tk.Entry(root)
year_entry.pack()

tk.Label(root,text="Enter the month in numbers:").pack()
month_entry=tk.Entry(root)
month_entry.pack()

#Button
tk.Button(root,text="Show Calendar",command=show_calendar).pack()

# Output
output_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
output_label.pack()

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def appointment():
    messagebox.showinfo(
        "Appointment",
        "Appointment booked successfully!\nDoctor: Dr. Sharma\nDate: Tomorrow\nTime: 10:00 AM"
    )

def reminder():
    messagebox.showinfo(
        "Medicine Reminder",
        "Take your medicine at 8:00 AM and 8:00 PM."
    )

def records():
    messagebox.showinfo(
        "Health Records",
        "Blood Group: O+\nBP: Normal\nSugar: Normal"
    )

def about():
    messagebox.showinfo(
        "About",
        "Hospital Healthcare App\nDeveloped using Python Tkinter."
    )

root = tk.Tk()
root.title("Hospital Healthcare App")
root.geometry("500x450")
root.configure(bg="#E8F6F3")

title = tk.Label(
    root,
    text="Hospital Healthcare App",
    font=("Arial", 22, "bold"),
    bg="#E8F6F3",
    fg="darkblue"
)
title.pack(pady=20)

tk.Button(
    root,
    text="Book Appointment",
    font=("Arial", 14),
    width=25,
    command=appointment
).pack(pady=10)

tk.Button(
    root,
    text="Medicine Reminder",
    font=("Arial", 14),
    width=25,
    command=reminder
).pack(pady=10)

tk.Button(
    root,
    text="View Health Records",
    font=("Arial", 14),
    width=25,
    command=records
).pack(pady=10)

tk.Button(
    root,
    text="About",
    font=("Arial", 14),
    width=25,
    command=about
).pack(pady=10)

tk.Button(
    root,
    text="Exit",
    font=("Arial", 14),
    width=25,
    bg="red",
    fg="white",
    command=root.destroy
).pack(pady=20)

root.mainloop()
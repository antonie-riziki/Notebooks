from tkinter import *
import tkinter as tk

window = tk.Tk()

window.title("GUI Window")
window.geometry("400x400")

def submit_button():
    print("Submission Successful.!!")

frame1 = tk.Frame( master = window, height = 400, width = 400, bg = "Red")

label1 = tk.Label(text = "Decorations  ", font = ("Times New Roman", 14))
label1.grid()

entry1 = tk.Entry()
entry1.grid(row = 0, column = 2, sticky = W)

button1 = tk.Button(text = "  Submit  ", font = ("Cambria", 12), command = submit_button)
button1.grid(row = 0, column = 15)

window.mainloop()

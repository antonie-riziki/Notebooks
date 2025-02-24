import tkinter as tk
from tkinter import *
#import messagebox as msgbox

homepage = tk.Tk()
homepage.title("MARWAN JEWELLERY STORES")
#homepage.geometry("1550x1000")
homepage.maxsize(1370,900)
homepage.minsize(1370,900)

homeFrame = tk.Frame(homepage, width = 30, height = 70).grid(row = 0, column = 0)
homepage.mainloop()

from tkinter import *

def main_screen():
    screen = Tk()
    screen.geometry("300x250")
    screen.title("First Python window")
    Label(text = "First Python Window", bg = "grey", width = "300", height = "3", font = ("calibri" , 16)).pack()
    Label(text = "").pack()
    Button (text = "Login", height = "4", width = "30").pack()
    Label(text = "").pack()
    Button (text = "Register", height = "4", width = "30").pack()

    screen.mainloop()

main_screen()

import tkinter as tk 
from tkinter import *
from __Generate_Hotfix import test1, test2, test3, test4
#reference: https://www.geeksforgeeks.org/python-gui-tkinter/

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    window.geometry("500x500")
    text1 = Button(text="1. Mod Header", font=("Times New Roman", 18), command = test1)
    text2 = Button(text="2. Choose File", font=("Times New Roman", 18), command = test2)
    text3 = Button(text="3. Find All References", font=("Times New Roman", 18), command = test3)
    text4 = Button(text="4. Make Regular Hotfix", font=("Times New Roman", 18), command = test4)

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    #add all widgets before
    window.mainloop()
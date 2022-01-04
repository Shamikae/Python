from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def myClick():

myButton = Button(root, text="click", padx=50)
myButton2 = Button(root, text="Hello World! Hi There")

myButton.grid(row=0, column=0)
myButton2.grid(row=1, column=1)


root.mainloop()

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)
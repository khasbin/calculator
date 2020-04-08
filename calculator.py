from tkinter import *
import parser

root = Tk()
root.title("Calculator")

i = 0
val = 0


# function for variable input
def varinput(num):
    global i
    global val
    if val == 0:
        display.insert(i, num)
        i += 1
    else:
        allclear()
        display.insert(i, num)
        val = 0


# function for operator input
def opinput(op):
    global i
    global val
    display.insert(i, op)
    i = i + 1
    val = 0


# funtion for delete input button
def delete():
    get_entry = display.get()
    n = len(get_entry)
    newstring = get_entry[0:n - 1]
    allclear()
    display.insert(0, newstring)


# function for All Clear(AC) button
def allclear():
    display.delete(0, END)


# function for evaluating the expression
def evaluation():
    global val
    get_entry = display.get()
    try:
        val = eval(parser.expr(get_entry).compile())
        allclear()
        display.insert(0, val)
    except Exception:
        allclear()
        display.insert(0, "MATH ERROR")


# function for factorial
def fact():
    n = int(display.get())
    factorial = 1
    if n == 0 or n == 1:
        allclear()
        display.insert(0, 1)
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
            allclear()
            display.insert(0, factorial)


# function for percentage calulation
def percentcalc():
    x = int(display.get())
    value = (x / 100)
    allclear()
    display.insert(0, value)


# adding the input field
display = Entry(root)
display.grid(row=1, columnspan=4, sticky=E + W)

# adding buttons to the calculator
Button(root, text="AC", width=6, command=allclear).grid(row=2, column=0)
Button(root, text="del", width=6, command=delete).grid(row=2, column=1)
Button(root, text="%", width=6, command=percentcalc).grid(row=2, column=2)
Button(root, text="/", width=6, command=lambda: opinput("/")).grid(row=2, column=3, padx=4, pady=3)

Button(root, text="7", width=6, command=lambda: varinput(7)).grid(row=3, column=0)
Button(root, text="8", width=6, command=lambda: varinput(8)).grid(row=3, column=1)
Button(root, text="9", width=6, command=lambda: varinput(9)).grid(row=3, column=2)
Button(root, text="*", width=6, command=lambda: opinput('*')).grid(row=3, column=3, padx=4, pady=3)

Button(root, text="4", width=6, command=lambda: varinput(4)).grid(row=4, column=0)
Button(root, text="5", width=6, command=lambda: varinput(5)).grid(row=4, column=1)
Button(root, text="6", width=6, command=lambda: varinput(6)).grid(row=4, column=2)
Button(root, text="-", width=6, command=lambda: opinput("-")).grid(row=4, column=3, padx=4, pady=3)

Button(root, text="1", width=6, command=lambda: varinput(1)).grid(row=5, column=0)
Button(root, text="2", width=6, command=lambda: varinput(2)).grid(row=5, column=1)
Button(root, text="3", width=6, command=lambda: varinput(3)).grid(row=5, column=2)
Button(root, text="+", width=6, command=lambda: opinput("+")).grid(row=5, column=3, padx=4, pady=3)

Button(root, text="0", width=6, command=lambda: varinput(0)).grid(row=6, column=0, padx=4, pady=3)
Button(root, text=".", width=6, command=lambda: opinput(".")).grid(row=6, column=1, padx=4, pady=3)
Button(root, text="=", width=14, command=evaluation, bd=3).grid(row=6, column=2, columnspan=2, padx=4, pady=3)

Button(root, text="x!", width=31, command=fact).grid(row=7, columnspan=4, padx=4, pady=3)

root.mainloop()
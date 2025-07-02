

🧮 Simple GUI Calculator Using Tkinter

A basic calculator built using Python's tkinter library. This project demonstrates GUI design, event handling, and basic arithmetic evaluation.


---

📝 Code Explanation (Line-by-Line)

import tkinter as tk

> ✅ Imports the tkinter module for GUI development.



app = tk.Tk()

> ✅ Initializes the main application window.



app.geometry('300x400')

> ✅ Sets the window dimensions to 300x400 pixels.



app.configure(bg='skyblue')

> ✅ Sets the background color of the window.



app.title('GUI Calculator')

> ✅ Sets the title of the window.



exp = ''
eq = tk.StringVar()

> ✅ exp stores the math expression.
✅ eq is a dynamic string variable connected to the display.




---

🔧 Functions

def press(key):
    global exp 
    exp += str(key)
    eq.set(exp)

> ✅ Appends the pressed key to the expression and updates the screen.



def clear():
    global exp 
    exp = ''
    eq.set('')

> ✅ Clears the current expression.



def calculation():
    try:
        global exp
        ans = str(eval(exp))
        eq.set(ans)
        exp = ans
    except:
        eq.set('ERROR')
        exp = ''

> ✅ Evaluates the current expression using eval().
✅ Catches errors and displays "ERROR" if the input is invalid.




---

💻 Entry (Display) Widget

entry = tk.Entry(app, textvariable=eq, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

> ✅ Creates a display field at the top of the calculator.
✅ Linked to the eq variable so it auto-updates with the expression/result.




---

🔘 Button Generator

def buttons(txt, col, row, cmd=None):
    return tk.Button(app, text=txt, command=cmd, padx=20, pady=20, bg='lightblue', font=('Arial',14)).grid(column=col, row=row)

> ✅ Function to simplify button creation.
✅ Accepts label, grid position, and function to run on click.




---

🔢 Button Layout

buttons('1', 0, 1, lambda: press(1))
buttons('2', 1, 1, lambda: press(2))
buttons('3', 2, 1, lambda: press(3))
buttons('-', 3, 1, lambda: press('-'))

buttons('4', 0, 2, lambda: press(4))
buttons('5', 1, 2, lambda: press(5))
buttons('6', 2, 2, lambda: press(6))
buttons('*', 3, 2, lambda: press('*'))

buttons('7', 0, 3, lambda: press(7))
buttons('8', 1, 3, lambda: press(8))
buttons('9', 2, 3, lambda: press(9))
buttons('/', 3, 3, lambda: press('/'))

buttons('0', 0, 4, lambda: press(0))
buttons('C', 1, 4, clear)
buttons('+', 2, 4, lambda: press('+'))
buttons('=', 3, 4, calculation)

> ✅ Buttons are placed in a grid layout (like a real calculator).
✅ Each button is connected to a function.




---

app.mainloop()

> ✅ Starts the event loop to keep the GUI responsive.




---

📌 Features

Clean and minimal layout.

Performs basic arithmetic: +, -, *, /

Error handling for invalid inputs.

Uses tk.StringVar() to auto-update display.



---

import tkinter as tk

app= tk.Tk()
app.geometry('300x400')
app.configure(bg='skyblue')
app.title('GUI Calculator')

exp=''
eq = tk.StringVar()

def press(key):
    global exp 
    exp += str(key)
    eq.set(exp)

def clear():
    global exp 
    exp=''
    eq.set('')

def calculation():
    try:
        global exp
        ans = str(eval(exp))
        eq.set(ans)
        exp=ans
    except:
        eq.set('ERROR')
        exp=''


entry = tk.Entry(app, textvariable=eq, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

def buttons(txt, col, row, cmd=None):
    return tk.Button(app, text=txt,  command=cmd, padx=20, pady=20, bg='lightblue',font=('Arial',14)).grid(column=col, row=row)

buttons('1',0, 1, lambda: press(1))
buttons('2',1, 1, lambda: press(2))
buttons('3',2, 1, lambda: press(3))
buttons('-',3, 1, lambda: press('-'))

buttons('4',0, 2, lambda: press(4))
buttons('5',1, 2, lambda: press(5))
buttons('6',2, 2, lambda: press(6))
buttons('*',3, 2, lambda: press('*'))

buttons('7',0, 3, lambda: press(7))
buttons('8',1, 3, lambda: press(8))
buttons('9',2, 3, lambda: press(9))
buttons('/',3, 3, lambda: press('/'))

buttons('0',0, 4, lambda: press(0))
buttons('C',1, 4, clear)
buttons('+',2, 4, lambda: press('+'))
buttons('=',3, 4, calculation)


app.mainloop()

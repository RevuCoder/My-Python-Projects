
def fun(Btn) :

    if (Btn['text'] == NIL and label['text'] == " X's Chance ") :
        Btn.configure(text = 'X', fg = 'red')
        label.configure(text = " O's Chance ", bg = 'blue')
        check()
    elif (Btn['text'] == NIL and label['text'] == " O's Chance ") :
        Btn.configure(text = '0', fg = 'blue')
        label.configure(text = " X's Chance ", bg = 'red')
        check()

def fun1() :
    fun(Btn1)
def fun2() :
    fun(Btn2)
def fun3() :
    fun(Btn3)
def fun4() :
    fun(Btn4)
def fun5() :
    fun(Btn5)
def fun6() :
    fun(Btn6)
def fun7() :
    fun(Btn7)
def fun8() :
    fun(Btn8)
def fun9() :
    fun(Btn9)

def win(winner, a, b, c) :

    if (winner == 1):
        label.configure(text = ' X wins ! ', bg = 'red')
        a['bg'] = 'red'
        a['fg'] = 'black'
        b['bg'] = 'red'
        b['fg'] = 'black'
        c['bg'] = 'red'
        c['fg'] = 'black'
        rr = messagebox.askretrycancel("Game Over", 'X won the game ! \n Want to retry ?')
        if (rr == True) :
            reset()
        else :
            root.destroy()

    elif (winner == 0):
        a['bg'] = 'blue'
        a['fg'] = 'black'
        b['bg'] = 'blue'
        b['fg'] = 'black'
        c['bg'] = 'blue'
        c['fg'] = 'black'
        label.configure(text = ' O wins ! ', bg = 'blue')
        rr = messagebox.askretrycancel("Game Over", 'O won the game ! \n Want to retry ?')
        if (rr == True) :
            reset()
        else :
            root.destroy()

    elif (winner == 2):
        label.configure(text = ' Match Tied ! ', bg = 'purple')
        rr = messagebox.askretrycancel("Game Over", 'Match Tied ! \n Want to retry ?')
        if (rr == True) :
            reset()
        else :
            root.destroy()    


def reset():
    label.configure(text = " X's Chance ", bg = 'red')
    Btn1['text'] = NIL
    Btn1['bg'] = 'black'
    Btn2['text'] = NIL
    Btn2['bg'] = 'black'
    Btn3['text'] = NIL
    Btn3['bg'] = 'black'
    Btn4['text'] = NIL
    Btn4['bg'] = 'black'
    Btn5['text'] = NIL
    Btn5['bg'] = 'black'
    Btn6['text'] = NIL
    Btn6['bg'] = 'black'
    Btn7['text'] = NIL
    Btn7['bg'] = 'black'
    Btn8['text'] = NIL    
    Btn8['bg'] = 'black'
    Btn9['text'] = NIL
    Btn9['bg'] = 'black'

def check() :
     
    if (Btn1['text'] == 'X' and Btn2['text'] == 'X' and Btn3['text'] == 'X') :
        win(1, Btn1, Btn2, Btn3)

    elif (Btn4['text'] == 'X' and Btn5['text'] == 'X' and Btn6['text'] == 'X') :
        win(1, Btn4, Btn5, Btn6)

    elif (Btn7['text'] == 'X' and Btn8['text'] == 'X' and Btn9['text'] == 'X') :
        win(1, Btn7, Btn8, Btn9)

    elif (Btn1['text'] == 'X' and Btn4['text'] == 'X' and Btn7['text'] == 'X') :
        win(1, Btn1, Btn4, Btn7)

    elif (Btn8['text'] == 'X' and Btn5['text'] == 'X' and Btn2['text'] == 'X') :
        win(1, Btn8, Btn5, Btn2)

    elif (Btn9['text'] == 'X' and Btn6['text'] == 'X' and Btn3['text'] == 'X') :
        win(1, Btn9, Btn6, Btn3)

    elif (Btn7['text'] == 'X' and Btn5['text'] == 'X' and Btn3['text'] == 'X') :
        win(1, Btn7, Btn5, Btn3)

    elif (Btn1['text'] == 'X' and Btn5['text'] == 'X' and Btn9['text'] == 'X') :
        win(1, Btn1, Btn5, Btn9)

    elif (Btn1['text'] == '0' and Btn5['text'] == '0' and Btn9['text'] == '0') :
        win(0, Btn1, Btn5, Btn9)

    elif (Btn7['text'] == '0' and Btn5['text'] == '0' and Btn3['text'] == '0') :
        win(0, Btn7, Btn5, Btn3)

    elif (Btn1['text'] == '0' and Btn4['text'] == '0' and Btn7['text'] == '0') :
        win(0, Btn1, Btn4, Btn7)

    elif (Btn2['text'] == '0' and Btn5['text'] == '0' and Btn8['text'] == '0') :
        win(0, Btn2, Btn5, Btn8)

    elif (Btn3['text'] == '0' and Btn6['text'] == '0' and Btn9['text'] == '0') :
        win(0, Btn3, Btn6, Btn9)

    elif (Btn1['text'] == '0' and Btn2['text'] == '0' and Btn3['text'] == '0') :
        win(0, Btn1, Btn2, Btn3)

    elif (Btn4['text'] == '0' and Btn5['text'] == '0' and Btn6['text'] == '0') :
        win(0, Btn4, Btn5, Btn6)

    elif (Btn7['text'] == '0' and Btn8['text'] == '0' and Btn9['text'] == '0') :
        win(0, Btn7, Btn8, Btn9)

    elif (Btn1['text'] != NIL and Btn2['text'] != NIL and Btn3['text'] != NIL and Btn4['text'] != NIL and Btn5['text'] != NIL and Btn6['text'] != NIL and Btn7['text'] != NIL and Btn8['text'] != NIL and Btn9['text'] != NIL) :
        win(2, "", "", "")

###############################################

from tkinter import *
from tkinter import messagebox

###############################################

NIL = ""

###############################################

root = Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)
root.configure(bg = "black")

###############################################

Btn1 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun1)
Btn1.grid(row = 0, column = 0)
 
Btn2 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun2)
Btn2.grid(row = 0, column = 1)
 
Btn3 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun3)
Btn3.grid(row = 0, column = 2)
 
Btn4 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun4)
Btn4.grid(row = 1, column = 0)
 
Btn5 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun5)
Btn5.grid(row = 1, column = 1)
 
Btn6 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun6)
Btn6.grid(row = 1, column = 2)
 
Btn7 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun7)
Btn7.grid(row = 2, column = 0)
 
Btn8 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun8)
Btn8.grid(row = 2, column = 1)
 
Btn9 = Button(root, text = NIL, font = ('arial', 50 ,'bold'), width = 3, bd = 5, bg = 'black', command = fun9)
Btn9.grid(row = 2, column = 2)

label = Label(root, text = " X's Chance ", font = ('arial', 40 ,'bold'), fg = "snow", bg = 'red')
label.grid(row = 3, column = 0, columnspan = 3)
 
###############################################

root.mainloop()
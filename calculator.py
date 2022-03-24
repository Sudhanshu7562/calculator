"""calculator"""

from ast import Expression
import tkinter

from tkinter import*

app =Tk()
app.title("calculator by Sudhanshu")
app.geometry("300x400") 

equation = StringVar()

Expression= ""

def press(num):
    global Expression
    Expression = Expression+num
    equation.set(Expression)

def clear():
    global Expression
    Expression=""
    equation.set("0")

def total(): 
    global Expression
    data= str(eval(Expression))
    equation.set(data)




display = Entry(app,width=17,font=("Arial",26),textvariable=equation)
display.grid(row=0,column=0,columnspan=4)
#########################################

one= Button(app,text="1",padx=20,pady=20,fg="aqua",bg="blue",command=lambda:press("1"))
one.grid(row=1,column=0,padx=20,pady=20)

one= Button(app,text="2",padx=20,pady=20,fg="aqua",bg="blue",command=lambda:press("2"))
one.grid(row=1,column=1,padx=20,pady=20)

one= Button(app,text="3",padx=20,pady=20,fg="aqua",bg="blue",command=lambda:press("3"))
one.grid(row=1,column=2,padx=20,pady=20)

one= Button(app,text="+",padx=20,pady=20,fg="aqua",bg="brown",command=lambda:press("+"))
one.grid(row=1,column=3,padx=20,pady=20)
###############################################
one= Button(app,text="4",padx=20,pady=20,fg="aqua",bg="pink",command=lambda:press("4"))
one.grid(row=2,column=0,padx=20,pady=20)

one= Button(app,text="5",padx=20,pady=20,fg="aqua",bg="pink",command=lambda:press("5"))
one.grid(row=2,column=1,padx=20,pady=20)

one= Button(app,text="6",padx=20,pady=20,fg="aqua",bg="pink",command=lambda:press("6"))
one.grid(row=2,column=2,padx=20,pady=20)

one= Button(app,text="-",padx=20,pady=20,fg="aqua",bg="orange",command=lambda:press("-"))
one.grid(row=2,column=3,padx=20,pady=20)
##################################################

one= Button(app,text="7",padx=20,pady=20,fg="aqua",bg="yellow",command=lambda:press("7"))
one.grid(row=3,column=0,padx=20,pady=20)

one= Button(app,text="8",padx=20,pady=20,fg="aqua",bg="yellow",command=lambda:press("8"))
one.grid(row=3,column=1,padx=20,pady=20)

one= Button(app,text="9",padx=20,pady=20,fg="aqua",bg="yellow",command=lambda:press("9"))
one.grid(row=3,column=2,padx=20,pady=20)

one= Button(app,text="*",padx=20,pady=20,fg="aqua",bg="yellow",command=lambda:press("*"))
one.grid(row=3,column=3,padx=20,pady=20)
###############################################
one= Button(app,text="0",padx=20,pady=20,fg="aqua",bg="green",command=lambda:press("0"))
one.grid(row=4,column=0,padx=20,pady=20)

one= Button(app,text="=",padx=20,pady=20,fg="aqua",bg="green",command=total)
one.grid(row=4,column=1,padx=20,pady=20)

one= Button(app,text="c",padx=20,pady=20,fg="aqua",bg="red",command=clear)
one.grid(row=4,column=2,padx=20,pady=20)

one= Button(app,text="/",padx=20,pady=20,fg="aqua",bg="green",command=lambda:press("/"))
one.grid(row=4,column=3,padx=20,pady=20)
###############################################
app.mainloop()

from tkinter import *
from math import factorial

e=""

def IN(n, E):
	global e
	e=e+str(n)
	E.set(e)


def EV(E):
	global e
	try:
		r=str(eval(e))
		E.set(r)
		e=""
	except:
		e=""
def CN(E):
	global e
	e=""
	E.set(e)

w=Tk()
E=StringVar()

w.title('Divyanshu - Calculator')


t1=Entry(w, textvariable=E, justify="right",font=40)
t1.grid(columnspan=7, ipadx=60, ipady=100)

b1=Button(w, text="1", height=2, width=4, command=lambda:IN(1,E),bg="white")
b1.grid(row=2, column=0)

b2=Button(w, text="2", height=2, width=4, command=lambda:IN(2,E),bg="white")
b2.grid(row=2, column=1)

b3=Button(w, text="3", height=2, width=4, command=lambda:IN(3,E),bg="white")
b3.grid(row=2, column=2)


b4=Button(w, text="4", height=2, width=4, command=lambda:IN(4,E),bg="white")
b4.grid(row=3, column=0)

b5=Button(w, text="5", height=2, width=4, command=lambda:IN(5,E),bg="white")
b5.grid(row=3, column=1)

b6=Button(w, text="6", height=2, width=4, command=lambda:IN(6,E),bg="white")
b6.grid(row=3, column=2)


b7=Button(w, text="7", height=2, width=4, command=lambda:IN(7,E),bg="white")
b7.grid(row=4, column=0)

b8=Button(w, text="8", height=2, width=4, command=lambda:IN(8,E),bg="white")
b8.grid(row=4, column=1)

b9=Button(w, text="9", height=2, width=4, command=lambda:IN(9,E),bg="white")
b9.grid(row=4, column=2)

b10=Button(w, text="0", height=2, width=4, command=lambda:IN(0,E),bg="white")
b10.grid(row=5, column=1)


bcl=Button(w,text="C", height=2, width=4, command=lambda:CN(E),bg="red")
bcl.grid(row=2, column=5)

be=Button(w, text="=", height=2, width=4, command=lambda:EV(E),bg="green")
be.grid(row=2, column=6)

bp=Button(w, text="+", height=2, width=4, command=lambda:IN("+",E),bg="pink")
bp.grid(row=3, column=5)

bp=Button(w, text="**", height=2, width=4, command=lambda:IN("**",E),bg="pink")
bp.grid(row=3, column=6)

bp=Button(w, text="-", height=2, width=4, command=lambda:IN("-",E),bg="pink")
bp.grid(row=4, column=5)

bp=Button(w, text="*", height=2, width=4, command=lambda:IN("*",E),bg="pink")
bp.grid(row=4, column=6)

bp=Button(w, text="%", height=2, width=4, command=lambda:IN("%",E),bg="pink")
bp.grid(row=5, column=5)

bp=Button(w, text="/", height=2, width=4, command=lambda:IN("/",E),bg="pink")
bp.grid(row=5, column=6)

bdot=Button(w,text=".",height=2, width=4, command=lambda :IN(".",E),bg="pink")
bdot.grid(row=6, column=5)

w.mainloop()
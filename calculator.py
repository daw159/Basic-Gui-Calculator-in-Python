from tkinter import *

def button_press(n):
    global text
    label.config(fg='white') 
    text=text+str(n)
    equation_label.set(text)
    
def equals():
    global text
    try:
        tot=str(eval(text))
        text=tot
        equation_label.set(tot)
    except SyntaxError:

        equation_label.set("syntax error")

        text = ""
        label.config(fg='red')

    except ZeroDivisionError:

        equation_label.set(" Math error")

        text = ""
    
def clears():
    global text
    label.config(fg='white') 
    equation_label.set("")
    text=""
    
window=Tk()
window.title("Simple Calculator")
window.config(bg="black")
window.geometry("500x500")

text=""
equation_label=StringVar()

label=Label(window,textvariable=equation_label,font=('consolas',30),fg='white',bg='black',width=20,height=4,highlightbackground='orange',highlightthickness=2,highlightcolor='orange',anchor='e')
label.pack(pady=10)
frame=Frame(window,bg='grey')
frame.pack()

button1=Button(frame,height=4,width=9,font=55,text=1,fg='white',bg="#1D1F1E",command=lambda:button_press(1)).grid(row=0,column=0)
button2=Button(frame,height=4,width=9,font=55,text=2,fg='white',bg="#1D1F1E",command=lambda:button_press(2)).grid(row=0,column=1)
button3=Button(frame,height=4,width=9,font=55,text=3,fg='white',bg="#1D1F1E",command=lambda:button_press(3)).grid(row=0,column=2)
button4=Button(frame,height=4,width=9,font=55,text=4,fg='white',bg="#1D1F1E",command=lambda:button_press(4)).grid(row=1,column=0)
button5=Button(frame,height=4,width=9,font=55,text=5,fg='white',bg="#1D1F1E",command=lambda:button_press(5)).grid(row=1,column=1)
button6=Button(frame,height=4,width=9,font=55,text=6,fg='white',bg="#1D1F1E",command=lambda:button_press(6)).grid(row=1,column=2)
button7=Button(frame,height=4,width=9,font=55,text=7,fg='white',bg="#1D1F1E",command=lambda:button_press(7)).grid(row=2,column=0)
button8=Button(frame,height=4,width=9,font=55,text=8,fg='white',bg="#1D1F1E",command=lambda:button_press(8)).grid(row=2,column=1)
button9=Button(frame,height=4,width=9,font=55,text=9,fg='white',bg="#1D1F1E",command=lambda:button_press(9)).grid(row=2,column=2)
button0=Button(frame,height=4,width=9,font=55,text=0,fg='white',bg="#1D1F1E",command=lambda:button_press(0)).grid(row=3,column=0)

plus=Button(frame,height=4,width=9,font=55,text='+',fg='orange', bg="#1D1F1E",command=lambda:button_press('+')).grid(row=0,column=3)
minus=Button(frame,height=4,width=9,font=55,text='-',fg='orange', bg="#1D1F1E",command=lambda:button_press('-')).grid(row=1,column=3)
multiply=Button(frame,height=4,width=9,font=55,text='*',fg='orange', bg="#1D1F1E",command=lambda:button_press('*')).grid(row=2,column=3)
divide=Button(frame,height=4,width=9,font=55,text='/',fg='orange', bg="#1D1F1E",command=lambda:button_press('/')).grid(row=3,column=3)
decimal=Button(frame,height=4,width=9,font=75,text='.',fg='white',bg="#1D1F1E",command=lambda:button_press('.')).grid(row=3,column=1)
equal=Button(frame,height=4,width=9,font=55,text='=',fg='orange', bg="#1D1F1E",command=equals).grid(row=3,column=2)
clear=Button(frame,height=4,width=9,font=55,text='C',fg='red', bg="#1D1F1E",command=clears).grid(row=4,column=3)



window.mainloop()

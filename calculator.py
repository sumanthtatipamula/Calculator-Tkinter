import tkinter
from tkinter import RIGHT,CENTER,END,DISABLED,NORMAL,GROOVE,RIDGE,SUNKEN,FLAT,RAISED
from tkinter import messagebox,StringVar

#Window
root = tkinter.Tk()
root.title('Basic Calculator')
root.iconbitmap('calculator.ico')
root.resizable(0, 0)
sv = StringVar()
operation = ''

#Functions
def append_number(number):
    display.insert(END,number)
    if '.' in display.get():
        dot.config(state = DISABLED)

def validate_float(var):
    new_value = var.get()
    try:
        new_value == '' or float(new_value)
    except:
        var.set(var.get()[:-1])    

def operate(operator):
    global first_number
    global operation
    try:
        operation = operator
        first_number = float(display.get())
        display.delete(0, END)
        set_operators_state(DISABLED)
        dot.config(state = NORMAL)
    except (TypeError,ValueError): 
        pass


def set_operators_state(state):
    modulus.config(state=state)
    plus.config(state=state)
    minus.config(state=state)
    division.config(state=state)
    multiplication.config(state=state)

def clear():
    display.delete(0, END)
    set_operators_state(NORMAL)

def evaluate():
    try:
        if operation == '+':
            value = float(first_number) + float(display.get())
        elif operation == '-':
            value = float(first_number) - float(display.get())
        elif operation == '*':
            value = float(first_number) * float(display.get())
        elif operation == '/':
            if display.get() == "0":
                messagebox.showinfo('Divsion',"A number can't be divided by zero")
                display.delete(0, END)
                return
            else:
                value = float(first_number) / float(display.get())
        elif operation == '%':
            if display.get() == "0":
                messagebox.showinfo('Divsion',"A number can't be divided by zero")
                display.delete(0, END)
                return
            else:
                value = float(first_number) % float(display.get())

        display.delete(0, END)
        display.insert(0, value)
        set_operators_state(NORMAL);  
    except:
        pass    

#Colors and fonts
display_frame_color = '#a5bacb'
buttons_frame_color = '#d9e0e0'
display_box_color = '#d1dcba'
top_row_buttons_color = '#4d738a'
buttons_color = '#a5bccb'
equal_button_color = '#fc8103'
button_font = ('Arial', 15)
display_font = ('Arial', 20)


#Frames
display_frame = tkinter.Frame(root,bg = display_frame_color)
display_frame.pack()
buttons_frame = tkinter.Frame(root, bg = buttons_frame_color)
buttons_frame.pack(fill = 'both',expand = True)

#Widgets
#Display Frame
sv.trace('w', lambda nm, idx, mode,var=sv: validate_float(var))
display = tkinter.Entry(display_frame, width=15, font=display_font, bg=display_box_color, borderwidth=10 ,justify=RIGHT, textvariable=sv)
display.pack(padx=15, pady=(20,20))

#Buttons Frame
#First Row
clear = tkinter.Button(buttons_frame,text='C',bg =top_row_buttons_color,font=button_font,fg='white',width=4,command =clear)
modulus = tkinter.Button(buttons_frame,text='%',bg=top_row_buttons_color,font=button_font,fg='white',width=4,command = lambda: operate('%'))
division = tkinter.Button(buttons_frame,text = '/',bg =top_row_buttons_color,font=button_font,fg='white',width=4,command = lambda: operate('/'))
multiplication = tkinter.Button(buttons_frame,text = 'X',bg =top_row_buttons_color,font=button_font,fg='white',width=4,command = lambda: operate('*'))

#Second row
seven = tkinter.Button(buttons_frame,text='7',bg =buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(7))
eight = tkinter.Button(buttons_frame,text='8',bg =buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(8))
nine = tkinter.Button(buttons_frame,text='9',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(9))
minus = tkinter.Button(buttons_frame,text='-',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda: operate('-'))

#Thrid row
four = tkinter.Button(buttons_frame,text='4',bg =buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(4))
five = tkinter.Button(buttons_frame,text='5',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(5))
six = tkinter.Button(buttons_frame,text='6',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(6))
plus = tkinter.Button(buttons_frame,text='+',bg=buttons_color,font=button_font,fg ='white',cursor='plus',width=4,command =lambda:operate('+'))

#Fourth Row
one = tkinter.Button(buttons_frame,text='1',bg =buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(1))
two = tkinter.Button(buttons_frame,text='2',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(2))
three = tkinter.Button(buttons_frame,text='3',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(3))
equal = tkinter.Button(buttons_frame,text='=',bg=equal_button_color,font=button_font,fg ='white',width=4,command = evaluate)

#Fifth Row
zero = tkinter.Button(buttons_frame,text='0',bg=buttons_color,font=button_font,fg ='white',width=4,command = lambda:append_number(0))
dot =  tkinter.Button(buttons_frame,text='.',bg=buttons_color,font=button_font,fg ='white',width=4,cursor='dotbox',anchor='center',command = lambda:append_number('.'))


clear.grid(row = 0,column = 0,pady=(20,2),padx=(15,5))
modulus.grid(row = 0,column = 1,pady=(20,2),padx=(5,5))
division.grid(row = 0,column=2,pady=(20,2),padx=(5,5))
multiplication.grid(row = 0,column = 3,pady=(20,2),padx=(5,5))

seven.grid(row = 1,column = 0,pady=2,padx=(15,5))
eight.grid(row = 1,column = 1,pady=2,padx=(5,5))
nine.grid(row = 1,column=2,pady=2,padx=(5,5))
minus.grid(row = 1,column = 3,pady=2,padx=(5,5))

four.grid(row = 2,column = 0,pady=2,padx=(15,5))
five.grid(row = 2,column = 1,pady=2,padx=(5,5))
six.grid(row = 2,column=2,pady=2,padx=(5,5))
plus.grid(row = 2,column = 3,pady=2,padx=(5,5))

one.grid(row = 3,column = 0,pady=2,padx=(15,5))
two.grid(row = 3,column = 1,pady=2,padx=(5,5))
three.grid(row = 3,column=2,pady=2,padx=(5,5))
equal.grid(row = 3,column = 3,rowspan=2,pady=(2,10),padx=(5,5),sticky='ns')

zero.grid(row = 4,columnspan=2,pady=(2,10),padx=(15,5),sticky='ew')
dot.grid(row = 4,column = 2,pady=(2,10),padx=(5,5))

#Window's mainloop
root.mainloop()

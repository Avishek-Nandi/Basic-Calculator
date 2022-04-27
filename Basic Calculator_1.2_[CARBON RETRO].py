

# GUI functions
from tkinter import *
main_gui = Tk()
main_gui.title("Basic Calculator")
main_gui.configure(bg='#333333')
main_gui.geometry("308x450")
main_gui.overrideredirect(True)

# Calculator functions
i = 0
string_out = ""

def get_var(num):
    global i,string_out
    display.insert(i, num)
    string_out += str(num)
    i = i+1


def get_operation(operator):
    if operator == "x":
        operator1 = "*"
    elif operator == "^":
        operator1 = "**"
    elif operator == "÷":
        operator1 = "/"
    else:
        operator1 = operator
    global i,string_out
    length = len(operator)
    display.insert(i, operator)
    string_out += operator1
    i += length


def clear_all():
    global string_out
    display.delete(0, END)
    string_out = ""


def undo():
    global string_out
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        string_out = string_out[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


def calculate():
    global string_out
    entire_string = display.get()
    try:
        result = eval(string_out)
        clear_all()
        display.insert(0, result)
        string_out += str(result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# Title Bar


def move_app(a):
    main_gui.geometry(f'+{a.x_root}+{a.y_root}')


def close_app(a):
    main_gui.quit()

titlebar = Frame(main_gui, bg='#242424', relief="raised", bd=0)
titlebar.pack(fill=X)
titlebar_label = Label(titlebar, text="  Basic Calculator", bg='#242424', font="Calibri", fg='#F27A17')
titlebar_label.pack(side=LEFT, pady=2)
titlebar_cancel = Label(titlebar, text="  x  ", fg='#9A9898', bg='#242424',)
titlebar_cancel.pack(side=RIGHT, pady=2)
titlebar_cancel.bind("<Button-1>", close_app)
titlebar.bind("<B1-Motion>", move_app)

display = Entry(main_gui, justify="right", width=35, borderwidth=1, bg='#333333', fg='white', font="Calibri, 14")
display.pack(fill=X, ipady=12)

menu_frame = Frame(main_gui, bg='#333333', bd=0,)
menu_frame.pack(fill=X)
menu_frame2 = Frame(main_gui, bg='#333333', bd=0,)
menu_frame2.pack(fill=X)
menu_frame3 = Frame(main_gui, bg='#333333', bd=0,)
menu_frame3.pack(fill=X)
menu_frame4 = Frame(main_gui, bg='#333333', bd=0,)
menu_frame4.pack(fill=X)
menu_frame5 = Frame(main_gui, bg='#333333', bd=0,)
menu_frame5.pack(fill=X)
menu_frame6 = Frame(main_gui, bg='#333333', bd=0,)
menu_frame6.pack(fill=X)

# button frame

def button_add(a):
    return a


buttonCE = Button(menu_frame, text="AC ", font="Calibri, 18", fg='#242424', bg='#F27A17', bd= 0, padx=5, pady=5,
                  command=lambda: clear_all())
buttonC = Button(menu_frame, text=" C ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd= 0, padx=5, pady=5,
                 command=lambda: undo())
button_percent = Button(menu_frame, text=" % ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                        command=lambda: get_operation("%"))
button_back = Button(menu_frame, text=" <- ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                     command=lambda: undo())

button_inverse = Button(menu_frame2, text="1/x", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                        command=lambda: get_operation("1/x"))
button_square = Button(menu_frame2, text="x^ ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                       command=lambda: get_operation("^"))
button_root = Button(menu_frame2, text="√x ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                     command=lambda: get_operation("√"))
button_devide = Button(menu_frame2, text=" ÷ ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                       command=lambda: get_operation("÷"))

button7 = Button(menu_frame3, text="  7  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(7))
button8 = Button(menu_frame3, text="  8  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(8))
button9 = Button(menu_frame3, text="  9  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(9))
button_multiply = Button(menu_frame3, text="  x  ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd= 0, padx=5,
                         pady=5, command=lambda: get_operation("x"))

button4 = Button(menu_frame4, text="  4  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(4))
button5 = Button(menu_frame4, text="  5  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(5))
button6 = Button(menu_frame4, text="  6  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(6))
button_minus = Button(menu_frame4, text="  -  ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                      command=lambda: get_operation("-"))

button1 = Button(menu_frame5, text="  1  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(1))
button2 = Button(menu_frame5, text="  2  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(2))
button3 = Button(menu_frame5, text="  3  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                 command=lambda: get_var(3))
button_plus = Button(menu_frame5, text="  +  ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                     command=lambda: get_operation("+"))

button0 = Button(menu_frame6, text="       0        ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5,
                 pady=5, command=lambda: get_var(0))
button_deci = Button(menu_frame6, text="  .  ", font="Calibri, 18", fg='#F27A17', bg='#303030', bd=0, padx=5, pady=5,
                     command=lambda: get_var("."))
button_equal = Button(menu_frame6, text="  =  ", font="Calibri, 18", fg='#F27A17', bg='#242424', bd=0, padx=5, pady=5,
                      command=lambda: calculate())


buttonCE.pack(side=LEFT, ipadx=1, padx=5, pady=5)
buttonC.pack(side=LEFT, ipadx=5, padx=4, pady=5)
button_percent.pack(side=LEFT, ipadx=4, padx=5, pady=5)
button_back.pack(side=LEFT, ipadx=3, padx=5, pady=5)

button_inverse.pack(side=LEFT, ipadx=5, padx=5, pady=5)
button_square.pack(side=LEFT, ipadx=5, padx=5, pady=5)
button_root.pack(side=LEFT, ipadx=5, padx=5, pady=5)
button_devide.pack(side=LEFT, ipadx=8, padx=5, pady=5)

button7.pack(side=LEFT, padx=5, pady=5)
button8.pack(side=LEFT, padx=5, pady=5)
button9.pack(side=LEFT, padx=5, pady=5)
button_multiply.pack(side=LEFT, ipadx=2, padx=5, pady=5)

button4.pack(side=LEFT, padx=5, pady=5)
button5.pack(side=LEFT, padx=5, pady=5)
button6.pack(side=LEFT, padx=5, pady=5)
button_minus.pack(side=LEFT, ipadx=3, padx=5, pady=5)

button1.pack(side=LEFT, padx=5, pady=5)
button2.pack(side=LEFT, padx=5, pady=5)
button3.pack(side=LEFT, padx=5, pady=5)
button_plus.pack(side=LEFT, padx=5, pady=5)

button0.pack(side=LEFT, padx=5, pady=5)
button_deci.pack(side=LEFT, ipadx=3, padx=5, pady=5)
button_equal.pack(side=LEFT, padx=5, pady=5)


main_gui.mainloop()

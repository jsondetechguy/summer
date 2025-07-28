from tkinter import *
from math import *
calc = ""

# Function to add numbers to the calculator display
def add_to_calc(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, END)
    text_result.insert(1.0, calc)

def evaluate_calc():
    global calc
    try:
        calc = str(eval(calc))
        text_result.delete(1.0, END)
        text_result.insert(1.0, calc)
    except:
        clear_calc()
        text_result.insert(1.0, "Error")
def clear_calc():
    global calc
    calc = ""
    text_result.delete(1.0, END)
def delete_last():
    global calc
    calc = calc[:-1]
    text_result.delete(1.0, END)
    text_result.insert(1.0, calc)

root = Tk()
root.title("Calculator")
root.geometry("500x500")

text_result = Text(root, height=2, width=30, bg="black", fg="white", font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = Button(root, text="7", command=lambda: add_to_calc(7), bg="white", fg="black", font=("Arial", 18))
btn_1.grid(row=2, column=0)
btn_2 = Button(root, text="8", command=lambda: add_to_calc(8), bg="white", fg="black", font=("Arial", 18))
btn_2.grid(row=2, column=1)
btn_3 = Button(root, text="9", command=lambda: add_to_calc(9), bg="white", fg="black", font=("Arial", 18))
btn_3.grid(row=2, column=2)
btn_4 = Button(root, text="4", command=lambda: add_to_calc(4), bg="white", fg="black", font=("Arial", 18))
btn_4.grid(row=3, column=0)
btn_5 = Button(root, text="5", command=lambda: add_to_calc(5), bg="white", fg="black", font=("Arial", 18))
btn_5.grid(row=3, column=1)
btn_6 = Button(root, text="6", command=lambda: add_to_calc(6), bg="white", fg="black", font=("Arial", 18))
btn_6.grid(row=3, column=2)
btn_7 = Button(root, text="1", command=lambda: add_to_calc(1), bg="white", fg="black", font=("Arial", 18))
btn_7.grid(row=4, column=0)
btn_8 = Button(root, text="2", command=lambda: add_to_calc(2), bg="white", fg="black", font=("Arial", 18))
btn_8.grid(row=4, column=1)
btn_9 = Button(root, text="3", command=lambda: add_to_calc(3), bg="white", fg="black", font=("Arial", 18))
btn_9.grid(row=4, column=2)
btn_0 = Button(root, text="0", command=lambda: add_to_calc(0), bg="white", fg="black", font=("Arial", 18))
btn_0.grid(row=5, column=1)

# making the buttons for operations
btn_delete = Button(root, text="Del", command=delete_last, bg="white", fg="black", font=("Arial", 18))
btn_delete.grid(row=2, column=3)
btn_plus = Button(root, text="+", command=lambda: add_to_calc("+"), bg="white", fg="black", font=("Arial", 18))
btn_plus.grid(row=5, column=2)
btn_minus = Button(root, text="-", command=lambda: add_to_calc("-"), bg="white", fg="black", font=("Arial", 18))
btn_minus.grid(row=3, column=3)
btn_multiply = Button(root, text="x", command=lambda: add_to_calc("*"), bg="white", fg="black", font=("Arial", 18))
btn_multiply.grid(row=4, column=3)
btn_divide = Button(root, text="/", command=lambda: add_to_calc("/"), bg="white", fg="black", font=("Arial", 18))
btn_divide.grid(row=5, column=3) 
btn_clear = Button(root, text="C", command=clear_calc, bg="white", fg="black", font=("Arial", 18))
btn_clear.grid(row=5, column=0)
btn_dot = Button(root, text=".", command=lambda: add_to_calc("."), bg="white", fg="black", font=("Arial", 18))
btn_dot.grid(row=6, column=0)
btn_sqrt = Button(root, text="√", command=lambda: add_to_calc("sqrt("), bg="white", fg="black", font=("Arial", 18))
btn_sqrt.grid(row=6, column=1)
btn_open_paren = Button(root, text="(", command=lambda: add_to_calc("("), bg="white", fg="black", font=("Arial", 18))
btn_open_paren.grid(row=6, column=2)
btn_close_paren = Button(root, text=")", command=lambda: add_to_calc(")"), bg="white", fg="black", font=("Arial", 18)) 
btn_close_paren.grid(row=6, column=3)
btn_sqrt = Button(root, text="x²", command=lambda: add_to_calc("**2"), bg="white", fg="black", font=("Arial", 18))
btn_sqrt.grid(row=7, column=0)
btn_pie = Button(root, text="π", command=lambda: add_to_calc("pi"), bg="white", fg="black", font=("Arial", 18))
btn_pie.grid(row=7, column=1)
btn_log = Button(root, text="log", command=lambda: add_to_calc("log("), bg="white", fg="black", font=("Arial", 18))
btn_log.grid(row=7, column=2)

btn_sin = Button(root, text="sin", command=lambda: add_to_calc("sin("), bg="white", fg="black", font=("Arial", 18))
btn_sin.grid(row=7, column=3)


btn_equal = Button(root, text="=", command=evaluate_calc, bg="white", fg="black", font=("Arial", 18), width=20)
btn_equal.grid(row=8, column=0, columnspan=4)
root.mainloop()
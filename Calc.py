import tkinter as tk

calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_sum.delete(1.0, "end")
    text_sum.insert(1.0, calculation)

def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_sum.delete(1.0, "end")
        text_sum.insert(1.0, calculation)
    except:
        clear_space()
        text_sum.insert(1.0, "Error")
        

def clear_space():
    global calculation
    calculation = ""
    text_sum.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_sum = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_sum.grid(columnspan=5)

button_1 = tk.Button(root, text="1", command=lambda: add_calculation(1), width=5, font=("Arial", 14) )
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text="2", command=lambda: add_calculation(2), width=5, font=("Arial", 14) )
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_calculation(3), width=5, font=("Arial", 14) )
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text="4", command=lambda: add_calculation(4), width=5, font=("Arial", 14) )
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text="5", command=lambda: add_calculation(5), width=5, font=("Arial", 14) )
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_calculation(6), width=5, font=("Arial", 14) )
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text="7", command=lambda: add_calculation(7), width=5, font=("Arial", 14) )
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text="8", command=lambda: add_calculation(8), width=5, font=("Arial", 14) )
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text="9", command=lambda: add_calculation(9), width=5, font=("Arial", 14) )
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text="0", command=lambda: add_calculation(0), width=5, font=("Arial", 14) )
button_0.grid(row=5, column=2)
button_plus = tk.Button(root, text="+", command=lambda: add_calculation("+"), width=5, font=("Arial", 14) )
button_plus.grid(row=2, column=4)
button_sub = tk.Button(root, text="-", command=lambda: add_calculation("-"), width=5, font=("Arial", 14) )
button_sub.grid(row=3, column=4)
button_mul = tk.Button(root, text="*", command=lambda: add_calculation("*"), width=5, font=("Arial", 14) )
button_mul.grid(row=4, column=4)
button_div = tk.Button(root, text="/", command=lambda: add_calculation("/"), width=5, font=("Arial", 14) )
button_div.grid(row=5, column=4)
button_opbrac = tk.Button(root, text="(", command=lambda: add_calculation("("), width=5, font=("Arial", 14) )
button_opbrac.grid(row=5, column=1)
button_clobrac = tk.Button(root, text=")", command=lambda: add_calculation(")"), width=5, font=("Arial", 14) )
button_clobrac.grid(row=5, column=3)
button_clear = tk.Button(root, text="C", command=clear_space, width=11, font=("Arial", 14) )
button_clear.grid(row=6, column=1, columnspan=2)
button_equals = tk.Button(root, text="=", command=eval_calculation, width=11, font=("Arial", 14) )
button_equals.grid(row=6, column=3, columnspan=2)
root.mainloop()
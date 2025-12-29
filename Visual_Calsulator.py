
from tkinter import *

current_expression = ""
input_field = None  

def click_button(value):
    global current_expression, input_field
    current_expression += str(value)
    input_field.delete(0, END)
    input_field.insert(0, current_expression)

def clear():
    global current_expression, input_field
    current_expression = ""
    input_field.delete(0, END)


def calculate():
    global current_expression, input_field
    
    print("калькулятор") 
    
    operation = current_expression.strip() 
    
    if operation == '+':
        input_field.delete(0, END)
        input_field.insert(0, "Введите 2 числа через + (5+3)")
        
    elif operation == '-': 
        input_field.delete(0, END)
        input_field.insert(0, "Введите 2 числа через - (5-3)")
        
    elif operation == '*':
        input_field.delete(0, END)
        input_field.insert(0, "Введите 2 числа через * (5*3)")
        
    elif operation == ':':
        input_field.delete(0, END)
        input_field.insert(0, "Введите 2 числа через : (5:3)")
        
    elif operation == '^': 
        input_field.delete(0, END)
        input_field.insert(0, "Введите 2 числа через ^ (2^3)")
    
    elif '+' in operation:
        try:
            parts = operation.split('+')
            if len(parts) == 2:
                a = float(parts[0])
                b = float(parts[1])
                result = a + b
                input_field.delete(0, END)
                input_field.insert(0, f"{result:g}")
                current_expression = ""
                return
        except:
            pass
    
    elif '-' in operation:
        try:
            parts = operation.split('-')
            if len(parts) == 2:
                a = float(parts[0])
                b = float(parts[1])
                result = a - b
                input_field.delete(0, END)
                input_field.insert(0, f"{result:g}")
                current_expression = ""
                return
        except:
            pass
    
    elif '*' in operation:
        try:
            parts = operation.split('*')
            if len(parts) == 2:
                a = float(parts[0])
                b = float(parts[1])
                result = a * b
                input_field.delete(0, END)
                input_field.insert(0, f"{result:g}")
                current_expression = ""
                return
        except:
            pass
    
    elif ':' in operation:
        try:
            parts = operation.split(':')
            if len(parts) == 2:
                a = float(parts[0])
                b = float(parts[1])
                if b != 0:
                    result = a / b
                    input_field.delete(0, END)
                    input_field.insert(0, f"{result:g}")
                else:
                    input_field.delete(0, END)
                    input_field.insert(0, "Ошибка")
                current_expression = ""
                return
        except:
            pass
    
    elif '^' in operation:
        try:
            parts = operation.split('^')
            if len(parts) == 2:
                a = float(parts[0])
                b = float(parts[1])
                result = a ** b
                input_field.delete(0, END)
                input_field.insert(0, f"{result:g}")
                current_expression = ""
                return
        except:
            pass
    
    else: 
        input_field.delete(0, END)
        input_field.insert(0, "неверная операция")


root = Tk()
root.title("Калькулятор")
root.geometry("500x700")
root.configure(bg='lightgray')


input_field = Entry(root, font=('Arial', 16), width=20, justify=RIGHT)
input_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), (':', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    Button(root, text=text, padx=30, pady=30, font=('Arial', 14),
           command=lambda t=text: click_button(t)).grid(row=row, column=col, padx=5, pady=5)

Button(root, text="^", padx=60, pady=30, font=('Arial', 14),
       command=lambda: click_button('^')).grid(row=5, column=0, columnspan=2)
Button(root, text="C", padx=60, pady=30, font=('Arial', 14),
       command=clear).grid(row=5, column=2, columnspan=2)
Button(root, text="=", padx=120, pady=40, font=('Arial', 16), bg="lightblue",
       command=calculate).grid(row=6, column=0, columnspan=4, pady=20)

root.mainloop()

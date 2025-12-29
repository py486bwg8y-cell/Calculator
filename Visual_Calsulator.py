from tkinter import *

current_expression = ""
input_field = None  
last_result = ""  

def click_button(value):
    global current_expression, input_field, last_result
    current_expression += str(value)
    input_field.delete(0, END)
    input_field.insert(0, current_expression)

def clear():
    global current_expression, input_field, last_result
    current_expression = ""
    last_result = "" 
    input_field.delete(0, END)
    input_field.insert(0, "0")

def calculate():
    global current_expression, input_field, last_result
    
    print("калькулятор")
    operation = current_expression.strip()
    
    result = None 
    
    
    if operation == '+':
        input_field.delete(0, END)
        input_field.insert(0, f"{last_result or '0'}+ (введите число)")
        return
        
    elif operation == '-': 
        input_field.delete(0, END)
        input_field.insert(0, f"{last_result or '0'}- (введите число)")
        return
        
    
    elif '+' in operation:
        try:
            parts = operation.split('+')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a + b
        except: pass
    
    elif '-' in operation:
        try:
            parts = operation.split('-')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a - b
        except: pass
    
    elif 'X' in operation:
        try:
            parts = operation.split('*')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a * b
        except: pass
    
    elif ':' in operation:
        try:
            parts = operation.split(':')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                if b != 0:
                    result = a / b
                else:
                    input_field.delete(0, END)
                    input_field.insert(0, "Ошибка")
                    return
        except: pass
    
    elif '^' in operation:
        try:
            parts = operation.split('^')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a ** b
        except: pass
    
    else: 
        input_field.delete(0, END)
        input_field.insert(0, "неверная операция")
        return
    

    if result is not None:
        last_result = str(result)
        input_field.delete(0, END)
        input_field.insert(0, f"{result:g}")  
        current_expression = ""  


root = Tk()
root.title("Калькулятор")
root.geometry("500x700")
root.configure(bg='lightgray')

root.eval('tk::PlaceWindow . center')

input_field = Entry(root, font=('Arial', 18), width=22, justify=RIGHT, relief=SOLID, bd=2)
input_field.insert(0, "0")  
input_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="ew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('X', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), (':', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    Button(root, text=text, padx=25, pady=25, font=('Arial', 16),
           command=lambda t=text: click_button(t), 
           bg='white', relief=RAISED, bd=2)\
    .grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

Button(root, text="^", padx=40, pady=25, font=('Arial', 16),
       command=lambda: click_button('^'), bg='yellow', relief=RAISED, bd=2)\
       .grid(row=5, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")

Button(root, text="C", padx=40, pady=25, font=('Arial', 16),
       command=clear, bg='orange', relief=RAISED, bd=2)\
       .grid(row=5, column=2, columnspan=2, padx=3, pady=3, sticky="nsew")

Button(root, text="=", padx=100, pady=35, font=('Arial', 20), bg="lightblue",
       command=calculate, relief=RAISED, bd=3)\
       .grid(row=6, column=0, columnspan=4, pady=20, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1, uniform="col")
for i in range(7):
    root.grid_rowconfigure(i, weight=1, uniform="row")

root.mainloop()

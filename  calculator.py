print("калькулятор")
 # ввод чисел
a = float(input("Первое число"))  # float - дробные числа 
b = float(input("Второе число"))
# выбор действия
operation = input("выберите операцию(+ для сложения; - для вычитания; x для умножения; : для деления: ")
# выбор сложения
if operation ==  '+' : # if - истинное условие
    result = a + b
    print(f"сумма  сложения: {result}")
# выбор вычитания
elif operation == '-' : # elif - доп условия
    result = a - b
    print(f"результат вычитания: {result}")
# выбор умножения
elif operation == '*' :
    result = a * b
    print(f" результат умножения: {result}")
# выбор деления
elif operation == ':' :
    result = a / b
    print(f" результат деления: {result}")
else: 
    print("неверная операция")
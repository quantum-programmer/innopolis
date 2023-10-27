# Условие "case _:" сделано для демонстрации кода. На практике при переводе введенной строки в int
# мы никогда не попадем в это условие.

limit = 999999999999

def Fibbonachi(n):
    i = 0
    x0 = 0
    x1 = 1
    x = 0
    while i < n-1:
        x = x0 + x1
        x0 = x1
        x1 = x
        i += 1
    return x

digit = int(input("Какое число последовательности Фиббоначи вы хотите узнать? - "))
match digit:
    case int() | float() as command if 0 <= command <= limit:
        if command == 1:
            x = 1
        else:
            x = Fibbonachi(digit)
        print (f"Число с номером {digit} = {x}")
    case _:
        print (f"Введите корректный номер в последовательности Фиббоначи от 0 до {limit}")
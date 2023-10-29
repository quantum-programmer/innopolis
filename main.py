numbers = input("Введите список значений через пробел: ").split()
numbers = [int(x) for x in numbers]
list_tuples = [(x, x**2) for x in numbers]
print(numbers)
print(list_tuples)

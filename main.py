global_value = 0

def SumScopes(param):
    ext_val = int(input("Введите значение переменной из охватывающей области: "))

    def inner_func(param):
        local_val = int(input("Введите значение локальной переменной: "))
        global global_value
        return global_value + ext_val + param + local_val

    return inner_func(param)

global_value = int(input("Введите значение глобальной переменной: "))
print( SumScopes(int(input("Введите значение параметра, передаваемого в функцию"))) )
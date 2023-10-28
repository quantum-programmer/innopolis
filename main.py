msg = input("Введите команду (save, load, something else): ")
match msg:
    case 'save':
        print ("Сохранить")
    case 'load':
        print ("Загрузить")
    case _:
        print ("Неизвестная операция")
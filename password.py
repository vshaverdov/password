enter = input('Введите пароль: ')


try:
    result = 10/len(enter)
    result1 = int(enter)
    print('Ваш пароль состоит толькоиз цифр')  
except ZeroDivisionError:    
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требование к паролю соблюдены')

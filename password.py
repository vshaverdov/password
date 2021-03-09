enter = input('Введите пароль: ')


try:
    result = 10/len(enter)
    result1 = int(enter)
    print('Требования к паролю соблюдены')  
except ZeroDivisionError:    
    print('Вы ввели пустой пароль')
except ValueError:
    print('Ваш пароль состоит только из цифр')

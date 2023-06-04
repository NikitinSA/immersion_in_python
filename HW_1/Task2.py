'''Напишите код, который запрашивает число и сообщает 
является ли оно простым или составным. Используйте 
правило для проверки: “Число является простым, если делится 
нацело только на единицу и на себя”. Сделайте ограничение на ввод 
отрицательных чисел и чисел больше 100 тысяч.'''

user_num = int(input('Введите положительное число не больше 100К: '))
count = 0

if user_num < 0 or user_num > 100000:
    print('Ошибка, введите другое число.')
else:
    for i in range(1, user_num + 1):
        if user_num % i == 0:
            count += 1
    if count == 2:
        print('Число является простым.')
    else:
        print('Число является составным.')
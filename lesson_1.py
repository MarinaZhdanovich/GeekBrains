# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

number = int(input('Enter your number: '))

while number >= 10 or number <= 0:
    print('The number is invalid. Enter a number in the range 0 to 10.')
    number_another = int(input('Enter another number: '))
    if 0 < number_another < 10:
        print(f'Result is {number_another ** 2}')
        break
else:
    print(f'Result is {number ** 2}')


# Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
result = int(input('Enter your number: '))
print(result + 2)


# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
#
# (Формула не соответствует реальной действительности и здесь используется только ради примера)
# Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. В случае ошибок, уточните условия для той или иной ситуации.
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('Enter your age: '))
weight = int(input('Enter your weight: '))

if age < 30 and 50 < weight < 120:
    print(f'{name} {surname}, {age} год, вес {weight} - хорошее состояние')
elif 30 < age < 40 and (weight < 50 or weight > 120):
    print(f'{name} {surname}, {age} год, вес {weight} - следует заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print(f'{name} {surname}, {age} год, вес {weight} - следует обратиться к врачу')
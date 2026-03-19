"""
Игра 'Быки и коровы'
Компьютер загадывает 4-значное число с уникальными цифрами.
Игрок отгадывает число, вводя варианты.
Бык - цифра на своей позиции.
Корова - цифра есть в числе, но на другой позиции.
Цель - отгадать число.
"""

import random

generated_number = str(random.randint(1000, 9999))  # pylint: disable=invalid-name
while len(set(generated_number)) != 4:
    generated_number = str(random.randint(1000, 9999))  # pylint: disable=invalid-name

print("Компьютер загадал 4-значное число из уникальных цифр.")

while True:
    users_try = input('Твой вариант: ')

    bulls = 0  # pylint: disable=invalid-name
    cows = 0  # pylint: disable=invalid-name

    for i in range(4):
        if users_try[i] == generated_number[i]:
            bulls += 1
        elif users_try[i] in generated_number:
            cows += 1

    print(f"Быков: {bulls}, Коров: {cows}")

    if bulls == 4:
        print("Вы выиграли!")
        break

"""
Игра 'Быки и коровы'
Компьютер загадывает 4-значное число с уникальными цифрами.
Игрок отгадывает число, вводя варианты.
Бык - цифра на своей позиции.
Корова - цифра есть в числе, но на другой позиции.
Цель - отгадать число.
"""


import random


def number_generation():
    """Генерирует 4-значное число с уникальными числами"""

    generator_list = list(range(10))
    random.shuffle(generator_list)
    if generator_list[0] == 0:
        generator_list[0] = generator_list[4]
    return "".join(map(str, generator_list[:4]))


generated_number = number_generation()  # pylint: disable=invalid-name
print("Компьютер загадал 4-значное число из уникальных цифр.")

while True:
    users_try = input('Твой вариант: ')
    if (
            not users_try.isdigit()
            or len(set(users_try)) != 4
            or len(users_try) != 4
    ):
        print('Ошибка. Введите 4-значное число с уникальными цифрами.')
        continue
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

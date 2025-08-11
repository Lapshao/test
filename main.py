# # # # # Запрашиваем у пользователя две строки
# # # # string1 = input("Введите первую строку: ")
# # # # string2 = input("Введите вторую строку: ")
# # # #
# # # # # Соединяем строки
# # # # combined_string = string1 + string2
# # # #
# # # # # Функция для проверки, является ли строка палиндромом
# # # # def is_palindrome(s):
# # # #     return s == s[::-1]
# # # #
# # # # # Проверяем, является ли полученная строка палиндромом
# # # # if is_palindrome(combined_string):
# # # #     print("Строка является палиндромом")
# # # # else:
# # # #     print("Строка не является палиндромом")
# # # #
# # # # # ЗАДАНИЕ 2
# # # # import random
# # # #
# # # # # Компьютер загадывает случайное число от 1 до 100
# # # # secret_number = random.randint(1, 100)
# # # # attempts = 0
# # # #
# # # # print("Добро пожаловать в игру 'Угадай число'!")
# # # # print("Я загадал число от 1 до 100. Попробуйте угадать!")
# # # #
# # # # while True:
# # # #     # Запрашиваем у пользователя ввод числа
# # # #     guess = int(input("Введите ваше предположение: "))
# # # #     attempts += 1
# # # #
# # # #     # Проверяем, угадал ли пользователь
# # # #     if guess < secret_number:
# # # #         print("Загаданное число больше.")
# # # #     elif guess > secret_number:
# # # #         print("Загаданное число меньше.")
# # # #     else:
# # # #         print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
# # # #         break
# # # #
# # # # # ЗАДАНИЕ 3
# # # #
# # # # # Создаем игровое поле 3x3
# # # # board = [[" " for _ in range(3)] for _ in range(3)]
# # # #
# # # # # Функция для отображения игрового поля
# # # # def display_board():
# # # #     for row in board:
# # # #         print("|".join(row))
# # # #         print("-" * 5)
# # # #
# # # # # Функция для проверки победителя
# # # # def check_winner(symbol):
# # # #     # Проверка строк и столбцов
# # # #     for i in range(3):
# # # #         if all([cell == symbol for cell in board[i]]) or all([board[j][i] == symbol for j in range(3)]):
# # # #             return True
# # # #     # Проверка диагоналей
# # # #     if all([board[i][i] == symbol for i in range(3)]) or all([board[i][2 - i] == symbol for i in range(3)]):
# # # #         return True
# # # #     return False
# # # #
# # # # # Функция для проверки ничьей
# # # # def is_draw():
# # # #     return all([cell != " " for row in board for cell in row])
# # # #
# # # # # Основной цикл игры
# # # # current_player = "X"
# # # # while True:
# # # #     display_board()
# # # #     print(f"Ход игрока {current_player}")
# # # #
# # # #     # Запрашиваем у игрока координаты
# # # #     try:
# # # #         row, col = map(int, input("Введите строку и столбец (через пробел): ").split())
# # # #         if board[row][col] != " ":
# # # #             print("Эта ячейка уже занята! Попробуйте снова.")
# # # #             continue
# # # #     except (ValueError, IndexError):
# # # #         print("Некорректный ввод! Введите два числа через пробел (например, '0 1').")
# # # #         continue
# # # #
# # # #     # Ставим символ игрока на поле
# # # #     board[row][col] = current_player
# # # #
# # # #     # Проверяем, выиграл ли игрок
# # # #     if check_winner(current_player):
# # # #         display_board()
# # # #         print(f"Игрок {current_player} победил!")
# # # #         break
# # # #
# # # #     # Проверяем, есть ли ничья
# # # #     if is_draw():
# # # #         display_board()
# # # #         print("Ничья!")
# # # #         break
# # # #
# # # #     # Меняем игрока
# # # #     current_player = "O" if current_player == "X" else "X"
# # #
# # #
# # # # ДЕНЬ 2
# # #
# # #
# # # # # ЗАДАНИЕ 2.1
# # # #
# # # # # 1. Программа приветствует пользователя
# # # # print("Добро пожаловать в мир приключений!")
# # # #
# # # # # 2. Запрос имени у пользователя
# # # # name = input("Как вас зовут? ")
# # # #
# # # # # 3. Создание списка с возможными расами для героя
# # # # races = ['эльф', 'гном', 'человек', 'хоббит']
# # # #
# # # # # 4. Вывод надписи на консольное окно
# # # # print(f"Я рад видеть тебя, {name}! К какому виду ты принадлежишь: {races}?")
# # # #
# # # # # 5. Создание переменных hp и damage с нулевыми значениями
# # # # hp = 0
# # # # damage = 0
# # # #
# # # # # 6. Переменная для хранения ответа пользователя о выборе расы
# # # # race_choice = input("Введите вашу расу: ").lower()
# # # #
# # # # # 7. Условная конструкция для начисления здоровья и урона в зависимости от расы
# # # # if race_choice == 'эльф':
# # # #     hp = 80
# # # #     damage = 25
# # # # elif race_choice == 'гном':
# # # #     hp = 100
# # # #     damage = 20
# # # # elif race_choice == 'человек':
# # # #     hp = 90
# # # #     damage = 30
# # # # elif race_choice == 'хоббит':
# # # #     hp = 70
# # # #     damage = 35
# # # # else:
# # # #     print("Такой расы нет. Выбрана раса по умолчанию: человек.")
# # # #     race_choice = 'человек'
# # # #     hp = 90
# # # #     damage = 30
# # # #
# # # # # 8. Вывод характеристик игрока на консольное окно
# # # # print(f"\nХарактеристики вашего героя:")
# # # # print(f"Имя: {name}")
# # # # print(f"Раса: {race_choice}")
# # # # print(f"Здоровье: {hp}")
# # # # print(f"Урон: {damage}")
# # # #
# # # # # 9. Создание списка с вариантами уровней
# # # # levels = [1, 2, 3, 4, 5]
# # # #
# # # # # 10. Цикл for для перебора списка с уровнями и увеличения характеристик героя
# # # # for level in levels:
# # # #     hp += 10  # Увеличиваем здоровье на 10 за каждый уровень
# # # #     damage += 5  # Увеличиваем урон на 5 за каждый уровень
# # # #     print(f"\nПосле прохождения уровня {level}:")
# # # #     print(f"Здоровье: {hp}")
# # # #     print(f"Урон: {damage}")
# # # #
# # # # print("\nПоздравляем! Вы успешно улучшили своего героя!")
# # #
# # # # Задание 1
# # #
# # # def factorial(n):
# # #     if n < 0:
# # #         return "Факториал определен только для неотрицательных чисел."
# # #     result = 1
# # #     for i in range(1, n + 1):
# # #         result *= i
# # #     return result
# # #
# # # # Пример использования
# # # num = int(input("Введите число для вычисления факториала: "))
# # # print(f"Факториал числа {num} равен: {factorial(num)}")
# # #
# # # # Задание 2
# # #
# # # def is_palindrome(word):
# # #     word = word.lower().replace(" ", "")  # Убираем пробелы и делаем нижний регистр
# # #     return word == word[::-1]
# # #
# # # # Пример использования
# # # word = input("Введите слово для проверки на палиндром: ")
# # # if is_palindrome(word):
# # #     print(f"Слово '{word}' является палиндромом.")
# # # else:
# # #     print(f"Слово '{word}' не является палиндромом.")
# # #
# # # # Задание 3
# # #
# # # import random
# # #
# # # def guess_the_number():
# # #     number_to_guess = random.randint(1, 100)
# # #     attempts = 0
# # #     while True:
# # #         guess = int(input("Угадайте число от 1 до 100: "))
# # #         attempts += 1
# # #         if guess < number_to_guess:
# # #             print("Загаданное число больше.")
# # #         elif guess > number_to_guess:
# # #             print("Загаданное число меньше.")
# # #         else:
# # #             print(f"Вы угадали число за {attempts} попыток!")
# # #             break
# # #
# # # # Запуск игры
# # # guess_the_number()
# # #
# # # # Задание 4
# # #
# # # def count_words(text):
# # #     words = text.split()
# # #     return len(words)
# # #
# # # # Пример использования
# # # text = input("Введите текст: ")
# # # print(f"Количество слов в тексте: {count_words(text)}")
# # #
# # # # Задание 5
# # #
# # # def caesar_cipher(text, shift):
# # #     result = ""
# # #     for char in text:
# # #         if char.isalpha():
# # #             offset = 65 if char.isupper() else 97
# # #             result += chr((ord(char) - offset + shift) % 26 + offset)
# # #         else:
# # #             result += char
# # #     return result
# # #
# # # # Пример использования
# # # text = input("Введите текст для шифрования: ")
# # # shift = int(input("Введите сдвиг: "))
# # # encrypted_text = caesar_cipher(text, shift)
# # # print(f"Зашифрованный текст: {encrypted_text}")
# # #
# # # # Задание 6
# # #
# # # def complex_calculator():
# # #     a = complex(input("Введите первое комплексное число (например, 3+4j): "))
# # #     b = complex(input("Введите второе комплексное число (например, 1-2j): "))
# # #     operation = input("Выберите операцию (+, -, *, /): ")
# # #
# # #     if operation == "+":
# # #         result = a + b
# # #     elif operation == "-":
# # #         result = a - b
# # #     elif operation == "*":
# # #         result = a * b
# # #     elif operation == "/":
# # #         result = a / b
# # #     else:
# # #         return "Неверная операция."
# # #
# # #     return f"Результат: {result}"
# # #
# # # # Пример использования
# # # print(complex_calculator())
# # #
# # # # Задание 7
# # #
# # # import math
# # #
# # # def solve_quadratic(a, b, c):
# # #     discriminant = b**2 - 4*a*c
# # #     if discriminant > 0:
# # #         x1 = (-b + math.sqrt(discriminant)) / (2*a)
# # #         x2 = (-b - math.sqrt(discriminant)) / (2*a)
# # #         return f"Корни: x1 = {x1}, x2 = {x2}"
# # #     elif discriminant == 0:
# # #         x = -b / (2*a)
# # #         return f"Один корень: x = {x}"
# # #     else:
# # #         return "Нет действительных корней."
# # #
# # # # Пример использования
# # # a = float(input("Введите коэффициент a: "))
# # # b = float(input("Введите коэффициент b: "))
# # # c = float(input("Введите коэффициент c: "))
# # # print(solve_quadratic(a, b, c))
# # #
# # # # Задание 8
# # #
# # # def gcd(a, b):
# # #     while b != 0:
# # #         a, b = b, a % b
# # #     return a
# # #
# # # # Пример использования
# # # num1 = int(input("Введите первое число: "))
# # # num2 = int(input("Введите второе число: "))
# # # print(f"НОД чисел {num1} и {num2}: {gcd(num1, num2)}")
# # #
# # # # Задание 9
# # #
# # # import random
# # # import string
# # #
# # # def generate_password(length):
# # #     characters = string.ascii_letters + string.digits + string.punctuation
# # #     password = ''.join(random.choice(characters) for _ in range(length))
# # #     return password
# # #
# # # # Пример использования
# # # length = int(input("Введите длину пароля: "))
# # # print(f"Сгенерированный пароль: {generate_password(length)}")
# # #
# # # # Задание 10
# # #
# # # def convert_temperature(temp, from_scale, to_scale):
# # #     if from_scale == "C":
# # #         if to_scale == "F":
# # #             return temp * 9/5 + 32
# # #         elif to_scale == "K":
# # #             return temp + 273.15
# # #     elif from_scale == "F":
# # #         if to_scale == "C":
# # #             return (temp - 32) * 5/9
# # #         elif to_scale == "K":
# # #             return (temp - 32) * 5/9 + 273.15
# # #     elif from_scale == "K":
# # #         if to_scale == "C":
# # #             return temp - 273.15
# # #         elif to_scale == "F":
# # #             return (temp - 273.15) * 9/5 + 32
# # #     return "Ошибка конвертации."
# # #
# # # # Пример использования
# # # temp = float(input("Введите температуру: "))
# # # from_scale = input("Исходная шкала (C, F, K): ").upper()
# # # to_scale = input("Целевая шкала (C, F, K): ").upper()
# # # print(f"Конвертированная температура: {convert_temperature(temp, from_scale, to_scale)}")
# #
# #
# # # ДЕНЬ 3
# #
# #
# # # Задание 1
# #
# # def calculate_average(*args):
# #     numbers = [arg for arg in args if isinstance(arg, (int, float))]
# #     if not numbers:
# #         return 0
# #     return sum(numbers) / len(numbers)
# #
# # # Пример использования
# # print(calculate_average(10, 20, 30, "a", None))  # Вывод: 20.0
# # print(calculate_average(5, 15, 25))             # Вывод: 15.0
# # print(calculate_average("hello", True, 42))     # Вывод: 42.0
# #
# # # Задание 2
# #
# # def reverse_words(sentence):
# #     words = sentence.split()
# #     reversed_words = [word[::-1] for word in words]
# #     return ' '.join(reversed_words)
# #
# # # Пример использования
# # print(reverse_words("Hello world"))  # Вывод: "olleH dlrow"
# # print(reverse_words("Python is fun"))  # Вывод: "nohtyP si nuf"
# #
# # # Задание 3
# #
# # import string
# #
# # def is_palindrome(s):
# #     s = ''.join(char.lower() for char in s if char.isalnum())
# #     return s == s[::-1]
# #
# # # Пример использования
# # print(is_palindrome("A man, a plan, a canal, Panama"))  # Вывод: True
# # print(is_palindrome("racecar"))                         # Вывод: True
# # print(is_palindrome("hello"))                           # Вывод: False
# #
# # # Задание 4
# #
# # def find_longest_subsequence(s1, s2):
# #     m, n = len(s1), len(s2)
# #     dp = [[0] * (n + 1) for _ in range(m + 1)]
# #     for i in range(1, m + 1):
# #         for j in range(1, n + 1):
# #             if s1[i - 1] == s2[j - 1]:
# #                 dp[i][j] = dp[i - 1][j - 1] + 1
# #             else:
# #                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# #     lcs = []
# #     i, j = m, n
# #     while i > 0 and j > 0:
# #         if s1[i - 1] == s2[j - 1]:
# #             lcs.append(s1[i - 1])
# #             i -= 1
# #             j -= 1
# #         elif dp[i - 1][j] > dp[i][j - 1]:
# #             i -= 1
# #         else:
# #             j -= 1
# #     return ''.join(reversed(lcs))
# #
# # # Пример использования
# # print(find_longest_subsequence("abcde", "ace"))  # Вывод: "ace"
# # print(find_longest_subsequence("abc", "def"))    # Вывод: ""
# #
# # # Задание 5
# #
# # def add_numbers(a, b):
# #     return a + b
# #
# # # Пример использования
# # print(add_numbers(5, 7))  # Вывод: 12
# #
# # # Задание 6
# #
# # square = lambda x: x ** 2
# #
# # # Пример использования
# # print(square(5))  # Вывод: 25
# #
# # # Задание 7
# #
# # def is_even(n):
# #     return n % 2 == 0
# #
# # # Пример использования
# # print(is_even(4))  # Вывод: True
# # print(is_even(7))  # Вывод: False
# #
# # # Задание 8
# #
# # def find_max(lst):
# #     return max(lst)
# #
# # # Пример использования
# # print(find_max([3, 1, 4, 1, 5, 9]))  # Вывод: 9
# #
# # # Задание 9
# #
# # to_lower = lambda s: s.lower()
# #
# # # Пример использования
# # print(to_lower("HELLO"))  # Вывод: "hello"
# #
# # # Задание 10
# #
# # def count_vowels(s):
# #     vowels = "aeiouAEIOU"
# #     return sum(1 for char in s if char in vowels)
# #
# # # Пример использования
# # print(count_vowels("hello world"))  # Вывод: 3
# #
# # # Задание 11
# #
# # remove_spaces = lambda s: s.replace(" ", "")
# #
# # # Пример использования
# # print(remove_spaces("hello world"))  # Вывод: "helloworld"
# #
# # # Задание 12
# #
# # def celsius_to_fahrenheit(c):
# #     return c * 9/5 + 32
# #
# # # Пример использования
# # print(celsius_to_fahrenheit(0))   # Вывод: 32.0
# #
# # # Задание 13
# #
# # def string_length(s):
# #     return len(s)
# #
# # # Пример использования
# # print(string_length("hello"))  # Вывод: 5
# #
# # # Задание 14
# #
# # replace_char = lambda s, old, new: s.replace(old, new)
# #
# # # Пример использования
# # print(replace_char("hello", "l", "x"))  # Вывод: "hexxo"
# #
# # # Задание 15
# #
# # def average(lst):
# #     return sum(lst) / len(lst)
# #
# # # Пример использования
# # print(average([1, 2, 3, 4, 5]))  # Вывод: 3.0
# #
# # # Задание 16
# #
# # is_positive = lambda x: x > 0
# #
# # # Пример использования
# # print(is_positive(5))   # Вывод: True
# # print(is_positive(-3))  # Вывод: False
# #
# # # Задание 17
# #
# # def concatenate_strings(s1, s2):
# #     return s1 + s2
# #
# # # Пример использования
# # print(concatenate_strings("hello", "world"))  # Вывод: "helloworld"
# #
# # # Задание 18
# #
# # subtract = lambda a, b: a - b
# #
# # # Пример использования
# # print(subtract(10, 3))  # Вывод: 7
# #
# # # Задание 19
# #
# # def unique_elements(lst):
# #     return list(set(lst))
# #
# # # Пример использования
# # print(unique_elements([1, 2, 2, 3, 4, 4]))  # Вывод: [1, 2, 3, 4]
# #
# # # Задание 20
# #
# # last_char = lambda s: s[-1] if s else ''
# #
# # # Пример использования
# # print(last_char("hello"))  # Вывод: "o"
# #
# # # Задание 21
# #
# # def is_palindrome(s):
# #     s = ''.join(char.lower() for char in s if char.isalnum())
# #     return s == s[::-1]
# #
# # # Пример использования
# # print(is_palindrome("racecar"))  # Вывод: True
# #
# # # Задание 22
# #
# # min_element = lambda lst: min(lst)
# #
# # # Пример использования
# # print(min_element([3, 1, 4, 1, 5, 9]))  # Вывод: 1
# #
# # # Задание 23
# #
# # def squares(lst):
# #     return [x ** 2 for x in lst]
# #
# # # Пример использования
# # print(squares([1, 2, 3, 4]))  # Вывод: [1, 4, 9, 16]
# #
# # # Задание 24
# #
# # merge_lists = lambda lst1, lst2: lst1 + lst2
# #
# # # Пример использования
# # print(merge_lists([1, 2], [3, 4]))  # Вывод: [1, 2, 3, 4]
#
#
#
# # ДЕНЬ 4
#
# # Задание 1
#
# # math_utils.py
#
# def factorial(n):
#     if n < 0:
#         raise ValueError("Факториал определен только для неотрицательных чисел.")
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)
#
# def is_perfect_square(n):
#     if n < 0:
#         return False
#     root = int(n**0.5)
#     return root * root == n
#
# # Задание 2
#
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius**2
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def area(self):
#         # Формула Герона
#         s = (self.side1 + self.side2 + self.side3) / 2
#         return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
#
#     def perimeter(self):
#         return self.side1 + self.side2 + self.side3
#
# # Задание 3
#
# import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         print(f"Запуск функции {func.__name__}...")
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Функция {func.__name__} выполнена за {end_time - start_time:.4f} секунд.")
#         return result
#     return wrapper
#
# # Пример использования
# @measure_time
# def example_function():
#     time.sleep(2)
#
# example_function()
#
# # Задание 4
#
# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции {func.__name__} с аргументами:")
#         print(f"Позиционные аргументы: {args}")
#         print(f"Именованные аргументы: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Результат: {result}")
#         return result
#     return wrapper
#
# # Пример использования
# @debug
# def add(a, b):
#     return a + b
#
# add(5, b=3)
#
# # Задание 5
#
# from dataclasses import dataclass
#
# @dataclass
# class Person:
#     name: str
#     age: int
#     email: str
#
# # Задание 6
#
# from dataclasses import dataclass
#
# @dataclass
# class Product:
#     name: str
#     price: float
#     quantity: int
#
# # Задание 7
#
# from dataclasses import dataclass
#
# @dataclass
# class Book:
#     title: str
#     author: str
#     year: int
#     isbn: str
#
# # Задание 8
#
# # math_utils.py
#
# import math
#
# def square_root(n):
#     return math.sqrt(n)
#
# def factorial(n):
#     return math.factorial(n)
#
# # main.py
#
# # from math_utils import square_root, factorial
#
# print(square_root(16))  # Вывод: 4.0
# print(factorial(5))     # Вывод: 120
#
# # Задание 9
#
# from datetime import datetime
#
# current_datetime = datetime.now()
# print(f"Текущая дата и время: {current_datetime}")
#
# # Задание 10
# # string_utils.py
#
# def to_uppercase(s):
#     return s.upper()
#
# def to_lowercase(s):
#     return s.lower()
#
# def is_palindrome(s):
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]
#
# # main.py
# # from string_utils import to_uppercase, to_lowercase, is_palindrome
#
# print(to_uppercase("hello"))  # Вывод: "HELLO"
# print(to_lowercase("WORLD"))  # Вывод: "world"
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Вывод: True
#
# # Задание 11
# # module_a.py
# # from module_b import greet_from_b
#
# def greet_from_a():
#     return "Привет из module_a!"
#
# def call_greet_from_b():
#     return greet_from_b()
# #
# # module_b.py
#
# # from module_a import greet_from_a
#
# def greet_from_b():
#     return "Привет из module_b!"
#
# def call_greet_from_a():
#     return greet_from_a()
#
# # main.py
#
# # from module_a import call_greet_from_b
# # from module_b import call_greet_from_a
#
# print(call_greet_from_b())  # Вывод: "Привет из module_b!"
# print(call_greet_from_a())  # Вывод: "Привет из module_a!"


# ДЕНЬ 5

# Задание 1

# import turtle
#
# # Create a turtle object
# pen = turtle.Turtle()
#
# # Draw a star
# for _ in range(5):
#     pen.forward(100)
#     pen.right(144)
#
# # Finish drawing and wait for user input
# turtle.done()

# # Задание 2.1
#
# import turtle
#
# pen = turtle.Turtle()
#
# # Draw a square
# for _ in range(4):
#     pen.forward(100)
#     pen.right(90)
#
# turtle.done()

# # Задание 2.2
#
# import turtle
#
# pen = turtle.Turtle()
#
# # Draw a rectangle
# pen.forward(150)  # Length
# pen.right(90)
# pen.forward(75)   # Width
# pen.right(90)
# pen.forward(150)  # Length
# pen.right(90)
# pen.forward(75)   # Width
#
# turtle.done()

# # Задание 2.3
#
# import turtle
#
# pen = turtle.Turtle()
#
# # Draw a circle
# pen.circle(50)
#
# turtle.done()

# Задание 2.4

# import turtle
#
# pen = turtle.Turtle()
#
# # Draw a triangle
# for _ in range(3):
#     pen.forward(100)
#     pen.left(120)
#
# turtle.done()

# Задание 3

# import turtle
# # Настройка экрана
# screen = turtle.Screen()
# screen.bgcolor("white")
# # Создание объекта черепахи
# pen = turtle.Turtle()
# pen.speed(2)  # Установка скорости рисования
# pen.color("#2CA5E0")  # Цвет логотипа Telegram (синий)
# # Начало рисования
# pen.penup()
# pen.goto(-50, 0)  # Начальная позиция
# pen.pendown()
# # Рисование "крыльев" самолетика
# pen.begin_fill()
# pen.forward(100)  # Горизонтальная линия
# pen.left(135)
# pen.forward(70)   # Первое крыло
# pen.right(90)
# pen.forward(70)   # Второе крыло
# pen.left(135)
# pen.forward(100)  # Завершение основной части
# pen.end_fill()
# # Рисование хвоста
# pen.penup()
# pen.goto(-10, 0)  # Переход к началу хвоста
# pen.pendown()
# pen.begin_fill()
# pen.right(90)
# pen.forward(40)   # Хвост вниз
# pen.right(135)
# pen.forward(50)   # Диагональная линия хвоста
# pen.right(135)
# pen.forward(40)   # Завершение хвоста
# pen.end_fill()
# # Добавление жёлтого круга рядом
# pen.penup()
# pen.goto(100, -30)  # Позиция для круга
# pen.pendown()
# pen.color("yellow")  # Жёлтый цвет
# pen.begin_fill()
# pen.circle(30)       # Рисование круга
# pen.end_fill()
# # Завершение программы
# pen.hideturtle()      # Скрываем черепаху
# turtle.done()

# Задание 4

# import turtle
#
# pen = turtle.Turtle()
#
# # Draw the body
# pen.fillcolor("blue")
# pen.begin_fill()
# pen.circle(50)
# pen.end_fill()
#
# # Draw the backpack
# pen.penup()
# pen.goto(-10, -50)
# pen.pendown()
# pen.fillcolor("gray")
# pen.begin_fill()
# pen.circle(30)
# pen.end_fill()
#
# # Draw the visor
# pen.penup()
# pen.goto(20, 60)
# pen.pendown()
# pen.fillcolor("white")
# pen.begin_fill()
# pen.circle(20)
# pen.end_fill()
#
# turtle.done()

# Задание 5

# import turtle
#
# pen = turtle.Turtle()
#
# # Draw the virus body
# pen.fillcolor("green")
# pen.begin_fill()
# pen.circle(50)
# pen.end_fill()
#
# # Draw spikes
# pen.penup()
# pen.goto(0, 50)
# pen.pendown()
# for _ in range(8):
#     pen.forward(30)
#     pen.backward(30)
#     pen.right(45)
#
# turtle.done()

# Задание 6

import turtle

# def draw_tree(branch_length, t):
#     if branch_length > 5:
#         t.forward(branch_length)
#         t.right(20)
#         draw_tree(branch_length - 15, t)
#         t.left(40)
#         draw_tree(branch_length - 15, t)
#         t.right(20)
#         t.backward(branch_length)
#
# def main():
#     t = turtle.Turtle()
#     screen = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("brown")
#     draw_tree(75, t)
#     screen.exitonclick()
#
# main()

# Задание 7

import turtle
#
# def koch_curve(t, iterations, length, shortening_factor, angle):
#     if iterations == 0:
#         t.forward(length)
#     else:
#         iterations -= 1
#         length /= shortening_factor
#         koch_curve(t, iterations, length, shortening_factor, angle)
#         t.left(angle)
#         koch_curve(t, iterations, length, shortening_factor, angle)
#         t.right(angle * 2)
#         koch_curve(t, iterations, length, shortening_factor, angle)
#         t.left(angle)
#         koch_curve(t, iterations, length, shortening_factor, angle)
#
# def main():
#     t = turtle.Turtle()
#     screen = turtle.Screen()
#     t.speed(0)
#     for _ in range(3):
#         koch_curve(t, 4, 200, 3, 60)
#         t.right(120)
#     screen.exitonclick()
#
# main()

# Задание 8 8 8

import turtle
import math

def lissajous(t, a, b, delta):
    t.penup()
    for i in range(0, 361):
        x = 100 * math.sin(math.radians(a * i))
        y = 100 * math.sin(math.radians(b * i + delta))
        t.goto(x, y)
        t.pendown()

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    lissajous(t, 3, 2, 90)
    screen.exitonclick()

main()

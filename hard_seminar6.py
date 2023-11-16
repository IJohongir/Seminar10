# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# def get_file_info(file_path):


#     dirname= os.path.dirname(file_path)
#     dirname=os.path.split(file_path)[0]
#     basename=os.path.split(file_path)[1]
#     basename,expentc=os.path.splitext(basename)
#     result=(str(dirname),str(basename),str(expentc))
#     return result
#     Geekbrains
# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)



# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.

# Сумма рассчитывается как ставка умноженная на процент премии.

# Не забудьте распечатать в конце результат.

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

# result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
# print(result)

#funksiya fibonaci
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# Расстановка ферзей


#_______________________________________

# import random
# from itertools import combinations

# def generate_board():
#     # Генерируем случайную доску
#     board = []

#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board

# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True

# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list

# print(generate_boards())

# Задача о 8 ферзях
# from itertools import combinations
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] 


# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True


#_______________________________________

# Проверка корректности даты
# from sys import argv

# def is_leap(year: int) :
#     return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

# def valid(full_date: str) :
#     date, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
#         return False
#     if month in (4, 6, 9, 11) and date > 30:
#         return False
#     if month == 2 and is_leap(year) and date > 29:
#         return False
#     if month == 2 and not is_leap(year) and date > 28:
#         return False
#     return True
# date_to_prove = "15.4.2023"
# if len(argv) > 1:
#     print(valid(argv[1]))
# else:
#     print(valid(date_to_prove ))

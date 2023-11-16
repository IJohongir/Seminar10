# import re

# str="3 товара за 200.99"
# pat= r'\d+.\d'
# match= re.search(pat,str)

# print(match.group())
# link='https://jut.su/jujutsu-kaisen/season-2/episode-15.html'
# prefix,*_,suffix=link.split('/')
# print(suffix)
# print(prefix)
# print(_)

# import os


# file_path = "C:/Users/User/Documents/example.txt"
# print(get_file_info(file_path))
# list1=(str(dirname),str(basename),str(ecpent))

# d=[2,3,4,5,6]
# for i in d :
#     print(i,end='\t')

# print(end=' \n')

# print(*d,sep='\t')
# a=12;b=42;c=73
# if a < b < c: b=None;print("Ujas")

# data={10,9,8,1,6,3}
# a,b,c,*d,e= data
# print(a,b,c,d,e)

# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if isinstance(value, (int, str, float, bool, tuple)):
#             result[value] = key
#         else:
#             result[str(value)] = key
#     return result


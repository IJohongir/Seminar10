# my_list=[4,5,3,2,3,45,54]
# # res = list(reversed(my_list))
# # print(res)
# # my_list.reverse()
# # print(my_list)
# new_list = my_list[::-1]
# print(my_list,new_list,sep='\n')

# my_list=['h','e','l','l','o']
# # my_list.sort()
# my_list=sorted(my_list)
# print(my_list)
# my_dict ={'one':1,'two':2,'four':4,'ten':10}
# print(my_dict.keys())

# for key in my_dict:
#     print(key)

# print(my_dict.values())

# for key in my_dict.values():
# #     print(key)
# print(my_dict.items())
# for key,value in my_dict.items():
#     print(f'{key =} bla bla 100 {value}')




# items_dict = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
# max1=[]

# for value in items_dict.values():
#     max1.append(value)

# backpack={}
# max1=max(max1)
# for keys,value in items_dict.items():
#     print(value)
    
#     backpack.fromkeys(keys[value])

# print(backpack)
# text='слова был один пробел между ним и номером строки'

# text=text.split()
# text.sort()
# print(text)
#Hard-Seminar3
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0

# backpack = {}

# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight
# print(backpack)
#my-work
# import string
# import itertools

# line = "Python 3.9 is the latest version of Python. It's awesome!"

# line = ((line.translate(str.maketrans('', '', string.punctuation))).lower()).split()
# d = list()
# for word in line:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] = d[word] + 1
   
# d = ({k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)})
# d = dict(itertools.islice(d.items(),10))
# print(d)

#Geekwork
# import re
# from collections import Counter
# text = 'Hello world,World. Hello Python. Hello again.'
# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)


# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}

# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1
# print(word_counts)
# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# print(top_words)



# items = {

#     "ключи": 0.3,

#     "кошелек": 0.2,

#     "телефон": 0.5,

#     "зажигалка": 0.1

# }





# max_weight = 1.0
# from pprint import pprint
# backpacks = []
# sorted_result = []
# for i in range(2**len(items)):
#     backpack = {}
#     weight = 0
#     for j, item in enumerate(items):
#         if i & (1 << j):
#             if weight + items[item] <= max_weight:
#                 backpack[item] = items[item]
#                 weight += items[item]
#             else:
#                 break
#     backpacks.append(backpack)

# full_result = [backpack for backpack in backpacks if backpack]
# result = []
# for item in full_result:
#     if item not in result:
#         result.append(item)
# pprint(result)

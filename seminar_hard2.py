# frac1=input("Введите дроб через '/' ")
# frac2=input("Введите дроб через '/' ")


# list1=list(map(int,(frac1.split('/'))))
# list2=list(map(int,(frac2.split('/'))))


# if list1[1] != list2[1]:
#     sum1=int((list1[0]*list2[1]+list1[1]*list2[0]))
#     sum2=int(list1[1]*list2[1])
#     P1=int(list1[0]*list2[0])
#     P2=int(list1[1]*list2[1])

# elif list1[1]==list2[1]:
#     sum1=int((list1[0]*list2[1]+list1[1]*list2[0]))
#     sum2=int(list1[1])
#     P1=int(list1[0]*list2[1])
#     P2=int(list1[1]*list2[1])

# print(f"Summa : {sum1}/{sum2}")
# print(f"Произведения : {P1}/{P2}")



# a=int(input('kirit :'))
# b=a
# list2=[]
# while a > 0 :
#     q=a%16
#     list2.append(q)
#     a=a//16
# num16=''
# list1=list(reversed(list2))
# for i in list1 :
#     if i>=0 and i<=9:
#         num16+=str(i)
#     elif i ==10:
#         num16+="A"
#     elif i ==11:
#         num16+="B"
#     elif i ==12:
#         num16+="C"
#     elif i ==13:
#         num16+="D"
#     elif i ==14:
#         num16+="E"
#     elif i ==15:
#         num16+="F"
# print(num16)
# print(hex(b))

#№2
# my_list = [1,1,2,2,3,4]
# new_list =[]
# # print(list(set(my_list)))

# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)

# #№3
# info = input('Введите информацию: ')
# if info.isdigit():
#     print(int(info))
# elif info.replace('.', '').isdigit():
#     print(float(info))
# else:
#     print(info.lower())

# t1=(12,342,True,'Hello',"bye",3.14,43.23,1123.3,False,False)


# d=dict()

# for item in t1 :
#     key=type(item)
#     if key in d :
#         d[key].append(item)
#     else :
#         d[key]=[item]
# print(d)

# print(d)
# list1=["hello",'bye','hello','sd','sdd',2,3,4,4,4]
# list2=[]
# import math 
# n = int(input(" sonni kiriting :  "))
# count = None
# for i in range(2,int(math.sqrt(n))+1):
#     if n % i != 0:
#         count=True
# print(count)


# count=0
# for i in range(1,n+1):
#     if n % i == 0 :
#         count+=1

# if count==2 :
#     print(f" Bu son tub son {n}")

# else :
#     print("tub son emas")

# """16lik sistema"""
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c" "d", "e", "f" ]
# print(len(my_list))
# n = int(input("Lyuboy sonni kirirting: "))
# d = n
# sanab_beraman = 0
# i = 0
# while i < n:
#     sanab_beraman += 1
#     butun = n // 16
#     qoldiq = n % 16
#     d //= 16
#     if d <= i:
#         break
# if butun >= 16:
    
#     a_str = str(sanab_beraman)
#     a = len(a_str)
#     b = int(a_str)
#     g = (b-1) * my_list[-1]
#     resalt1 = my_list[qoldiq] 
#     yangi_list = [g, resalt1]
#     for x in yangi_list:
#         if x != 0:
#             print(x, end="")
            
#     # print(f"{g}{resalt1}")
   
# else:
#     # print(f" butun {butun} qoldiq{qoldiq} ")
#     alfa = my_list[butun]
#     betta = my_list[qoldiq]
#     print(f"{alfa}{betta}")
#########Algoritmlash
# a= int(input('a kiriting :'))
# b=[]

# for i in range(1,a+1):
#     cn=i
#     count=0 
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         b.append(cn)

# print(b)

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end='')
#     print()

# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(j,end='')
#     print()

# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for z in range(0,i):
#         print("*",end=" ")
        
#     print()

# for i in range(1,6 ):
#     for j in range(5,0,-1):
#         if i>=j:
#             print("*",end=" ")
#         else:
#             print(" ",end="")
#     print()
# items = (True, False, 1, 2, 5.5, 'salom')
# dic = {}
# son = []
# onlik = []
# matn = []
# boolin = []
# for n in items:
#     if type(n) == int:
#         son.append(n)
#     dic['class int>>'] = son
#     if type(n) == float:
#         onlik.append(n)
#     dic['class float>>'] = onlik
#     if type(n) == str:
#         matn.append(n)
#     dic['class str>>'] = matn
#     if type(n) == bool:
#         boolin.append(n)
#     dic['class bolin>>'] = boolin

# # print(dic)
# def transpose_matrix(matrix:list):
#     transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             transposed_matrix[j][i] = matrix[i][j]
#     return transposed_matrix

# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print(len(matrix))
# a=transpose_matrix(matrix)
# print(a)
# A = [[5, 4, 3], [2, 4, 6], [4, 7, 9]]

 

# d=transpose_matrix(A)
# print(d)
            
# matrix = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# row = []

# for i in range(3):
#     for j in range(3):
#         pass

# transport_matrix = [[matrix[j][i] for j in range(3)] for i in range(3)]

# print(transport_matrix)

# x=y=25
# # print(x, y)
# fruits = ["apple", "banana", "cherry", "ball", "banana"]
# print("apple" in fruits)
# vegs = ["tomoato"]
# fv = fruits + vegs
# print(fv * 5)
# print(fruits)
# # Change the second item
# fruits[1] = "bananaaaa"
# print(fruits)
# fruits.insert(6, "Cherryyyyy")
# print(fruits)
# fruits.append("shakeer")
# print(fruits)
# fruits.remove("shakeer")
# del fruits[0:1]
# print(fruits)
# fruits.pop()
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# fruits.sort(reverse= True)
# fruits.sort()
# print(fruits)

# l2=[x**3 for x in range(5)]

# print(l2)

# cart=[]

# cart.append("Eggs")
# print(cart)
# cart.insert(1,"Chiken")
# print(cart)









# empty_tuple = ()
# single_element_tuple = (4,)
# multi_element_tuple = ("banana", "5", "5.5")
# print(empty_tuple, single_element_tuple, multi_element_tuple)

# fruits = ["apple", "banana", "cherry", "ball", "banana"]
# f_tuple = tuple(fruits)
# print (f_tuple[0:], fruits)

# a = (1, 2)
# b = (3, 4)

# # Concatenate tuples
# c = a + b
# print(c)  # Output: (1, 2, 3, 4)

# # Repeat a tuple
# d = a * 3
# print(d)  # Output: (1, 2, 1, 2, 1, 2)


# print (1 in c , 100 in c)

# numbers = (1, 2, 3, 1, 1)
# print(numbers.index(2))  # Output: 1








person = ("John", 30, "shakeer","Engineer")

# name, age, profession = person
# name, *age, profession = person
# print(name)        # Output: John
# print(*age)         # Output: 30
# print(profession)  # Output: Engineer



# fruits = ["apple", "banana", "cherry", "ball", "banana"]
# name, age, profession,xxx,yyy = fruits

# print(xxx)



# my_tuple = (1, 2, 3, 4)
# my_list = list(my_tuple)

# print(my_list)  # Output: [1, 2, 3, 4]
# print(type(my_list))  # Output: <class 'list'>


# Tuple received from an external source
# data_tuple = (10, 20, 30, 40)

# # Convert to a list to modify
# data_list = list(data_tuple)
# data_list.append(50)
# print(data_list)  # Output: [10, 20, 30, 40, 50]
# data_tuple = data_list
# print(f'data tuple',data_tuple)

############################################################Range###############################
# print(tuple(range(5)))
# print(list(range(2, 7)))  # Output: [2, 3, 4, 5, 6]
# print(list(range(0,10,2)))

# for i in range(5):
#     print(i, end="-->")

# for i in range(5, 0, -1):
#     print(i, end="-->")

# for index, value in enumerate(range(5, 50, 5)):
#     print(index, value)

# # Print numbers divisible by 3
# for i in range(1, 20):
#     if i % 3 != 0:
#         print(i, end=" ")  # Output: 3 6 9 12 15 18

# num = 5
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")





# emty_dict = {}
# print(emty_dict)
# person = {"name": "John", "age": 30, "profession": "Engineer"}
# print(person["age"])

# dict1 = dict (name="Alice", age=25, profession="Doctor")
# print(dict1)

# # Converting list of tuples to dictionary
# pairs = [("name", "Bob"), ("age", 40)]
# person = dict(pairs)
# print(person)  # Output: {'name': 'Bob', 'age': 40}


# Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

# print(Dict[3]['B'])

import pandas as pd
random_dict = {'A1': {'age':20, 'city':"mumbai", 'tech':{'backend':'python', 'database':['mysql','mongo']}},
               'B1': {'age':25, 'city':"pune", 'tech':{'backend':'python', 'database':['mysql','pg','oracle']}},
               'C1': {'age':23, 'city':"nashik", 'tech':{'backend':'python', 'database':['mysql','oracle']}}}

# df = pd.DataFrame(random_dict)
# print(df['A1']['tech']['database'])
# print(random_dict['A1']['city'])
# print(random_dict.keys())
# print(random_dict.values())
# print(random_dict.items())

# oracle_users=[]
# for pd, details in random_dict.items():
#     if 'oracle' in details['tech']['database']:
#         oracle_users.append(pd)
# oracle_users=[]
# for dbcount, details in random_dict.items():
#     # print(details)
#     if 'oracle' in details['tech']['database']:
#         oracle_users.append(dbcount)
# print(oracle_users)

# uniqe_db=set()

# for details in random_dict.values():
#     uniqe_db.update(details['tech']['database'])

# print(uniqe_db)
    
# a = [1,2,3,0,False,None]
# numeric_values = list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), a))
# print(numeric_values)  # Output: [1, 2, 3, 0]




# Example: List of dictionaries
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35}
# ]

# print(people[0]['name'])





# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car.get("model"))


# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y=json.dumps(x)
# print(y)
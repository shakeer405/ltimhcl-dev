my_list = [1, 2, 3, "hello"]
print(my_list)
print (my_list.)
# my_list.append(4)  # Add item
# print(my_list[0])  # Access item
# my_list.remove(2)  # Remove item
# print(my_list)

# my_tuple = (1, 2, 3, "hello")
# print(my_tuple[1])

# # my_dict = {"name": "Alice", "age": 25}
# # print(my_dict["name"])  # Access value
# # my_dict["city"] = "NY"  # Add new key-value pair
# # print(my_dict)

# age = 13
# if age >= 18:
#     print("Adult")
# elif age > 12:
#     print("Teen")
# else:
#     print("Child")



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} {self.age}.")

# # Create an object
# person1 = Person("Alice", 25)
# person1.greet()


# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("Execution complete.")

# try:
#     with open("file.txt", "r") as file:
#         content = file.read()
#         print(content)
# except :
#   print("File Not found")


# import threading

# def print_numbers():
#     for i in range(1000):
#         print(i)

# t1 = threading.Thread(target=print_numbers)
# t1.start()
# t1.join()

# def my_gen():
#     yield 1
#     yield 2

# for val in my_gen():
#     print(val)


# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# import threading

# # Function to print a range of numbers
# def print_numbers(start, end):
#     for i in range(start, end):
#         print(i, end=' ')

# # Total numbers to print and thread count
# total_numbers = 1000
# num_threads = 100

# # Numbers per thread
# numbers_per_thread = total_numbers // num_threads

# # List to hold all threads
# threads = []

# # Create and start 100 threads
# for i in range(num_threads):
#     start = i * numbers_per_thread
#     end = start + numbers_per_thread
#     if i == num_threads - 1:  # Ensure the last thread gets any remaining numbers
#         end = total_numbers
#     t = threading.Thread(target=print_numbers, args=(start, end))
#     threads.append(t)
#     t.start()

# # Join all threads
# for t in threads:
#     t.join()

# print("\nAll threads finished!")


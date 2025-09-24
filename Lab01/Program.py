# Lab:
# 	- write a program that prints hello world

# print("hello world")


# 	- application to take a number in binary form from the user, and print it as a decimal

# print("Enter a binary number: ")
# binary = input()
# flag = True
# for i in binary:
#     if i not in "01":
#         print("invaild input")
#         flag = False
#         break
# if flag:        
#     print(f"binary : {binary} -----> decimal : {int(binary,2)}")

	# - write a function that takes a number as an argument and if the number
	# 	divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
	# 	divisible by both return "FizzBuzz"

# def FizzBuzz(num):
#     fizz = ""
#     buzz = ""
#     if num % 3 == 0:
#         fizz = "Fizz"
#     if num % 5 == 0:
#         buzz = "Buzz"
#     return fizz + buzz

# print(FizzBuzz(6))
# print(FizzBuzz(10))
# print(FizzBuzz(15))
# 	- Ask the user to enter the radius of a circle print its calculated area and circumference

# import math
# def circleArea(radius):
#     return math.pi * radius**2
# def circleCircumference(radius):
#     return 2 * math.pi * radius

# radius = input("Enter the radius of the circle: ")

# if not radius.isdecimal:
#     print("Invaild Input")
#     exit()


# print(f"The circle's area = {circleArea(radius)}")
# print(f"The circle's circumference = {circleCircumference(radius)}")

# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers).
#     then proceed to ask him for his email and print all this data
# def EnterName():
#     name = input("Enter your name: ")
#     if not name:
#         print("Invaild name, try again")
#         return EnterName()
#     if not name.isalpha():
#         print("Invaild name, name shoudln't contain any number")
#         return EnterName()
#     return name
# def EnterEmail():
#     email = input("Enter your email: ")
#     indexOfAT = email.find("@")
#     if indexOfAT == -1 or indexOfAT == 0:
#         print("invaild email")
#         return EnterEmail()
#     indexOfDOT = email.rfind(".") #elshater.hassan@email.com
#     if indexOfDOT == -1 or indexOfAT > indexOfDOT:
#         print("Invaild Email")
#         return EnterEmail()
    
#     return email
    

# name = EnterName()
# email = EnterEmail()


# print(f"Name: {name}")
# print(f"Email: {email}")



# 	- Write a program that prints the number of times the substring 'iti' occurs in a string

# iti = input("Enter a string: ").count("iti")

# print(iti)
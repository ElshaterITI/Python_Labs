
#     Python Practice Tasks
#     =====================

#     Rules:
#         - Everything must be written inside functions.
#         - The file should run as a script.
#         - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
#         - The user chooses a number, and the program runs the corresponding function.
#         - Each task should only run when chosen from the menu.
#         - At ANY stage: if the user enters invalid input, the program must:
#               * Show an error message
#               * Display what valid input looks like
#               * Let the user try again (do not crash or exit)

# Tasks:
# ------

# 1 - Ask the user to enter 5 numbers.
#     Store them, then display them in ascending order and descending order.

import math


def displayFiveNumbersAscAndDesc():
    fiveNums = []
    i = 0
    while i < 5:
        num = input(f"Enter value number {i + 1}: ")
        if not num.isdigit():
            print("Invalid Input!, retry again")
            continue
        fiveNums.append(int(num))
        i += 1
    print("Numbers in ascending order: ")
    fiveNums.sort()
    print(fiveNums)
    print("__________")
    print("Numbers in descending order: ")
    fiveNums.sort(reverse=True)
    print(fiveNums)

# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.


def generateSequence():
    start = input("Enter the first value of the sequence: ")
    if not start.isdigit:
        print("Invaild Input, retry again")
        return generateSequence()
    start = int(start)
    length = input("Enter the length of the sequence: ")
    if not length.isdigit:
        print("Invaild Input, retry again")
        return generateSequence()
    length = int(length)
    print([i for i in range(start, start + length)])


# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.


def numberStats():
    nums = []
    inputCounter = 0
    while True:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        inputCounter += 1
        if not inp.isdigit():
            print("invaild input")
            continue
        nums.append(int(inp))

    if len(nums) == 0:
        print(f"The total of all numbers entered : {inputCounter}")
        print(f"The count of valid entries: {len(nums)}")
        print(f"The average: none ")
        return
    print(f"The total of all numbers entered : {inputCounter}")
    print(f"The count of valid entries: {len(nums)}")
    print(f"The average: {sum(nums) / len(nums)}")


# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.

def enterListOfNums():
    mySet = set()
    i = 0
    while i < 10:
        inp = input("Enter a value: ")
        if inp.isalpha():
            print("Invalid input, try again")
            continue
        mySet.add(int(inp))
        i += 1
    myList = list(mySet)
    myList.sort()
    print(myList)


# 6 - Ask the user to enter a sentence.
#     Count how many times each word appears in the sentence
#     and display the result.

def wordCounter():
    sentence = input("Enter your sentence: ")
    freq = {}
    for word in sentence.split(" "):
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    for key in freq:
        print(f"{key} : {freq[key]}")


# 7 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.

def gradeBook():
    i = 5
    maxStudent = ""
    maxGrade = -1
    minStudent = ""
    minGrade = float("inf")
    gradeSum = 0
    while i != 0:
        student_name = input("Student name: ")
        grade = input("Enter the student's grade: ")
        if not grade.isdigit():
            print("invalid input")
            continue
        grade = int(grade)
        if grade > maxGrade:
            maxGrade = grade
            maxStudent = student_name
        if grade < minGrade:
            minGrade = grade
            minStudent = student_name
        gradeSum += grade
        i -= 1
    avgGrade = gradeSum / 5
    print(f"Highest student: {maxStudent}")
    print(f"{maxStudent} grade: {maxGrade}")
    print(f"Lowest student: {minStudent}")
    print(f"{minStudent} grade: {minGrade}")
    print(f"Average grades: {avgGrade}")

# 8 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.


class ShoppingCart:

    def __init__(self):
        self.shopping_cart = {}

    def addItem(self,item_name, price):
        self.shopping_cart[item_name] = int(price)

    def removeItem(self,item_name):
        if item_name in self.shopping_cart:
            self.shopping_cart.pop(item_name)
    def viewTotalCost(self):
        cost = 0
        for key in self.shopping_cart:
            cost += self.shopping_cart[key]
        print(f"Total Cost: {cost}")
    def viewAllItems(self):
        for key in self.shopping_cart:
            print(f"item {key} costs {self.shopping_cart[key]}")

def SimulateShoppingCart():
    shoppingCart = ShoppingCart()
    def addItem():
        item_name = input("Enter the item's name: ")
        item_price = input("Enter the item's price: ")
        shoppingCart.addItem(item_name, item_price)
    def removeItem():
        item_name = input("Enter the item's name to be removed: ")
        shoppingCart.removeItem(item_name)

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View All Items")
        print("4. View Total Cost")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            addItem()
        elif choice == "2":
            removeItem()
        elif choice == "3":
            shoppingCart.viewAllItems()
        elif choice == "4":
            shoppingCart.viewTotalCost()
        elif choice == "5":
            print("Exiting simulation. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# 9 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts."""

import random

import random

def gussingGame():
    print("Hello player! 🎮 I will pick a number between 1 and 20. Your mission is to guess it! The fewer trials you need, the better your score (low score = good).")
    print("Are you ready? Let's start!")

    secret_number = random.randint(1, 20)
    trials = 0
    while True:
        trials += 1
        guess = int(input("Enter your guess: "))
        diff = abs(guess - secret_number)
        if diff > 15:
            print("I'm freezing 🪟🪟")
        elif diff > 10:
            print("Too cold 🥶")
        elif diff > 7:
            print("It's cold over here")
        elif diff > 5:
            print("It's warm over here")
        elif diff > 3:
            print("It's warmer 🔥")
        elif diff >= 1:
            print("It's too hot over here 🥵")
        elif diff == 0:
            print("NO WAY, you got it!! 🎉")
            break
    print(f"Your total score is {trials}, congrats!")


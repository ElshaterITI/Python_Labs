import random

def generate_random_nums():
    n = int(input("Enter how many random numbers you want: "))
    file = open("random_numbers.csv",'a')
    file.write("index,value\n")
    total = 0
    for i in range(n):
        element = (i + 1, random.randint(1, 1000))
        file.write(f"{element[0]}, {element[1]}\n")
        total += element[1]
    
    file.close()
    print(f"Total: {total}")
    print(f"Average: {total / n}")


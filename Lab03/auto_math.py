import math
import decorator_task
@decorator_task.log_time
def auto_math():
    file = open("math_report.txt", "a")
    numbers = input("Enter multiple numbers (comma-separated): ")
    for num in numbers.split(","):
        try:
            num = float(num)
            floor_num = math.floor(num)
            ceil_num = math.ceil(num)
            sqrt_num = math.sqrt(num)
            circle_area = math.pi * num**2
            file.write(f"{num} \n floor: {floor_num} \n ceil: {ceil_num} \n Square Root: {sqrt_num} \n Area of Circle: {circle_area}")
            file.write("\n\n")
        except ValueError:
            print(f"Invalid number")
            
            file.close()
            return
    file.close()

    
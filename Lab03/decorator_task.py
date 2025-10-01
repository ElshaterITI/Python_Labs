
import time

def log_time(func):
    def wrapper():
        beggining_time = time.time()
        func()
        ending_time = time.time()
        print(f"{func.__name__} function took {ending_time - beggining_time} seconds")
        file = open("execution_log.txt", "a")
        file.write(f"{func.__name__} function took {ending_time - beggining_time} seconds\n")
        file.close()
    return wrapper


from datetime import date
def date_reminder():
    file = open("reminders.txt", "a")
    input_date = input("Input a date YYYY-MM-DD: ")
    try:
        arr = input_date.split("-")
        year = arr[0]
        month = arr[1]
        day = arr[2]
    except Exception:
        print("Invaild input b")
        return
        
    if len(year) != 4 or int(month) not in range(12 + 1) or int(day) not in range(31 + 1):
        print("Invaild input a")
        return
    current_date = date.today()
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    my_date = date(year,month,day)
    if my_date < current_date:
        print("This date has already passed.")
        return
    
    file.write(f"{my_date} -> {my_date - current_date} left\n\n")
    print("The reminder has been added sucessfuly!")
    file.close()
    return

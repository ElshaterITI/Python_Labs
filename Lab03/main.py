
import auto_math
import email_validator
import reminder
import product_transformer
import os_file_manager
import random_number_generator

# ------------------------------------------------
# Rules:
#     1. Every user input must be validated.
#     2. Each task must be implemented in a separate .py file.
#     3. A main.py file must import all task modules.
#     4. When main.py runs:
#          - Display a menu showing all tasks with their number & name.
#          - Let the user select which task to execute by entering the task number.
#          - Run only the selected task.
#     5. Use if __name__ == "__main__": script only run in main.py.
#     6. Use functions and avoid code duplication.
#     7. Add comments explaining each step.
#     8. Automate as much as possible (e.g., file creation, processing).
#     9. No hardcoding results.
#     10. Decorators (Task 7) must be applied to at least two tasks.
# ------------------------------------------------

TASKS = {
    1: ("Math Automation", auto_math.auto_math),
    2: ("Regex Log Cleaner", email_validator.extract_emails),
    3: ("Datetime Reminder Script", reminder.date_reminder),
    4: ("Product Data Transformer", product_transformer.transform_product_data),
    5: ("OS File Manager", os_file_manager.manage_os),
    6: ("Random Data Generator", random_number_generator.generate_random_nums),
}

def print_menu():
    """Display all available tasks."""
    print("\nSelect a task to execute:")
    for num, (name, _) in TASKS.items():
        print(f"{num}) {name}")
    print("0) Exit")

def get_valid_choice(max_choice=6):
    """Get a valid numeric choice from the user."""
    while True:
        try:
            choice = int(input(f"Enter task number (0-{max_choice}): "))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 0 and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main menu loop for running selected tasks."""
    while True:
        print_menu()
        choice = get_valid_choice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice in TASKS:
            TASKS[choice][1]()  # Call the selected function
        else:
            print("Unknown task.")

if __name__ == "__main__":
    main()

from to_do import TaskManager
import time

def main_input():
    print()
    print("1. Add New Task")
    print("2. Mark Task as Completed")
    print("3. View All Tasks")
    print("4. Exit")

def valid_choice(input_choice):
    choices = ["1", "2", "3", "4"]

    # If invalid, prints a warning and prevents execution
    if input_choice not in choices:
        print("Please only choose valid Number between 1 to 4")
        return False 
    return True
    
def main():
    task = TaskManager()
    print("\n=== TO DO LIST ===")
    while True:

        main_input()
        choice = input("\nEnter your choice (1-4): ").strip()
        valid_choice(choice)
        
        if choice == "1":
            new_task = input("Enter your task details: ")
            if len(new_task) < 40:
                task.add_task(new_task)
                print(f"Task - '{new_task}' Successfully Added")
            else:
                print("Note : Consider keeping task details under 40 characters.\n")

        elif choice == "2":

            try:
                if task.show_pending_task():
                    complete_task = int(input("\nEnter the pending task ID number you want to mark as completed: "))
                    task.mark_completed(complete_task)

            except Exception as e:
                print(e)
                print("Note : Only Select Pending task's ID")

        elif choice == "3":
            task.view_task()
            input("Press Enter to go back to the main menu...") # This gives users control to continue
            
        elif choice == "4":
            print("Goodbye!!")
            break

        else:
            pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
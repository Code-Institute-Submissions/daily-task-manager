from datetime import datetime

class Task():
    """ Class to create instance of a task """
    def __init__(self, task_title, task_description, task_date):
        self.task_title = task_title
        self.task_description = task_description
        self.task_date = task_date
    
    def display_one_task(self):
        print("Title: ", self.task_title)
        print("Description: ", self.task_description)
        print("Due Date: ", self.task_date)
    
class TaskManager():
    """ Class to create instance of the task manager """ 
    def __init__(self):
        """ List to store the created task objects """
        self.tasks = []

    def create_task(self):
        """
        - Gets user input
        - Checks if task_date input is a valid date
        - Creates task and appends to list
        - Prints out message to user
        """
        task_title = str(input("Enter a task title: "))
        task_description = str(input("Describe the new task: "))
        task_date = str(input("When must the task be finished (YYYY-MM-DD): "))

        try:
            """ Converts string into datetime object and checks if it is valid """
            task_date = datetime.strptime(task_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Task creation failed.")

            return False
        
        task = Task(task_title, task_description, task_date)
        self.tasks.append(task)
        print("Task created succesfully.")
        
    def display_all_tasks(self):
        """
        - Checks if tasks list is empty, if so, prints out error message.
        - Loops through tasks list and calls display_one_task method for every task in list.

        """
        if not self.tasks:
            print("No tasks found.")
            return False
        
        print("Tasks:")
        for index in range(len(self.tasks)):
            print(f"{index + 1}.")
            self.tasks[index].display_one_task()

    def delete_task(self):
        """
        - Checks if tasks is empty, if so, prints error message.
        - Displays all tasks and ask user for the task that should be deleted.
        - Checks if the number is valid, if so, deletes given task in list.
        """
        if not self.tasks:
            print("No tasks found.")

            return False
        
        self.display_all_tasks()
        deletion_index = int(input("Enter the task number to delete: ")) - 1

        if deletion_index < 0 or deletion_index >= len(self.tasks):
            print("Invalid task number. Task deletion failed.")
        
        del self.tasks[deletion_index]
        print("Task deleted successfully.")
    
    def main(self):
        """ Main method to run the program """
        while True:
            print("Welcome to DAILY - your task manager.\n")
            print("What would you like to do?\n")
            print("1. Create a task")
            print("2. Display your tasks")
            print("3. Delete a task")
            print("4. Quit\n")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.display_all_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Please try again.")


task_manager = TaskManager()
task_manager.main()


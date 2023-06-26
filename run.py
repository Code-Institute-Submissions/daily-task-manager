from datetime import datetime

class Task():
    """ Class to create instance of a task """
    def __init__(self, task_title, task_description, task_date):
        self.task_title = task_title
        self.task_description = task_description
        self.task_date = task_date
    
class TaskManager():
    """ Class to create instance of the task manager """ 
    def __init__(self):
        """ List to store the created task objects """
        self.tasks = []

    def create_task():
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
            task_date = datetime.strptime(task_date, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Task creation failed.")
        
        task = Task(task_title, task_description, task_date)
        self.tasks.append(task)
        print("Task created succesfully.")
    
    def main():
        """ Main method to run the program """
        while True:
            print("Welcome to DAILY - your task manager.")

task_manager = TaskManager()


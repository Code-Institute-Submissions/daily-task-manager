from datetime import datetime

class Task():
    def __init__(self, task_title, task_description, task_date):
        self.task_title = task_title
        self.task_description = task_description
        self.task_date = task_date
    



class TaskManager():
    def __init__(self):
        self.tasks = []

    def create_task():
        task_title = str(input("Enter a task title: "))
        task_description = str(input("Describe the new task: "))
        task_date = str(input("When must the task be finished (YYYY-MM-DD): "))

        try:
            task_date = datetime.strptime(task_date, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Task creation failed.")
    
    def main():
        while True:
            print("Welcome to DAILY - your task manager.")

task_manager = TaskManager()


from datetime import datetime

class Task():
    def __init__(self, task_title, task_description, task_date):
        self.task_title = task_title
        self.task_description = task_description
        self.task_date = task_date


class TaskManager():
    def __init__(self):
        self.tasks = []
    
    def main():
        while True:
            print("Welcome to DAILY - your task manager.")

task_manager = TaskManager()
task_manager.main()


from datetime import datetime

APP_MENU = """
What would you like to do?

1. Create A New Task
2. Display Your Tasks
3. Delete A Task
4. Quit program

"""


class Task:
    """
    A class representing a task.

    Attributes:
        task_title (str): The title of the task.
        task_description (str): The description of the task.
        task_date (str): The due date of the task.
    """
    
    def __init__(self, task_title, task_description, task_date):
        self.task_title = task_title
        self.task_description = task_description
        self.task_date = task_date

    def display_task(self):
        """
        Displays the task information.

        Prints:
            Title: <task_title>
            Description: <task_description>
            Due Date: <task_date>
        """
        print("Title: ", self.task_title)
        print("Description: ", self.task_description)
        print("Due Date: ", self.task_date)


class TaskManager:
    """
    A class representing a task manager.

    Attributes:
        tasks (list): A list to store the tasks.
    """
    
    def __init__(self):
        """
        Initializes an instance of TaskManager.
        """

        self.tasks = []

    def create_task(self):
        """
        Creates a new task based on user input.
        """

        task_title = input("\nEnter a task title: ")
        task_description = input("\nDescribe the new task: ")
        task_date = input("\nWhen must the task be finished (YYYY-MM-DD): ")

        try:
            task_date = datetime.strptime(task_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Task creation failed.")

            return False

        task = Task(task_title, task_description, task_date)
        self.tasks.append(task)
        print("\nTask created succesfully.")

    def display_all_tasks(self):
        """
        Displays all tasks stored in the TaskManager.
        """
 
        if not self.tasks:
            print("\nNo tasks found.\n")
            return False

        print("\nTasks:")
        for index in range(len(self.tasks)):
            print(f"\n{index + 1}.")
            self.tasks[index].display_task()

    def delete_task(self):
        """
        Deletes a task from the TaskManager based on user input.
        """

        if not self.tasks:
            print("No tasks found.")

            return False

        self.display_all_tasks()
        deletion_index = int(input("\nEnter the task number to delete: ")) - 1

        if deletion_index < 0 or deletion_index >= len(self.tasks):
            print("Invalid task number. Task deletion failed.")

        del self.tasks[deletion_index]
        print("Task deleted successfully.")

    def main(self):
        """
        The main function of the TaskManager class.
        """
        
        print("\nWelcome to DAILY - your task manager.")
        while True:
            print(APP_MENU)

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


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.main()



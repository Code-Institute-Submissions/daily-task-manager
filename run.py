from datetime import datetime

WELCOME_MSG = """Welcome to DAILY - The Task Manager

DAILY will help you to stay organized and maximize your productivity.

Let's begin!"""

APP_MENU = """
What would you like to do?

1. Create A New Task
2. Display Your Tasks
3. Update A Task Status
4. Delete A Task
5. Quit Program

"""


class Task:
    """
    A class representing a task.

    Attributes:
        task_title (str): The title of the task.
        task_description (str): The description of the task.
        task_date (str): The due date of the task.
        task_status (str): The status of the task.
    """

    def __init__(self, task_title, task_description, task_date, task_status):
        self.task_title = task_title
        self.task_description = task_description
        self.task_date = task_date
        self.task_status = task_status

    def display_task(self, index):
        """
        Displays the task information.

        Prints:
            <index> Title: <task_title>
                    Description: <task_description>
                    Due Date: <task_date>
                    Status: <task_status>
        """
        print(
            f"""
        {index}. Title: {self.task_title}
           Description: {self.task_description}
           Due Date: {self.task_date}
           Status: {self.task_status}
        """
        )


class TaskManager:
    """
    A class representing a task manager implemented as a singleton.

    Attributes:
        tasks (list): A list to store the tasks.
    """

    # Private variable to store the only instance of TaskManager.
    __instance = None

    @staticmethod
    # Private method, means that the method belongs to the class.
    def get_instance():
        """
        Creates the only instance of TaskManager if it doesn't exist yet.
        """
        if TaskManager.__instance is None:
            TaskManager()
        return TaskManager.__instance

    def __init__(self):
        """
        Initializes an instance of TaskManager.
        """

        if TaskManager.__instance is not None:
            # Raises an exception if an instance of TaskManager already exist.
            raise Exception("This class is a singleton!")
        else:
            # Sets the instance variable to reference the current instance.
            TaskManager.__instance = self
            self.tasks = []

    def create_task(self):
        """
        Creates a new task based on user input.
        """

        task_title = input("\nEnter a task title: ")

        if task_title == "":
            print("I'm sorry! You need to give your task a title.")

            return

        task_description = input("\nDescribe the new task: ")
        task_date = input("\nWhen must the task be finished (DD-MM-YYYY): ")

        try:
            """
            Converts task_date (str) in to a datetime object
            and checks for correct format (DD-MM-YYYY).
            """
            task_date = datetime.strptime(task_date, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Task creation failed.")

            return

        task = Task(task_title, task_description, task_date, "Open")
        self.tasks.append(task)
        print("\nTask created succesfully.")

    def display_all_tasks(self):
        """
        Displays all tasks stored in the TaskManager.
        """

        if not self.tasks:
            print("\nSorry, you don't have any tasks yet.")

            return

        print("\nTasks:")
        # Gets element and index in list.
        for index, task in enumerate(self.tasks):
            task.display_task(index + 1)

    def delete_task(self):
        """
        Deletes a task from the TaskManager based on user input.
        """

        if not self.tasks:
            print("\nSorry, you don't have any tasks yet.")

            return

        self.display_all_tasks()

        try:
            deletion_index = int(input("\nEnter the task number to delete: ")) - 1
        except ValueError:
            print("Sorry, you didn't enter a number.")

            return

        if deletion_index < 0 or deletion_index >= len(self.tasks):
            print("I'm sorry, invalid task number. Task deletion failed.")

            return

        del self.tasks[deletion_index]
        print("\nTask deleted successfully.")

    def update_task_status(self):
        """
        Allows the user to update the task status of a task.
        """
        if not self.tasks:
            print("\nSorry, no tasks found. There is nothing to update.")

            return

        self.display_all_tasks()

        try:
            update_index = (
                int(
                    input(
                        "Enter the task number whose task status you want to change: "
                    )
                )
                - 1
            )
        except ValueError:
            print("Sorry, you didn't enter a number.")

            return

        if update_index < 0 or update_index >= len(self.tasks):
            print("\nI'm sorry, invalid task number. Task status update failed.")

            return

        task = self.tasks[update_index]
        print(
            "\nWould you like to change the status to Open, in Progress or Completed?"
        )
        new_status = input("\nPlease choose (O / P / C): ")

        if new_status == "O":
            task.task_status = "Open"
        elif new_status == "P":
            task.task_status = "In Progress"
        elif new_status == "C":
            task.task_status = "Completed"
        else:
            print("Invalid task status. Task status update failed.")

        print("\nTask status updated successfully.")

        self.display_all_tasks()

    def main(self):
        """
        The main function of the TaskManager class that runs the program.
        """

        print(WELCOME_MSG)
        while True:
            print(APP_MENU)

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.display_all_tasks()
            elif choice == "3":
                self.update_task_status()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                break
            else:
                print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    task_manager = TaskManager.get_instance()
    task_manager.main()
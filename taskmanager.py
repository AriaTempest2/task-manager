class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        task_name = input("Enter the task name: ")
        if task_name in self.tasks:
            print(f"Task '{task_name}' already exists.")
        else:
            self.tasks[task_name] = []
            print(f"Task '{task_name}' added successfully.")

    def add_step(self):
        task_name = input("Enter the task name to add a step to: ")
        if task_name in self.tasks:
            step_desc = input("Enter the step description: ")
            self.tasks[task_name].append({"description": step_desc, "completed": False})
            print(f"Step '{step_desc}' added to task '{task_name}'.")
        else:
            print(f"Task '{task_name}' not found.")

    def mark_step_completed(self):
        task_name = input("Enter the task name: ")
        if task_name in self.tasks:
            for i, step in enumerate(self.tasks[task_name], 1):
                status = "✓" if step["completed"] else "✗"
                print(f"{i}. [{status}] {step['description']}")
            step_num = int(input("Enter step number to mark as completed: ")) - 1
            if 0 <= step_num < len(self.tasks[task_name]):
                self.tasks[task_name][step_num]["completed"] = True
                print(f"Step '{self.tasks[task_name][step_num]['description']}' marked as completed.")
            else:
                print("Invalid step number.")
        else:
            print(f"Task '{task_name}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task, steps in self.tasks.items():
                print(f"Task: {task}")
                for step in steps:
                    status = "Done!" if step["completed"] else "X"
                    print(f"  - [{status}] {step['description']}")

    def remove_task(self):
        task_name = input("Enter the task name to remove: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed successfully.")
        else:
            print(f"Task '{task_name}' not found.")

    def total_tasks(self):
        print(f"Total number of tasks: {len(self.tasks)}")

    def menu(self):
        while True:
            print("\n--- Task Manager ---")
            print("1. Add a Task")
            print("2. Add a Step to a Task")
            print("3. Mark Step as Completed")
            print("4. View All Tasks")
            print("5. Remove a Task")
            print("6. Display Total Number of Tasks")
            print("7. Quit")

            choice = input("Choose an option (1-7): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.add_step()
            elif choice == "3":
                self.mark_step_completed()
            elif choice == "4":
                self.view_tasks()
            elif choice == "5":
                self.remove_task()
            elif choice == "6":
                self.total_tasks()
            elif choice == "7":
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid number.")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.menu()


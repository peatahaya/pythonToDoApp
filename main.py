import json
import os
from datetime import datetime

class TodoApp:
    """A console-based to-do list application."""
    
    def __init__(self, filename="tasks.json"):
        """Initialize the app with a JSON file for task storage."""
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid JSON file. Starting with an empty task list.")
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, name, priority="medium"):
        """Add a new task with a name and priority."""
        task = {
            "id": len(self.tasks) + 1,
            "name": name,
            "priority": priority.lower(),
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{name}' added with priority '{priority}'.")

    def remove_task(self, task_id):
        """Remove a task by its ID."""
        task = next((task for task in self.tasks if task["id"] == task_id), None)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task '{task['name']}' removed.")
        else:
            print(f"No task found with ID {task_id}.")

    def mark_done(self, task_id):
        """Mark a task as done by its ID."""
        task = next((task for task in self.tasks if task["id"] == task_id), None)
        if task:
            task["done"] = True
            self.save_tasks()
            print(f"Task '{task['name']}' marked as done.")
        else:
            print(f"No task found with ID {task_id}.")

    def filter_tasks(self, priority=None, done=None):
        """Filter tasks by priority and/or completion status."""
        filtered_tasks = self.tasks
        if priority:
            filtered_tasks = [task for task in filtered_tasks if task["priority"] == priority.lower()]
        if done is not None:
            filtered_tasks = [task for task in filtered_tasks if task["done"] == done]
        return filtered_tasks

    def display_tasks(self, tasks=None):
        """Display tasks in a formatted way."""
        if tasks is None:
            tasks = self.tasks
        if not tasks:
            print("No tasks to display.")
            return
        print("\nTasks:")
        print("-" * 50)
        for task in tasks:
            status = "Done" if task["done"] else "Not Done"
            print(f"ID: {task['id']} | Name: {task['name']} | Priority: {task['priority']} | "
                  f"Status: {status} | Created: {task['created_at']}")
        print("-" * 50)

def main():
    """Run the to-do list application."""
    app = TodoApp()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as done")
        print("4. Show all tasks")
        print("5. Filter tasks by priority")
        print("6. Filter tasks by status")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (low/medium/high, default: medium): ") or "medium"
            if priority.lower() not in ["low", "medium", "high"]:
                print("Invalid priority. Using default (medium).")
                priority = "medium"
            app.add_task(name, priority)
        
        elif choice == "2":
            app.display_tasks()
            try:
                task_id = int(input("Enter task ID to remove: "))
                app.remove_task(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        
        elif choice == "3":
            app.display_tasks()
            try:
                task_id = int(input("Enter task ID to mark as done: "))
                app.mark_done(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        
        elif choice == "4":
            app.display_tasks()
        
        elif choice == "5":
            priority = input("Enter priority to filter (low/medium/high): ")
            if priority.lower() in ["low", "medium", "high"]:
                filtered = app.filter_tasks(priority=priority)
                app.display_tasks(filtered)
            else:
                print("Invalid priority.")
        
        elif choice == "6":
            status = input("Show done tasks? (yes/no): ").lower()
            done = True if status == "yes" else False if status == "no" else None
            if done is not None:
                filtered = app.filter_tasks(done=done)
                app.display_tasks(filtered)
            else:
                print("Invalid input. Use 'yes' or 'no'.")
        
        elif choice == "7":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
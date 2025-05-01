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

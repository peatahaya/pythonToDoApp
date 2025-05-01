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
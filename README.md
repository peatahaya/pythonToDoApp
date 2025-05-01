To-Do List Manager

Overview

To-Do List Manager is a console-based Python application for managing tasks. It allows users to add, remove, mark as done, and filter tasks by priority or completion status. Tasks are stored persistently in a JSON file, demonstrating practical use of Python's data structures, file I/O, and user interaction.

This project showcases my Python programming skills, including:





Working with lists and dictionaries.



Object-oriented programming (OOP).



File handling with JSON.



Error handling and user input validation.



List comprehensions for filtering data.

Features





Add Task: Create a new task with a name and priority (low, medium, high).



Remove Task: Delete a task by its ID.



Mark as Done: Update a task's completion status.



Display Tasks: View all tasks with details (ID, name, priority, status, creation date).



Filter Tasks: Filter tasks by priority or completion status (done/not done).



Persistent Storage: Tasks are saved to and loaded from tasks.json.

Prerequisites





Python 3.x installed.



No external dependencies required (uses standard library modules: json, os, datetime).

Installation





Clone the repository:

git clone https://github.com/peatahaya/pythonToDoApp.git



Navigate to the project directory:

cd todo-list-manager



Ensure tasks.json (included) is in the same directory as todo_app.py for loading sample tasks.

Usage





Run the application:

python todo_app.py



Follow the console menu to interact with the application:





Select options 1-7 to add, remove, mark, display, or filter tasks.



Enter task details (e.g., name, priority) when prompted.



Choose option 7 to exit.



Tasks are automatically saved to tasks.json after each operation.

Sample Data

The repository includes a tasks.json file with example tasks:

[
    {
        "id": 1,
        "name": "Learn Python",
        "priority": "high",
        "done": false,
        "created_at": "2025-05-01 10:00:00"
    },
    ...
]

You can modify or replace tasks.json with your own data, ensuring the same structure (fields: id, name, priority, done, created_at).

Project Structure





todo_app.py: Main application script containing the TodoApp class and console interface.



tasks.json: Sample JSON file for storing tasks.



README.md: Project documentation.

Example Output

To-Do List Manager
1. Add task
2. Remove task
3. Mark task as done
4. Show all tasks
5. Filter tasks by priority
6. Filter tasks by status
7. Exit
Enter your choice (1-7): 4

Tasks:
--------------------------------------------------
ID: 1 | Name: Learn Python | Priority: high | Status: Not Done | Created: 2025-05-01 10:00:00
ID: 2 | Name: Write README | Priority: medium | Status: Done | Created: 2025-05-01 12:30:00
--------------------------------------------------

Future Improvements





Add unit tests using pytest to ensure code reliability.



Implement task categories or due dates.



Create a web-based version using Flask for broader accessibility.



Add sorting options (e.g., by priority or creation date).

Contact

For feedback or questions: 





GitHub: peatahaya



Email: piotrbi3licki@icloud.com

License

This project is licensed under the MIT License - see the LICENSE file for details.

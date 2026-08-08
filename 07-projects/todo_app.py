"""
PROJECT 2: To-Do List App (File Handling + OOP)
Stores tasks in todo.json
"""

import json
import os

FILE = "todo.json"

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load()

    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.tasks = json.load(f)
    
    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save()
        print(f"Added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks!")
            return
        for i, t in enumerate(self.tasks, 1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {status} {t['task']}")

    def mark_done(self, index):
        try:
            self.tasks[index-1]["done"] = True
            self.save()
            print("Marked as done!")
        except IndexError:
            print("Invalid task number!")

    def delete(self, index):
        try:
            removed = self.tasks.pop(index-1)
            self.save()
            print(f"Deleted: {removed['task']}")
        except IndexError:
            print("Invalid task number!")

def main():
    app = TodoApp()
    while True:
        print("\n--- TO-DO APP ---")
        print("1. List\n2. Add\n3. Mark Done\n4. Delete\n5. Exit")
        choice = input("Choice: ")
        
        if choice == "1":
            app.list_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            app.add(task)
        elif choice == "3":
            app.list_tasks()
            try:
                n = int(input("Task number to mark done: "))
                app.mark_done(n)
            except ValueError:
                print("Enter number!")
        elif choice == "4":
            app.list_tasks()
            try:
                n = int(input("Task number to delete: "))
                app.delete(n)
            except ValueError:
                print("Enter number!")
        elif choice == "5":
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()

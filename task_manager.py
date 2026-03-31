import json

class Task :

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Checked" if self.completed else " "
        return f"[{status}] #{self.id} : {self.description}" 
    


class TaskManager :

    FILENAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {task}")
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else: 
            for task in self.tasks:
                print(task)

    def complete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                task.completed = True
                print(f"Task completed: {task}")
                self.save_tasks()
                return
        print(f"Task with ID {id} not found.")

    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print(f"Task deleted: {task}")
                self.save_tasks()
                return
        print(f"Task with ID {id} not found.")

    def load_tasks(self):
        try: 
            with open(self.FILENAME, "r") as file: 
                data = json.load(file)
                self.tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self.tasks:
                    self.next_id = self.tasks[-1].id + 1
                else: 
                    self.next_id = 1
        except FileNotFoundError:   
            self.tasks = []


    def save_tasks(self):
        with open (self.FILENAME, "w") as file:
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self.tasks], file, indent=4)

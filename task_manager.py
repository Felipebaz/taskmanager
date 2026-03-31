class Task :

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Checked" if self.completed else " "
        return f"[{status}] #{self.id} : {self.description}" 
    


class TaskManager :
    
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {task}")

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
                return
        print(f"Task with ID {id} not found.")

    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print(f"Task deleted: {task}")
                return
        print(f"Task with ID {id} not found.")

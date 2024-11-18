from task import Task

class Project:
    """class for managing projects"""
    def __init__(self,name):
        self.name=name
        self.tasks={}
    def add_task(self,task):
        """add a task to the projects"""
        if task.id in self.tasks:
            raise ValueError('Task ID must be unique within the project.')
        self.tasks[task.id]=task
    def edit_task(self,task_id,**kwargs):
        """Edit an exising task's details"""
        if task_id in self.tasks:
            task=self.tasks[task_id]
            for k,v in kwargs.items():
                setattr(task,k,v)
        else:
            raise ValueError('Task not found')
    def remove_task(self,task_id):
        """Remove a task from project"""
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError("task not found")
    def get_task(self,task_id):
        """Get task details by ID"""
        return self.tasks.get(task_id,None)
    def display_task(self):
        """display all tasks in the project"""
        for task in self.tasks.values():
            print(task)
    def __str__(self):
        return f"Project:{self.name},Tasks:{len(self.tasks)}"
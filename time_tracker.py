from project import Project

class TimeTracker:
    """class for managing the entire system"""
    def __init__(self):
        self.projects={}

    def add_project(self,project_name):
        """add a new project"""
        if project_name in self.projects:
            raise ValueError('project name must be unique')
        self.projects[project_name]=Project(project_name)
    def edit_project(self,old_name,new_name):
        """edit project name"""
        if old_name in self.projects:
            self.projects[new_name]=self.projects.pop(old_name)
            self.projects[new_name].name=new_name
        else:
            raise ValueError("project not found")
        
    def remove_project(self,project_name):
        """Remove a project and all its tasks"""
        if project_name in self.projects:
            del self.projects[project_name]
        else:
            raise ValueError ('project not found')
    def display_projects(self):
        """Display all projects"""
        for project_name, Project in self.projects.items():
            print(Project)
    def search_project(self,project_name):
        """serach for a project by its name"""
        return self.projects.get(project_name,None)
    def search_task(self,project_name,task_name):
        """search for a task by its name within a specific project"""
        if project_name in self.projects:
            
            project=self.projects[project_name]
            for task in project.tasks.values():
                if task.name == task_name:
                    return task
        return None
    def __str__(self):
        return f"Time tracker system with {len(self.projects)} projects."
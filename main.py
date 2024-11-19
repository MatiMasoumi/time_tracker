from task import Task
from project import Project
from time_tracker import TimeTracker

def main():
     tracker = TimeTracker()
     while True:
         print("\n===== Time Tracker Menu =====")
         print("1. Add Project")
         print("2. Remove Project")
         print("3. Display All Projects")
         print("4. Add Task to a Project")
         print("5. Remove Task from a Project")
         print("6. Mark Task as Done")
         print("7. Display Tasks in a Project")
         print("8. Search Project")
         print("9. Search Task in a Project")
         print("10. Exit")
         choice = input("Enter your choice: ")
         if choice == "1":
            project_name = input("Enter the project name: ")
            try:
                tracker.add_project(project_name)
                print(f"Project '{project_name}' added successfully!")
            except ValueError as e:
                print(e)
         elif choice == "2":
            project_name = input("Enter the project name to remove: ")
            try:
                tracker.remove_project(project_name)
                print(f"Project '{project_name}' removed successfully!")
            except ValueError as e:
                 print(e)
         elif choice == "3":
             print("\nProjects List:")
             tracker.display_projects()
         elif choice == "4":
             project_name = input("Enter the project name: ")
             if project_name in tracker.projects:
                 task_id = input("Enter task ID: ")
                 task_name = input("Enter task name: ")
                 description = input("Enter task description (optional): ")
                 try:
                     tracker.projects[project_name].add_task(Task(task_id, task_name, description))
                     print(f"Task '{task_name}' added to project '{project_name}'.")
                 except ValueError as e:
                     print(e)
             else:
                 print("Project not found.")
         elif choice == "5":
             project_name = input("Enter the project name: ")
             if project_name in tracker.projects:
                 task_id = input("Enter the task ID to remove: ")
                 try:
                     tracker.projects[project_name].remove_task(task_id)
                     print(f"Task '{task_id}' removed from project '{project_name}'.")
                 except ValueError as e:
                     print(e)
             else: print("Project not found.")
         elif choice == "6":
             project_name = input("Enter the project name: ")
             if project_name in tracker.projects:
                 task_id = input("Enter the task ID to mark as done: ")
                 if task_id in tracker.projects[project_name].tasks:
                     tracker.projects[project_name].tasks[task_id].mark_done()
                     print(f"Task '{task_id}' marked as done.")
                 else:
                    print("Task not found.")
             else:
                 print("Project not found.")
         elif choice == "7":
             project_name = input("Enter the project name: ")
             if project_name in tracker.projects:
                 print(f"\nTasks in Project '{project_name}':")
                 tracker.projects[project_name].display_tasks()
             else:
                 print("Project not found.")
         elif choice == "8":
             project_name = input("Enter the project name to search: ")
             project = tracker.search_project(project_name)
             if project:
                 print(f"\nProject '{project_name}' details:")
                 print(project)
                 print("Tasks:") 
                 project.display_tasks()
             else:
                 print("Project not found.")
         elif choice == "9":
             project_name = input("Enter the project name: ")
             if project_name in tracker.projects:
                 task_name = input("Enter the task name to search: ")
                 task = tracker.search_task(project_name, task_name)
                 if task:
                     print(f"\nTask '{task_name}' details:")
                     print(task)
                 else:
                    print("Task not found.")
             else:
                 print("Project not found.")
         elif choice == "10":
             print("Exiting the Time Tracker. Goodbye!")
             break
         else:
             print("Invalid choice. Please try again.")
if __name__ == "__main__":
     main()
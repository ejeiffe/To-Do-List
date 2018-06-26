import os.path

from create_new_db import *
from db_controller import *

def main_menu():
    print('\n')
    print("Main Menu: ")
    print('\n')
    print("1. View Tasks")
    print("2. View Projects")
    print("0. Exit")
    print('\n')

def view_tasks_menu():
    print('\n')
    print("View Tasks: ")
    print('\n')
    print("1. Active Tasks")
    print("2. Completed Tasks")
    print("3. All Tasks")
    print("0. Return to Main Menu")
    print('\n')

def tasks_menu():
    print('\n')
    print("1. Add Task")
    print("2. Edit Task Description")
    print("3. Edit Task Deadline")
    print("4. Assign Task to Project")
    print("5. Delete Task")
    print("6. Mark Task as Complete")
    print("7. Return to View Tasks Menu")
    print("0. Return to Main Menu")
    print('\n')

def view_projects_menu():
    print('\n')
    print("View Projects: ")
    print('\n')
    print("1. Active Projects")
    print("2. Completed Projects")
    print("3. All Projects")
    print("0. Return to Main Menu")
    print('\n')

def projects_menu():
    print('\n')
    print("1. Add Project")
    print("2. Edit Project Description")
    print("3. Edit Project Deadline")
    print("4. Delete Project")
    print("5. Mark Project as Complete")
    print("6. View Project Tasks")
    print("7. Return to View Project Menu")
    print("0. Return to Main Menu")
    print('\n')

def project_tasks_menu():
    print('\n')
    print("1. Add Task")
    print("2. Edit Task Description")
    print("3. Edit Task Deadline")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Return to Projects Menu")
    print("0. Return to Main Menu")
    print('\n')

def menu_select(len_menu):
    valid = False
    while not valid:
        try:
            selection = int(input("Select an option: "))
            if selection in range(len_menu):
                valid = True
            else:
                print(f"Enter a number between 0 and {str(len_menu-1)}")
        except:
            print(f"Enter a number between 0 and {str(len_menu-1)}")
    return selection

def display_list_headings(headings):
    print('{0:<{width}}'.format(headings[0], width=15), end=' ')
    print('{0:<{width}}'.format(headings[1], width=50), end=' ')
    for heading in headings[2:]:
        print('{0:<{width}}'.format(heading, width=17), end=' ')
    print('\n')

def display_list(list_items):
    for row in list_items:
        print('{0:<{width}}'.format(row[0], width=15), end=' ')
        print('{0:<{width}}'.format(row[1], width=50), end=' ')
        for item in row[2:]:
            if not item:
                item = ""
            print('{0:<{width}}'.format(str(item)[:16], width=17), end=' ')
        print('\n')

def display_task_list(tasks):
    if tasks:
        display_list_headings(["TaskID", "Decription", "Deadline", "Created", "Completed", "ProjectID"])
        display_list(tasks)
    else:
        print("No tasks found.")

def display_project_list(projects):
    if projects:
        display_list_headings(["ProjectID", "Decription", "Deadline", "Created", "Completed"])
        display_list(projects)
    else:
        print("No projects found.")

def add_task_inputs():
    description = input("Enter task description: ")
    deadline_select = input("Add a deadline? y/n: ").lower()
    if deadline_select.startswith('y'):
        deadline = input("Enter a deadline (YYYY-MM-DD): ")
    else:
        print("No deadline set.")
        deadline = None
    project_select = input("Add task to project? y/n: ")
    if project_select.startswith('y'):
        project_id = input("Enter Project ID: ")
    else:
        print("Task not assigned to project.")
        project_id = None
    return description, deadline, project_id

def edit_task_description_inputs():
    task_id = input("Enter Task ID: ")
    description = input("Enter new description: ")
    return task_id, description

def set_task_deadline_inputs():
    task_id = input("Enter Task ID: ")
    deadline = input("Enter new deadline (YYYY-MM-DD): ")
    return task_id, deadline

def assign_task_to_project_inputs():
    task_id = input("Enter Task ID: ")
    project_id = input("Enter Project ID: ")
    return task_id, project_id

def check_project_completed(task_id):
    controller = DbController("to_do.db")
    project_id = controller.get_task_project_id(task_id)
    if project_id:
        if controller.check_project_completed(project_id):
            print(f"All tasks for project {project_id} completed.")
            project_complete = input("Mark project complete? y/n: ").lower()
            if project_complete.startswith('y'):
                controller.mark_project_completed(project_id)

def add_project_inputs():
    description = input("Enter project description: ")
    deadline_select = input("Add a deadline? y/n: ").lower()
    if deadline_select.startswith('y'):
        deadline = input("Enter a deadline (YYYY-MM-DD): ")
    else:
        print("No deadline set.")
        deadline = None
    return description, deadline

def edit_project_description_inputs():
    project_id = input("Enter Project ID: ")
    description = input("Enter new description: ")
    return project_id, description

def set_project_deadline_inputs():
    project_id = input("Enter Task ID: ")
    deadline = input("Enter new deadline (YYYY-MM-DD): ")
    return project_id, deadline

def add_project_task_inputs(project_id):
    description = input("Enter task description: ")
    deadline_select = input("Add a deadline? y/n: ").lower()
    if deadline_select.startswith('y'):
        deadline = input("Enter a deadline (YYYY-MM-DD): ")
    else:
        print("No deadline set.")
        deadline = None
    return description, deadline, project_id

if __name__ == "__main__":
    #creates new database if not found in folder
    if not os.path.exists("to_do.db"):
        create_new_db("to_do.db")
        print("New database created")
    controller = DbController("to_do.db")
    db_open = True
    while db_open:
        main_menu()
        main_select = menu_select(3)
        if main_select == 1:
            view_tasks = True
            while view_tasks:
                view_tasks_menu()
                view_tasks_select = menu_select(4)
                if view_tasks_select == 0:
                    view_tasks = False
                else:
                    if view_tasks_select == 1:
                        active_tasks = controller.show_active_tasks()
                        print("Active Tasks: \n")
                        display_task_list(active_tasks)
                    elif view_tasks_select == 2:
                        completed_tasks = controller.show_completed_tasks()
                        print("Completed Tasks: \n")
                        display_task_list(completed_tasks)
                    else:
                        all_tasks = controller.show_all_tasks()
                        print("All Tasks: \n")
                        display_task_list(all_tasks)
                    tasks = True
                    while tasks:
                        tasks_menu()
                        tasks_select = menu_select(8)
                        if tasks_select == 1:
                            task_inputs = add_task_inputs()
                            controller.add_task(*task_inputs)
                        elif tasks_select == 2:
                            task_inputs = edit_task_description_inputs()
                            controller.edit_task_description(*task_inputs)
                        elif tasks_select == 3:
                            task_inputs = set_task_deadline_inputs()
                            controller.set_task_deadline(*task_inputs)
                        elif tasks_select == 4:
                            task_inputs = assign_task_to_project_inputs()
                            controller.assign_task_to_project(*task_inputs)
                        elif tasks_select == 5:
                            task_id = input("Enter Task ID to delete: ")
                            controller.delete_task(task_id)
                            print("Task deleted.")
                        elif tasks_select == 6:
                            task_id = input("Enter Task ID to mark as complete: ")
                            controller.mark_task_completed(task_id)
                            check_project_completed(task_id)
                        else: 
                            tasks = False
                            if tasks_select == 0:
                                view_tasks = False
        elif main_select == 2:
            view_projects = True
            while view_projects:
                view_projects_menu()
                view_projects_select = menu_select(4)
                if view_projects_select == 0:
                    view_projects = False
                else:
                    if view_projects_select == 1:
                        active_projects = controller.show_active_projects()
                        print("Active Projects: \n")
                        display_project_list(active_projects)
                    elif view_projects_select == 2:
                        completed_projects = controller.show_completed_projects()
                        print("Completed Projects: \n")
                        display_project_list(completed_projects)
                    else:
                        all_projects = controller.show_all_projects()
                        print("All Projects: \n")
                        display_project_list(all_projects)
                    projects = True
                    while projects:
                        projects_menu()
                        projects_select = menu_select(8)
                        if projects_select == 1:
                            project_inputs = add_project_inputs()
                            controller.add_project(*project_inputs)
                        elif projects_select == 2:
                            project_inputs = edit_project_description_inputs()
                            controller.edit_project_description(*project_inputs)
                        elif projects_select == 3:
                            project_inputs = set_project_deadline_inputs()
                            controller.set_project_deadline(*project_inputs)
                        elif projects_select == 4:
                            project_id = input("Enter Project ID to delete: ")
                            delete_project_option = input("Delete all associated tasks? y/n: ")
                            if delete_project_option.startswith('y'):
                                controller.delete_project_and_tasks(project_id)
                            else:
                                controller.delete_project_only(project_id)
                            print("Project deleted.")
                        elif projects_select == 5:
                            project_id = input("Enter Project ID to mark as complete: ")
                            controller.mark_project_completed(project_id)
                            mark_tasks = input("Mark all project tasks as complete? y/n: ").lower()
                            if mark_tasks.startswith('y'):
                                controller.mark_project_tasks_completed(project_id)
                        elif projects_select == 6:
                            project_id = input("Enter Project ID to view: ")
                            project = controller.show_single_project(project_id)
                            display_project_list(project)
                            project_task_list = controller.show_project_tasks(project_id)
                            display_task_list(project_task_list)
                            project_tasks = True
                            while project_tasks:
                                project_tasks_menu()
                                project_tasks_select = menu_select(7)
                                if project_tasks_select == 1:
                                    task_inputs = add_project_task_inputs(project_id)
                                    controller.add_task(*task_inputs)
                                elif project_tasks_select == 2:
                                    task_inputs = edit_task_description_inputs()
                                    controller.edit_task_description(*task_inputs)
                                elif project_tasks_select == 3:
                                    task_inputs = set_task_deadline_inputs()
                                    controller.set_task_deadline(*task_inputs)
                                elif project_tasks_select == 4:
                                    task_id = input("Enter Task ID to delete: ")
                                    controller.delete_task(task_id)
                                    print("Task deleted.")
                                elif project_tasks_select == 5:
                                    task_id = input("Enter Task ID to mark as complete: ")
                                    controller.mark_task_completed(task_id)
                                    check_project_completed(task_id)
                                else:
                                    project_tasks = False
                                    if project_tasks_select == 0:
                                        projects = False
                                        view_projects = False
                        else:
                            projects = False
                            if projects_select == 0:
                                view_projects = False
        else:
            db_open = False

                            


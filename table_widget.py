from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from datetime import datetime

from db_controller import *


class TableWidget(QTableWidget):

    def __init__(self):
        super().__init__()
        self.controller = DbController("to_do.db")

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(False)

    def show_items(self, item_list):
        if len(item_list) == 0:
            self.setRowCount(0)
        else:
            row = 0
            for entry in item_list:
                self.setRowCount(row+1)
                column = 0
                for item in entry:
                    if item == None:
                        item = ""
                    elif column == 3 or column == 4:
                        item = str(item[:-7])
                    table_item = QTableWidgetItem(str(item))
                    if column == 2 and item != "":
                        if self.check_overdue(item):
                            table_item.setForeground(QColor(255,0,0))
                    self.setItem(row, column, table_item)
                    column += 1
                row += 1
        
    def check_completed(self):
        return self.item(self.currentRow(), 4).text() != ""

    def get_id(self):
        return int(self.item(self.currentRow(), 0).text())

    def check_overdue(self, deadline):
        deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
        if deadline_date <= datetime.today():
            return True
        return False
        
class TasksTable(TableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(["TaskID", "Decription", "Deadline", "Created", "Completed", "ProjectID"])

    def get_tasks(self, task_type):
        if task_type == 0:
            tasks = self.controller.get_active_tasks()
        elif task_type == 1:
            tasks = self.controller.get_completed_tasks()
        else:
            tasks = self.controller.get_all_tasks()
        return tasks

    def get_task_project_id(self):
        return int(self.item(self.currentRow(), 5).text())

class ProjectTasksTable(TasksTable):

    def __init__(self, project_id):
        super().__init__()
        self.project_id = project_id

    def get_project_tasks(self):
        return self.controller.get_project_tasks(self.project_id)


class ProjectsTable(TableWidget):

    def __init__(self):
        super().__init__()
        
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["ProjectID", "Decription", "Deadline", "Created", "Completed"])

    def get_projects(self, project_type):
        if project_type == 0:
            projects = self.controller.get_active_projects()
        elif project_type == 1:
            projects = self.controller.get_completed_projects()
        else:
            projects = self.controller.get_all_projects()
        return projects
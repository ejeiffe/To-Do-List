from PyQt5.QtWidgets import *

from db_controller import *

class TableWidget(QTableWidget):

    def __init__(self):
        super().__init__()
        self.controller = DbController("to_do.db")

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        
class TasksTable(TableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(["TaskID", "Decription", "Deadline", "Created", "Completed", "ProjectID"])

    def show_active_tasks(self):
        pass

    def show_completed_tasks(self):
        pass

    def show_all_tasks(self):
        pass


class ProjectsTable(TableWidget):

    def __init__(self):
        super().__init__()
        
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["ProjectID", "Decription", "Deadline", "Created", "Completed"])

    def show_active_projects(self):
        pass

    def show_completed_projects(self):
        pass

    def show_all_projects(self):
        pass
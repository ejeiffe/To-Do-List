from PyQt5.QtWidgets import *

from db_controller import *
from table_widget import *
from add_new_dialog import *
from mark_complete_dialog import *
from edit_dialog import *
from delete_dialog import *

class ProjectTasksDialog(QDialog):

    def __init__(self, project_id):
        super().__init__()
        self.project_id = project_id
        self.controller = DbController("to_do.db")

        self.setWindowTitle("Project Tasks")
        
        self.project_label = QLabel("<b>Project:</b>")
        self.tasks_label = QLabel("<b>Tasks:</b>")

        self.project_labels_list = ["ProjectID", "Decription", "Deadline", "Created", "Completed"]
        self.project_details = self.get_project_details()

        self.project_details_layout = QGridLayout()
        col = 0
        for label in self.project_labels_list:
            self.project_details_layout.addWidget(QLabel(label), 0, col)
            col += 1
        col = 0
        for item in self.project_details:
            self.project_details_layout.addWidget(QLabel(item), 1, col)
            col += 1

        self.project_tasks_table = ProjectTasksTable(self.project_id)
        self.populate_project_tasks_table()

        self.add_task_button = QPushButton("Add Task")
        self.mark_task_complete_button = QPushButton("Mark Complete")
        self.mark_task_complete_button.setEnabled(False)
        self.edit_task_button = QPushButton("Edit Task")
        self.edit_task_button.setEnabled(False)
        self.delete_task_button = QPushButton("Delete Task")
        self.delete_task_button.setEnabled(False)
        self.close_window_button = QPushButton("Close")

        self.project_tasks_button_layout = QHBoxLayout()
        self.project_tasks_button_layout.addWidget(self.add_task_button)
        self.project_tasks_button_layout.addWidget(self.mark_task_complete_button)
        self.project_tasks_button_layout.addWidget(self.edit_task_button)
        self.project_tasks_button_layout.addWidget(self.delete_task_button)
        self.project_tasks_button_layout.addWidget(self.close_window_button)

        self.project_tasks_layout = QVBoxLayout()
        self.project_tasks_layout.addWidget(self.project_label)
        self.project_tasks_layout.addLayout(self.project_details_layout)
        self.project_tasks_layout.addWidget(self.tasks_label)
        self.project_tasks_layout.addWidget(self.project_tasks_table)
        self.project_tasks_layout.addLayout(self.project_tasks_button_layout)

        self.setLayout(self.project_tasks_layout)

        self.project_tasks_table.clicked.connect(self.enable_buttons)

        self.add_task_button.clicked.connect(self.open_new_project_task_dialog)
        self.mark_task_complete_button.clicked.connect(self.mark_task_completed)
        self.edit_task_button.clicked.connect(self.open_edit_task_dialog)
        self.delete_task_button.clicked.connect(self.open_delete_task_dialog)
        self.close_window_button.clicked.connect(self.close)

    def get_project_details(self):
        project_details = []
        controller_results = self.controller.get_single_project(self.project_id)
        for item in controller_results[0][:3]:
            if item == None:
                item = ""
            project_details.append(str(item))
        for item in controller_results[0][3:]:
            if item == None:
                item = ""
                project_details.append(item)
            else:
                project_details.append(str(item[:-7]))
        return project_details

    def populate_project_tasks_table(self):
        table_items = self.project_tasks_table.get_project_tasks()
        self.project_tasks_table.show_items(table_items)

    def enable_buttons(self):
        if not self.project_tasks_table.check_completed():
            self.mark_task_complete_button.setEnabled(True)
        else:
            self.mark_task_complete_button.setEnabled(False)
        self.edit_task_button.setEnabled(True)
        self.delete_task_button.setEnabled(True)

    def open_new_project_task_dialog(self):
        new_project_task_dialog = NewProjectTaskDialog(self.project_id)
        new_project_task_dialog.exec_()
        self.populate_project_tasks_table()

    def mark_task_completed(self):
        task_id = self.project_tasks_table.get_id()
        self.controller.mark_task_completed(task_id)
        if self.check_project_tasks_completed():
            mark_project_complete_dialog = MarkProjectCompleteDialog(self.project_id)
            mark_project_complete_dialog.exec_()
        self.populate_project_tasks_table()

    def check_project_tasks_completed(self):
        if self.controller.check_project_tasks_completed(self.project_id):
            return True
        else:
            return False

    def open_edit_task_dialog(self):
        task_id = self.project_tasks_table.get_id()
        edit_task_dialog = EditTaskDialog(task_id)
        edit_task_dialog.exec_()
        self.populate_project_tasks_table()

    def open_delete_task_dialog(self):
        task_id = self.project_tasks_table.get_id()
        delete_task_dialog = DeleteTaskDialog(task_id)
        delete_task_dialog.exec_()
        self.populate_project_tasks_table()
from PyQt5.QtWidgets import *

from db_controller import *

class DeleteTaskDialog(QDialog):

    def __init__(self, task_id):
        super().__init__()
        self.task_id = task_id
        self.controller = DbController("to_do.db")

        self.setWindowTitle("Delete Task")

        self.delete_task_message_label = QLabel("Are you sure you want to delete the selected task?")

        self.yes_button = QPushButton("Yes")
        self.no_button = QPushButton("No")

        self.delete_task_button_layout = QHBoxLayout()
        self.delete_task_button_layout.addWidget(self.yes_button)
        self.delete_task_button_layout.addWidget(self.no_button)

        self.delete_task_layout = QVBoxLayout()
        self.delete_task_layout.addWidget(self.delete_task_message_label)
        self.delete_task_layout.addLayout(self.delete_task_button_layout)

        self.setLayout(self.delete_task_layout)

        self.yes_button.clicked.connect(self.delete_task)
        self.no_button.clicked.connect(self.close)

    def delete_task(self):
        self.controller.delete_task(self.task_id)
        delete_task_confirmation = QMessageBox()
        delete_task_confirmation.setWindowTitle(" ")
        delete_task_confirmation.setInformativeText("Task deleted")
        delete_task_confirmation.exec_()
        self.close()

class DeleteProjectDialog(QDialog):

    def __init__(self, project_id):
        super().__init__()
        self.project_id = project_id
        self.controller = DbController("to_do.db")

        self.setWindowTitle("Delete Project")

        self.delete_project_message_label = QLabel("Delete this project and all associated tasks?")

        self.delete_project_tasks_button = QPushButton("Delete project and tasks")
        self.delete_project_only_button = QPushButton("Delete project only")
        self.delete_project_cancel_button = QPushButton("Cancel")

        self.delete_project_button_layout = QHBoxLayout()
        self.delete_project_button_layout.addWidget(self.delete_project_tasks_button)
        self.delete_project_button_layout.addWidget(self.delete_project_only_button)
        self.delete_project_button_layout.addWidget(self.delete_project_cancel_button)

        self.delete_project_layout = QVBoxLayout()
        self.delete_project_layout.addWidget(self.delete_project_message_label)
        self.delete_project_layout.addLayout(self.delete_project_button_layout)

        self.setLayout(self.delete_project_layout)

        self.delete_project_tasks_button.clicked.connect(self.delete_project_and_tasks)
        self.delete_project_only_button.clicked.connect(self.delete_project_only)
        self.delete_project_cancel_button.clicked.connect(self.close)

    def delete_project_and_tasks(self):
        self.controller.delete_project_and_tasks(self.project_id)
        delete_project_tasks_confirmation = QMessageBox()
        delete_project_tasks_confirmation.setWindowTitle("Project deleted")
        delete_project_tasks_confirmation.setInformativeText("Project and associated tasks deleted")
        delete_project_tasks_confirmation.exec_()
        self.close()

    def delete_project_only(self):
        self.controller.delete_project_only(self.project_id)
        delete_project_only_confirmation = QMessageBox()
        delete_project_only_confirmation.setWindowTitle("Project deleted")
        delete_project_only_confirmation.setInformativeText("Associated tasks are no longer assigned to any project")
        delete_project_only_confirmation.exec_()
        self.close()


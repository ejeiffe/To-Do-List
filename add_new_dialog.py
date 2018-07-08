from PyQt5.QtWidgets import *

from db_controller import *
from datetime import datetime

class AddNewDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.controller = DbController("to_do.db")

        self.description_label = QLabel("Description:")
        self.description_line_edit = QLineEdit()
        self.deadline_label = QLabel("Deadline: ")
        self.deadline_calendar_widget = QCalendarWidget()
        self.deadline_calendar_widget.setMinimumDate(datetime.today())

        self.description_deadline_layout = QVBoxLayout()
        self.description_deadline_layout.addWidget(self.description_label)
        self.description_deadline_layout.addWidget(self.description_line_edit)
        self.description_deadline_layout.addWidget(self.deadline_label)
        self.description_deadline_layout.addWidget(self.deadline_calendar_widget)

        self.save_new_button = QPushButton("Save")
        self.save_new_button.setEnabled(False)
        self.cancel_new_button = QPushButton("Cancel")

        self.add_new_button_layout = QHBoxLayout()
        self.add_new_button_layout.addWidget(self.save_new_button)
        self.add_new_button_layout.addWidget(self.cancel_new_button)

        self.description_line_edit.textEdited.connect(self.enable_save_button)
        self.cancel_new_button.clicked.connect(self.close)

    def enable_save_button(self):
        self.save_new_button.setEnabled(True)

class NewTaskDialog(AddNewDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Task")

        self.project_assign_label = QLabel("Assign to Project")
        self.project_assign_combobox = QComboBox()
        self.project_assign_combobox.addItem("None")
        for project in self.get_project_list():
            self.project_assign_combobox.addItem(project)

        self.project_assign_layout = QVBoxLayout()
        self.project_assign_layout.addWidget(self.project_assign_label)
        self.project_assign_layout.addWidget(self.project_assign_combobox)

        self.new_task_layout = QVBoxLayout()
        self.new_task_layout.addLayout(self.description_deadline_layout)
        self.new_task_layout.addLayout(self.project_assign_layout)
        self.new_task_layout.addLayout(self.add_new_button_layout)

        self.setLayout(self.new_task_layout)

        self.save_new_button.clicked.connect(self.add_new_task)

    def get_project_list(self):
        project_list = []
        for entry in self.controller.get_all_projects():
            project_list.append(str(entry[0])+": "+entry[1])
        return project_list

    def add_new_task(self):
        description = self.description_line_edit.text()
        deadline = self.deadline_calendar_widget.selectedDate().toPyDate()
        if self.project_assign_combobox.currentText() == "None":
            project_id = None
        else:
            project_id = int(self.project_assign_combobox.currentText()[0])
        self.controller.add_task(description, deadline, project_id)
        self.close()

class NewProjectDialog(AddNewDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Project")

        self.new_project_layout = QVBoxLayout()
        self.new_project_layout.addLayout(self.description_deadline_layout)
        self.new_project_layout.addLayout(self.add_new_button_layout)

        self.setLayout(self.new_project_layout)

        self.save_new_button.clicked.connect(self.add_new_project)

    def add_new_project(self):
        description = self.description_line_edit.text()
        deadline = self.deadline_calendar_widget.selectedDate().toPyDate()
        self.controller.add_project(description, deadline)
        self.close()



from PyQt5.QtWidgets import *

from db_controller import *

class MarkCompleteDialog(QDialog):

    def __init__(self, project_id):
        super().__init__()
        self.controller = DbController("to_do.db")
        self.project_id = project_id

        self.description = self.get_project_description()

        self.project_id_label = QLabel("Project ID: "+str(self.project_id))
        self.project_description_label = QLabel(self.description)

        self.project_info_layout = QHBoxLayout()
        self.project_info_layout.addWidget(self.project_id_label)
        self.project_info_layout.addWidget(self.project_description_label)

        self.yes_button = QPushButton("Yes")
        self.no_button = QPushButton("No")

        self.mark_complete_button_layout = QHBoxLayout()
        self.mark_complete_button_layout.addWidget(self.yes_button)
        self.mark_complete_button_layout.addWidget(self.no_button)

        self.no_button.clicked.connect(self.close)

    def get_project_description(self):
        return self.controller.get_single_project(self.project_id)[0][1]

class MarkProjectCompleteDialog(MarkCompleteDialog):

    def __init__(self, project_id):
        super().__init__(project_id)

        self.setWindowTitle("Mark Project Complete")

        self.project_completed_message = QLabel("All tasks for this project are completed.")
        self.mark_project_complete_message = QLabel("Mark project complete?")

        self.mark_project_complete_layout = QVBoxLayout()
        self.mark_project_complete_layout.addLayout(self.project_info_layout)
        self.mark_project_complete_layout.addWidget(self.project_completed_message)
        self.mark_project_complete_layout.addWidget(self.mark_project_complete_message)
        self.mark_project_complete_layout.addLayout(self.mark_complete_button_layout)

        self.setLayout(self.mark_project_complete_layout)

        self.yes_button.clicked.connect(self.mark_project_completed)

    def mark_project_completed(self):
        self.controller.mark_project_completed(self.project_id)
        self.close()

class MarkProjectTasksCompleteDialog(MarkCompleteDialog):

    def __init__(self, project_id):
        super().__init__(project_id)

        self.setWindowTitle("Mark Project Tasks Complete")

        self.project_tasks_message = QLabel("Some tasks for this project are not yet completed.")
        self.mark_project_tasks_complete_message = QLabel("Mark all project tasks complete?")

        self.mark_project_tasks_complete_layout = QVBoxLayout()
        self.mark_project_tasks_complete_layout.addLayout(self.project_info_layout)
        self.mark_project_tasks_complete_layout.addWidget(self.project_tasks_message)
        self.mark_project_tasks_complete_layout.addWidget(self.mark_project_tasks_complete_message)
        self.mark_project_tasks_complete_layout.addLayout(self.mark_complete_button_layout)

        self.setLayout(self.mark_project_tasks_complete_layout)

        self.yes_button.clicked.connect(self.mark_project_tasks_completed)

    def mark_project_tasks_completed(self):
        self.controller.mark_project_tasks_completed(self.project_id)
        self.close()
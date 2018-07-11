from PyQt5.QtWidgets import *

from db_controller import *
from radio_button_widget import *
from table_widget import *
from add_new_dialog import *
from mark_complete_dialog import *
from edit_dialog import *
from delete_dialog import *

class TaskProjectTabs(QWidget):

    def __init__(self):
        super().__init__()
        self.controller = DbController("to_do.db")

        self.tabs = QTabWidget()
        self.tasks_tab = QWidget()
        self.projects_tab = QWidget()

        self.tabs.addTab(self.tasks_tab, "Tasks")
        self.tabs.addTab(self.projects_tab, "Projects")

        self.tasks_tab_layout = QVBoxLayout()
        self.projects_tab_layout = QVBoxLayout()

        self.tasks_radio_buttons = RadioButtonWidget(['Active Tasks', 'Completed Tasks', 'All Tasks'])
        self.projects_radio_buttons = RadioButtonWidget(['Active Projects', 'Completed Projects', 'All Projects'])

        self.tasks_table = TasksTable()
        self.populate_tasks_table()
        self.projects_table = ProjectsTable()
        self.populate_projects_table()

        self.new_task_button = QPushButton("Add New")
        self.task_complete_button = QPushButton("Mark Completed")
        self.task_complete_button.setEnabled(False)
        self.task_edit_button = QPushButton("Edit")
        self.task_edit_button.setEnabled(False)
        self.task_delete_button = QPushButton("Delete")
        self.task_delete_button.setEnabled(False)
        self.task_exit_button = QPushButton("Exit")

        self.new_project_button = QPushButton("Add New")
        self.project_tasks_button = QPushButton("View Project Tasks")
        self.project_tasks_button.setEnabled(False)
        self.project_complete_button = QPushButton("Mark Completed")
        self.project_complete_button.setEnabled(False)
        self.project_edit_button = QPushButton("Edit")
        self.project_edit_button.setEnabled(False)
        self.project_delete_button = QPushButton("Delete")
        self.project_delete_button.setEnabled(False)
        self.project_exit_button = QPushButton("Exit")

        self.tasks_tab_button_layout = QHBoxLayout()
        self.tasks_tab_button_layout.addWidget(self.new_task_button)
        self.tasks_tab_button_layout.addWidget(self.task_complete_button)
        self.tasks_tab_button_layout.addWidget(self.task_edit_button)
        self.tasks_tab_button_layout.addWidget(self.task_delete_button)
        self.tasks_tab_button_layout.addWidget(self.task_exit_button)

        self.projects_tab_button_layout = QHBoxLayout()
        self.projects_tab_button_layout.addWidget(self.new_project_button)
        self.projects_tab_button_layout.addWidget(self.project_tasks_button)
        self.projects_tab_button_layout.addWidget(self.project_complete_button)
        self.projects_tab_button_layout.addWidget(self.project_edit_button)
        self.projects_tab_button_layout.addWidget(self.project_delete_button)
        self.projects_tab_button_layout.addWidget(self.project_exit_button)

        self.tasks_tab_layout.addWidget(self.tasks_radio_buttons)
        self.tasks_tab_layout.addWidget(self.tasks_table)
        self.tasks_tab_layout.addLayout(self.tasks_tab_button_layout)
        self.tasks_tab.setLayout(self.tasks_tab_layout)

        self.projects_tab_layout.addWidget(self.projects_radio_buttons)
        self.projects_tab_layout.addWidget(self.projects_table)
        self.projects_tab_layout.addLayout(self.projects_tab_button_layout)
        self.projects_tab.setLayout(self.projects_tab_layout)

        self.tab_widget_layout = QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)

        self.tabs.currentChanged.connect(self.refresh_tab)

        self.tasks_radio_buttons.radio_button_group.buttonClicked.connect(self.populate_tasks_table)
        self.projects_radio_buttons.radio_button_group.buttonClicked.connect(self.populate_projects_table)

        self.tasks_table.clicked.connect(self.enable_task_buttons)
        self.projects_table.clicked.connect(self.enable_project_buttons)

        self.new_task_button.clicked.connect(self.open_new_task_dialog)
        self.new_project_button.clicked.connect(self.open_new_project_dialog)
        
        self.task_complete_button.clicked.connect(self.mark_task_completed)
        self.project_complete_button.clicked.connect(self.mark_project_completed)

        self.task_edit_button.clicked.connect(self.open_edit_task_dialog)
        self.project_edit_button.clicked.connect(self.open_edit_project_dialog)

        self.task_delete_button.clicked.connect(self.open_delete_task_dialog)
        self.project_delete_button.clicked.connect(self.open_delete_project_dialog)

    def populate_tasks_table(self):
        table_type = self.tasks_radio_buttons.selected_button()
        table_items = self.tasks_table.get_tasks(table_type)
        self.tasks_table.show_items(table_items)
        
    def populate_projects_table(self):
        table_type = self.projects_radio_buttons.selected_button()
        table_items = self.projects_table.get_projects(table_type)
        self.projects_table.show_items(table_items)

    def refresh_tab(self):
        if self.tabs.currentIndex() == 0:
            self.populate_tasks_table()
        else:
            self.populate_projects_table()

    def enable_task_buttons(self):
        if not self.tasks_table.check_completed():
            self.task_complete_button.setEnabled(True)
        else:
            self.task_complete_button.setEnabled(False)
        self.task_edit_button.setEnabled(True)
        self.task_delete_button.setEnabled(True)

    def enable_project_buttons(self):
        self.project_tasks_button.setEnabled(True)
        if not self.projects_table.check_completed():
            self.project_complete_button.setEnabled(True)
        else:
            self.project_complete_button.setEnabled(False)
        self.project_edit_button.setEnabled(True)
        self.project_delete_button.setEnabled(True)

    def open_new_task_dialog(self):
        new_task_dialog = NewTaskDialog()
        new_task_dialog.exec_()
        self.populate_tasks_table()

    def open_new_project_dialog(self):
        new_project_dialog = NewProjectDialog()
        new_project_dialog.exec_()
        self.populate_projects_table()

    def open_edit_task_dialog(self):
        task_id = self.tasks_table.get_id()
        edit_task_dialog = EditTaskDialog(task_id)
        edit_task_dialog.exec_()
        self.populate_tasks_table()

    def open_edit_project_dialog(self):
        project_id = self.projects_table.get_id()
        edit_project_dialog = EditProjectDialog(project_id)
        edit_project_dialog.exec_()
        self.populate_projects_table()

    def mark_task_completed(self):
        task_id = self.tasks_table.get_id()
        self.controller.mark_task_completed(task_id)
        project_id = self.check_project_tasks_completed()
        if project_id:
            mark_project_complete_dialog = MarkProjectCompleteDialog(project_id)
            mark_project_complete_dialog.exec_()
        self.populate_tasks_table()

    def check_project_tasks_completed(self):
        project_id = self.tasks_table.get_task_project_id()
        if self.controller.check_project_completed(project_id):
            return project_id
        else:
            return False

    def mark_project_completed(self):
        project_id = self.projects_table.get_id()
        self.controller.mark_project_completed(project_id)
        if not self.check_project_tasks_completed():
            mark_project_tasks_complete_dialog = MarkProjectTasksCompleteDialog(project_id)
            mark_project_tasks_complete_dialog.exec_()
        self.populate_projects_table()

    def open_delete_task_dialog(self):
        task_id = self.tasks_table.get_id()
        delete_task_dialog = DeleteTaskDialog(task_id)
        delete_task_dialog.exec_()
        self.populate_tasks_table()

    def open_delete_project_dialog(self):
        project_id = self.projects_table.get_id()
        delete_project_dialog = DeleteProjectDialog(project_id)
        delete_project_dialog.exec_()
        self.populate_projects_table()








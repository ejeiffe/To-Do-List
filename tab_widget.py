from PyQt5.QtWidgets import *

from radio_button_widget import *
from table_widget import *

class TaskProjectTabs(QWidget):

    def __init__(self):
        super().__init__()
        self.tab_widget_layout = QVBoxLayout()

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
        self.projects_table = ProjectsTable()

        self.tasks_tab_layout.addWidget(self.tasks_radio_buttons)
        self.tasks_tab_layout.addWidget(self.tasks_table)

        self.projects_tab_layout.addWidget(self.projects_radio_buttons)
        self.projects_tab_layout.addWidget(self.projects_table)
        self.projects_tab.setLayout(self.projects_tab_layout)

        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)
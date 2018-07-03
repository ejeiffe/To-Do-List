import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from create_new_db import *
from db_controller import *

class ToDoWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.controller = DbController("to_do.db")
        
        self.setWindowTitle("To Do List")
        self.resize(300,500)
        
        self.central_widget = TaskProjectTabs()
        self.setCentralWidget(self.central_widget)

class TaskProjectTabs(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tasks_tab = QWidget()
        self.projects_tab = QWidget()
        self.tabs.resize(300, 500)

        self.tabs.addTab(self.tasks_tab, "Tasks")
        self.tabs.addTab(self.projects_tab, "Projects")

        self.tasks_tab_layout = QVBoxLayout()
        self.projects_tab_layout = QVBoxLayout()

        self.tasks_radio_buttons = RadioButtonWidget(['Active Tasks', 'Completed Tasks', 'All Tasks'])
        self.projects_radio_buttons = RadioButtonWidget(['Active Projects', 'Completed Projects', 'All Projects'])

        self.tasks_tab_layout.addWidget(self.tasks_radio_buttons)
        self.tasks_tab.setLayout(self.tasks_tab_layout)

        self.projects_tab_layout.addWidget(self.projects_radio_buttons)
        self.projects_tab.setLayout(self.projects_tab_layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class RadioButtonWidget(QWidget):
    def __init__(self, button_list):
        super().__init__()

        self.radio_button_group = QButtonGroup()

        self.radio_button_list = []
        for item in button_list:
            self.radio_button_list.append(QRadioButton(item))

        #set first button checked as default
        self.radio_button_list[0].setChecked(True)

        self.radio_button_layout = QHBoxLayout()

        for counter, item in enumerate(self.radio_button_list):
            self.radio_button_layout.addWidget(item)
            self.radio_button_group.addButton(item)
            self.radio_button_group.setId(item, counter)

        self.setLayout(self.radio_button_layout)

    def selected_button(self):
        return self.radio_button_group.checkedId()         
      
if __name__ == "__main__":
    to_do = QApplication(sys.argv)
    main_window = ToDoWindow()
    main_window.show()
    main_window.raise_()
    #creates new database when run for the first time
    if not os.path.exists("to_do.db"):
        create_new_db("to_do.db")
        new_db = QMessageBox()
        new_db.setWindowTitle("New Database")
        new_db.setText("New database created")
        new_db.exec_()
    to_do.exec_()

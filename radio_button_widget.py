from PyQt5.QtWidgets import *

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
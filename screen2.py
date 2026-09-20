from PySide6.QtWidgets import (QWidget,
                               QLabel,
                               QPushButton,
                               QVBoxLayout)
from PySide6.QtCore import (Qt)
class Screen2(QWidget):
    def __init__(self, screenControl):
        super().__init__()
        #The super makes it so that
        #the class inherits all of the 
        #properties of the class in the brackets.
        self.screenControl = screenControl
        self.label = QLabel("Screen 2")
        self.label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Button")
        self.button.clicked.connect(self.pastScreen)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setStyleSheet("""
                QWidget {background-color:dark-blue;
                color: blue;}
                QPushButton{ padding: 50px; color:cyan;}""")
    def pastScreen(self):
        self.screenControl.changeScreen(0)
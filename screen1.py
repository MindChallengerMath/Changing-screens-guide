from PySide6.QtWidgets import (QWidget,
                               QLabel,
                               QPushButton,
                               QVBoxLayout)
from PySide6.QtCore import (Qt)
class Screen1(QWidget):
    def __init__(self, screenControl):
        super().__init__()
        #The super makes it so that
        #the class inherits all of the 
        #properties of the class in the brackets.
        self.screenControl = screenControl
        self.label = QLabel("Screen 1")
        self.label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Button")
        self.button.clicked.connect(self.nextScreen)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setStyleSheet("""
        QWidget {background-color:maroon;
        color: red;}
        QPushButton{ padding: 50px; color:pink;}""")
    def nextScreen(self):
        self.screenControl.changeScreen(1)



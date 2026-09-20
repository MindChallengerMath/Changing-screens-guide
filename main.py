from PySide6.QtWidgets import (QApplication)
from screen1 import Screen1
from screen2 import Screen2
from screenControl import ScreenControl

if __name__ == "__main__":
    app = QApplication()
    screenControl = ScreenControl()
    screen1 = Screen1(screenControl)
    screen2 = Screen2(screenControl)
    screenControl.stack.insertWidget(0, screen1)
    screenControl.stack.insertWidget(1, screen2)
    screenControl.stack.show()
    app.exec()

    
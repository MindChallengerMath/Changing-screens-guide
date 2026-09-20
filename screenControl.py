from PySide6.QtWidgets import (QStackedWidget)

class ScreenControl():
    def __init__(self):
        self.stack = QStackedWidget()

    def changeScreen(self, screen):
        self.stack.setCurrentIndex(screen)

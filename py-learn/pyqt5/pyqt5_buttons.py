import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clefairy GUI")
        self.setGeometry(500, 300, 500, 500)
        self.setWindowIcon(QIcon("py-learn/pyqt5/icon.png"))
        self.button = QPushButton("Clefairy", self)
        self.label = QLabel("Label", self)
        self.checkbox = QCheckBox("Do you wanna build a snowman?", self)
        self.InitUI()

    def InitUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 20px")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(225, 300, 200, 100)
        self.label.setStyleSheet("font-size: 20px")
        self.checkbox.setGeometry(125, 400, 400, 100)
        self.checkbox.setStyleSheet("font-size: 20px")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.on_checked)

    def on_click(self):
        print("Button Clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Boo!")

    def on_checked(self, state):
        if state == Qt.Checked:
            print("Checked!")
        else:
            print("Unchecked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

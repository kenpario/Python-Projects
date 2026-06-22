import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QRadioButton,
    QButtonGroup,
    QLineEdit,
    QPushButton,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clefairy GUI")
        self.setGeometry(500, 300, 500, 500)
        self.setWindowIcon(QIcon("py-learn/pyqt5/icon.png"))
        # self.radiobutton1 = QRadioButton("Visa", self)
        # self.radiobutton2 = QRadioButton("MasterCard", self)
        # self.radiobutton3 = QRadioButton("PayPal", self)
        # self.radiobutton4 = QRadioButton("In-Store", self)
        # self.radiobutton5 = QRadioButton("Online", self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        #     self.radiobutton1.setGeometry(5, 0, 100, 50)
        #     self.radiobutton2.setGeometry(5, 25, 150, 50)
        #     self.radiobutton3.setGeometry(5, 50, 100, 50)
        #     self.radiobutton4.setGeometry(5, 75, 150, 50)
        #     self.radiobutton5.setGeometry(5, 100, 100, 50)
        #     self.setStyleSheet(
        #         "QRadioButton{" "font-size: 20px;" "font-family: Arial;" "padding: 5px;" "}"
        #     )
        #     self.button_group1.addButton(self.radiobutton1)
        #     self.button_group1.addButton(self.radiobutton2)
        #     self.button_group1.addButton(self.radiobutton3)
        #     self.button_group2.addButton(self.radiobutton4)
        #     self.button_group2.addButton(self.radiobutton5)

        #     self.radiobutton1.toggled.connect(self.radio_button_changed)
        #     self.radiobutton2.toggled.connect(self.radio_button_changed)
        #     self.radiobutton3.toggled.connect(self.radio_button_changed)
        #     self.radiobutton4.toggled.connect(self.radio_button_changed)
        #     self.radiobutton5.toggled.connect(self.radio_button_changed)

        # def radio_button_changed(self):
        #     radio_button = self.sender()
        #     if radio_button.isChecked():
        #         print(f"{radio_button.text()} is selected")
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setStyleSheet("font-size: 20px;")
        self.button.setGeometry(210, 10, 100, 40)
        self.button.setStyleSheet("font-size: 20px;")
        self.line_edit.setPlaceholderText("Enter you name")

        self.button.clicked.connect(self.submit)

    def submit(self):
        line_edit_text = self.line_edit.text()
        print(f"{line_edit_text} was submitted.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

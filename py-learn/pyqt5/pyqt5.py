import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clefairy GUI")
        self.setGeometry(500, 300, 500, 500)
        self.setWindowIcon(QIcon("py-learn/pyqt5/icon.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet(
            "color: #7d6265;"
            "background-color: black;"
            "font-wight:bold;"
            "font-style:italic;"
        )
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(110, 85)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("This is a test project")
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

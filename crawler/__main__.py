import sys

from PyQt5.QtWidgets import QApplication

from crawler.view.mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())

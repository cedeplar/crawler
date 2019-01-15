import sys
from PyQt5.QtWidgets import QApplication

from crawler.view.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
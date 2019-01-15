import sys
from PyQt5.QtWidgets import QApplication

from crawler.view.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
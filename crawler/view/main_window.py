from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("CEDEPLAR - WebCrawler - UFMG")

        cedeplar_win_logo = Path('icons', 'cedeplar_ufmg_small.png')
        icon_window = QIcon(str(cedeplar_win_logo))
        self.setWindowIcon(icon_window)

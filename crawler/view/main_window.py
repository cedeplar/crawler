from PyQt5.QtWidgets import QMainWindow

from crawler.view.ui.mainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._gui = Ui_MainWindow()
        self._gui.setupUi(self)

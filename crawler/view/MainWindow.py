from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from crawler.ConfigSearchData import ConfigSearchData
from crawler.view.ConfigSearch import ConfigSearch
from crawler.view.ui.mainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._gui = Ui_MainWindow()
        self._gui.setupUi(self)
        self._gui.btn_configureSearch.clicked.connect(self.open_config_search)
        self._config_search_data = None
        self.reset()

    def reset(self):
        self._gui.progressBar.setValue(0)
        self._gui.progressBar.setEnabled(False)
        self._gui.lcs_counter.display(0)

    @pyqtSlot()
    def open_config_search(self):
        config_search = ConfigSearch(self)
        config_search.exec_()
        self.config_search_data = config_search.get_data()

    @property
    def config_search_data(self):
        if not self._config_search_data:
            self._config_search_data = ConfigSearchData()
        return self._config_search_data

    @config_search_data.setter
    def config_search_data(self, config_data):
        self._config_search_data = config_data

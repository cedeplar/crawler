from functools import partial

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QCheckBox, QLineEdit

from crawler.ConfigSearchData import ConfigSearchData
from crawler.constants import Transacao
from crawler.view.ui.ConfigSearch_ui import Ui_ConfigSearch


class ConfigSearch(QDialog):

    OPTIONS_ACTIVATED = {
        'cb_valor_minimo': 'text_valor_minimo',
        'cb_valor_maximo': 'text_valor_maximo',
        'cb_idade_minima': 'text_idade_minima',
        'cb_suites': 'text_suites',
        'cb_banheiros': 'text_banheiros',
        'cb_min_area': 'text_min_area',
        'cb_max_area': 'text_max_area',
        'cb_num_quartos': 'text_num_quartos',
        'cb_num_garagem': 'text_num_garagem',
    }

    def __init__(self, parent=None):
        super(ConfigSearch, self).__init__(parent)
        self._tipos_imoveis = {
            'cb_andar_pilotis': ['andar-pilotis', True],
            'cb_apartamento': ['apartamento', True],
            'cb_apart_hotel': ['apart-hotel', True],
            'cb_area_privativa': ['area-privativa', True],
            'cb_barracao': ['barracao', True],
            'cb_casa': ['casa', True],
            'cb_casa_comercial': ['casa-comercial', True],
            'cb_casa_geminada': ['casa-germinada', True],
            'cb_casa_condominio': ['casa-em-condominio', True],
            'cb_chacara': ['chacara', True],
            'cb_clube': ['clube', True],
            'cb_cobertura': ['cobertura', True],
            'cb_conjunto_lojas': ['conjunto-de-lojas', True],
            'cb_conjunto_salas': ['conjunto-de-salas', True],
            'cb_duplex': ['duplex', True],
            'cb_estacionamento': ['estacionamento', True],
            'cb_empreendimento': ['empreendimento', True],
            'cb_fazenda': ['fazenda', True],
            'cb_flat': ['flat', True],
            'cb_galpao': ['galpao', True],
            'cb_garagem': ['garagem', True],
            'cb_haras': ['haras', True],
            'cb_hotel': ['hotel', True],
            'cb_hotel_fazenda': ['hotel-fazenda', True],
            'cb_ilha': ['ilha', True],
            'cb_kitchenette': ['kitchenette', True],
            'cb_loft': ['loft', True],
            'cb_loja': ['loja', True],
            'cb_area_terreno': ['lote-area-terreno', True],
            'cb_lote_condominio': ['lote-em-condominio', True],
            'cb_motel': ['motel', True],
            'cb_pousada': ['pousada', True],
            'cb_ponto_comercial': ['ponto-comercial', True],
            'cb_predio': ['predio', True],
            'cb_sala': ['sala', True],
            'cb_shopping': ['shopping', True],
            'cb_sitio': ['sitio', True],
            'cb_sobrado': ['sobrado', True],
            'cb_sobre_loja': ['sobre-loja', True],
        }
        self._gui = Ui_ConfigSearch()
        self._gui.setupUi(self)
        self.setWindowModality(Qt.WindowModal)
        self.check_all_imoveis()

        self._gui.cb_todos.clicked.connect(self.check_all_imoveis)
        self._gui.btn_uncheck_all.clicked.connect(self.uncheck_all_imoveis)

        list_cb_tipo_imovel = self._gui.bt_group_tipo_imovel.buttons()
        for button in list_cb_tipo_imovel:
            slot_btn = partial(self._change_conf, button)
            button.stateChanged.connect(slot_btn)

        list_cb_opt_activated = self._gui.bt_group_options_activated.buttons()
        for button in list_cb_opt_activated:
            slot_btn = partial(self._change_opt_activated, button)
            button.stateChanged.connect(slot_btn)
            validator = QIntValidator()
            wd_validate = self.findChild(QLineEdit,
                           self.OPTIONS_ACTIVATED[button.objectName()])
            wd_validate.setValidator(validator)

        self.show()

    @pyqtSlot()
    def check_all_imoveis(self):
        if not self._gui.cb_todos.isChecked():
            return
        self._check_all_imoveis(True)

    @pyqtSlot()
    def uncheck_all_imoveis(self):
        self._check_all_imoveis(False)
        self._gui.cb_todos.setChecked(False)

    def _check_all_imoveis(self, checked):
        for button in self._gui.bt_group_tipo_imovel.buttons():
            button.setChecked(checked)
            self._config_tipo_imovel(button.objectName(), checked)

    def _config_tipo_imovel(self, check_box, checked):
        self._tipos_imoveis[check_box][1] = checked

    @pyqtSlot(QCheckBox)
    def _change_conf(self, checkbox):
        if not checkbox.isChecked():
            self._gui.cb_todos.setChecked(False)
        self._config_tipo_imovel(checkbox.objectName(), checkbox.isChecked())

    @pyqtSlot(QCheckBox)
    def _change_opt_activated(self, checkbox):
        name_wd_to_enable = self.OPTIONS_ACTIVATED[checkbox.objectName()]
        wd_to_enable = self.findChild(QLineEdit, name_wd_to_enable)
        wd_to_enable.setEnabled(checkbox.isChecked())

        if not checkbox.isChecked():
            wd_to_enable.setText('')

    def get_data(self):
        list_imovel = []
        if not self._is_imoveis_all_true():
            for key, value in self._tipos_imoveis:
                list_imovel.append(value[0])

        valor_minimo = None
        if self._gui.cb_valor_minimo.isChecked():
            valor_minimo = self._gui.text_valor_minimo.text()

        valor_maximo = None
        if self._gui.cb_valor_maximo.isChecked():
            valor_maximo = self._gui.text_valor_maximo.text()

        quartos = None
        if self._gui.cb_num_quartos.isChecked():
            quartos = self._gui.text_num_quartos.text()

        suites = None
        if self._gui.cb_suites.isChecked():
            suites = self._gui.text_suites.text()

        banhos = None
        if self._gui.cb_banheiros.isChecked():
            banhos = self._gui.text_banheiros.text()

        vagas = None
        if self._gui.cb_num_garagem.isChecked():
            vagas = self._gui.text_num_garagem.text()

        idade_minima = None
        if self._gui.cb_idade_minima.isChecked():
            idade_minima = self._gui.text_idade_minima.text()

        area_minima = None
        if self._gui.cb_min_area.isChecked():
            area_minima = self._gui.text_min_area.text()

        area_maxima = None
        if self._gui.cb_max_area.isChecked():
            area_maxima = self._gui.text_max_area.text()

        options = {
            'valorMinimo': valor_minimo,
            'valorMaximo': valor_maximo,
            'quartos': quartos,
            'suites': suites,
            'banhos': banhos,
            'vagas': vagas,
            'idadeMinima': idade_minima,
            'areaMinima': area_minima,
            'areaMaxima': area_maxima,
            'bairros': [],
            'ordenar': None
        }

        state = self._gui.combo_estado.currentText()
        state = self._fix_string_to_json(state)

        city = self._gui.txt_cidade.text()
        city = self._fix_string_to_json(city)

        transacao = self._get_venda_locacao_combo()

        return ConfigSearchData(options, list_imovel, state, city, transacao)

    def _fix_string_to_json(self, value):
        value = value.strip()
        value = value.replace(' ', '-')
        return value.lower()

    def _get_venda_locacao_combo(self):
        val_selected = self._gui.cb_tipo_transacao.currentIndex()
        if val_selected == 1:
            return Transacao.Locacao
        if val_selected == 2:
            return Transacao.Venda
        return Transacao.Venda_locacao


    def _is_imoveis_all_true(self):
        for key, value in self._tipos_imoveis:
            if not value[1]:
                return False
        return True
from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget,QComboBox
from PyQt5.QtCore import Qt
from Window_layouts.main_window_layout import Icon,title_font

#Switch window
switch_window = QWidget()
switch_window.resize(400,400)
switch_window.setWindowIcon(Icon)
switch_window.setObjectName("main_window")
#Switch window layout
choose_language_title = QLabel("Choose a language")
choose_language_title.setFont(title_font)
languages_list = QComboBox()
languages_list.setMinimumWidth(100)
languages_list.addItems(("English","Українська"))
switch_window_layout = QVBoxLayout()
switch_window_layout.addStretch(1)
switch_window_layout.addWidget(choose_language_title,alignment=Qt.AlignHCenter)
switch_window_layout.addWidget(languages_list,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
switch_window_layout.addStretch(1)

switch_window.setLayout(switch_window_layout)
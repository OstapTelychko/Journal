white_theme = """QWidget#main_window{
    background-color:rgb(215,215,215);
    color:rgb(25,25,25);
}
QWidget#Scroll_window{
    background-color:rgb(215,215,215);
}
QWidget#lesson_window{
    background-color:rgb(195,195,195);
    margin:0;
    padding:0;
}
QPushButton{
    background-color: qlineargradient( x1:0, y1:0, x2:1, y2:0, stop:0 rgb(165,165,165),stop:1 rgb(195,195,195));
    border-radius:10px;
    color:rgb(25,25,25);
}
QPushButton:hover{
    background-color: qlineargradient( x1:0, y1:0, x2:1, y2:0, stop:0 rgb(160,160,160),stop:1 rgb(190,190,190));
}
QPushButton:pressed{
    background-color: qlineargradient( x1:0, y1:0, x2:1, y2:0, stop:0 rgb(150,150,150),stop:1 rgb(180,180,180));
}
QListWidget{
    background-color: qlineargradient( x1:0, y1:1, x2:1, y2:1, stop:0 rgb(155,155,155),stop:1 rgb(205,205,205));
    border:hidden;
    border-radius:15px;
    color:rgb(25,25,25);
}
QListWidget::item {
    border:hidden;
    border-radius:10px;
    color:rgb(25,25,25);
}
QListView{
    outline:none;
}
QListWidget::item:selected {
    background-color: rgb(205,205,205);
}


QScrollArea{
    border:none;
    background-color:none;
}
QScrollBar:horizontal {
    border:none;
    background-color:rgb(210,210,210)    
}
QScrollBar::handle:horizontal {
    background-color: rgb(185,185,185);
    border-radius:7px;
}
QScrollBar::handle:horizontal:hover {
    background-color: rgb(180,180,180);
}
QScrollBar::handle:horizontal:pressed {
    background-color: rgb(170,170,170);
}
QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal {
    border:none;
    background:rgb(205,205,205);
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: rgb(200,200,200);
    border-radius:5px;
}
QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    background-color:none;
}
QScrollBar:vertical {
    border:none;
   background-color:rgb(210,210,210)    
}
QScrollBar::handle:vertical {
    background-color: rgb(185,185,185);
    border-top-right-radius:10px;
    border-bottom-right-radius:10px;
}
QScrollBar::handle:vertical:hover {
    background-color: rgb(180,180,180);
}
QScrollBar::handle:vertical:pressed {
    background-color: rgb(170,170,170);
}
QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical {
    border:none;
    background: rgb(200,200,200);
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: rgb(200,200,200);
    border-top-right-radius:10px;
    border-bottom-right-radius:10px;
}
QScrollBar:up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
    background-color:none;
}

QLabel{
    background-color:none;
    color:rgb(25,25,25);
}
QComboBox{
    border-radius:5px;
    background-color:rgb(205,205,205);
    color:rgb(25,25,25);
}
QComboBox QAbstractItemView {
  background-color: rgb(195,195,195);
  color: rgb(25,25,25);
  selection-background-color: rgb(200,200,200);
}
QComboBox QAbstractItemView:selected {
  background: rgb(205,205,205);
  color: rgb(25,25,25);
}
QLineEdit{
    background-color:rgb(205,205,205);
    color:rgb(25,25,25);
    border-radius:5px;
}
QToolButton{
    background-color:rgb(215,215,215);
    border:none;
}
"""
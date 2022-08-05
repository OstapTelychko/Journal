black_theme = """QWidget#main_window{
    background-color:rgb(30,30,30);
    color:rgb(220,220,220);
}
QWidget#Scroll_window{
    background-color:rgb(30,30,30);
}
QWidget#lesson_window{
    background-color:rgb(50,50,50);
    margin:0;
    padding:0;
}
QPushButton{
    background-color: qlineargradient( x1:0, y1:0, x2:1, y2:0, stop:0 rgb(80,80,80),stop:1 rgb(50,50,50));
    border-radius:10px;
    color:rgb(220,220,220);
}
QPushButton:hover{
    background-color: qlineargradient( x1:0, y1:0, x2:1, y2:0, stop:0 rgb(70,70,70),stop:1 rgb(45,45,45));
}
QPushButton:pressed{
    background-color: qlineargradient( x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60,60,60),stop:1 rgb(35,35,35));
}
QListWidget{
    background-color: qlineargradient( x1:0, y1:1, x2:1, y2:1, stop:0 rgb(90,90,90),stop:1 rgb(40,40,40));
    border:hidden;
    border-radius:15px;
    color:rgb(220,220,220);
}
QListWidget::item {
    border:hidden;
    border-radius:10px;
    color:rgb(220,220,220);
}
QListView{
    outline:none;
}
QListWidget::item:selected {
    background-color: rgb(40,40,40);
    border-color:red;
}


QScrollArea{
    border:none;
    background-color:none;
}
QScrollBar:horizontal {
    border:none;
    background-color:rgb(35,35,35)    
}
QScrollBar::handle:horizontal {
    background-color: rgb(60,60,60);
    border-radius:7px;
}
QScrollBar::handle:horizontal:hover {
    background-color: rgb(55,55,55);
}
QScrollBar::handle:horizontal:pressed {
    background-color: rgb(45,45,45);
}
QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal {
    border:none;
    background:rgb(30,30,30);
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: rgb(35,35,35);
    border-radius:5px;
}
QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    background-color:none;
}
QScrollBar:vertical {
    border:none;
    background-color:rgb(35,35,35)    
}
QScrollBar::handle:vertical {
    background-color: rgb(60,60,60);
    border-top-right-radius:10px;
    border-bottom-right-radius:10px;
}
QScrollBar::handle:vertical:hover {
    background-color: rgb(55,55,55);
}
QScrollBar::handle:vertical:pressed {
    background-color: rgb(45,45,45);
}
QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical {
    border:none;
    background:rgb(30,30,30);
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: rgb(35,35,35);
    border-top-right-radius:10px;
    border-bottom-right-radius:10px;
}
QScrollBar:up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
    background-color:none;
}

QLabel{
    background-color:none;
    color:rgb(220,220,220);
}
QComboBox{
    border-radius:5px;
    background-color:rgb(40,40,40);
    color:rgb(220,220,220);
}
QComboBox QAbstractItemView {
  background-color: rgb(50,50,50);
  color: rgb(220,220,220);
  selection-background-color: rgb(45,45,45);
}
QComboBox QAbstractItemView:selected {
  background: rgb(40,40,40);
  color: rgb(220,220,220);
}
QLineEdit{
    background-color:rgb(40,40,40);
    color:rgb(220,220,220);
    border-radius:5px;
}
QToolButton{
    background-color:rgb(30,30,30);
    border:none;
}
"""
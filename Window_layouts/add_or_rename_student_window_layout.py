from PyQt5.QtWidgets import QWidget,QLineEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from Window_layouts.main_window_layout import Icon,title_font,basic_font,Qt

#Add student window
add_or_rename_student_window = QWidget()
add_or_rename_student_window.resize(400,400)
add_or_rename_student_window.setWindowIcon(Icon)
add_or_rename_student_window.setObjectName("main_window")
#Add student window layout
add_or_rename_student_title = QLabel("Enter your student's name and surname")
add_or_rename_student_title.setFont(title_font)
students_name_line = QLineEdit()
students_name_line.setPlaceholderText("Name")
students_surname_line = QLineEdit()
students_surname_line.setPlaceholderText("Surname")
lines_layout = QHBoxLayout()
lines_layout.addWidget(students_name_line,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
lines_layout.addWidget(students_surname_line,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
okay_button = QPushButton("Ok")
okay_button.setMinimumSize(180,20)
okay_button.setMaximumSize(180,20)
okay_button.setFont(basic_font)
Add_student_window_layout = QVBoxLayout()
Add_student_window_layout.addWidget(add_or_rename_student_title,alignment=Qt.AlignHCenter)
Add_student_window_layout.addLayout(lines_layout)
Add_student_window_layout.addWidget(okay_button,alignment=Qt.AlignHCenter)

add_or_rename_student_window.setLayout(Add_student_window_layout)
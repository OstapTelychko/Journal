from Window_layouts.main_window_layout import title_font,basic_font,Icon,QScrollArea,Qt,QHBoxLayout,QVBoxLayout,QPushButton,QWidget,QLabel

#Joint and today's lesson window
joint_and_todays_lesson_window = QWidget()
joint_and_todays_lesson_window.resize(700,500)
joint_and_todays_lesson_window.setWindowIcon(Icon)
joint_and_todays_lesson_window.setObjectName("main_window")
##Joint and today's lesson window layout
###Joint lessons layout
joint_lessons_title = QLabel("Joint lesson with:")
joint_lessons_title.setFont(title_font)
####Scroll joint lessons area
Scroll_joint_lessons_layout = QVBoxLayout()
Scroll_joint_lessons_window = QWidget()
Scroll_joint_lessons_window.setLayout(Scroll_joint_lessons_layout)
Scroll_joint_lessons_window.setObjectName("lesson_window")
Scroll_joint_lessons_area = QScrollArea()
Scroll_joint_lessons_area.setWidget(Scroll_joint_lessons_window)
Scroll_joint_lessons_area.setWidgetResizable(True)
Scroll_joint_lessons_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
Scroll_joint_lessons_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
Scroll_joint_lessons_area.setMinimumWidth(300)
joint_lessons_layout = QVBoxLayout()
joint_lessons_layout.addWidget(joint_lessons_title,alignment=Qt.AlignLeft)
joint_lessons_layout.addWidget(Scroll_joint_lessons_area,alignment=Qt.AlignLeft)
###Today's lessons layout
todays_lessons_title = QLabel("Today's lessons with:")
todays_lessons_title.setFont(title_font)
####Scroll today's lessons area
Scroll_todays_lessons_layout = QVBoxLayout()
Scroll_todays_lessons_window = QWidget()
Scroll_todays_lessons_window.setLayout(Scroll_todays_lessons_layout)
Scroll_todays_lessons_window.setObjectName("lesson_window")
Scroll_todays_lessons_area = QScrollArea()
Scroll_todays_lessons_area.setWidget(Scroll_todays_lessons_window)
Scroll_todays_lessons_area.setWidgetResizable(True)
Scroll_todays_lessons_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
Scroll_todays_lessons_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
delete_lesson_button = QPushButton("Delete lesson")
delete_lesson_button.setMinimumSize(180,20)
delete_lesson_button.setMaximumSize(180,20)
delete_lesson_button.setFont(basic_font)
todays_lessons_layout = QVBoxLayout()
todays_lessons_layout.addWidget(todays_lessons_title,alignment=Qt.AlignRight)
todays_lessons_layout.addWidget(Scroll_todays_lessons_area,alignment=Qt.AlignRight)
todays_lessons_layout.addWidget(delete_lesson_button,alignment=Qt.AlignRight)
#Joint and today's lesson window layout
joint_and_todays_lesson_window_layout = QHBoxLayout()
joint_and_todays_lesson_window_layout.addLayout(joint_lessons_layout)
joint_and_todays_lesson_window_layout.addLayout(todays_lessons_layout)

joint_and_todays_lesson_window.setLayout(joint_and_todays_lesson_window_layout)
import datetime
import json
import os


from Window_layouts.main_window_layout import*
from Window_layouts.switch_language_window_layout import*
from Window_layouts.add_or_rename_student_window_layout import*
from Window_layouts.error_windows import*
from Window_layouts.add_lesson_window_layout import*
from Window_layouts.joint_and_todays_lessons_window_layout import*
from language_packs import Languages
from Themes.black_theme import black_theme
from Themes.white_theme import white_theme
def find_file(file:str) -> str:
    "Return path to file"
    Path = os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),file).replace("\\","/")
    return Path if os.path.exists(Path) else print(f"[ERROR] File {Path} doesn't exist [ERROR]")


language = None
theme = None
active_date = None
active_student = None
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_lists = [january_activity_list,february_activity_list,march_activity_list,april_activity_list,may_activity_list,june_activity_list,july_activity_list,august_activity_list,september_activity_list,october_activity_list,november_activity_list,december_activity_list]
buttons_list = [add_activity_to_january_button,add_activity_to_february_button,add_activity_to_march_button,add_activity_to_april_button,add_activity_to_may_button,add_activity_to_june_button,add_activity_to_july_button,add_activity_to_august_button,add_activity_to_september_button,add_activity_to_october_button,add_activity_to_november_button,add_activity_to_december_button]
actual_year = datetime.datetime.now().strftime("%Y")
active_year = actual_year
joint_lesson = []
joint_lesson_windows = []
todays_lesson_windows = []
#Application
def add_lesson_to_list(list:QListWidget,day:str,hour:str,date:str|int):
    if language == "English":
        if day == ["Monday","Понеділок"]:
            list.addItem("Monday        "+hour+"          "+date)
        if day == ["Tuesday","Вівторок"]:
            list.addItem("Tuesday        "+hour+"          "+date)
        if day == ["Wednesday","Середа"]:
            list.addItem("Wednesday   "+hour+"          "+date)
        if day == ["Thursday","Четвер"]:
            list.addItem("Thursday       "+hour+"         "+date)
        if day == ["Friday","П'ятниця"]:
            list.addItem("Friday            "+hour+"          "+date)
        if day == ["Saturday","Субота"]:
            list.addItem("Saturday       "+hour+"          "+date)
        if day == ["Sunday","Неділя"]:
            list.addItem("Sunday          "+hour+"          "+date)
    else:
        if day == ["Monday","Понеділок"]:
            list.addItem("Понеділок  "+hour+"          "+date)
        if day == ["Tuesday","Вівторок"]:
            list.addItem("Вівторок     "+hour+"          "+date)
        if day == ["Wednesday","Середа"]:
            list.addItem("Середа       "+hour+"          "+date)
        if day == ["Thursday","Четвер"]:
            list.addItem("Четвер       "+hour+"          "+date)
        if day == ["Friday","П'ятниця"]:
            list.addItem("П'ятниця     "+hour+"          "+date)
        if day == ["Saturday","Субота"]:
            list.addItem("Субота        "+hour+"          "+date)
        if day == ["Sunday","Неділя"]:
            list.addItem("Неділя        "+hour+"          "+date)
def update_students_list():
    students_list.clear()
    all_students = [student for student in students]
    all_students.sort()
    students_list.addItems(all_students)
def change_language(chosen_language:str):
    "Changes the text on each button label and list"
    global theme,language
    language = chosen_language
    #Main window
    students_list_title.setText(Languages[language]["main window"]["managment of students list and info"][0])
    add_student_button.setText(Languages[language]["main window"]["managment of students list and info"][1])
    delete_student_button.setText(Languages[language]["main window"]["managment of students list and info"][2])
    rename_student_button.setText(Languages[language]["main window"]["managment of students list and info"][3])
    january_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    january_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    january_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    january_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    january_title.setText(Languages[language]["main window"]["Student's annual activity"]["January"][0])
    add_activity_to_january_button.setText(Languages[language]["main window"]["Student's annual activity"]["January"][1])
    february_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    february_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    february_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    february_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    february_title.setText(Languages[language]["main window"]["Student's annual activity"]["February"][0])
    add_activity_to_february_button.setText(Languages[language]["main window"]["Student's annual activity"]["February"][1])
    march_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    march_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    march_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    march_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    march_title.setText(Languages[language]["main window"]["Student's annual activity"]["March"][0])
    add_activity_to_march_button.setText(Languages[language]["main window"]["Student's annual activity"]["March"][1])
    april_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    april_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    april_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    april_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    april_title.setText(Languages[language]["main window"]["Student's annual activity"]["April"][0])
    add_activity_to_april_button.setText(Languages[language]["main window"]["Student's annual activity"]["April"][1])
    may_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    may_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    may_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    may_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    may_title.setText(Languages[language]["main window"]["Student's annual activity"]["May"][0])
    add_activity_to_may_button.setText(Languages[language]["main window"]["Student's annual activity"]["May"][1])
    june_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    june_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    june_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    june_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    june_title.setText(Languages[language]["main window"]["Student's annual activity"]["June"][0])
    add_activity_to_june_button.setText(Languages[language]["main window"]["Student's annual activity"]["June"][1])
    july_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    july_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    july_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    july_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    july_title.setText(Languages[language]["main window"]["Student's annual activity"]["July"][0])
    add_activity_to_july_button.setText(Languages[language]["main window"]["Student's annual activity"]["July"][1])
    august_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    august_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    august_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    august_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    august_title.setText(Languages[language]["main window"]["Student's annual activity"]["August"][0])
    add_activity_to_august_button.setText(Languages[language]["main window"]["Student's annual activity"]["August"][1])
    september_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    september_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    september_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    september_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    september_title.setText(Languages[language]["main window"]["Student's annual activity"]["September"][0])
    add_activity_to_september_button.setText(Languages[language]["main window"]["Student's annual activity"]["September"][1])
    october_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    october_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    october_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    october_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    october_title.setText(Languages[language]["main window"]["Student's annual activity"]["October"][0])
    add_activity_to_october_button.setText(Languages[language]["main window"]["Student's annual activity"]["October"][1])
    november_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    november_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    november_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    november_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    november_title.setText(Languages[language]["main window"]["Student's annual activity"]["November"][0])
    add_activity_to_november_button.setText(Languages[language]["main window"]["Student's annual activity"]["November"][1])
    december_day_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][0])
    december_hour_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][1])
    december_date_title.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][2])
    december_total_lessons_amount.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][3])
    december_title.setText(Languages[language]["main window"]["Student's annual activity"]["December"][0])
    add_activity_to_december_button.setText(Languages[language]["main window"]["Student's annual activity"]["December"][1])
    #Main window errors
    student_exists_error.setText(Languages[language]["add or rename student window"]["errors"][0])
    not_enough_information_error.setText(Languages[language]["add or rename student window"]["errors"][1])
    unselected_student_error.setText(Languages[language]["main window"]["error"])
    student_remove_warning.button(QMessageBox.StandardButton.Ok).setText(Languages[language]["add or rename student window"]["Ok button"])
    student_remove_warning.button(QMessageBox.StandardButton.Cancel).setText(Languages[language]["add lesson window"]["warning"]["buttons"][1])
    lesson_remove_warning.button(QMessageBox.StandardButton.Ok).setText(Languages[language]["add or rename student window"]["Ok button"])
    lesson_remove_warning.button(QMessageBox.StandardButton.Cancel).setText(Languages[language]["add lesson window"]["warning"]["buttons"][1])
    #Switch language window
    Switch_languages_button.setText(Languages[language]["switch language window"][0])
    choose_language_title.setText(Languages[language]["switch language window"][0])
    #Add or rename student window
    add_or_rename_student_title.setText(Languages[language]["add or rename student window"]["titles"][0])
    students_name_line.setPlaceholderText(Languages[language]["add or rename student window"]["Placeholders"][0])
    students_surname_line.setPlaceholderText(Languages[language]["add or rename student window"]["Placeholders"][1])
    okay_button.setText(Languages[language]["add or rename student window"]["Ok button"])
    #Translate days of week
    if len(students_list.selectedItems()):
        show_student_annual_activity(students_list.selectedItems()[0].text())
    #Add lesson window
    add_lesson_title.setText(Languages[language]["add lesson window"]["title"])
    add_lesson_example.setText(Languages[language]["add lesson window"]["example"])
    hour_line.setPlaceholderText(Languages[language]["add lesson window"]["Placeholders"][0])
    minute_line.setPlaceholderText(Languages[language]["add lesson window"]["Placeholders"][1])
    date_line.setPlaceholderText(Languages[language]["add lesson window"]["Placeholders"][2])
    add_lesson_button.setText(Languages[language]["add lesson window"]["Placeholders"][3])
    #Add lesson errors
    entered_incorrect_type_of_information_error.setText(Languages[language]["add lesson window"]["errors"][0])
    entered_incorrect_time_amount_error.setText(Languages[language]["add lesson window"]["errors"][4])
    student_has_this_lesson_error.setText(Languages[language]["add lesson window"]["errors"][5])
    #Add lesson warning
    add_student_warning_title.setText(Languages[language]["add lesson window"]["warning"]["warning title"])
    agree_button.setText(Languages[language]["add lesson window"]["warning"]["buttons"][0])
    disagree_button.setText(Languages[language]["add lesson window"]["warning"]["buttons"][1])
    #Joint and today's lesson window
    joint_lessons_title.setText(Languages[language]["joint and today's lesson window"][0])
    todays_lessons_title.setText(Languages[language]["joint and today's lesson window"][1])
    delete_lesson_button.setText(Languages[language]["joint and today's lesson window"][2])
    with open(find_file("active_settings.json"),"w",encoding="utf-8") as file:
        json.dump({"language":language,"theme":theme},file,ensure_ascii=False,indent=4)
    switch_window.hide()
def add_student():
    "Add a new student to list"
    global students,active_student
    if students_name_line.text() != "" and students_surname_line.text() != "":
        new_student = f"{students_name_line.text()} {students_surname_line.text()}"
        if new_student not in students:
            students[new_student] = {actual_year:{}}
            for month in months_list:
                students[new_student][actual_year][month] = {}
            update_students_list()
            with open(find_file("students.json"),"w",encoding="utf-8") as file:
                json.dump(students,file,indent=4,ensure_ascii=False)
                active_student = new_student
            for button in buttons_list:
                button.setDisabled(False)
            delete_lesson_button.setDisabled(False)
            add_or_rename_student_window.hide()
        else:
            student_exists_error.exec()
    else:
        not_enough_information_error.exec()
def show_add_student_window():
    okay_button.disconnect()
    add_or_rename_student_title.setText(Languages[language]["add or rename student window"]["titles"][0])
    okay_button.clicked.connect(add_student)
    add_or_rename_student_window.show()
def delete_student():
    "Delete a student from list"
    global students
    if len(students_list.selectedItems()):
        student_to_delete = students_list.selectedItems()[0].text()
        student_remove_warning.setText(Languages[language]["main window"]["warnings"][0]+" "+student_to_delete+"?")
        result = student_remove_warning.exec()
        if result == QMessageBox.Ok:
            del students[student_to_delete]
            update_students_list()
            with open(find_file("students.json"),"w",encoding="utf-8") as file:
                json.dump(students,file,indent=4,ensure_ascii=False)
    else:
        unselected_student_error.exec()
def show_rename_window():
    "Show a rename window"
    global student_to_rename
    if len(students_list.selectedItems()):
        student_to_rename = students_list.selectedItems()[0].text()
        students_name_line.setText(student_to_rename.split()[0])
        students_surname_line.setText(student_to_rename.split()[1])
        add_or_rename_student_title.setText(Languages[language]["add or rename student window"]["titles"][1])
        okay_button.disconnect()
        okay_button.clicked.connect(rename_student)
        add_or_rename_student_window.show()
    else:
        unselected_student_error.exec()
def rename_student():
    "Rename a student"
    global students,student_to_rename
    new_student_name = students_name_line.text()+" "+students_surname_line.text()
    if student_to_rename != new_student_name and new_student_name not in students:
        students_dictionary_with_renamed_student = {}
        for student_name,value in students.items():
            students_dictionary_with_renamed_student[student_name.replace(student_to_rename,new_student_name)]=value
        students = students_dictionary_with_renamed_student
        students_name_line.clear()
        students_surname_line.clear()
        student_to_rename = None
        add_or_rename_student_window.hide()
        update_students_list()
        with open(find_file("students.json"),"w",encoding="utf-8") as file:
            json.dump(students,file,indent=4,ensure_ascii=False)
    else:
        student_exists_error.exec()
def show_student_annual_activity(student):
    global active_student,students
    for button in buttons_list:
        button.setDisabled(False)
    delete_lesson_button.setDisabled(False)
    actual_year_title.setText(actual_year)
    if type(student) is not str:
        active_student = student.text()
    else:
        active_student = student
    if actual_year in students[active_student]:
        total_lessons_amount_per_year.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][4]+"0")
        for (month,month_list) in zip(months_list,months_lists):
            month_list.clear()
            #Add total lessons amount
            month_lessons_amount = len(students[active_student][actual_year][month].keys())
            current_lessons_amount = int(total_lessons_amount_per_year.text().split(":")[1]) if total_lessons_amount_per_year.text().split(":")[1] != "" else 0
            total_lessons_amount_per_year.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][4]+str(current_lessons_amount+month_lessons_amount))
            month_list.addItem("                                                            "+str(month_lessons_amount))
            if len(students[active_student][actual_year][month].keys()):
                #Adding lessons to lists
                for lesson in students[active_student][actual_year][month]:
                    day = students[active_student][actual_year][month][lesson]["Day"]
                    hour = students[active_student][actual_year][month][lesson]["Hour"]
                    date = students[active_student][actual_year][month][lesson]["Date"]
                    add_lesson_to_list(month_list,day,hour,date)
    else:
        students[active_student][actual_year] = {}
        for (month,month_list) in zip(months_list,months_lists):
            month_list.clear()
            students[active_student][actual_year][month] = {}
            month_list.addItem("                                                            "+str(len(students[active_student][actual_year][month].keys())))
        with open(find_file("students.json"),"w",encoding="utf-8") as file:
            json.dump(students,file,indent=4,ensure_ascii=False)

def show_add_lesson_window():
    global active_student,month_name
    if joint_and_todays_lesson_window.isHidden():
        if add_lesson_window.isHidden():
            for (month,button) in zip(months_list,buttons_list):
                if button.sender() == button:
                    month_name = month
            if len(students_list.selectedItems()):
                active_student = students_list.selectedItems()[0].text()
                if language == "English":
                    select_day_box.clear()
                    select_day_box.addItems(["","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
                else:
                    select_day_box.clear()
                    select_day_box.addItems(["","Понеділок","Вівторок","Середа","Четвер","П'ятниця","Субота","Неділя"])
                add_lesson_window.show()
            else:
                unselected_student_error.exec()
def add_lesson():
    global day_index,hour,date,day
    day = select_day_box.currentText()
    day_index=select_day_box.currentIndex()
    try:
        int(hour_line.text())
        int(minute_line.text())
        int(date_line.text())
    except ValueError:
        entered_incorrect_type_of_information_error.exec()
    else:
        hour = int(hour_line.text())
        minute = int(minute_line.text())
        date = int(date_line.text())
        months_index = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
        for month,index in months_index.items():
            if month_name == month:
                month_index = index
        try:
            weekday_index=datetime.date(int(actual_year),month_index,date).isocalendar()[2]
        except ValueError:
            if date >=0:
                entered_incorrect_date_error.setText(Languages[language]["add lesson window"]["errors"][1])
            else:
                entered_incorrect_date_error.setText(Languages[language]["add lesson window"]["errors"][2])
            entered_incorrect_date_error.exec()
        else:
            if day_index == weekday_index:
                if  0 < hour < 24 and -1 < minute < 60:
                    lesson_exists = False
                    # students_amount = len(students)
                    hour = f"0{str(hour)}:0{str(minute)}" if hour < 10 and minute < 10 else f"0{str(hour)}:{str(minute)}" if hour < 10 else f"{str(hour)}:0{str(minute)}"if minute < 10 else f"{str(hour)}:{str(minute)}"
                    date = str(date)
                    joint_lesson.clear()
                    for student in students:
                        if len(students[student][actual_year][month_name]):
                            #Check if student already has this lesson
                            if student == active_student:
                                for lesson in students[student][actual_year][month_name]:
                                    if date == students[student][actual_year][month_name][lesson]["Date"] and day in students[student][actual_year][month_name][lesson]["Day"] and hour == students[student][actual_year][month_name][lesson]["Hour"]:
                                        return student_has_this_lesson_error.exec()
                            else:
                                #Check if another student has a lesson on the same day
                                for lesson in students[student][actual_year][month_name]:
                                    if date == students[student][actual_year][month_name][lesson]["Date"] and day in students[student][actual_year][month_name][lesson]["Day"] and hour == students[student][actual_year][month_name][lesson]["Hour"]:
                                        joint_lesson.append(f"{student} {day} {hour} {date}")
                                        lesson_exists = True
                    if lesson_exists is False:
                        lesson_number = "lesson "+str(len(students[active_student][actual_year][month_name].keys()))
                        students[active_student][actual_year][month_name][lesson_number] = {
                            "Day":[Languages["English"]["add lesson window"]["day's index"][day_index],Languages["Українська"]["add lesson window"]["day's index"][day_index]],
                            "Hour":hour,
                            "Date":date
                        }
                        show_student_annual_activity(active_student)
                        add_lesson_window.hide()
                        with open(find_file("students.json"),"w",encoding="utf-8") as file:
                            json.dump(students,file,indent=4,ensure_ascii=False)
                    else:
                        show_add_student_to_joint_lesson_warning()
                else:
                    entered_incorrect_time_amount_error.exec()
            else:
                entered_incorrect_weekday_error.setText(Languages[language]["add lesson window"]["errors"][3]+Languages[language]["add lesson window"]["day's index"][weekday_index])
                entered_incorrect_weekday_error.exec()
def show_add_student_to_joint_lesson_warning():
    if len(joint_lesson_windows):
        for window in joint_lesson_windows:
            Scroll_students_layout.removeWidget(window)
        joint_lesson_windows.clear()
    for lesson in joint_lesson:
        lesson = lesson.split(" ")
        lesson_student = QLabel(lesson[0]+" "+lesson[1])
        lesson_student.setMinimumWidth(80)
        lesson_day = QLabel(lesson[2])
        lesson_day.setMinimumWidth(60)
        lesson_hour = QLabel(lesson[3])
        lesson_hour.setMinimumWidth(60)
        lesson_date = QLabel(lesson[4])
        lesson_layout = QHBoxLayout()
        lesson_layout.addWidget(lesson_student,alignment=Qt.AlignLeft | Qt.AlignTop)
        lesson_layout.addStretch(1)
        lesson_layout.addWidget(lesson_day,alignment=Qt.AlignHCenter | Qt.AlignTop)
        lesson_layout.addWidget(lesson_hour,alignment=Qt.AlignHCenter | Qt.AlignTop)
        lesson_layout.addWidget(lesson_date,alignment=Qt.AlignRight | Qt.AlignTop)
        lesson_window = QWidget()
        lesson_window.setLayout(lesson_layout)
        lesson_window.setMaximumHeight(35)
        lesson_window.setObjectName("lesson_window")
        Scroll_students_layout.addWidget(lesson_window)
        joint_lesson_windows.append(lesson_window)
    add_student_to_joint_lesson_warning.show()
def add_student_to_joint_lesson():
    global lesson_number,hour,date
    joint_lesson.append(f"{active_student} {day} {hour} {date}")
    #Add lessson
    lesson_number = "lesson "+str(len(students[active_student][actual_year][month_name].keys()))
    students[active_student][actual_year][month_name][lesson_number] = {
        "Day":[Languages["English"]["add lesson window"]["day's index"][day_index],Languages["Українська"]["add lesson window"]["day's index"][day_index]],
        "Hour":hour,
        "Date":date
    }
    for lesson_data in joint_lesson:
        lesson_data = lesson_data.split(" ")
        student = lesson_data[0]+" "+lesson_data[1]
        hour = lesson_data[3]
        for lesson in students[student][actual_year][month_name]:
            if len(students[student][actual_year][month_name][lesson].keys()) != 4:
                students[student][actual_year][month_name][lesson]["joint lesson"] = []
            if students[student][actual_year][month_name][lesson]["Hour"] == hour:
                for lesson_to_add_data in joint_lesson:
                    lesson_info = lesson_to_add_data.split(" ")
                    student_to_add = lesson_info[0]+" "+lesson_info[1]
                    if student_to_add != student and lesson_to_add_data not in students[student][actual_year][month_name][lesson]["joint lesson"]:
                        students[student][actual_year][month_name][lesson]["joint lesson"].append(lesson_to_add_data)
                with open(find_file("students.json"),"w",encoding="utf-8") as file:
                    json.dump(students,file,indent=4,ensure_ascii=False)
    add_student_to_joint_lesson_warning.hide()
    add_lesson_window.hide()
    show_student_annual_activity(active_student)
def show_joint_and_daily_lessons(lesson):
    global month_name,lesson_text
    month_name = "January" if lesson.listWidget()==january_activity_list else "February" if lesson.listWidget() == february_activity_list else "March" if lesson.listWidget() == march_activity_list  else "April" if lesson.listWidget() == april_activity_list else "May" if lesson.listWidget() == may_activity_list else "June" if lesson.listWidget() == june_activity_list else "July" if lesson.listWidget() == july_activity_list else "August"if lesson.listWidget() == august_activity_list else "September" if lesson.listWidget() == september_activity_list else "October" if lesson.listWidget() == october_activity_list else "November" if lesson.listWidget() == november_activity_list else "December"
    if len(joint_lesson_windows):
        for window in joint_lesson_windows:
            Scroll_joint_lessons_layout.removeWidget(window)
        joint_lesson_windows.clear()
    if len(todays_lesson_windows):
        for window in todays_lesson_windows:
            Scroll_todays_lessons_layout.removeWidget(window)
        todays_lesson_windows.clear()
    lesson.setSelected(False)
    lesson_text = lesson.text()
    lesson = lesson.text().split()
    day = lesson[0]
    hour = lesson[1]
    date = lesson[2]
    for student_lesson in students[active_student][actual_year][month_name]:
        if students[active_student][actual_year][month_name][student_lesson]["Date"] == date and len(students[active_student][actual_year][month_name][student_lesson].keys()) == 4 and students[active_student][actual_year][month_name][student_lesson]["Hour"] == hour:
            for joint_lesson in students[active_student][actual_year][month_name][student_lesson]["joint lesson"]:
                joint_lesson = joint_lesson.split(" ")
                lesson_student = QLabel(joint_lesson[0]+" "+joint_lesson[1])
                lesson_student.setMinimumWidth(80)
                lesson_day = QLabel(day)
                lesson_day.setMinimumWidth(60)
                lesson_hour = QLabel(hour)
                lesson_hour.setMinimumWidth(60)
                lesson_date = QLabel(date)
                lesson_layout = QHBoxLayout()
                lesson_layout.addWidget(lesson_student,alignment=Qt.AlignLeft | Qt.AlignTop)
                lesson_layout.addStretch(1)
                lesson_layout.addWidget(lesson_day,alignment=Qt.AlignHCenter | Qt.AlignTop)
                lesson_layout.addWidget(lesson_hour,alignment=Qt.AlignHCenter | Qt.AlignTop)
                lesson_layout.addWidget(lesson_date,alignment=Qt.AlignRight | Qt.AlignTop)
                lesson_window = QWidget()
                lesson_window.setLayout(lesson_layout)
                lesson_window.setMaximumHeight(35)
                lesson_window.setObjectName("lesson_window")
                Scroll_joint_lessons_layout.addWidget(lesson_window)
                joint_lesson_windows.append(lesson_window)
    for student in students:
        for student_lesson in students[student][actual_year][month_name]:
            if students[student][actual_year][month_name][student_lesson]["Date"] == date:
                lesson_student = QLabel(student)
                lesson_student.setMinimumWidth(80)
                lesson_day = QLabel(day)
                lesson_day.setMinimumWidth(60)
                lesson_hour = QLabel(students[student][actual_year][month_name][student_lesson]["Hour"])
                lesson_hour.setMinimumWidth(60)
                lesson_date = QLabel(date)
                lesson_layout = QHBoxLayout()
                lesson_layout.addWidget(lesson_student,alignment=Qt.AlignLeft | Qt.AlignTop)
                lesson_layout.addStretch(1)
                lesson_layout.addWidget(lesson_day,alignment=Qt.AlignHCenter | Qt.AlignTop)
                lesson_layout.addWidget(lesson_hour,alignment=Qt.AlignHCenter | Qt.AlignTop)
                lesson_layout.addWidget(lesson_date,alignment=Qt.AlignRight | Qt.AlignTop)
                lesson_window = QWidget()
                lesson_window.setLayout(lesson_layout)
                lesson_window.setMaximumHeight(35)
                lesson_window.setObjectName("lesson_window")
                Scroll_todays_lessons_layout.addWidget(lesson_window)
                todays_lesson_windows.append(lesson_window)
    joint_and_todays_lesson_window.show()
def show_last_or_next_year():
    global active_year
    if len(students_list.selectedItems()):
        if str(int(active_year)-1 if previous_year_button.sender()==previous_year_button else int(active_year)+1) in students[active_student]:
            active_year = str(int(active_year)-1 if previous_year_button.sender()==previous_year_button else int(active_year)+1)
            actual_year_title.setText(active_year)
            total_lessons_amount_per_year.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][4]+"0")
            for (month,month_list) in zip(months_list,months_lists):
                month_list.clear()
                #Add total lessons amount
                month_lessons_amount = len(students[active_student][actual_year][month].keys())
                current_lessons_amount = int(total_lessons_amount_per_year.text().split(":")[1]) if total_lessons_amount_per_year.text().split(":")[1] != "" else 0
                total_lessons_amount_per_year.setText(Languages[language]["main window"]["Student's annual activity"]["Global"][4]+str(current_lessons_amount+month_lessons_amount))
                month_list.addItem("                                                            "+str(month_lessons_amount))
                if len(students[active_student][active_year][month].keys()):
                    #Adding lessons to lists
                    for lesson in students[active_student][active_year][month]:
                        day = students[active_student][active_year][month][lesson]["Day"]
                        hour = students[active_student][active_year][month][lesson]["Hour"]
                        date = students[active_student][active_year][month][lesson]["Date"]
                        add_lesson_to_list(month_list,day,hour,date)
            #Disable buttons
            for button in buttons_list:
                button.setDisabled(True)
            delete_lesson_button.setDisabled(True)
    else:
        unselected_student_error.exec()
def switch_theme():
    global theme
    if theme == "Black":
        theme = "White"
        Switch_themes_button.setIcon(QIcon(find_file("Images/black_theme.png")))
        switch_window.setStyleSheet(white_theme)
        main_window.setStyleSheet(white_theme)
        add_or_rename_student_window.setStyleSheet(white_theme)
        not_enough_information_error.setStyleSheet(white_theme)
        student_exists_error.setStyleSheet(white_theme)
        unselected_student_error.setStyleSheet(white_theme)
        student_remove_warning.setStyleSheet(white_theme)
        add_lesson_window.setStyleSheet(white_theme)
        entered_incorrect_date_error.setStyleSheet(white_theme)
        entered_incorrect_type_of_information_error.setStyleSheet(white_theme)
        entered_incorrect_weekday_error.setStyleSheet(white_theme)
        add_student_to_joint_lesson_warning.setStyleSheet(white_theme)
        entered_incorrect_time_amount_error.setStyleSheet(white_theme)
        student_has_this_lesson_error.setStyleSheet(white_theme)
        joint_and_todays_lesson_window.setStyleSheet(white_theme)
        lesson_remove_warning.setStyleSheet(white_theme)
    else:
        theme = "Black"
        Switch_themes_button.setIcon(QIcon(find_file("Images/white_theme.png")))
        switch_window.setStyleSheet(black_theme)
        main_window.setStyleSheet(black_theme)
        add_or_rename_student_window.setStyleSheet(black_theme)
        not_enough_information_error.setStyleSheet(black_theme)
        student_exists_error.setStyleSheet(black_theme)
        unselected_student_error.setStyleSheet(black_theme)
        student_remove_warning.setStyleSheet(black_theme)
        add_lesson_window.setStyleSheet(black_theme)
        entered_incorrect_date_error.setStyleSheet(black_theme)
        entered_incorrect_type_of_information_error.setStyleSheet(black_theme)
        entered_incorrect_weekday_error.setStyleSheet(black_theme)
        add_student_to_joint_lesson_warning.setStyleSheet(black_theme)
        entered_incorrect_time_amount_error.setStyleSheet(black_theme)
        student_has_this_lesson_error.setStyleSheet(black_theme)
        joint_and_todays_lesson_window.setStyleSheet(black_theme)
        lesson_remove_warning.setStyleSheet(black_theme)
    with open(find_file("active_settings.json"),"w",encoding="utf-8") as file:
        json.dump({"language":language,"theme":theme},file,indent=4,ensure_ascii=False)
def delete_lesson():
    global lesson_text
    lesson_remove_warning.setText(Languages[language]["main window"]["warnings"][1]+lesson_text+"?")
    result = lesson_remove_warning.exec()
    if result == QMessageBox.Ok:
        #Delete lesson from student lesson list
        lesson_text = lesson_text.split()
        day = lesson_text[0]
        hour = lesson_text[1]
        date = lesson_text[2]
        for lesson in students[active_student][actual_year][month_name].copy():
            if students[active_student][actual_year][month_name][lesson]["Hour"] == hour and students[active_student][actual_year][month_name][lesson]["Date"] == date:
                if len(students[active_student][actual_year][month_name][lesson].keys())==4:
                    #Delete lesson from joint lesson, if the lesson is there
                    for joint_lesson in students[active_student][actual_year][month_name][lesson]["joint lesson"]:
                        student = joint_lesson.split()[0]+" "+joint_lesson.split()[1]
                        for student_lesson in students[student][actual_year][month_name]:
                            if students[student][actual_year][month_name][student_lesson]["Hour"] == hour and students[student][actual_year][month_name][lesson]["Date"] == date:
                                for student_joint_lesson in students[student][actual_year][month_name][student_lesson]["joint lesson"]:
                                    if student_joint_lesson.split(" ")[0]+" "+student_joint_lesson.split(" ")[1] == active_student:
                                        lesson_to_delete=students[student][actual_year][month_name][student_lesson]["joint lesson"].index(student_joint_lesson)
                                        del students[student][actual_year][month_name][student_lesson]["joint lesson"][lesson_to_delete]
                                    if len(students[student][actual_year][month_name][student_lesson]["joint lesson"]) == 0:
                                        del students[student][actual_year][month_name][student_lesson]["joint lesson"]
                del students[active_student][actual_year][month_name][lesson]
        joint_and_todays_lesson_window.hide()
        show_student_annual_activity(active_student)
        with open(find_file("students.json"),"w",encoding="utf-8") as file:
            json.dump(students,file,indent=4,ensure_ascii=False)

if __name__ == "__main__":
    with open(find_file("active_settings.json"),encoding="utf-8") as file:
        active_settings = json.load(file)
    theme = active_settings["theme"]
    language = active_settings["language"]
    with open(find_file("students.json"),encoding="utf-8") as file:
        students = json.load(file)
    if language != "English":
        languages_list.clear()
        languages_list.addItems(("Українська","English"))
    change_language(language)
    if theme == "Black":
        Switch_themes_button.setIcon(QIcon(find_file("Images/white_theme.png")))
        switch_window.setStyleSheet(black_theme)
        main_window.setStyleSheet(black_theme)
        add_or_rename_student_window.setStyleSheet(black_theme)
        not_enough_information_error.setStyleSheet(black_theme)
        student_exists_error.setStyleSheet(black_theme)
        unselected_student_error.setStyleSheet(black_theme)
        student_remove_warning.setStyleSheet(black_theme)
        add_lesson_window.setStyleSheet(black_theme)
        entered_incorrect_date_error.setStyleSheet(black_theme)
        entered_incorrect_type_of_information_error.setStyleSheet(black_theme)
        entered_incorrect_weekday_error.setStyleSheet(black_theme)
        add_student_to_joint_lesson_warning.setStyleSheet(black_theme)
        entered_incorrect_time_amount_error.setStyleSheet(black_theme)
        student_has_this_lesson_error.setStyleSheet(black_theme)
        joint_and_todays_lesson_window.setStyleSheet(black_theme)
        lesson_remove_warning.setStyleSheet(black_theme)
    else:
        Switch_themes_button.setIcon(QIcon(find_file("Images/black_theme.png")))
        switch_window.setStyleSheet(white_theme)
        main_window.setStyleSheet(white_theme)
        add_or_rename_student_window.setStyleSheet(white_theme)
        not_enough_information_error.setStyleSheet(white_theme)
        student_exists_error.setStyleSheet(white_theme)
        unselected_student_error.setStyleSheet(white_theme)
        student_remove_warning.setStyleSheet(white_theme)
        add_lesson_window.setStyleSheet(white_theme)
        entered_incorrect_date_error.setStyleSheet(white_theme)
        entered_incorrect_type_of_information_error.setStyleSheet(white_theme)
        entered_incorrect_weekday_error.setStyleSheet(white_theme)
        add_student_to_joint_lesson_warning.setStyleSheet(white_theme)
        entered_incorrect_time_amount_error.setStyleSheet(white_theme)
        student_has_this_lesson_error.setStyleSheet(white_theme)
        joint_and_todays_lesson_window.setStyleSheet(white_theme)
        lesson_remove_warning.setStyleSheet(white_theme)
    update_students_list()
    main_window.setWindowTitle(Languages[language]["app name"])
    switch_window.setWindowTitle(Languages[language]["app name"])
    add_or_rename_student_window.setWindowTitle(Languages[language]["app name"])
    add_lesson_window.setWindowTitle(Languages[language]["app name"])
    not_enough_information_error.setWindowTitle(Languages[language]["app name"])
    student_exists_error.setWindowTitle(Languages[language]["app name"])
    unselected_student_error.setWindowTitle(Languages[language]["app name"])
    entered_incorrect_type_of_information_error.setWindowTitle(Languages[language]["app name"])
    entered_incorrect_date_error.setWindowTitle(Languages[language]["app name"])
    entered_incorrect_weekday_error.setWindowTitle(Languages[language]["app name"])
    student_remove_warning.setWindowTitle(Languages[language]["app name"])
    add_student_to_joint_lesson_warning.setWindowTitle(Languages[language]["app name"])
    entered_incorrect_time_amount_error.setWindowTitle(Languages[language]["app name"])
    student_has_this_lesson_error.setWindowTitle(Languages[language]["app name"])
    joint_and_todays_lesson_window.setWindowTitle(Languages[language]["app name"])
    lesson_remove_warning.setWindowTitle(Languages[language]["app name"])
    main_window.show()
    Switch_themes_button.clicked.connect(switch_theme)
    previous_year_button.clicked.connect(show_last_or_next_year)
    next_year_button.clicked.connect(show_last_or_next_year)
    Switch_languages_button.clicked.connect(switch_window.show)
    add_student_button.clicked.connect(show_add_student_window)
    delete_student_button.clicked.connect(delete_student)
    rename_student_button.clicked.connect(show_rename_window)
    add_lesson_button.clicked.connect(add_lesson)
    delete_lesson_button.clicked.connect(delete_lesson)
    agree_button.clicked.connect(add_student_to_joint_lesson)
    disagree_button.clicked.connect(add_student_to_joint_lesson_warning.hide)
    add_activity_to_january_button.clicked.connect(show_add_lesson_window)
    add_activity_to_february_button.clicked.connect(show_add_lesson_window)
    add_activity_to_march_button.clicked.connect(show_add_lesson_window)
    add_activity_to_april_button.clicked.connect(show_add_lesson_window)
    add_activity_to_may_button.clicked.connect(show_add_lesson_window)
    add_activity_to_june_button.clicked.connect(show_add_lesson_window)
    add_activity_to_july_button.clicked.connect(show_add_lesson_window)
    add_activity_to_august_button.clicked.connect(show_add_lesson_window)
    add_activity_to_september_button.clicked.connect(show_add_lesson_window)
    add_activity_to_october_button.clicked.connect(show_add_lesson_window)
    add_activity_to_november_button.clicked.connect(show_add_lesson_window)
    add_activity_to_december_button.clicked.connect(show_add_lesson_window)
    languages_list.currentTextChanged.connect(change_language)
    students_list.itemClicked.connect(show_student_annual_activity)
    january_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    february_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    march_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    april_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    may_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    june_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    july_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    august_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    september_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    october_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    november_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    december_activity_list.itemClicked.connect(show_joint_and_daily_lessons)
    app.exec()
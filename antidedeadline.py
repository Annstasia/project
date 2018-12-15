import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QAction
from PyQt5.QtGui import QIcon
from datetime import datetime
from PyQt5.QtCore import QDate
import json

class Show(QWidget):
    def __init__(self):
        super(Show, self).__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(826, 482)
        MainWindow.setStyleSheet('background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius: 1, '
                                 'fx:0.5, fy:0.511364, stop:0 rgba(255, 255, 0, 255), '
                                 'stop:0.778409 rgba(255, 185, 92, 255));')
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 10, 431, 301))
        self.calendarWidget.setStyleSheet('''QWidget{background-color: yellow; color: #7109aa};''')
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setToolTip('Нажмите на дату, расписание которой хотите увидеть')
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(510, 20, 301, 411))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setToolTip('Здесь будет показано расписание')
        self.listWidget.setStyleSheet('background-color: #FFFFFF;')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 390, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('background-color: yellow; color: green;')
        self.pushButton.setToolTip('Здесь можно добавить события. Отличительной особенностью\n'
                                   'событий является то, что они выполняются в обозначенный день\n'
                                   'а не к этому дню.\n'
                                   'События могут как добавить так и отнять время')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 340, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('background-color: yellow; color: red;')
        self.pushButton_2.setToolTip('Здесь можно добавить дедлайн.')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр событий"))
        self.pushButton.setText(_translate("MainWindow", "Добавить событие"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить дедлайн"))


class CreateDeadline(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(826, 482)
        MainWindow.setStyleSheet('background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius: 1, '
                                 'fx:0.5, fy:0.511364, stop:0 rgba(255, 255, 0, 255), '
                                 'stop:0.778409 rgba(255, 185, 92, 255));')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 420, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('background-color: yellow; color: green;')
        self.pushButton.setToolTip('Здесь можно добавить события. Отличительной особенностью\n'
                                   'событий является то, что они выполняются в обозначенный день\n'
                                   'а не к этому дню.\n'
                                   'События могут как добавить так и отнять время')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 420, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('background-color: yellow; color: blue;')
        self.pushButton_2.setToolTip('Здесь можно посмотреть ваше расписание на какой-либо день')
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 110, 431, 301))
        self.calendarWidget.setToolTip('Выберите дату дедлайна')
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet('''QWidget{background-color: yellow; color: #7109aa};''')
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 0, 825, 100))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setStyleSheet('background-color: white;')
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.setToolTip('Измените количество свободных часов на каждый день недели\n'
                                      'Формат ввода: hh, h, h.m, h:m, h:mm, hh:mm, hh.mm')
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 110, 191, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet('background-color: white;')
        self.lineEdit.setToolTip('Введите название задания')
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(470, 170, 191, 42))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setStyleSheet('background-color: white;')
        self.timeEdit.setToolTip('Введите время, которое вы отводите на выполнение задания')
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(470, 240, 191, 42))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet('background-color: white;')
        self.dateEdit.setToolTip('Введите дату, с каторой планируете начать выполнение дедлайна')
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 310, 191, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('background-color: white;')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить дедлайн"))
        self.pushButton.setText(_translate("MainWindow", "Добавить событие"))
        self.pushButton_2.setText(_translate("MainWindow", "Просмотр событий"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Пн"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Вт"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ср"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Чт"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Пт"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сб"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Вс"))
        self.pushButton_3.setText(_translate("MainWindow", "ОК"))


class CreateDevelopment(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(826, 482)
        MainWindow.setStyleSheet('background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius: 1, '
                                 'fx:0.5, fy:0.511364, stop:0 rgba(255, 255, 0, 255), '
                                 'stop:0.778409 rgba(255, 185, 92, 255));')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 10, 431, 301))
        self.calendarWidget.setToolTip('Выберите дату события')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet('background-color: yellow; color: #7109aa;')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 390, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('background-color: yellow; color: blue;')
        self.pushButton.setToolTip('Здесь можно посмотреть ваше расписание на какой-либо день')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 340, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('background-color: yellow; color: red;')
        self.pushButton_2.setToolTip('Здесь можно добавить дедлайн.')
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 100, 181, 71))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setToolTip('Введите время которое освободится/затратится из-за события\n'
                                   'Фромат ввода: hh, h, h.m, h:m, h:mm, hh:mm, hh.mm\n'
                                   'Если время затратится, то введите знак "-". Например, -3')
        self.lineEdit_2.setStyleSheet('background-color: white;')
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 20, 181, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip('Введите название события')
        self.lineEdit.setStyleSheet('background-color: white;')
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 190, 101, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('background-color: white;')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить событие"))
        self.pushButton.setText(_translate("MainWindow", "Просмотр событий"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить дедлайн"))
        self.pushButton_3.setText(_translate("MainWindow", "Ок"))


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = {}
        if os.path.exists(os.getcwd() + '\\table.txt'):
            table_clone = open(os.getcwd() + '\\table.txt', mode='r')
            tab = json.loads(table_clone.read())
            # print(tab)
            for i in tab:
                self.table[QDate.fromString(i, "dd/MM/yyyy")] = tab[i]
        self.developments = {}
        if os.path.exists(os.getcwd() + '\\developments.txt'):
            developments_clone = open(os.getcwd() + '\\table.txt', mode='r')
            dev = json.loads(developments_clone.read())
            for i in dev:
                self.developments[QDate.fromString(i, "dd/MM/yyyy")] = dev[i]
        self.free = {'Пн': '1', 'Вт': '1', 'Ср': '1', 'Чт': '1', 'Пт': '1', 'Сб': '1', 'Вс': '1'}
        self.deadlines = {}
        if os.path.exists(os.getcwd() + '\\deadlines.txt'):
            deadlines_clone = open(os.getcwd() + '\\deadlines.txt')
            dead = json.loads(deadlines_clone.read())
            for i in dead:
                self.deadlines[i] = [QDate.fromString(dead[i][0], "dd/MM/yyyy")] +\
                                    [QDate.fromString(dead[i][1], "dd/MM/yyyy")] + [dead[i][2]]

        self.showdeadlines()

    def showdeadlines(self):
        try:
            # Функция отвечает за отображения окна Просотр событий
            self.w1 = Show()
            self.w1.setWindowIcon(QIcon('icon.png'))
            self.w1.pushButton_2.clicked.connect(self.createdeadline)
            self.w1.pushButton_2.clicked.connect(self.w1.close)
            self.w1.pushButton.clicked.connect(self.createdevelopment)
            self.w1.pushButton.clicked.connect(self.w1.close)
            self.w1.calendarWidget.clicked.connect(self.show_list)
            self.w1.show()
        except Exception as e:
            print(e)

    def show_list(self):
        try:
            # Функция отвечает за вывод информации
            self.w1.listWidget.clear()
            # Добавляем в список значения, сосотящие из названия дедлайна и времени, которое
            # отводится на выполнения в каждый из дней
            if self.w1.calendarWidget.selectedDate() in self.table:
                for i in range(1, len(self.table[self.w1.calendarWidget.selectedDate()])):
                    name, number = self.table[self.w1.calendarWidget.selectedDate()][i]
                    self.w1.listWidget.addItem(
                        '{} {}:{}'.format(name, str(int(number) // 60).rjust(2, '0'),
                                          str(int(number) % 60).ljust(2, '0')))
            # Добавляем в список события
            if self.w1.calendarWidget.selectedDate() in self.developments:
                for i in range(len(self.developments[self.w1.calendarWidget.selectedDate()])):
                    name, number = self.developments[self.w1.calendarWidget.selectedDate()][i]
                    self.w1.listWidget.addItem(
                        'СОБЫТИЕ {} {}:{}'.format(name, str(int(number) // 60).rjust(2, '0'),
                                                  str(int(number) % 60).ljust(2, '0')))
        except Exception as e:
            print(e)

    def createdeadline(self):
        try:
            # Функция отвечает за отображение окна Создать дедалйн
            self.w2 = CreateDeadline()
            self.w2.setWindowIcon(QIcon('icon.png'))
            self.w2.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(self.free['Пн'])))
            self.w2.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(self.free['Вт'])))
            self.w2.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(self.free['Ср'])))
            self.w2.tableWidget_2.setItem(0, 3, QTableWidgetItem(str(self.free['Чт'])))
            self.w2.tableWidget_2.setItem(0, 4, QTableWidgetItem(str(self.free['Пт'])))
            self.w2.tableWidget_2.setItem(0, 5, QTableWidgetItem(str(self.free['Сб'])))
            self.w2.tableWidget_2.setItem(0, 6, QTableWidgetItem(str(self.free['Вс'])))
            self.w2.calendarWidget.setMinimumDate(datetime.today())
            self.w2.dateEdit.setMinimumDate(datetime.today())
            self.w2.pushButton_3.clicked.connect(self.deadlinedo)
            self.w2.pushButton_2.clicked.connect(self.showdeadlines)
            self.w2.pushButton_2.clicked.connect(self.w2.close)
            self.w2.pushButton.clicked.connect(self.createdevelopment)
            self.w2.pushButton.clicked.connect(self.w2.close)
            self.w2.show()
        except Exception as e:
            print(e)

    def createdevelopment(self):
        try:
            # Функция отвечает за отображение окна создать событие
            self.w3 = CreateDevelopment()
            self.w3.setWindowIcon(QIcon('icon.png'))
            self.w3.pushButton_2.clicked.connect(self.createdeadline)
            self.w3.pushButton_2.clicked.connect(self.w3.close)
            self.w3.pushButton.clicked.connect(self.showdeadlines)
            self.w3.pushButton.clicked.connect(self.w3.close)
            self.w3.pushButton_3.clicked.connect(self.developmentdo)
            self.w3.show()
        except Exception as e:
            print(e)

    def developmentdo(self):
        try:
            # Функция отвечает за обраюотку событий
            name = self.w3.lineEdit.text()
            number = (self.w3.lineEdit_2.text().replace('.', ':') + ':0').split(':')
            assert (number[0].isdigit() or number[0][0] == '-' and number[0][1:].isdigit())\
                   and number[1].isdigit() # Проверка корректности ввода
            if int(number[0]) >= 0:
                time = str(int(number[0]) * 60 + int(number[1]))
            else:
                time = str(int(number[0]) * 60 - int(number[1]))
            date = self.w3.calendarWidget.selectedDate()
            self.developments[date] = self.developments.get(date, []) + [[name, time]]
            if date not in self.table:
                # Записываем в self.table, заодно проверяем возможноть выполнения
                table_time = (self.free[date.toString('ddd')] + ':0').replace('.', ':').split(':')
                self.table[date] = [str(int(table_time[0]) * 60 + int(table_time[1]))]
                assert int(self.table[date][0]) + int(time) <= 1440
                if int(self.table[date][0]) + int(time) < 0:
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText('Не хватает времени.')
                    msg.setWindowTitle('Error')
                    msg.show()
                self.table[date][0] = str(int(self.table[date][0]) + int(time))
            else:
                self.table[date][0] = str(int(self.table[date][0]) + int(time))
                # Изменяем расписание
                if int(time) > 0 and self.table[date][0] == time:
                    self.plus(date)
                elif int(time) < 0 and int(self.table[date][0]) < 0:
                    self.minus(date)
        except AssertionError:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Невeрный формат или неправдоподобный ввод\n'
                        'Верный формат: 1.03 или -1:03, '
                        'где 1 - кол-во часов, 03 - кол-во минут ')
            msg.setWindowTitle('Error')
            msg.show()
        except Exception as e:
            print(e)

    def plus(self, date):
        # Переносим занятия с поздних дат на раннюю
        end = max(self.table.keys())
        swap = []
        for i in range(1, date.daysTo(end) + 1):
            day = date.addDays(i)
            if int(self.table[day][0]) > 0:
                break
            swap.append(day)
            for j in range(1, len(self.table[day])):
                # Проверяем с какой даты пользователь указал выполнение задания
                if self.deadlines[self.table[day][j][0]][1] <= date:
                    min_time = min(int(self.table[date][0]), int(self.table[day][j][1]))
                    self.table[date][0] = str(int(self.table[date][0]) - min_time)
                    self.table[day][j][1] = str(int(self.table[day][j][1]) - min_time)
                    self.table[day][0] = str(int(self.table[date][0]) + min_time)
                    for q in range(1, len(self.table[date])):
                        if self.table[day][j][0] == self.table[date][q][0]:
                            self.table[date][q][1] = str(int(self.table[date][q][1]) + min_time)
                            min_time = 0
                            break
                    if min_time != 0:
                        self.table[date].append([self.table[day][j][0], str(min_time)])
                    if self.table[day][j][1] == '0':
                        del self.table[day][j]
                    if self.table[date][0] == '0':
                        break
            if self.table[date][0] == '0':
                break
        # При переносе событий у других дней так же появилось свободное время
        for i in swap:
            self.plus(i)
        self.write()

    def minus(self, date):
        swap = []
        need = -int(self.table[date][0])
        for i in range(1, len(self.table[date])):
            # свобождаем день от занятий, пока не выйдем из минусового времени
            min_time = min(int(self.table[date][i][1]), need)
            self.table[date][0] = str(-need + min_time)
            swap.append(self.table[date][i][0])
            self.table[date][i][1] = str(int(self.table[date][i][1]) - min_time)
            self.deadlines[self.table[date][i][0]][-1] = \
                self.deadlines[self.table[date][i][0]][-1] + min_time
            if self.table[date][0] == '0':
                break
        # Удаленные занятия надо выполнить, распределяем их по дням
        for i in swap:
            self.control(i)

    def deadlinedo(self):
        try:
            # Функция обрабатывает значения окна создат дедлайн
            whenfree = [self.w2.tableWidget_2.item(0, i).text() for i in range(7)]
            # Проверка корректности аргументов
            assert all([i.replace('.', '').replace(':', '').isdigit() for i in whenfree])
            assert all([int(i) >= 0 for i in whenfree])
            self.free['Пн'] = whenfree[0]
            self.free['Вт'] = whenfree[1]
            self.free['Ср'] = whenfree[2]
            self.free['Чт'] = whenfree[3]
            self.free['Пт'] = whenfree[4]
            self.free['Сб'] = whenfree[5]
            self.free['Вс'] = whenfree[6]
            name = self.w2.lineEdit.text()
            # Имена не должны пересекаться
            if name in self.deadlines or name == '':
                i, okBtnPressed = QInputDialog.getText(
                    self, "Некорректное имя", "Введенное название уже занято или не было введено\n"
                                              "Введите корректное название")
                if okBtnPressed:
                    if i == '' or i in self.deadlines:
                        name = name + '(' + str(len(list(filter(lambda s: s[:len(name)] == name,
                                                                self.deadlines.keys()))) + 1)
                    else:
                        name = i
            time = int(self.w2.timeEdit.text().split(':')[0]
                       ) * 60 + int(self.w2.timeEdit.text().split(':')[1])
            end = self.w2.calendarWidget.selectedDate()
            start = self.w2.dateEdit.date()
            # Расширяем список обробатываемых дней
            if bool(self.table) == False:
                for i in range(start.daysTo(end) + 1):
                    free_time = (self.free[start.addDays(i).toString('ddd')] + ':0'
                                 ).replace('.', ':').split(':')
                    self.table[start.addDays(i)] = self.table.get(start.addDays(i), [str(
                            int(free_time[0]) * 60 + int(free_time[1]))])
            else:
                table_min, table_max = min(self.table.keys()), max(self.table.keys())
                if start < table_min:
                    for i in range(start.daysTo(table_min)):
                        free_time = (self.free[start.addDays(i).toString('ddd')] + ':0').replace('.', ':').split(':')
                        self.table[start.addDays(i)] = self.table.get(start.addDays(i), [str(
                            int(free_time[0]) * 60 + int(free_time[1]))])
                if table_max < end:
                    for i in range(table_max.daysTo(end)):
                        free_time = (self.free[table_max.addDays(i + 1).toString('ddd')] + ':0').replace('.', ':').split(':')
                        self.table[table_max.addDays(i + 1)] = self.table.get(table_max.addDays(i + 1), [str(
                            int(free_time[0]) * 60 + int(free_time[1]))])
            # Проверяем возможно ли уложиться в срок
            if sum(int(self.table[start.addDays(i)][0]) for i in range(start.daysTo(end))) < time:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Не хватает времени. \nОсвободите время на какой-нибудь'
                            ' день и попробуйте снова')
                msg.setWindowTitle('Error')
                msg.show()
            else:
                self.deadlines[name] = [end, start, time]
                self.control(name)
        except AssertionError as e:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Невeрный формат. \n'
                        'Верный формат: 1.03 или 1:03, '
                        'где 1 - кол-во часов, 03 - кол-во минут ')
            msg.setWindowTitle('Error')
            msg.show()
        except Exception as e:
            print(e)

    def control(self, name):
        try:
            # Собственно, распределитель дедлайнов
            end = self.deadlines[name][0]
            start = self.deadlines[name][1]
            time = self.deadlines[name][2]
            swap = []
            # Новый дедлайн забирает на свое выполнение свобдное время дня а также дедлайнов,
            # назначенных на более поздний срок. Дни сменяются от указнанного начала до конца
            for i in range(start.daysTo(end)):
                day = start.addDays(i)
                min_time = min(int(self.table[day][0]), time)
                self.table[day][0] = str(int(self.table[day][0]) - min_time)
                time -= min_time
                for j in range(1, len(self.table[day])):
                    if self.deadlines[self.table[day][j][0]][0] > end:
                        min_time2 = min(int(self.table[day][j][1]), time)
                        self.table[day][j][1] = str(int(self.table[day][j][1]) - min_time2)
                        self.deadlines[self.table[day][j][0]][-1] += min_time2
                        self.deadlines[self.table[day][j][0]][1] =\
                            self.deadlines[self.table[day][j][0]][1].addDays(1)
                        time -= min_time2
                        min_time += min_time2
                        swap.append(self.table[day][j][0])
                    if self.table[day][j][1] == '0':
                        del self.table[day][j]
                if min_time != 0:
                    self.table[day].append([name, str(min_time)])
                sorted_day = sorted(self.table[day][1:], key=lambda s: self.deadlines[s[0]][0])
                self.table[day] = [self.table[day][0]] + sorted_day
                if time == 0:
                    break
            self.deadlines[name][0] = end
            self.deadlines[name][1] = start
            self.deadlines[name][2] = time
            # Смещенные дедлайны распределяются на свободные дни
            for i in swap:
                self.control(i)
            self.write()
        except Exception as e:
            print(e)

    def write(self):
        # Функция отвечает за сохранение данных после закрытия
        table = open('table.txt', mode='w')
        deadlines = open('deadlines.txt', mode='w')
        table_clone, developments_clone, deadlines_clone = {}, {}, {}
        for i in self.table:
            table_clone[i.toString('dd/MM/yyyy')] = self.table[i]
        for i in self.developments:
            developments_clone[i.toString('dd/MM/yyyy')] = self.table[i]
        for i in self.deadlines:
            deadlines_clone[i] = [self.deadlines[i][0].toString('dd/MM/yyyy'),
                                  self.deadlines[i][1].toString('dd/MM/yyyy'), self.deadlines[i][2]]
        table.write(json.dumps(table_clone))
        deadlines.write(json.dumps(deadlines_clone))
        table.close()
        deadlines.close()
        if bool(self.developments):
            developments = open('developments.txt', mode='w')
            for i in self.developments:
                developments_clone[i.toString('dd/MM/yyyy')] = self.developments[i]
            developments.write(json.dumps(developments_clone))
            developments.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())

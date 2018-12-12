import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem


class Show(QWidget):
    def __init__(self):
        super(Show, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(826, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 10, 431, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(510, 20, 301, 411))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 390, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 340, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 18))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

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
        # uic.loadUi('create_deadline.ui', self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 420, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 420, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 110, 431, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 0, 825, 100))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(1)
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 110, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(470, 150, 191, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(470, 190, 191, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 250, 191, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        '''MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)'''

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
        MainWindow.resize(825, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 10, 431, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 390, 281, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 340, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 100, 181, 71))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 20, 181, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 190, 101, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        '''MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)'''

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
        # uic.loadUi('create_development.ui', self)
        # self.show()
        self.table = {}
        self.developments = {}
        self.free = {'Пн': '1', 'Вт': '1', 'Ср': '1', 'Чт': '1', 'Пт': '1', 'Сб': '1', 'Вс': '1'}
        self.deadlines = {}
        self.showdeadlines()

    def showdeadlines(self):
        try:
            self.w1 = Show()
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
            self.w1.listWidget.clear()
            if self.w1.calendarWidget.selectedDate() in self.table:
                for i in range(1, len(self.table[self.w1.calendarWidget.selectedDate()])):
                    # print(self.table[self.w1.calendarWidget.selectedDate()])
                    self.w1.listWidget.addItem(' '.join(self.table[self.w1.calendarWidget.selectedDate()][i]))
            if self.w1.calendarWidget.selectedDate() in self.developments:
                for i in range(len(self.developments[self.w1.calendarWidget.selectedDate()])):
                    self.w1.listWidget.addItem(' '.join(self.developments[self.w1.calendarWidget.selectedDate()][i]))
        except Exception as e:
            print(e)
    def createdeadline(self):
        try:
            self.w2 = CreateDeadline()
            self.w2.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(self.free['Пн'])))
            self.w2.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(self.free['Вт'])))
            self.w2.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(self.free['Ср'])))
            self.w2.tableWidget_2.setItem(0, 3, QTableWidgetItem(str(self.free['Чт'])))
            self.w2.tableWidget_2.setItem(0, 4, QTableWidgetItem(str(self.free['Пт'])))
            self.w2.tableWidget_2.setItem(0, 5, QTableWidgetItem(str(self.free['Сб'])))
            self.w2.tableWidget_2.setItem(0, 6, QTableWidgetItem(str(self.free['Вс'])))
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
            self.w3 = CreateDevelopment()
            self.w3.pushButton_2.clicked.connect(self.createdeadline)
            self.w3.pushButton_2.clicked.connect(self.w3.close)
            self.w3.pushButton.clicked.connect(self.showdeadlines)
            self.w3.pushButton.clicked.connect(self.w3.close)
            self.w3.pushButton_3.clicked.connect(self.developmentdo)
            # self.developments[]
            self.w3.show()
        except Exception as e:
            print(e)


    def developmentdo(self):
        try:
            name = self.w3.lineEdit.text()
            number = (self.w3.lineEdit_2.text().replace('.', ':') + ':0').split(':')
            time = str(int(number[0]) * 60 + int(number[1]))
            date = self.w3.calendarWidget.selectedDate()
            self.developments[date] = self.developments.get(date, []) + [[name, time]]
            if date not in self.table:
                table_time = (self.free[date.toString('ddd')] + ':0').replace('.', ':').split(':')
                self.table[date] = [str(int(table_time[0]) * 60 + int(table_time[1]))]
                if int(self.table[date][0]) + int(time) < 0:
                    print('Нехватка времени!')
                self.table[date][0] = str(int(self.table[date][0]) + int(time))

            elif self.table[date][0] == '0':
                self.table[date][0] = str(int(self.table[date][0]) + int(time))
                if int(time) > 0:
                    self.plus(date)
                elif int(time) < 0:
                    self.minus(date)


            # print(date, 'developmentdo', self.table)
        except Exception as e:
            print(e)


    def plus(self, date):
        end = max(self.table.keys())
        swap = []
        for i in range(1, date.daysTo(end) + 1):
            day = date.addDays(i)
            swap.append(day)
            for j in range(1, len(self.table[day])):
                min_time = min(int(self.table[date][0]), int(self.table[day][j][1]))
                self.table[date][0] = str(int(self.table[date][0]) - min_time)
                self.table[day][j][1] = str(int(self.table[day][j][1]) - min_time)
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
        for i in swap:
            self.plus(i)



    def minus(self, date):
        pass

    def deadlinedo(self):
        try:

            whenfree = [self.w2.tableWidget_2.item(0, i).text() for i in range(7)]
            assert all([i.replace('.', '').replace(':', '').isdigit() for i in whenfree])
            self.free['Пн'] = whenfree[0]
            self.free['Вт'] = whenfree[1]
            self.free['Ср'] = whenfree[2]
            self.free['Чт'] = whenfree[3]
            self.free['Пт'] = whenfree[4]
            self.free['Сб'] = whenfree[5]
            self.free['Вс'] = whenfree[6]
            name = self.w2.lineEdit.text()
            time = int(self.w2.timeEdit.text().split(':')[0]) * 60 + int(self.w2.timeEdit.text().split(':')[1])
            end = self.w2.calendarWidget.selectedDate()
            # start = QDate.addDays(self.w2.dateEdit.date(), 4)
            start = self.w2.dateEdit.date()
            #print(end)
            self.deadlines[name] = [end, start, time]
            if bool(self.table) == False:
                for i in range(start.daysTo(end) + 1):
                    time = (self.free[start.addDays(i).toString('ddd')] + ':0').replace('.', ':').split(':')
                    self.table[start.addDays(i)] = self.table.get(start.addDays(i), [str(
                            int(time[0]) * 60 + int(time[1]))])
            else:
                table_min, table_max = min(self.table.keys()), max(self.table.keys()),
                if start < table_min:
                    for i in range(start.daysTo(table_min)):
                        time = (self.free[start.addDays(i).toString('ddd')] + ':0').replace('.', ':').split(':')
                        self.table[start.addDays(i)] = self.table.get(start.addDays(i), [str(
                            int(time[0]) * 60 + int(time[1]))])
                if table_max < end:
                    for i in range(table_max.daysTo(end)):
                        time = (self.free[table_max.addDays(i + 1).toString('ddd')] + ':0').replace('.', ':').split(':')
                        self.table[table_max.addDays(i + 1)] = self.table.get(table_max.addDays(i), [str(
                            int(time[0]) * 60 + int(time[1]))])
            self.control(name)
            # print(self.table)
        except Exception as e:
            print(e, 'deadlinedo')

    def control(self, name):
        try:
            end, start, time = self.deadlines[name][0], self.deadlines[name][1], self.deadlines[name][2]
            swap = []
            for i in range(start.daysTo(end)):
                day = start.addDays(i)
                min_time = min(int(self.table[day][0]), time)
                self.table[day][0] = str(int(self.table[day][0]) - min_time)
                time -= min_time
                for j in range(1, len(self.table[day])):
                    if self.deadlines[self.table[day][j][0]][0] > end:  # self.table[day][j] - список из названия и времени
                        min_time2 = min(int(self.table[day][j][1]), time)
                        self.table[day][j][1] = str(int(self.table[day][j][1]) - min_time2)
                        self.deadlines[self.table[day][j][0]][-1] += min_time2
                        self.deadlines[self.table[day][j][0]][1] = self.deadlines[self.table[day][j][0]][1].addDays(1)
                        time -= min_time2
                        min_time += min_time2
                        swap.append(self.table[day][j][0])
                    if self.table[day][j][1] == '0':
                        del self.table[day][j]
                if min_time != 0:
                    self.table[day].append([name, str(min_time)])
                # print('sdfghjkl')
                # print(self.table[day][1:]) # [['qwertyui', '120']]
                # print(sorted(self.table[day][1:], key=lambda s: self.deadlines[s[0]][0]))
                self.table[day] = [self.table[day][0]] + sorted(self.table[day][1:], key=lambda s: self.deadlines[s[0]][0])
                # print('sdfghjkl')
                if time == 0:
                    break
            self.deadlines[name][0], self.deadlines[name][1], self.deadlines[name][2] = end, start, time
            if time != 0:
                print('Нехватка времени', time)
            for i in swap:
                self.control(i)
        except Exception as e:
            print(e, 'controlError')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())



'''
в словаре хранятся ключи от min start до max end значения: свободное врем на день(уменьшается с добавлением дел)
дела + время выполнения каждого( также вычитается из deadlines), обытия отсортированы по близости дедлайна

В дедлайне время - число, в расписании время - строка

бработка control

Дедлайны выводятся как события
Проверить корректность работы control
'''
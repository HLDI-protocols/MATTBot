"""
Designed and Developed by: Akhil P Jacob
FOr personal use only

"""


from PyQt5 import QtCore, QtGui, QtWidgets
from Seeker import timeMapper
import AutomataLib


class MATTBOT(object):
    def mattbot(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(477, 358)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphix/ubuntu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 461, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.Terminal = QtWidgets.QWidget()
        self.Terminal.setObjectName("Terminal")
        self.label = QtWidgets.QLabel(self.Terminal)
        self.label.setGeometry(QtCore.QRect(210, 40, 231, 221))
        self.label.setStyleSheet("border-image: url(Graphix/MattBot.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_10 = QtWidgets.QPushButton(self.Terminal)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 270, 161, 25))
        self.pushButton_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(3, 0, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_2 = QtWidgets.QLabel(self.Terminal)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 71, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Terminal)
        self.lineEdit.setGeometry(QtCore.QRect(10, 270, 251, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.Terminal)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 191, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.label_16 = QtWidgets.QLabel(self.Terminal)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 331, 17))
        self.label_16.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.Terminal, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.progressBar = QtWidgets.QProgressBar(self.Settings)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_9 = QtWidgets.QPushButton(self.Settings)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 10, 161, 25))
        self.pushButton_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(3, 0, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_14 = QtWidgets.QLabel(self.Settings)
        self.label_14.setGeometry(QtCore.QRect(10, 70, 81, 17))
        self.label_14.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.Settings)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 40, 281, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.Settings)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 141, 141))
        self.label_12.setStyleSheet("border-image: url(Graphix/HLD.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.Settings)
        self.label_15.setGeometry(QtCore.QRect(70, 260, 291, 20))
        self.label_15.setObjectName("label_15")
        self.label_3 = QtWidgets.QLabel(self.Settings)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.Settings)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 40, 61, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.Settings)
        self.label_10.setGeometry(QtCore.QRect(330, 170, 101, 81))
        self.label_10.setStyleSheet("border-image: url(Graphix/ubuntu.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Settings)
        self.label_11.setGeometry(QtCore.QRect(180, 120, 131, 141))
        self.label_11.setStyleSheet("border-image: url(Graphix/HLEngine.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.Settings)
        self.lineEdit_9.setGeometry(QtCore.QRect(90, 70, 61, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.tabWidget.addTab(self.Settings, "")

        self.timer = QtCore.QTimer(Dialog)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        self.pushButton_10.clicked.connect(self.seek)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MATTBot 2020 ver 2.0"))
        self.pushButton_10.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "loading..."))
        self.label_16.setText(_translate("Dialog", "Reminder:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Terminal), _translate("Dialog", "Terminal"))
        self.pushButton_9.setText(_translate("Dialog", "Check for Updates"))
        self.label_14.setText(_translate("Dialog", "Shutdown"))
        self.label_15.setText(_translate("Dialog", "Designed and Developed by Akhil P Jacob"))
        self.label_3.setText(_translate("Dialog", "Reminder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("Dialog", "Settings"))
    
    def displayTime(self):
        self.label_2.setText(QtCore.QDateTime.currentDateTime().time().toString())
        reminder=self.lineEdit_7.text()
        reminder_data=self.lineEdit_8.text()
        self.label_16.setText("Reminder: "+reminder_data)
        AutomataLib.automata(self.label_2.text(),reminder)
        
    def seek(self):
        import terminal
        data=self.lineEdit.text()
        data=terminal.terminalAccess(data)
        self.textBrowser.setText(data)
        self.lineEdit.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MATTBOT()
    ui.mattbot(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

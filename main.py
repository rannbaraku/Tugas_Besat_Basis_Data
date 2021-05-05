import sys, res
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

# GUI FILE
from ui_main import Ui_MainWindow
from uji2 import Ui_Form
from uji2 import *
# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
 
        QMainWindow.__init__(self)
        #Ui_Form.tutup(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.Form = QtWidgets.QWidget()
        # ui = Ui_Form()
        # ui.setupUi(Form)
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        center(self.Form)
        self.Form.show()
        self.ui.Loginkan.clicked.connect(self.call)

    def call (self):    
        if self.ui.lineEdit.text() == "Yukibara" and self.ui.lineEdit_2.text() == "Lavatera21" :
            self.Form.close()
            MainWindow()


def center(self):
        # geometry of the main window
    qr = self.frameGeometry()

        # center point of screen
    cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
    qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
    self.move(qr.topLeft())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = Login()
   # window = MainWindow()
    sys.exit(app.exec_())

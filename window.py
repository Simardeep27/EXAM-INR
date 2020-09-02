from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QDialog,QGroupBox,QHBoxLayout, QVBoxLayout,QLabel
from PyQt5 import QtWidgets
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PyQt5 import QtCore



class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title='Examinr'
        self.top=100
        self.left=100
        self.width=400
        self.height=300
        self.iconName='login'


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('images.png'))


        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.showMaximized()


        vbox=QVBoxLayout()
        labelImage=QLabel(self)
        pixmap=QPixmap('WhatsApp Image 2020-09-02 at 8.15.46 AM')
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)


        self.setLayout(vbox)
        #self.setWindowIcon(QtGui.QIcon(self.iconName))




        self.show()




if __name__=='__main__':
    App=QApplication(sys.argv)
    #login = Login()

    #if login.exec_() == QtWidgets.QDialog.Accepted:
    window = Window()
    window.show()
    sys.exit(App.exec_())



    #window=Window()
    #sys.exit(App.exec())

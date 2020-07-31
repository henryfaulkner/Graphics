from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QSize
from Transformations import transformations
import sys

class Window_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Main Window'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.file_lab = QLabel(self)
        self.file_lab.setText('External File')
        self.file_lab.move(20,50)
        self.file_lab.resize(200, 30)

        self.file_text = QLineEdit(self)
        self.file_text.move(20,80)
        self.file_text.resize(250, 30)
        
        self.plot_button = QPushButton('Plot Image', self)
        self.plot_button.move(20, 120)
        self.plot_button.resize(200, 30)

        self.plot_button.clicked.connect(self.add_on_click())

        self.show()

    @pyqtSlot()
    def add_on_click(self):
        externalFile = self.file_text.text()
        if externalFile != '':
            file_matrix = transformations.InputLines(externalFile)
            Transformations.DisplayPygame(file_matrix)
            

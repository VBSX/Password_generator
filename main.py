import sys
import random
from PySide2.QtWidgets import QPushButton, QMainWindow
from PySide2 import QtCore

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QVBoxLayout,QApplication, QWidget, QLabel

class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setWindowTitle('Password Generator')
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 
             'v', 'w', 'x', 'y', 'z']
        self.especialchars = ['#', '@', '$', '%']
        self.button = QPushButton("Generate a password")
                          
        self.btn = QPushButton('Copy to clipboard', clicked=self.copy_to_clipboard)
        self.lbl = QLabel()
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.text = QLabel()
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setStyleSheet('color: rgb(128,0,0);')

        widget = QWidget()
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        # widget.setLayout(self.layout)
        # self.setCentralWidget(widget)
        # self.layout.addWidget(self.button)
        # self.layout.addWidget(self.btn)
        # self.layout.addWidget(self.lbl)
        # self.button.clicked.connect(self.magic)
        
        
    def copy_to_clipboard(self): 
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.text.text(),  mode=cb.Clipboard)
        self.show_dialog('Content was copied')
              
        
    def magic(self):
        self.text.setText(str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          random.choice(self.especialchars)+
                          random.choice(self.letters)+
                          random.choice(self.letters)+
                          random.choice(self.letters)+
                          random.choice(self.letters))
    
    def show_dialog(self, text):
        QMessageBox.about(self, text, "Message")
        
if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()
    sys.exit(app.exec_())
import sys
import random
from turtle import width
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.numbers = ['0' ,'1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 
             'v', 'w', 'x', 'y', 'z']
        self.especialchars = ['#', '@', '$', '%']
        
        self.setWindowTitle('Password Generator')
        self.button = QtWidgets.QPushButton("Generate a password")
        
                                  
        self.btn = QtWidgets.QPushButton('Copy to clipboard', clicked=self.copy_to_clipboard)
        self.lbl = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet('color: rgb(128,0,0);')

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.lbl)
        self.button.clicked.connect(self.magic)
        
        
    def copy_to_clipboard(self):
        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.text.text(),  mode=cb.Clipboard)
        self.lbl.setText('Content was copied')
        
        
    def magic(self):
        self.text.setText(random.choice(self.numbers)+
                          random.choice(self.numbers)+
                          random.choice(self.numbers)+
                          random.choice(self.numbers)+
                          random.choice(self.numbers)+
                          random.choice(self.especialchars)+
                          random.choice(self.letters)+
                          random.choice(self.letters)+
                          random.choice(self.letters)+
                          random.choice(self.letters))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())
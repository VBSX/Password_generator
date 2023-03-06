import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
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
        clip = QtWidgets.QApplication.clipboard()
        clip.clear(mode=clip.Clipboard)
        clip.setText(self.text.text(),  mode=clip.Clipboard)
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
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
      
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())
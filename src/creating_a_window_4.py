import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)  # <1>


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self,sizex= 300,sizey = 400):
        super().__init__( ) # <2>

        self.setWindowTitle("My Calories")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)




        #self.set_fixed_window_size(sizex,sizey)
        self.set_base_window_size(sizex,sizey)



        # Set the central widget of the Window.
        self.setCentralWidget(button)  # <3> means goes into the center of the window

    def set_base_window_size(self,x,y):
        """sets window size"""

        self.setBaseSize(x,y)
        return

    
    def set_fixed_window_size(self,x,y):
        """sets window size"""

        self.setFixedSize(x,y)
        return


    def button_clicked(self):
        """this is called by pushing the button"""
        
        print("you clicked me")

        return

if __name__  == "__main__":  
    app = QApplication(sys.argv)




    window = MainWindow(sizex = 200, sizey=300)
    window.show() # we inherit the show from the QTclass QmainWindow ak

app.exec()

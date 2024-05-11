from PySide6.QtCore import (

             Qt,
             QFileSystemWatcher,
             QSettings,
             Signal)


from PySide6.QtWidgets import (
            QApplication,
            QComboBox,
            QMainWindow,
            QSlider

)

import sys




class DoubleSlider(QSlider): # we inherit from QSlider

    # create our our signal that we can connect to if necessary
    doubleValueChanged = Signal(float)

    def __init__(self, decimals=1, *args, **kargs):
        #super(DoubleSlider, self).__init__( *args, **kargs)
        super(DoubleSlider, self).__init__( *args, **kargs)
        self._multi = 10 ** decimals

        self.valueChanged.connect(self.emitDoubleValueChanged)

    def emitDoubleValueChanged(self):
        value = float(super(DoubleSlider, self).value())/self._multi  # here we are using the inhreited structures and objexcts
        self.doubleValueChanged.emit(value)

    def setTickPosition(self):  #ak
        return super(DoubleSlider, self).setTickPosition(QSlider.TicksRight)
    
    def value(self):
        return float(super(DoubleSlider, self).value()) / self._multi

    def setMinimum(self, value):
        return super(DoubleSlider, self).setMinimum(value * self._multi)

    def setMaximum(self, value):
        return super(DoubleSlider, self).setMaximum(value * self._multi)

    def setSingleStep(self, value):
        return super(DoubleSlider, self).setSingleStep(value * self._multi)

    def singleStep(self):
        return float(super(DoubleSlider, self).singleStep()) / self._multi

    def setValue(self, value):
        super(DoubleSlider, self).setValue(int(value * self._multi))

    def setSize(self,x,y): #ak
            super(DoubleSlider, self).setFixedSize(x,y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DoubleSlider(orientation=Qt.Orientation.Horizontal)
    window.setMaximum(200)
    window.setMinimum(100)
    window.setSize(600,200)
    window.setTickPosition()
    window.show()
    app.exec()
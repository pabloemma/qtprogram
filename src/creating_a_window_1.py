from PySide6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()

#ak
window1 = QPushButton("push me")
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
window1.show()
window2=QMainWindow()
window2.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.

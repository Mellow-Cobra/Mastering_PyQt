import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5  import QtCore as qtc

class MainWindow(qtw.QWidget):
    """Main UI"""
    def __init__(self):
        if __name__ == '__main__':
            """MainWindow constructor.
                    
            This widget will be our main window.
            We'll define all the UI components in here.
            """
            super().__init__()
            # Main UI code goes here

            # End main UI code
            self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's requrired to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())

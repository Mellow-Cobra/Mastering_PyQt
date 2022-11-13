import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    """ Main UI"""
    def __init__(self):
        if __name__ == '__main__':
            """
            widget will be our main window.
            We'll define all the UI components in here.
            """
            super().__init__(windowTitle='Qt Widget demo')
            # Main UI code goes here
            # QWidget
            subwidget = qtw.QWidget(self, toolTip='This is my widget')

            # QLabel
            label = qtw.QLabel('<b>Hello Widgets!</b>', self)

            # QLine Widget
            line_edit = qtw.QLineEdit(
                'default value',
                self,
                placeholderText='Type here',
                clearButtonEnabled=True,
                maxLength=20
            )

            # QPushButton
            button = qtw.QPushButton("Push Me", self,
                                     checkable=True,
                                     checked=True,
                                     shortcut=qtg.QKeySequence('Ctrl+p'))

            # QComboBox
            combobox = qtw.QComboBox(self,
                                     editable=True,
                                     insertPolicy=qtw.QComboBox.InsertAtTop
                                     )
            combobox.addItem('Lemon', 1)
            combobox.addItem('Peach', 'Ohh I like Peaches!')
            combobox.addItem('Strawberry', qtw.QWidget)
            combobox.insertItem(1, 'Radish', 2)

            # QSpinBox
            spinbox = qtw.QSpinBox(
                self,
                value=12,
                maximum=100,
                minimum=10,
                prefix='$',
                suffix=' + Tax',
                singleStep=5
            )

            # QTextEdit
            textedit = qtw.QTextEdit(
                self,
                acceptRichText=False,
                placeholderText='Enter your text here'
            )

            layout = qtw.QVBoxLayout()
            self.setLayout(layout)

            layout.addWidget(label)
            layout.addWidget(line_edit)

            sublayout = qtw.QHBoxLayout()
            layout.addLayout(sublayout)

            sublayout.addWidget(button)
            sublayout.addWidget(combobox)

            grid_layout = qtw.QGridLayout()
            layout.addLayout(grid_layout)

            grid_layout.addWidget(spinbox, 0, 0)
            grid_layout.addWidget(textedit, 1, 0, 2, 2)

            form_layout = qtw.QFormLayout()
            layout.addLayout(form_layout)

            form_layout.addRow('Item 1', qtw.QLineEdit(self))
            form_layout.addRow('Item 2', qtw.QLineEdit(self))
            form_layout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))





            # End main UI code
            self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's requrired to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())


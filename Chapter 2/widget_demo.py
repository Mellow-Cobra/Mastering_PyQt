import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class IPv4Validator(qtg.QValidator):
    """Enforce entry IPv4 Addresses"""

    def validate(self, string, index):
        """Validator Method"""
        octets = string.split('.')
        if len(octets) > 4:
            state = qtg.QValidator.Invalid
        elif not all([x.isdigit() for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        elif not all([0 <= int(x) <= 255 for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        elif len(octets) < 4:
            state = qtg.QValidator.Intermediate
        elif any([x == '' for x in octets]):
            state = qtg.QValidator.Intermediate
        else:
            state = qtg.QValidator.Acceptable
        return (state, string, index)


class ChoiceSpinBox(qtw.QSpinBox):
    """A spinbox for selecting choices."""

    def __init__(selfself, choices, *args, **kwargs):
        """Spinbox"""
        self.choices = choices
        super().__init__(
            *args,
            maximum=len(self.choices) - 1,
            minimum=0,
            **kwargs
        )

    def textFromValue(self, value):
        """Method for text from value"""
        try:
            return self.choices[value]
        except IndexError:
            return '!Error'

    def validate(self, string, index):
        if string in self.choices:
            state = qtg.QValidator.Acceptable
        elif any([v.startswith(string) for v in self.choices]):
            state = qtg.QValidator.Intermediate
        else:
            state = qtg.QValidator.Invalid
        return (state, string, index)

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
            label.setFixedSize(150, 40)

            # QLine Widget
            line_edit = qtw.QLineEdit(
                'default value',
                self,
                placeholderText='Type here',
                clearButtonEnabled=True,
                maxLength=20
            )
            line_edit.setMinimumSize(150, 15)
            line_edit.setMaximumSize(500, 50)
            line_edit.setText('0.0.0.0')
            line_edit.setValidator(IPv4Validator())

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
            spinbox.setSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Preferred)

            # QTextEdit
            textedit = qtw.QTextEdit(
                self,
                acceptRichText=False,
                placeholderText='Enter your text here'
            )
            textedit.setSizePolicy(qtw.QSizePolicy.MinimumExpanding,
                                   qtw.QSizePolicy.MinimumExpanding)
            textedit.sizeHint = lambda: qtc.QSize(500, 500)

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

            stretch_layout = qtw.QHBoxLayout()
            layout.addLayout(stretch_layout)
            stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
            stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)

            form_layout.addRow('Item 1', qtw.QLineEdit(self))
            form_layout.addRow('Item 2', qtw.QLineEdit(self))
            form_layout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))

            tab_widget = qtw.QTabWidget()
            layout.addWidget(tab_widget)

            tab_widget = qtw.QTabWidget(
                movable=True,
                tabPosition=qtw.QTabWidget.West,
                tabShape=qtw.QTabWidget.Triangular
            )
            layout.addWidget(tab_widget)
            container = qtw.QWidget(self)
            grid_layout = qtw.QGridLayout()
            # layout.addLayout(grid_layout)
            container.setLayout(grid_layout)

            tab_widget.addTab(container, 'Tab the first')
            tab_widget.addTab(subwidget, 'Tab the second')

            groupbox = qtw.QGroupBox('Buttons')
            groupbox.setLayout(qtw.QHBoxLayout())
            groupbox.layout().addWidget(qtw.QPushButton('OK'))
            groupbox.layout().addWidget(qtw.QPushButton('Cancel'))
            layout.addWidget(groupbox)

            # End main UI code
            self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's requrired to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())

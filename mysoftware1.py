from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QComboBox, QPlainTextEdit
from PyQt6 import uic
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from Crypto.Util.number import getPrime
from qtgui import *
from functions import *

class SimpleDialogForm(Ui_MainWindow):

    def __init__(self, parent=None):
        super(SimpleDialogForm, self).__init__()


def setComboBox(mycomboBox: QComboBox):
    function_list = ["请选择一个功能", "reverse", "base64decode", "二进制", "frequency"]

    mycomboBox.addItems(function_list)
    return



def listen2comboBox(mycomboBox: QComboBox, myplainTextEdit_2: QPlainTextEdit):
    if mycomboBox.currentIndex() == 2:
        myplainTextEdit_2.clear()
        myplainTextEdit_2.setPlaceholderText("可以在这里输入换表base64")
    return


def listen2button(myplainTextEdit: QPlainTextEdit, mycomboBox: QComboBox, myplainTextEdit_2: QPlainTextEdit):
    text = myplainTextEdit.toPlainText()
    index = mycomboBox.currentIndex()

    if not text:
        return

    if index == 0:
        myplainTextEdit_2.setPlainText("请选择一个功能")
    elif index == 1:
        myplainTextEdit_2.clear()
        myplainTextEdit_2.setPlainText(text[::-1])
    elif index == 2:
        text2 = myplainTextEdit_2.toPlainText()
        myplainTextEdit_2.setPlainText(base64decode(text, text2))
    elif index == 3:
        myplainTextEdit_2.setPlainText(bindecode(text))
    elif index == 4:
        myplainTextEdit_2.setPlainText(frequencycount(text))
    else:
        return
    return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = SimpleDialogForm()
    main = QtWidgets.QMainWindow()
    ui.setupUi(main)

    mycomboBox: QComboBox = ui.comboBox
    setComboBox(mycomboBox)

    mypushButton: QPushButton = ui.pushButton
    myplainTextEdit: QPlainTextEdit = ui.plainTextEdit
    myplainTextEdit_2: QPlainTextEdit = ui.plainTextEdit_2

    mypushButton.clicked.connect(lambda: listen2button(myplainTextEdit, mycomboBox, myplainTextEdit_2))

    mycomboBox.currentIndexChanged.connect(lambda: listen2comboBox(mycomboBox, myplainTextEdit_2))

    main.show()

    sys.exit(app.exec())

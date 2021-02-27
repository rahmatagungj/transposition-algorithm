from GUI import *

def signals(self):
    self.pushButton.clicked.connect(encrypt)
    self.pushButton_2.clicked.connect(decrypt)

def encrypt(self):
    curr = '';encrypted=''

    message = ui.plainTextEdit.toPlainText()
    key = ui.spinBox.text()
    
    for i in str(message):
        curr += str(ord(i) + int(key)) + " "

    for j in curr.split():
        encrypted += str(chr(int(j)))
    
    ui.plainTextEdit.setPlainText(encrypted)


def decrypt(message,key=0):
    curr = '';decrypted=''

    message = ui.plainTextEdit.toPlainText()
    key = ui.spinBox.text()


    for k in message:
        curr += str(ord(k) - int(key)) + " "

    for l in curr.split():
        decrypted += str(chr(int(l)))

    ui.plainTextEdit.setPlainText(decrypted)


def init_function():
    Ui_MainWindow.signals = signals
    Ui_MainWindow.encrypt = encrypt
    Ui_MainWindow.decrypt = decrypt

init_function()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
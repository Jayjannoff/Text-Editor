from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class gui(QMainWindow):

    def __init__(self):
        super(gui,self).__init__()
        uic.loadUi('editor.ui',self)
        self.show()

        self.setWindowTitle('jay_jannoff text editor')
        self.action12pt.triggered.connect(lambda :self.change_size(12))
        self.action18pt.triggered.connect(lambda :self.change_size(18))
        self.action24pt.triggered.connect(lambda :self.change_size(24))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.closeEvent)



    def open_file(self):
        options = QFileDialog.options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open file","","Text Files ()*.txt;;Python Files (*.py)",options=options)
        if filename !="":
            with open(filename,'r') as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)",
                                                  options=options)
        if filename != "":
            with open(filename, 'w') as f:
                f.write(self.plainTextEdit.toPlainText())


    def closeEvent(self, event):
        dialog=QMessageBox()
        dialog.setText('Do you really want to save your work?')
        dialog.addButton((QPushButton('Yes'),QMessageBox.YesRole))
        dialog.addButton((QPushButton('No'),QMessageBox.NoRole))
        dialog.addButton((QPushButton('Cancel'),QMessageBox.RejectRole))

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()

    def change_size(self,size):

        self.plainTextEdit.setFont(QFont('Arial',size))

def main():
    app = QApplication([])
    window = gui()
    app.exec_()

if __name__ == '__main__':
    main()

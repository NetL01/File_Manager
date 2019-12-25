import shutil
from pathlib import Path
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from lstint import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list_with_words = list()
        self.list_with_dirs = list()
        self.list_select = list()
        self.change_directory()
        self.path = ''
        i, okBtnPressed = QInputDialog.getItem(self, "...", 
                                       "Выберите диск?", 
                                       self.list_with_dirs, 
                                       1, False)
        if okBtnPressed:
            self.path = i + '\\'

        os.chdir(self.path)
        self.list_dir = os.listdir(self.path)
        self.list_dir.insert(0, '..')
        self.highlight_mode = False
        self.list_with_select = set()
        self.change_directory()
        self.update_table()
        self.tableWidget.itemClicked.connect(self.onClicked)
        self.Button_create.clicked.connect(self.create)
        self.Button_del.clicked.connect(self.delete)
        self.Button_cut.clicked.connect(self.cut)
        self.disable_all.clicked.connect(self.disable_all_method)
        self.select_all.clicked.connect(self.select_all_method)
        self.Button_paste.clicked.connect(self.paste)
        self.as_hilight.clicked.connect(self.highlight_m)
        


    def table_widget2(self):
        self.tableWidget2.setRowCount(len(self.cells))
        self.tableWidget2.setColumnCount(1)
        count = 0
        for nel in self.cells:
            self.tableWidget2.setItem(0, count, QTableWidgetItem(nel))
            count += 1

    def table_widget2_select(self):
        self.tableWidget2.clear()
        self.tableWidget2.setRowCount(len(self.kells))
        self.tableWidget2.setColumnCount(1)
        count = 0
        for nel in self.kells:
            self.tableWidget2.setItem(0, count, QTableWidgetItem(nel))
            count += 1
        

    
    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
    def onClicked(self, cell):
        if not self.highlight_mode:
            print(cell)
            if cell.text() == '..':
                self.path = str(Path(self.path).parent)
                print(self.path)
            else:
                if not os.path.isfile(self.path + "\\" + str(cell.text())):
                    self.path = self.path + "\\" + str(cell.text())

            print(self.path)
            try:
                os.chdir(self.path)
                self.list_dir = os.listdir(self.path)
                self.list_dir.insert(0, '..')
            except:
                buttonReply = QMessageBox.question(self, 'ERROR', "ERROR",
                                                   QMessageBox.Ok, QMessageBox.Ok)
            self.update_table()            
        else:
            if cell.text() != '..':
                self.list_with_select.add(self.path + '\\' + str(cell.text()))
                print(self.list_with_select)

    def change_directory(self):
        self.list_with_words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for i in self.list_with_words:
            if os.path.exists(i + ":\\"):
                self.list_with_dirs.append(i + ':')

    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
                

    def update_table(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.list_dir))
        self.tableWidget.setColumnCount(1)
        count = 0
        for nel in self.list_dir:
            self.tableWidget.setItem(0, count, QTableWidgetItem(nel))
            count += 1

    def delete(self):
        for i in list(self.list_with_select):
            print(i)
            if os.path.isfile(i):
                os.remove(i)
            elif os.path.isdir(i):
                os.rmdir(i)
            else:
                buttonReply = QMessageBox.question(self, 'ERROR', "ERROR",
                                                   QMessageBox.Ok, QMessageBox.Ok)
                
                
                

    def cut(self):
        for i in self.list_with_select:
            shutil.move(i, self.path + '\\')
        self.list_with_select.clear()           
            
    def paste(self):
        for i in self.list_with_select:
            shutil.move(i, self.path + '\\')
        self.list_with_select.clear()

    def rename(self):
        pass

    def create(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Процедура создания",
                                      "Что хотите создать?",
                                      ("Папка", "файл"),
                                               1, False)
        if okBtnPressed:
            if i == 'файл':
                create_folder = open("YourFolder", 'w')
                create_folder.close()
            elif i == 'Папка':
                try:
                    os.mkdir("YourFile")
                    os.mkdir(self.path)
                except:
                    buttonReply = QMessageBox.question(self, 'ERROR', "ERROR",
                                                   QMessageBox.Ok, QMessageBox.Ok)
                

    def highlight_m(self):
        if not(self.highlight_mode):
            self.highlight_mode = True
            self.label.setText('ON')
        else:
            self.highlight_mode = False
            self.label.setText('OFF')
            kell = list(self.list_with_select)
            self.kells = []
            for i in kell:
                self.kells.append((i.split('\\'))[-1])
                self.table_widget2_select()
            
        print(self.highlight_mode)
        
    def select_all_method(self):
        list_for_dir = os.listdir(self.path)
        print(self.path)
        print(list_for_dir)
        for i in list_for_dir:
            self.list_with_select.add(self.path + '\\' + i)
        print(self.list_with_select)
        f = list(self.list_with_select)
        self.cells = []
        for i in f:
            self.cells.append((i.split('\\'))[-1])
        self.table_widget2()
        
    def disable_all_method(self):
        print(self.list_with_select)
        self.list_with_select.clear()
        self.tableWidget2.clear()
        
        
    def selectedItems(self, list_with_select):
        print(list_with_select)
        

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

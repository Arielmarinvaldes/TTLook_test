import sys
import requests
import json
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 511, 351))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x3:1, y2:2, stop:0 rgba(195, 233, 154), stop:1 rgba(1, 229, 161, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.list_door = QtWidgets.QComboBox(self.centralwidget)
        self.list_door.setGeometry(QtCore.QRect(10, 30, 91, 20))
        self.list_door.setObjectName("list_door")
        self.label_door = QtWidgets.QLabel(self.centralwidget)
        self.label_door.setGeometry(QtCore.QRect(10, 10, 35, 10))
        self.label_door.setObjectName("label_door")
        self.get_door = QtWidgets.QPushButton(self.centralwidget)
        self.get_door.setGeometry(QtCore.QRect(130, 30, 56, 17))
        self.get_door.setObjectName("get_door")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 491, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.update_door_list()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_door.setText(_translate("MainWindow", "Puertas"))
        self.get_door.setText(_translate("MainWindow", "Get Door"))
        self.get_door.clicked.connect(self.show_door_info)

    def update_door_list(self):
        # Obtener la información de la API
        current_timestamp = int(time.time() * 1000)
        url = "https://euapi.ttlock.com/v3/lock/list"
        params = {
            'clientId': '196767a6f0e14a58ad4bddd75ae14c79',
            'accessToken': '51c4131921dc7d4c5874ffac76857ab3',
            'pageNo': 1,
            'pageSize': 20,
            'date': current_timestamp,
            # 'groupId': 618038
        }

        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            try:
                result = response.json()
                self.locks_list = result.get('list', [])
                
                # Limpiar el combo box antes de agregar elementos
                self.list_door.clear()
                
                # Agregar nombres de las puertas al combo box
                for lock in self.locks_list:
                    lock_name = lock.get('lockName', 'N/A')
                    self.list_door.addItem(lock_name)
                
            except json.JSONDecodeError:
                print("Error al decodificar la respuesta JSON.")
        else:
            print(f"Error en la solicitud: {response.status_code}")

    def show_door_info(self):
        selected_lock_name = self.list_door.currentText()
        selected_lock = next((lock for lock in self.locks_list if lock.get('lockName') == selected_lock_name), None)
        
        if selected_lock:
            lock_alias = selected_lock.get('lockAlias', 'N/A')
            
            # Agregar cabeceras
            headers = ["Lock Name", "Lock Alias"]
            self.tableWidget.setColumnCount(len(headers))
            self.tableWidget.setHorizontalHeaderLabels(headers)
            
            # Establecer el número de filas
            self.tableWidget.setRowCount(1)
            
            # Llenar la tabla con la información del candado seleccionado
            self.tableWidget.setItem(0, 0, QTableWidgetItem(selected_lock_name))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(lock_alias))

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
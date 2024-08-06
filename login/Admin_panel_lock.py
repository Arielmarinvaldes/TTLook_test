import sys
import requests
import json
import time
from security.protect import decrypt, data_date_time
from conexion.linked import establecer_conexion
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect

class CustomButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCheckable(True)
        self.setFixedSize(60, 30) # Tamaño del botón
        
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        radius = 15  # Radio de las esquinas redondeadas
        circle_diameter = 20  # Diámetro del círculo
        
        if self.isChecked():
            button_color = QColor('#55ff7f')
            circle_x = rect.width() - circle_diameter - 5
            circle_text = 'ON'
        else:
            button_color = QColor('#ff0000')
            circle_x = 5
            circle_text = 'OFF'
        
        # Dibujar el fondo del botón con esquinas redondeadas
        painter.setBrush(button_color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, radius, radius)
        
        # Dibujar el círculo
        painter.setBrush(QColor('#acacac'))
        circle_rect = QRect(circle_x, (rect.height() - circle_diameter) // 2, circle_diameter, circle_diameter)
        painter.drawEllipse(circle_rect)
        
        # Pintar el texto dentro del círculo
        painter.setPen(QColor('black'))
        painter.setFont(QFont('Arial', 6, QFont.Bold))
        text_rect = QRect(circle_rect.x(), circle_rect.y(), circle_diameter, circle_diameter)
        painter.drawText(text_rect, Qt.AlignCenter, circle_text)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, -10, 1121, 611))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x3:1, y2:2, stop:0 rgba(195, 233, 154), stop:1 rgba(1, 229, 161, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.list_door = QtWidgets.QComboBox(self.centralwidget)
        self.list_door.setGeometry(QtCore.QRect(10, 45, 101, 25))
        self.list_door.setObjectName("list_door")
        self.label_door = QtWidgets.QLabel(self.centralwidget)
        self.label_door.setGeometry(QtCore.QRect(20, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_door.setFont(font)
        self.label_door.setObjectName("label_door")
        self.get_door = QtWidgets.QPushButton(self.centralwidget)
        self.get_door.setGeometry(QtCore.QRect(480, 40, 70, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.get_door.setFont(font)
        self.get_door.setObjectName("get_door")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 541, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.key_obligatory = QtWidgets.QLineEdit(self.centralwidget)
        self.key_obligatory.setGeometry(QtCore.QRect(135, 45, 201, 25))
        self.key_obligatory.setObjectName("key_obligatory")
        self.key_label = QtWidgets.QLabel(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(140, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key_label.setFont(font)
        self.key_label.setObjectName("key_label")
        self.unlock_key = QtWidgets.QPushButton(self.centralwidget)
        self.unlock_key.setGeometry(QtCore.QRect(400, 40, 70, 30))
        self.unlock_key.setObjectName("unlock_key")
        self.date_time_start = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.date_time_start.setGeometry(QtCore.QRect(740, 130, 131, 22))
        self.date_time_start.setProperty("showGroupSeparator", False)
        self.date_time_start.setCalendarPopup(True)
        self.date_time_start.setTimeSpec(QtCore.Qt.UTC)
        self.date_time_start.setObjectName("date_time_start")
        self.date_time_end = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.date_time_end.setGeometry(QtCore.QRect(740, 200, 131, 22))
        self.date_time_end.setProperty("showGroupSeparator", False)
        self.date_time_end.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(9999, 12, 31), QtCore.QTime(23, 59, 59)))
        self.date_time_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(1, 0, 0)))
        self.date_time_end.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.date_time_end.setMinimumTime(QtCore.QTime(1, 0, 0))
        self.date_time_end.setCalendarPopup(True)
        self.date_time_end.setTimeSpec(QtCore.Qt.LocalTime)
        self.date_time_end.setObjectName("date_time_end")
        self.date_start_label = QtWidgets.QLabel(self.centralwidget)
        self.date_start_label.setGeometry(QtCore.QRect(740, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_start_label.setFont(font)
        self.date_start_label.setObjectName("date_start_label")
        self.date_end_label = QtWidgets.QLabel(self.centralwidget)
        self.date_end_label.setGeometry(QtCore.QRect(740, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_end_label.setFont(font)
        self.date_end_label.setObjectName("date_end_label")
        self.get_randon_code = QtWidgets.QPushButton(self.centralwidget)
        self.get_randon_code.setGeometry(QtCore.QRect(760, 260, 90, 30))
        self.get_randon_code.setObjectName("get_randon_code")
        self.lock_id_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.lock_id_entry.setGeometry(QtCore.QRect(740, 70, 131, 20))
        self.lock_id_entry.setObjectName("lock_id_entry")
        self.lock_id_label = QtWidgets.QLabel(self.centralwidget)
        self.lock_id_label.setGeometry(QtCore.QRect(740, 50, 47, 13))
        self.lock_id_label.setObjectName("lock_id_label")
        self.list_randon_code = QtWidgets.QTableWidget(self.centralwidget)
        self.list_randon_code.setGeometry(QtCore.QRect(880, 71, 191, 151))
        self.list_randon_code.setObjectName("list_randon_code")
        self.list_randon_code.setColumnCount(0)
        self.list_randon_code.setRowCount(0)
        self.batery_status = QtWidgets.QProgressBar(self.centralwidget)
        self.batery_status.setGeometry(QtCore.QRect(560, 527, 91, 23))
        self.batery_status.setProperty("value", 0)
        self.batery_status.setObjectName("batery_status")
        self.batery_status.setStyleSheet("""
            QProgressBar {
                border: 1px solid grey;
                border-radius: 10px; /* Radio de la esquina */
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #05B8CC; /* Color del progreso */
                border-radius: 10px; /* Radio de la esquina para el área de progreso */
            }
        """)
        self.battery_label = QtWidgets.QLabel(self.centralwidget)
        self.battery_label.setGeometry(QtCore.QRect(560, 503, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.battery_label.setFont(font)
        self.battery_label.setObjectName("battery_label")
        
        # Crear el botón personalizado
        self.on_off_button = CustomButton(self.centralwidget)
        self.on_off_button.setGeometry(QtCore.QRect(560, 460, 100, 50))
        
        self.randon_code_label = QtWidgets.QLabel(self.centralwidget)
        self.randon_code_label.setGeometry(QtCore.QRect(830, 25, 121, 21))
        self.user_label_custom = QtWidgets.QLabel(self.centralwidget)
        self.user_label_custom.setGeometry(QtCore.QRect(530, 5, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(80)
        self.user_label_custom.setFont(font)
        self.user_label_custom.setObjectName("user_label_custom")
        self.randon_code_label.setFont(font)
        self.randon_code_label.setObjectName("randon_code_label")
        MainWindow.setCentralWidget(self.centralwidget)

        # Deshabilitar botón de maximizar y evitar redimensionamiento
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        MainWindow.setFixedSize(MainWindow.size())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Inicialización de atributos
        self.cliente_id_decrypted = None
        self.accesstoken_decrypted = None
        self.locks_list = []
        self.current_timestamp = int(time.time() * 1000)
        key = self.key_obligatory.text()
        self.key_bytes = key.encode('utf-8')
        # Inicializa el nombre de usuario
        self.user_name = ""  # Variable para almacenar el nombre de usuario
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_door.setText(_translate("MainWindow", "Doors :"))
        self.get_door.setText(_translate("MainWindow", "Get Door"))
        self.key_label.setText(_translate("MainWindow", "Key Obliged"))
        self.unlock_key.setText(_translate("MainWindow", "Unlock Key"))
        self.date_start_label.setText(_translate("MainWindow", "Fecha de Inicio:"))
        self.date_end_label.setText(_translate("MainWindow", "Fecha de Fin:"))
        self.get_randon_code.setText(_translate("MainWindow", "Generar Codigo"))
        self.lock_id_label.setText(_translate("MainWindow", "Lock ID"))
        self.battery_label.setText(_translate("MainWindow", "Battery"))
        self.on_off_button.setText(_translate("MainWindow", "ON / OFF"))
        self.randon_code_label.setText(_translate("MainWindow", "Randon Códe"))
        self.user_label_custom.setText(_translate("MainWindow", ''))
        self.key_obligatory.setPlaceholderText("Obliged 16 or 24 or 32 characters")
        
        self.unlock_key.clicked.connect(self.unlocked)
        self.get_door.clicked.connect(self.show_door_info)
        self.get_randon_code.clicked.connect(self.access_new_code)
        self.on_off_button.toggled.connect(self.on_toggle)

    
    def establecer_conexion(self):
        return establecer_conexion()
    
    # Obtener credenciales desencriptadas
    def obtener_credenciales(self):
        key = self.key_obligatory.text()
        if not key:
            QMessageBox.critical(None, "Error", "La clave de encriptación es requerida.")
            return
        self.key_bytes = key.encode('utf-8')
        if len(self.key_bytes) not in (16, 24, 32):
            QMessageBox.critical(None, "Error", "La longitud de la clave debe ser de 16, 24 o 32 bytes.")
            return
        try:
            with self.establecer_conexion() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Name, Cliente_ID, Token FROM TT_Users WHERE User = ?", (self.user_name,))
                data = cursor.fetchone()
                if data:
                    return data
                else:
                    raise ValueError("No se encontraron credenciales en la base de datos.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al obtener usuarios: {e}")
            print(f"Error al obtener usuarios: {e}")

    def unlocked(self):
        data = self.obtener_credenciales()
        if data:
            self.get_key_master(data)

    def access_new_code(self):
        data = self.obtener_credenciales()

        # Obtener los valores de QDateTimeEdit
        datetime_start = self.date_time_start.dateTime()
        datetime_end = self.date_time_end.dateTime()

        # Convertir a timestamps en milisegundos
        timestamp_init = data_date_time(datetime_start)
        timestamp_end = data_date_time(datetime_end)
        cliente_id_decrypted = self.desencriptar(data[1])
        accesstoken_decrypted = self.desencriptar(data[2])

        if data:
            self.generate_random_code(cliente_id_decrypted, accesstoken_decrypted, self.lock_id_entry.text(), timestamp_init, timestamp_end)

    def desencriptar(self, encrypted_data):
        try:
            decrypted_data = decrypt(encrypted_data, self.key_bytes)
            self.show_door_info
            return decrypted_data
        except (ValueError, KeyError) as e:
            QMessageBox.critical(None, "Error de Desencriptación", f"Error al desencriptar datos: {e}")
            print(f"Error al desencriptar datos: {e}")
            return None
    def on_toggle(self, checked):
        command = 1 if checked else 2  # 1 para ON, 2 para OFF
        self.control_lock(command)


    def set_user_label(self, user_name):
        self.user_name = user_name  # Almacena el nombre del usuario
        self.user_label_custom.setText(f"Bienvenido, {user_name}")  # Actualiza el QLabel con el nombre del usuario


    def update_door_list(self):
        # Asegurarse de que las credenciales estén desencriptadas
        if self.cliente_id_decrypted is None or self.accesstoken_decrypted is None:
            print("Credenciales no disponibles. Asegúrese de que las credenciales estén desencriptadas correctamente.")
            return

        # Obtener la información de la API
        # current_timestamp = int(time.time() * 1000)
        url = "https://euapi.ttlock.com/v3/lock/list"
        params = {
            'clientId': self.cliente_id_decrypted,
            'accessToken': self.accesstoken_decrypted,
            'pageNo': 1,
            'pageSize': 20,
            'date': self.current_timestamp,
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
                    lock_name = lock.get('lockAlias', 'N/A')
                    self.list_door.addItem(lock_name)
            except json.JSONDecodeError:
                print("Error al decodificar la respuesta JSON.")
        else:
            print(f"Error en la solicitud: {response.status_code}")

    def show_door_info(self):
        # Asegurarse de que las credenciales estén desencriptadas
        if self.cliente_id_decrypted is None or self.accesstoken_decrypted is None:
            print("Credenciales no disponibles. Asegúrese de que las credenciales estén desencriptadas correctamente.")
            return
        
        selected_lock_name = self.list_door.currentText()
        selected_lock = next((lock for lock in self.locks_list if lock.get('lockAlias') == selected_lock_name), None)
        
        if selected_lock:
            lock_alias = selected_lock.get('lockAlias', 'N/A')
            self.get_hotel_lock_list(self.cliente_id_decrypted, self.accesstoken_decrypted, lock_alias=lock_alias)

    def get_key_master(self, data):
        self.cliente_id_decrypted = self.desencriptar(data[1])
        self.accesstoken_decrypted = self.desencriptar(data[2])
        if self.cliente_id_decrypted and self.accesstoken_decrypted:
            self.update_door_list()

    def generate_random_code(self, cl_id, cl_scrt, lock_id, time_srt, time_end):
        print(cl_id, cl_scrt, lock_id, time_srt, time_end)
        # current_timestamp = int(time.time() * 1000)
        url = "https://euapi.ttlock.com/v3/keyboardPwd/get"

        # Datos de la solicitud
        data = {
            'clientId': cl_id,
            'accessToken': cl_scrt,
            'lockId': lock_id,
            'keyboardPwdType': 3,
            'keyboardPwdName': 'test',
            'startDate': time_srt,
            'endDate': time_end,
            'date': self.current_timestamp
        }

        # Realizar la solicitud POST
        response = requests.post(url, data=data)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            try:
                # Intentar cargar el JSON solo si la respuesta no está vacía
                result = response.json()
                keyboard_pwd = result.get('keyboardPwd')
                keyboard_pwd_id = result.get('keyboardPwdId')
                # QMessageBox.critical(None, "Error", f"Response Content: {response.text}")
                print(f"Response Content: {response.text}")
                print(f"Passcode: {keyboard_pwd}")
                print(f"Passcode ID: {keyboard_pwd_id}")

                # Mostrar el código en list_randon_code
                if keyboard_pwd and keyboard_pwd_id:
                    # Agregar cabeceras si no están configuradas
                    if self.list_randon_code.columnCount() == 0:
                        headers = ["Passcode", "Passcode ID"]
                        self.list_randon_code.setColumnCount(len(headers))
                        self.list_randon_code.setHorizontalHeaderLabels(headers)
                        
                    # Obtener el número actual de filas
                    row_position = self.list_randon_code.rowCount()
                    # Añadir una fila
                    self.list_randon_code.insertRow(row_position)
                    # Añadir datos a la fila
                    self.list_randon_code.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(keyboard_pwd)))
                    self.list_randon_code.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(keyboard_pwd_id)))

            except json.decoder.JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
            # Imprimir el contenido de la respuesta en caso de un código de estado 400
            if response.status_code == 400:
                print(f"Contenido de la respuesta: {response.text}")

    def get_hotel_lock_list(self, client_id, access_token, page_no=1, page_size=20, group_id=None, lock_type=1, lock_alias=None):
        # Endpoint de la API
        url = 'https://euapi.ttlock.com/v3/lock/listByHotel'

        # Parámetros de la solicitud
        params = {
            'clientId': client_id,
            'accessToken': access_token,
            'pageNo': page_no,
            'pageSize': page_size,
            'date': self.current_timestamp,     # date if date else self.current_timestamp,  # Timestamp actual si no se proporciona
            'type': lock_type,
        }

        # Agregar parámetros opcionales si se proporcionan
        if group_id is not None:
            params['groupId'] = group_id
        if lock_alias is not None:
            params['lockAlias'] = lock_alias

        # Realizar la solicitud GET
        response = requests.get(url, params=params)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            try:
                # Parsear la respuesta JSON
                data = response.json()

                if data and 'list' in data:
                    # Suponiendo que solo queremos el primer candado encontrado
                    lock = data['list'][0] if data['list'] else None
                    if lock:
                        lock_id = lock.get('lockId', 'N/A')
                        lock_name = lock.get('lockName', 'N/A')
                        lock_alias = lock.get('lockAlias', 'N/A')
                        build_number = lock.get('buildNumber', 'N/A')
                        floor_number = lock.get('floorNumber', 'N/A')
                        has_gateway = lock.get('hasGateway', 'N/A')
                        electric_quantity = lock.get('electricQuantity', 0)
                        # Actualizar el campo de entrada con el lockId
                        self.lock_id_entry.setText(str(lock_id))

                        # Actualizar la barra de estado de la batería
                        self.batery_status.setValue(electric_quantity)

                        # Agregar cabeceras
                        headers = ["Lock ID", "Lock Alias", "Lock Name", "Build", "Floor", "Gateway"]
                        self.tableWidget.setColumnCount(len(headers))
                        self.tableWidget.setHorizontalHeaderLabels(headers)

                        # Establecer el número de filas
                        self.tableWidget.setRowCount(1)

                        # Llenar la tabla con la información del candado seleccionado
                        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(lock_id)))
                        self.tableWidget.setItem(0, 1, QTableWidgetItem(lock_alias))
                        self.tableWidget.setItem(0, 2, QTableWidgetItem(lock_name))
                        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(build_number)))
                        self.tableWidget.setItem(0, 4, QTableWidgetItem(str(floor_number)))
                        self.tableWidget.setItem(0, 5, QTableWidgetItem(str(has_gateway)))
                    else:
                        print("No se encontraron cerraduras en la respuesta.")
            except json.decoder.JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
            # Imprimir el contenido de la respuesta en caso de un error
            print(f"Contenido de la respuesta: {response.text}")

    def control_lock(self, command):
        # Endpoint de la API
        url = 'https://euapi.ttlock.com/v3/lock/control'
        
        # Parámetros de la solicitud
        data = {
            'clientId': self.cliente_id_decrypted,
            'accessToken': self.accesstoken_decrypted,
            'lockId': self.lock_id_entry,
            'command': command,
            'date': self.current_timestamp
        }
        
        # Hacer la solicitud POST
        response = requests.post(url, data=data)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
            self.on_off_button

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# pyuic5 -o xxxxxx.py TTlock.ui
    

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# from PyQt5.QtCore import Qt

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("On/Off Button Example")
#         self.setGeometry(100, 100, 300, 200)
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout(self)
        
#         # Crear el botón de encendido/apagado
#         self.on_off_button = QPushButton(self)
#         self.on_off_button.setCheckable(True)
#         self.on_off_button.setFixedSize(60, 30)
#         self.on_off_button.setStyleSheet(self.get_style_sheet(False))
#         self.on_off_button.setChecked(False)
#         self.on_off_button.toggled.connect(self.on_toggle)
        
#         layout.addWidget(self.on_off_button)
#         self.setLayout(layout)

#     def on_toggle(self, checked):
#         # Cambiar el estilo dependiendo del estado
#         self.on_off_button.setStyleSheet(self.get_style_sheet(checked))

#     def get_style_sheet(self, checked):
#         if checked:
#             # Encendido: verde
#             return """
#             QPushButton {
#                 background-color: green;
#                 border-radius: 15px;
#                 border: 2px solid #555;
#                 color: white;
#                 text-align: left;
#                 padding-left: 10px;
#             }
#             QPushButton:checked {
#                 background-color: green;
#                 color: white;
#             }
#             """
#         else:
#             # Apagado: rojo
#             return """
#             QPushButton {
#                 background-color: red;
#                 border-radius: 15px;
#                 border: 2px solid #555;
#                 color: white;
#                 text-align: right;
#                 padding-right: 10px;
#             }
#             QPushButton:!checked {
#                 background-color: red;
#                 color: white;
#             }
#             """

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()


# ----------------------------------------------------------------



# import requests
# from datetime import datetime

# def control_lock(client_id, access_token, lock_id, command):
#     # Endpoint de la API
#     url = 'https://euapi.ttlock.com/v3/lock/control'
    
#     # Obtener la hora actual en milisegundos
#     timestamp = int(datetime.now().timestamp() * 1000)
    
#     # Parámetros de la solicitud
#     data = {
#         'clientId': client_id,
#         'accessToken': access_token,
#         'lockId': lock_id,
#         'command': command,
#         'date': timestamp
#     }
    
#     # Hacer la solicitud POST
#     response = requests.post(url, data=data)
    
#     # Verificar si la solicitud fue exitosa
#     if response.status_code == 200:
#         return response.json()
#     else:
#         response.raise_for_status()

# # Parámetros para la solicitud
# client_id = '4773aa036f7f49c68d876bb4be85c80c'
# access_token = 'dfd5489d0cee31f0bdfaf59d0d42d71f'
# lock_id = 163377
# command = 1  # 1 para abrir, 2 para cerrar

# # Controlar la cerradura
# try:
#     result = control_lock(client_id, access_token, lock_id, command)
#     print("Resultado del comando de cerradura:", result)
# except Exception as e:
#     print("Error al controlar la cerradura:", e)


# =================================================================

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect

class CustomButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCheckable(True)
        self.setFixedSize(60, 30)  # Tamaño del botón más pequeño
        
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        radius = 15  # Radio de las esquinas redondeadas (mitad de la altura del botón)
        circle_diameter = 20  # Diámetro del círculo (ajustado para que quepa en el botón)
        
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
        painter.setFont(QFont('Arial', 6, QFont.Bold))  # Tamaño de fuente ajustado para el nuevo tamaño del botón
        text_rect = QRect(circle_rect.x(), circle_rect.y(), circle_diameter, circle_diameter)
        painter.drawText(text_rect, Qt.AlignCenter, circle_text)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("On/Off Button Example")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Crear el botón personalizado
        self.on_off_button = CustomButton(self)
        self.on_off_button.toggled.connect(self.on_toggle)
        
        layout.addWidget(self.on_off_button)
        self.setLayout(layout)

    def on_toggle(self, checked):
        # El botón se actualiza automáticamente debido al método paintEvent
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from login.Admin_panel_lock import Ui_MainWindow
import sys
from login.gui_register import Ui_Register_ttlock
from voices.voices import talk
from conexion.linked import establecer_conexion
from security.protect import (verificar_hash,
                              verificar_len_password,
                              verificar_capital_password,
                              verificar_digit_password,
                              verificar_illegal_character_password,
                              verificar_space_password,
                              verificar_exist_password_login,
                              )

class Estructured(QMainWindow):
    def __init__(self):
        super(Estructured, self).__init__()
        loadUi('interface\\Login.ui', self)

        
        # Controladores
        self.sign_in_button.clicked.connect(self.login)
        self.sign_up_button.clicked.connect(self.register)

        self.password_input.returnPressed.connect(self.sign_in_button.click)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.checkBox_login.stateChanged.connect(self.toggle_password_visibility)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x3:1, y2:2, stop:0 rgba(195, 233, 154, 255), stop:1 rgba(1, 229, 161, 255));")

        # Ajustes
        self.setWindowTitle("Login")

        # Deshabilitar botón de maximizar y evitar redimensionamiento
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setFixedSize(self.size())
        

    def toggle_password_visibility(self, state):
        if state == Qt.Checked:
            self.password_input.setEchoMode(QLineEdit.Normal)  # Mostrar contraseña
        else:
            self.password_input.setEchoMode(QLineEdit.Password)  # Mostrar asteriscos

    def login(self):
        user = self.user_input.text()
        password = self.password_input.text()
        if not user or not password:
            QMessageBox.critical(self, "Error", "Por favor, introduce un nombre de usuario y una contraseña.")
            return
        
        if verificar_exist_password_login(user, password) and \
                verificar_len_password(password) and \
                verificar_space_password(password) and \
                verificar_capital_password(password) and \
                verificar_digit_password(password) and \
                verificar_illegal_character_password(password):
            pass
        
        # Conexión a la base de datos
        conn = establecer_conexion()
        cursor = conn.cursor()

        try:
            # Busca el usuario en la base de datos
            cursor.execute('SELECT hashed_password, salt FROM TT_Users WHERE User=?', (user,))
            result = cursor.fetchone()

            if result:
                hashed_password, salt = result
                if verificar_hash(password, hashed_password, salt):
                    talk(f"Bienvenido, {user}!")
                    print(f"Bienvenido, {user}")

                    # Cierra la ventana de inicio de sesión y abre el panel de administración
                    self.open_admin_panel(user) # Pasa el usuario al abrir el panel de administración
                else:
                    QMessageBox.critical(self, "Error", "Contraseña incorrecta. Acceso denegado.")
            else:
                QMessageBox.critical(self, "Error", "Usuario no encontrado. Acceso denegado.")
        finally:
            conn.close()

    def open_admin_panel(self, user):
        self.hide()  # Oculta la ventana de inicio de sesión
        self.admin_panel = QtWidgets.QMainWindow()  # Crea una nueva ventana
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.admin_panel)
        self.ui.set_user_label(user)  # Pasa el nombre de usuario al panel de administración
        self.admin_panel.show()

    def register(self):
        self.ventana = QtWidgets.QMainWindow()
        self.uir = Ui_Register_ttlock()
        self.uir.setupUi(self.ventana)
        self.ventana.show()


def init():
    app = QApplication(sys.argv)
    login_window = Estructured()
    login_window.show()
    sys.exit(app.exec_())

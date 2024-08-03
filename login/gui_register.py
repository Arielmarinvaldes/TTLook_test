
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

import time
import requests
import os
import json
import hashlib
from Crypto.Random import get_random_bytes
from conexion.linked import establecer_conexion
from voices.voices import talk
from security.protect import (hash_password,
                              verificar_len_password,
                              verificar_capital_password,
                              verificar_digit_password,
                              verificar_illegal_character_password,
                              verificar_space_password,
                              verificar_exist_password_regist,
                              encrypt,
                              verification_key_encriptor,
                              )



class Ui_Register_ttlock(object):
    def setupUi(self, Register_ttlock):
        Register_ttlock.setObjectName("Register_ttlock")
        Register_ttlock.resize(390, 470)
        Register_ttlock.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Register_ttlock)
        self.centralwidget.setObjectName("centralwidget")
        self.name_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.name_entry.setGeometry(QtCore.QRect(111, 60, 190, 25))
        self.name_entry.setObjectName("name_entry")
        self.cliente_id_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.cliente_id_entry.setGeometry(QtCore.QRect(111, 110, 190, 25))
        self.cliente_id_entry.setObjectName("cliente_id_entry")
        self.cliente_secret_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.cliente_secret_entry.setGeometry(QtCore.QRect(111, 160, 190, 25))
        self.cliente_secret_entry.setObjectName("cliente_secret_entry")
        self.user_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.user_entry.setGeometry(QtCore.QRect(111, 210, 190, 25))
        self.user_entry.setObjectName("user_entry")
        self.password_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.password_entry.setGeometry(QtCore.QRect(111, 250, 190, 25))
        self.password_entry.setObjectName("password_entry")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(140, 390, 121, 41))
        self.register_button.setStyleSheet("")
        self.register_button.setObjectName("register_button")
        self.client_id_label = QtWidgets.QLabel(self.centralwidget)
        self.client_id_label.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.client_id_label.setObjectName("client_id_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.name_label.setObjectName("name_label")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.user_label.setObjectName("user_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 260, 71, 16))
        self.password_label.setObjectName("password_label")
        self.client_secret_label = QtWidgets.QLabel(self.centralwidget)
        self.client_secret_label.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.client_secret_label.setObjectName("client_secret_label")
        self.register_label = QtWidgets.QLabel(self.centralwidget)
        self.register_label.setGeometry(QtCore.QRect(160, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.register_label.setFont(font)
        self.register_label.setObjectName("register_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-70, -30, 511, 551))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x3:1, y2:2, stop:0 rgba(195, 233, 154, 255), stop:1 rgba(1, 229, 161, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.key_label = QtWidgets.QLabel(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(130, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.key_label.setFont(font)
        self.key_label.setObjectName("key_label")
        self.key_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.key_entry.setGeometry(QtCore.QRect(110, 320, 190, 25))
        self.key_entry.setToolTip("")
        self.key_entry.setAccessibleDescription("")
        self.key_entry.setObjectName("key_entry")
        self.frame.raise_()
        self.name_entry.raise_()
        self.cliente_id_entry.raise_()
        self.cliente_secret_entry.raise_()
        self.user_entry.raise_()
        self.password_entry.raise_()
        self.register_button.raise_()
        self.client_id_label.raise_()
        self.name_label.raise_()
        self.user_label.raise_()
        self.password_label.raise_()
        self.client_secret_label.raise_()
        self.register_label.raise_()
        self.key_label.raise_()
        self.key_entry.raise_()
        Register_ttlock.setCentralWidget(self.centralwidget)

        # Deshabilitar botón de maximizar y evitar redimensionamiento
        Register_ttlock.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        Register_ttlock.setFixedSize(Register_ttlock.size())

        self.retranslateUi(Register_ttlock)
        QtCore.QMetaObject.connectSlotsByName(Register_ttlock)
        self.key_entry.setPlaceholderText("Obliged 16 or 24 or 32 characters")

    def retranslateUi(self, Register_ttlock):
        _translate = QtCore.QCoreApplication.translate
        Register_ttlock.setWindowTitle(_translate("Register_ttlock", "MainWindow"))
        self.register_button.setText(_translate("Register_ttlock", "Register"))
        self.client_id_label.setText(_translate("Register_ttlock", "Client ID :"))
        self.name_label.setText(_translate("Register_ttlock", "Name :"))
        self.user_label.setText(_translate("Register_ttlock", "User :"))
        self.password_label.setText(_translate("Register_ttlock", "Password :"))
        self.client_secret_label.setText(_translate("Register_ttlock", "Client Secret :"))
        self.register_label.setText(_translate("Register_ttlock", "Register"))
        self.key_label.setText(_translate("Register_ttlock", "Don\'t forget this key"))
        self.register_button.clicked.connect(self.get_token_manager)


    def get_token_manager(self):
        cl_id = self.cliente_id_entry.text()
        cl_scrt = self.cliente_secret_entry.text()
        usr = self.user_entry.text()
        pasw = self.password_entry.text()
        key_text = self.key_entry.text()
        name = self.name_entry.text()

        url = "https://euapi.ttlock.com/oauth2/token"

        # Datos de la solicitud
        data = {
            'clientId': cl_id,
            'clientSecret': cl_scrt,
            'username': usr,
            'password': hashlib.md5(pasw.encode()).hexdigest()
        }

        # Realizr la solicitud POST
        response = requests.post(url, data=data)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            try:
                # Intentar cargar el JSON solo si la respuesta no está vacía
                result = response.json()
                access_token = result.get('access_token')
                uid = result.get('uid')
                expires_in = result.get('expires_in')
                refresh_token = result.get('refresh_token')

                self.registers(usr, pasw, cl_id, cl_scrt, access_token, key_text, name)

            except json.decoder.JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
            # Imprimir el contenido de la respuesta en caso de un código de estado 400
            if response.status_code == 400:
                print(f"Contenido de la respuesta: {response.text}")
        return
    
    def registers(self, usr, pasw, cl_id, cl_scrt, tkn, key, name):
        self.u = QtWidgets.QMainWindow()
        
        hashed_password, salt, = hash_password(pasw)

        if verificar_len_password(pasw) and \
                verificar_space_password(pasw) and \
                verificar_capital_password(pasw) and \
                verificar_digit_password(pasw) and \
                verificar_exist_password_regist(usr, pasw, name) and \
                verificar_illegal_character_password(pasw) and \
                verification_key_encriptor(key):
            pass

        else:
            talk("Contraseña no válida.")
            return
        key_bytes = key.encode('utf-8')
        cliente_id_encrypted = encrypt(cl_id, key_bytes)
        cliente_secreto_encrypted = encrypt(cl_scrt, key_bytes)
        token_encrypted = encrypt(tkn, key_bytes)

        conn = establecer_conexion()

        try:
            # Insertar datos en la base de datos
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO TT_Users (Name, User, Cliente_ID, Cliente_Secret, hashed_password, salt, Token) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (name, usr, cliente_id_encrypted, cliente_secreto_encrypted, hashed_password, salt, token_encrypted))
            conn.commit()
            QMessageBox.information(self.u, "Éxito", "Usuario creado con éxito")
            
            talk("Ya puede iniciar seción")
            
            self.name_entry.clear()
            self.cliente_id_entry.clear()
            self.cliente_secret_entry.clear()
            self.user_entry.clear()
            self.password_entry.clear()
            self.key_entry.clear()
            self.u.close()
        except Exception as e:
            QMessageBox.critical(self.u, "Error", f"Error al crear usuario: {e}")

        finally:
            conn.close()

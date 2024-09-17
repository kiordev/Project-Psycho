import flet as ft
import json
from cryptography.fernet import Fernet
from design import *
import os

# Путь к файлам
json_file = "patients.json"
encrypted_file = "patients_encrypted.json"
key_file = "secret.key"

# Функции для работы с шифрованием

# Функция для генерации ключа шифрования
def generate_key():
    key = Fernet.generate_key()
    with open(key_file, "wb") as key_out:
        key_out.write(key)

# Функция для чтения ключа
def load_key():
    if not os.path.exists(key_file):
        generate_key()
    with open(key_file, "rb") as key_in:
        return key_in.read()

# Функция для шифрования данных
def encrypt_data():
    key = load_key()
    fernet = Fernet(key)

    # Чтение содержимого файла JSON
    with open(json_file, "rb") as file:
        file_data = file.read()

    # Шифрование данных
    encrypted_data = fernet.encrypt(file_data)

    # Запись зашифрованных данных в новый файл
    with open(encrypted_file, "wb") as enc_file:
        enc_file.write(encrypted_data)
    
    with open("patients.json", "w") as file:
        pass

# Функция для дешифрования данных
def decrypt_data():
    key = load_key()
    fernet = Fernet(key)

    # Чтение зашифрованного файла
    if os.path.exists(encrypted_file):
        with open(encrypted_file, "rb") as enc_file:
            encrypted_data = enc_file.read()

        # Дешифрование данных
        decrypted_data = fernet.decrypt(encrypted_data)

        # Запись расшифрованных данных в файл
        with open(json_file, "wb") as file:
            file.write(decrypted_data)
    else:
        print("Зашифрованный файл не найден!")

# Функции для обработки событий кнопок
def encrypt_button_click(e):
    encrypt_data()
    print("Файл зашифрован и сохранён как", encrypted_file)

def decrypt_button_click(e):
    decrypt_data()
    print("Файл расшифрован и сохранён как", json_file)

# Кнопки кодирования
encryptionButton = ft.ElevatedButton(
    "Кодування бази", 
    icon="enhanced_encryption",
    width=250,
    height=50,
    bgcolor=prime_color,
    color=light_color,
    on_click=encrypt_button_click,
)
dencryptionButton = ft.ElevatedButton(
    "Роскодування бази", 
    icon="no_encryption",
    width=250,
    height=50,
    bgcolor=prime_color,
    color=light_color,
    on_click=decrypt_button_click
)

# Надпись статуса кодирования
codeStatusText = ft.Text("Кодування успешное!", size=25, weight=ft.FontWeight.W_600, color="green")

# Ряд для кнопок
encryptionButtonRow = ft.Row([encryptionButton, dencryptionButton],  alignment=ft.MainAxisAlignment.CENTER, spacing=15)

# Колонка для отображения данных из поиска
dataBaseColumn = ft.Column([encryptionButtonRow, codeStatusText], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

# Вторичное окно со всеми элементами
encryptionScreenMainContainer =  ft.Container(
    height=430, 
    width=750, 
    bgcolor=light_color, 
    content=dataBaseColumn)

# Основная колонка экрана
encryptionScreenMainColumn = ft.Column([
    ft.Text("Кодування даних", size=25, weight=ft.FontWeight.W_600, color=prime_color),
    encryptionScreenMainContainer,
], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5)

# Экран поиска
encryptionScreen = ft.Container(
    bgcolor=light_color, 
    width=200,
    height=600,
    content=encryptionScreenMainColumn,  
)
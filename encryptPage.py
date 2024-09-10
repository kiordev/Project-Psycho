import flet as ft
import json
from design import *

# Колонка для отображения данных из поиска
dataBaseColumn = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.START)

# Основная колонка экрана
encryptionScreenScreenMainColumn = ft.Column([
    ft.Text("Кодування даних", size=25, weight=ft.FontWeight.W_600, color=prime_color),
    ft.Container(height=350, width=600, bgcolor="white", content=dataBaseColumn),
], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5)

# Экран поиска
encryptionScreen = ft.Container(
    bgcolor=light_color, 
    width=200,
    height=600,
    content=encryptionScreenScreenMainColumn,  
)
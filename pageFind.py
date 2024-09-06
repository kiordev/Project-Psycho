import flet as ft
from design import *

# Функция для добавления текста (временная)
def addText(e):
    dataBaseColumn.controls.append(ft.Text(searchTextField.value))
    dataBaseColumn.update()

dataBaseColumn = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.START)
searchTextField = ft.TextField(label="Введіть запит", width=600)

findScreenMainColumn = ft.Column([
    ft.Text("ПОШУК", size=25, weight=ft.FontWeight.W_600, color=prime_color),
    searchTextField,
    ft.Container(height=350, width=600, bgcolor="white", content=dataBaseColumn),
], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5
)

findScreen = ft.Container(
    bgcolor=light_color, 
    width=200,
    height=600,
    content=findScreenMainColumn,  
)


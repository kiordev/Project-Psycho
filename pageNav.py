import flet as ft
from design import *

def main(page: ft.Page):
    # Page Settings
    page.title = "Med Storage Application"
    page.window_height = 600
    page.window_width = 1000
    page.window_resizable = True
    page.padding = 0

    leftPrimeContaierColumn = ft.Column([
        ft.ElevatedButton("Добавить пациента"),
        ft.ElevatedButton("Найти пациента"),
        ft.ElevatedButton("Инструкции"),
    ])

    # Левый контейнер
    leftPrimContainer = ft.Container(bgcolor=light_color, expand=2, content=leftPrimeContaierColumn, padding=10)

    # Правый контейнер
    rightPrimContainer = ft.Container(bgcolor=dark_color, expand=7)

    # Главный ряд
    primRow = ft.Row([leftPrimContainer, ft.VerticalDivider(width=1), rightPrimContainer], spacing=0, expand=8)

    # Контейнер с информацией
    namePrimContainer = ft.Container(content=ft.Text("MED STORAGE APPLICATION", size=25, weight=ft.FontWeight.W_500), bgcolor=sec_color, width=1000, expand=1, padding=10)
   
    # Главная колонка
    mainColumn = ft.Column([namePrimContainer, primRow], spacing=1)

    # Главный контейнер
    mainContainer = ft.Container(content=mainColumn, bgcolor=sec_color, expand=8)

    page.add(mainContainer)
    

ft.app(target=main)
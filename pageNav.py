import flet as ft
from design import *

def main(page: ft.Page):
    # Page Settings
    page.title = "Med Storage Application"
    page.icon = "assets/icon.png"
    page
    page.window_height = 600
    page.window_width = 1000
    page.window_resizable = True
    page.window_maximizable = False 
    page.padding = 0

    # Кнопки

    # Кнопка ДОБАВИТЬ ПАЦИЕНТА
    addPatientButton = ft.ElevatedButton(
        "Добавить", 
        icon="ADD",
        width=150,
        height=50,
        bgcolor=prime_color,
        style=ft.ButtonStyle(
        color={"2313": ft.colors.WHITE}  # Задаем цвет текста (например, белый)
        )
    )
    
    # Кнопка НАЙТИ ПАЦИЕНТА
    findPatientButton = ft.OutlinedButton(
        content=
            ft.Row([
                ft.Icon(name=ft.icons.SEARCH, color=prime_color),
                ft.Text("Найти", color=prime_color),
            ], alignment=ft.MainAxisAlignment.START, spacing=15),
        width=150,
        height=50,
        
    )
    # Кнопка ПРАВИЛА
    FAQPatientButton = ft.OutlinedButton(
        content=
            ft.Row([
                ft.Icon(name=ft.icons.WARNING, color=prime_color),
                ft.Text("Правила", color=prime_color),
            ], alignment=ft.MainAxisAlignment.START, spacing=15),
        width=150,
        height=50,
    )

    # Колонка для кнопок
    leftPrimeContaierColumn = ft.Column([
        ft.Container(alignment=ft.alignment.bottom_center, content=ft.Icon(name=ft.icons.LOCAL_HOSPITAL, color=prime_color, size=50)),
        addPatientButton,
        findPatientButton,
        FAQPatientButton,
        ft.Container(alignment=ft.alignment.bottom_left, content=ft.Text("Версия 0.1", text_align=ft.alignment.bottom_center, color=prime_color)),
    ], 
    )

    # Контейнер с информацией
    namePrimContainer = ft.Container(
        width=1000,
        height=70,
        bgcolor=prime_color,
        alignment=ft.alignment.center,
        content=ft.Text(
            "MEDICAL STORAGE SYSTEM", 
            color=light_color, 
            size=35, 
            weight=ft.FontWeight.W_700,
            )
        )

    # Левый контейнер
    leftPrimContainer = ft.Container(
        bgcolor=light_color, 
        expand=2, 
        content=leftPrimeContaierColumn, 
        padding=10)

    # Правый контейнер
    rightPrimContainer = ft.Container(
        bgcolor=light_color, 
        expand=9)

    # Главный ряд для левого и правого контейнера
    primRow = ft.Row([leftPrimContainer, ft.VerticalDivider(width=1), rightPrimContainer], 
                     spacing=0, expand=8)

    # Главная колонка
    mainColumn = ft.Column([namePrimContainer,ft.Divider(height=1),primRow], 
                           spacing=0)

    # Главный контейнер
    mainContainer = ft.Container(
        content=mainColumn, 
        bgcolor=sec_color, 
        expand=8)

    page.add(mainContainer)
    

ft.app(target=main)
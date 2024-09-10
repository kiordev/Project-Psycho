import flet as ft
from design import *
from pageFind import *
from pageRules import *
from addPatient import *
from encryptPage import *

def main(page: ft.Page):
    # Page Settings
    page.title = "Система адміністрування пацієнтів"
    page.window_height = 600
    page.window_width = 1000
    page.window_resizable = False
    page.window_maximizable = False 
    page.padding = 0

    # Функции переключения экранов
    def FindScreenRaise(e):
        rightPrimContainer.content = findScreen
        page.update()

    def RuleScreenRaise(e):
        rightPrimContainer.content = ruleScreen
        page.update()

    def AddPatientScreenRaise(e):
        rightPrimContainer.content = patientScreen
        page.update()
    
    def encryptionScreenRaise(e):
        rightPrimContainer.content = encryptionScreen
        page.update()

    # Кнопки

    # Кнопка ДОБАВИТЬ ПАЦИЕНТА
    addPatientButton = ft.ElevatedButton(
        "Додати", 
        icon="ADD",
        width=150,
        height=50,
        bgcolor=prime_color,
        color=light_color,
        on_click=AddPatientScreenRaise
    )
    encryptionButton = ft.ElevatedButton(
        "Кодування", 
        icon="KEY",
        width=150,
        height=50,
        bgcolor=sec_color,
        color=light_color,
        on_click=encryptionScreenRaise
    )

    # Кнопка быстрое добавление
    
    # Кнопка НАЙТИ ПАЦИЕНТА
    findPatientButton = ft.OutlinedButton(
        content=
            ft.Row([
                ft.Icon(name=ft.icons.SEARCH, color=prime_color),
                ft.Text("Знайти", color=prime_color),
            ], alignment=ft.MainAxisAlignment.START, spacing=15),
        width=150,
        height=50,
        on_click=FindScreenRaise,
        
    )
    # Кнопка ПРАВИЛА
    FAQPatientButton = ft.OutlinedButton(
        content=
            ft.Row([
                ft.Icon(name=ft.icons.WARNING, color=prime_color),
                ft.Text("Інструкція", color=prime_color),
            ], alignment=ft.MainAxisAlignment.START, spacing=15),
        width=150,
        height=50,
        on_click=RuleScreenRaise
    )

    # Колонка для кнопок
    leftPrimeContaierColumn = ft.Column([
        ft.Container(alignment=ft.alignment.bottom_center, content=ft.Icon(name=ft.icons.LOCAL_HOSPITAL, color=prime_color, size=50)),
        addPatientButton,
        encryptionButton,
        findPatientButton,
        FAQPatientButton,
        ft.Container(alignment=ft.alignment.bottom_left, content=ft.Text("Версія 0.7.5", text_align=ft.alignment.bottom_center, color=prime_color)),
    ], 
    )

    # Контейнер с информацией
    namePrimContainer = ft.Container(
        width=1000,
        height=70,
        bgcolor=prime_color,
        alignment=ft.alignment.center,
        content=ft.Text(
            "СИСТЕМА АДМІНІСТРУВАННЯ ПАЦІЄНТІВ", 
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
        expand=9,
        width=300,     
        height=600,
        )

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
        expand=9)

    page.add(mainContainer)
    

ft.app(target=main)
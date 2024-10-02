import flet as ft
from design import *
import subprocess

def main(page: ft.Page):
    page.title = "Система адміністрування пацієнтів"
    page.bgcolor = light_color
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_height = 500
    page.window_width = 350
    page.window_resizable = False
    page.window_maximizable = False 
    page.padding = 0

    password = "123"
    login = "123"

    def button_clicked(e):
        if loginfield.value == login and passfield.value == password:
            enterText.value = "Вітаємо!"
            enterText.size = 20
            enterText.color = ft.colors.GREEN
            page.update()

            # Запускаем файл pageNav.py
            subprocess.run(["python", "pageNav.py"], check=True)

        else:
            enterText.value = "Невірні дані"
            enterText.size = 20
            enterText.color = ft.colors.RED
            page.update()

    # Главная надпись
    mainText = ft.Text("Увійти", 
                       size=30, 
                       weight=ft.FontWeight.BOLD, 
                       color=prime_color)
    # Логин
    loginfield = ft.TextField(label="Логін", hint_text="Введіть ваш логін", width=300, border_color=prime_color, color="black")

    # Пароль
    passfield = ft.TextField(label="Пароль", hint_text="Введіть ваш пароль", width=300, border_color=prime_color, color="black", password=True)

    # Кнопка Принять
    accept = ft.ElevatedButton("Увійти", bgcolor=prime_color, color=light_color, width=250, height=50, on_click=button_clicked)

    # Входящее сообщение
    enterText = ft.Text("Обліковий запис", 
                       size=0, 
                       weight=ft.FontWeight.BOLD, 
                       color=ft.colors.GREEN)
    
    mainIcon = ft.Icon(name=ft.icons.LOCAL_HOSPITAL, color=prime_color, size=50)

    # Главный столбик с элементами
    mainColumn = ft.Column(controls=[mainIcon, mainText, loginfield, passfield, accept, enterText], 
                           alignment=ft.MainAxisAlignment.CENTER,
                           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                           spacing=20)

    # Главный контейнер
    mainForm = ft.Container(
        content=mainColumn,
        height=500,
        width=350,
        bgcolor=light_color,
        border_radius=0,
        alignment=ft.alignment.center
    )

    page.add(mainForm)

ft.app(target=main)

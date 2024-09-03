import flet as ft

def main(page: ft.Page):
    page.title = "Container Test" # Название страницы
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Группировка по У
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Группировка по Х

    blue = ft.Container(
        content=ft.Text("Non clickable"), # Контент внутри контейнера
        margin=10,
        padding=10,
        alignment=ft.alignment.center, # Группировка внутри контейнера
        bgcolor=ft.colors.BLUE_500,
        width=150,
        height=150,
        border_radius=10,

    )
    red = ft.Container(
        content=ft.Text("Clickable without Ink"), # Контент внутри контейнера
        margin=10,
        padding=10,
        alignment=ft.alignment.center, # Группировка внутри контейнера
        bgcolor=ft.colors.BLUE_500,
        width=150,
        height=150,
        border_radius=10,
    
    )
    green = ft.Container(
        content=ft.Text("Non clickable"), # Контент внутри контейнера
        margin=10,
        padding=10,
        alignment=ft.alignment.center, # Группировка внутри контейнера
        bgcolor=ft.colors.BLUE_500,
        width=150,
        height=150,
        border_radius=10,

    )

    page.add())

ft.app(main)

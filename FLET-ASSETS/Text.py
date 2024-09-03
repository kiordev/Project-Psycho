import flet as ft

def main(page: ft.Page):
    page.title = "Container Test" # Название страницы
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Группировка по У
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Группировка по Х
    page.scroll = "adaptive"

    text = ft.Text()


    page.add(text)

ft.app(main)

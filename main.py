import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Default Name"
    page.bgcolor = "#94B5C1"
    page.add()

ft.app(target=main)
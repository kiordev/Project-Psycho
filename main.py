import flet as ft

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, flet!")))

ft.app(main)
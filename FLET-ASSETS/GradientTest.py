import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Background"
    page.bgcolor = "#94B5C1"


    A = ft.Container(
        width=100, 
        height=100,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PURPLE, ft.colors.PINK],
        ))
    
    B = ft.Container(
        width=100, 
        height=100, 
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PURPLE, ft.colors.PINK],
        ))
    
    C = ft.Container(
        width=100, 
        height=100, 
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PURPLE, ft.colors.PINK],
        ))
    
    mainRow = ft.Row([A,B,C], alignment=ft.MainAxisAlignment.CENTER)

    main = ft.Container(
        content=mainRow,
        width=600, 
        height=400, 
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PURPLE, ft.colors.PINK, ft.colors.BLUE],
        ))
    

    page.add(main)

ft.app(target=main)
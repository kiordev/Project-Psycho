import flet as ft

def main(page: ft.Page):
    page.title = "MedStorage"
    page.bgcolor = '#412544'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    password = "123"
    login = "123"

    def button_clicked(e):
        if loginfield.value==login and passfield.value==password:
            enterText.value = "Welcomme!"
            enterText.size = 20
            enterText.color = ft.colors.GREEN
            page.update()
        else:
            enterText.value = "Wrong data!"
            enterText.size = 20
            enterText.color = ft.colors.RED
            page.update()

    # Главная надпись
    mainText = ft.Text("Med Storage Login", 
                       size=30, 
                       weight=ft.FontWeight.BOLD, 
                       color=ft.colors.WHITE)
    # Логин
    loginfield = ft.TextField(label="Login", hint_text="Please enter login here", width=300)

    # Пароль
    passfield = ft.TextField(label="Password", hint_text="Please enter password here", width=300)

    # Кнопка Принять
    accept = ft.ElevatedButton("Accept", bgcolor=ft.colors.WHITE, color="#885F8D", width=250, height=50, on_click=button_clicked)

    # Входящее сообщение
    enterText = ft.Text("Med Storage Login", 
                       size=0, 
                       weight=ft.FontWeight.BOLD, 
                       color=ft.colors.GREEN)

    # Главный столбик с элементами
    mainColumn = ft.Column(controls=[mainText, loginfield, passfield, accept, enterText], 
                           alignment=ft.MainAxisAlignment.CENTER,
                           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                           spacing=35,
                           )

    # Главный контейнер
    mainForm = ft.Container(
        content=mainColumn,
        height=500,
        width=350,
        bgcolor="#885F8D",
        border_radius=20,
        alignment=ft.alignment.center
    )

    page.add(mainForm)

ft.app(target=main)
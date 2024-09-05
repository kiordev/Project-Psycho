import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Med Storage Data Base"
    page.bgcolor = "#94B5C1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Смена даты в поле
    def set_date(e):
        dateTextField.value = f"Birthday: {e.control.value.strftime('%Y-%m-%d')}"
        page.update()
    
    def add_patient(e):
        AcardColumn = ft.Column([
        ft.Row([
            ft.Text(nameTextField.value, size=25, weight=ft.FontWeight.W_700), 
            ft.Text(surnameTextField.value, size=25, weight=ft.FontWeight.W_700)
            ]),

        ft.Row([
            ft.Text(sexDropDown.value, size=15, color=ft.colors.GREY_500), 
            ft.Text(dateTextField.value, size=15, color=ft.colors.GREY_500)
            ]),

        ft.Row([
            ft.Text("Disorder: ", size=25, weight=ft.FontWeight.W_700), 
            ft.Text(disorderTextField.value, size=25, weight=ft.FontWeight.W_800),
            ]),
        ], 
        spacing=0
    )
    
        Acard = ft.Container(content=AcardColumn, bgcolor="#1E4951", width = 400, height=100, border_radius=10, margin=10, padding=5)
        RightMainColumn.controls.append(Acard)
        page.update()
        

    # Надпись регистрация
    regLabel = ft.Text("SIGN UP", size=35, weight=ft.FontWeight.W_700, color=ft.colors.GREY_200)
    # Поле Имя
    nameTextField = ft.TextField(label = "Name", width=270, height=50, hint_text="Enter patient name")
    # Поле Фамилия
    surnameTextField = ft.TextField(label= "Surname", width=270, height=50, hint_text="Enter patient surname")
    # Поле Дата
    dateTextField = ft.TextField(label="Birthday", width=270, height=50, read_only=True, hint_text="Pick date")
    # Календарь
    dateBasa = ft.DatePicker(first_date=datetime.datetime(year=1990, month=10, day=1),
                  last_date=datetime.datetime(year=2024, month=10, day=1),
                  on_change=set_date,
                )
    # Date Picker
    dateButton = ft.ElevatedButton("Pick date", icon=ft.icons.CALENDAR_MONTH, color=ft.colors.GREY_200, bgcolor="#192E32", on_click=lambda e: page.open(dateBasa)
    )
    # Поле Пол
    sexDropDown = ft.Dropdown(
        label="Sex",
        hint_text="Choose your sex",
        options=[
        ft.dropdown.Option("Male"),
        ft.dropdown.Option("Female"),
        ], width=270, height=50)
    
    # Поле Диагноз
    disorderTextField = ft.TextField(label= "Disorder", width=270, height=50, hint_text="Enter patient disorder")
    
    # Кнопка Подтверждения
    submitButton = ft.ElevatedButton("Submit", color=ft.colors.GREY_200, bgcolor="#192E32", icon=ft.icons.CHECK, on_click=add_patient)


    # Левая главная колонка
    LeftMainColumn = ft.Column([regLabel,nameTextField, surnameTextField, dateTextField, dateButton,  sexDropDown, disorderTextField, submitButton],
                               alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    # Левый главный контейнер
    LeftMainContainer = ft.Container(content=LeftMainColumn, bgcolor="#1E4951", expand=2)
    
    # Правая главная колонка
    RightMainColumn = ft.Column([], spacing=10, scroll=ft.ScrollMode.ALWAYS)

    # Правый главный контейнер
    RightMainContainer = ft.Container(content=RightMainColumn, bgcolor="#192E32", expand=3, alignment=ft.alignment.center)

    # Главный ряд
    mainRow = ft.Row([LeftMainContainer, RightMainContainer], spacing=0)

    # Главный контейнер
    mainContainer = ft.Container(content=mainRow, height=600, width=1000)

    page.add(mainContainer)

ft.app(target=main)
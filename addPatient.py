import flet as ft
from design import *
import datetime

# Поля для первого ряда
nameTextField = ft.TextField(label="Им'я", width=200)
lastNameTextField = ft.TextField(label="Прізвище", width=200)
AgeTextField = ft.TextField(label="Вік", width=100)
sexField = ft.Dropdown(
        label="Стать",
        hint_text="Оберіть стать",
        options=[
        ft.dropdown.Option("Чоловік"),
        ft.dropdown.Option("Жінка"),
        ], width=70)

# Ряд Имя Фамилия Пол Возраст
NameLastNameSexAgeRow = ft.Row(
    [nameTextField, lastNameTextField, AgeTextField, sexField])

# Поля для второго ряда
dateTextField = ft.TextField(label="Дата звернення", width=200, height=50, read_only=True, hint_text="Pick date")
disorderTextField = ft.TextField(label= "Діагноз", width=200, height=50, hint_text="Enter patient disorder")

# Ряд Дата Поступления Диагноз
DateDisorderRow = ft.Row([dateTextField, disorderTextField])

# Поля для третьего ряда
DrugTextField = ft.TextField(label="Препарат", width=305)
ValueTextField = ft.TextField(label="Доза", width=95)

# Лекарство доза кнопка
DrugsDoseSubmitRow = ft.Row([DrugTextField, ValueTextField])

addPatientButton = ft.ElevatedButton("Додати пацієнта", bgcolor=prime_color, color=light_color)

patientMainColumn = ft.Column(
    [ft.Text("Заповніть дані", size=25, color=prime_color, weight=ft.FontWeight.W_500), 
     NameLastNameSexAgeRow,
     ft.Text("Дата звернення / Призначення", size=25, color=prime_color, weight=ft.FontWeight.W_500),
     DateDisorderRow,
     ft.Text("Лікування", size=25, color=prime_color, weight=ft.FontWeight.W_500), 
     DrugsDoseSubmitRow,
     addPatientButton,
     ])

patientScreenSecondaryContainer = ft.Container(
    content=patientMainColumn,
    bgcolor=light_color,
    margin=30,
)

# Главный контейнер
patientScreen = ft.Container(
    bgcolor=light_color, 
    width=200,
    height=600,
    content=patientScreenSecondaryContainer
)


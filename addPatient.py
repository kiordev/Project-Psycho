import flet as ft
from design import *
import datetime
import json

# Функция для добавления данных в JSON файл
def add_patient(e):
    # Собираем данные из всех полей
    patient_data = {
        "name": nameTextField.value,
        "last_name": lastNameTextField.value,
        "age": AgeTextField.value,
        "sex": sexField.value,
        "date": dateTextField.value,
        "disorder": disorderTextField.value,
        "drug": DrugTextField.value,
        "dose": ValueTextField.value
    }
    
    # Загружаем существующие данные из JSON файла, если есть
    try:
        with open("patients.json", "r", encoding="utf-8") as file:
            patients_list = json.load(file)
    except FileNotFoundError:
        patients_list = []  # Если файл не найден, создаем новый список

    # Добавляем нового пациента в список
    patients_list.append(patient_data)

    # Сохраняем данные обратно в JSON файл
    with open("patients.json", "w", encoding="utf-8") as file:
        json.dump(patients_list, file, ensure_ascii=False, indent=4)

    # Очищаем поля после добавления пациента
    nameTextField.value = ""
    lastNameTextField.value = ""
    AgeTextField.value = ""
    sexField.value = None
    dateTextField.value = ""
    disorderTextField.value = ""
    DrugTextField.value = ""
    ValueTextField.value = ""

# Поля для первого ряда
nameTextField = ft.TextField(label="Им'я", width=200, border_color=prime_color, color="black")
lastNameTextField = ft.TextField(label="Прізвище", width=200, border_color=prime_color, color="black")
AgeTextField = ft.TextField(label="Вік", width=100, border_color=prime_color, color="black")
sexField = ft.Dropdown(
        label="Стать",
        hint_text="Оберіть стать",
        border_color=prime_color,
        color="black",
        options=[
        ft.dropdown.Option("Чоловік"),
        ft.dropdown.Option("Жінка"),
        ], width=70)

# Ряд Имя Фамилия Пол Возраст
NameLastNameSexAgeRow = ft.Row(
    [nameTextField, lastNameTextField, AgeTextField, sexField])

# Поля для второго ряда
dateTextField = ft.TextField(label="Дата звернення", width=200, height=50, border_color=prime_color, color="black")
disorderTextField = ft.TextField(label= "Діагноз", width=200, height=50, border_color=prime_color, color="black")

# Ряд Дата Поступления Диагноз
DateDisorderRow = ft.Row([dateTextField, disorderTextField])

# Поля для третьего ряда
DrugTextField = ft.TextField(label="Препарат", width=305, border_color=prime_color, color="black")
ValueTextField = ft.TextField(label="Доза", width=95, border_color=prime_color, color="black")

# Лекарство доза кнопка
DrugsDoseSubmitRow = ft.Row([DrugTextField, ValueTextField])

addPatientButton = ft.ElevatedButton("Додати пацієнта", bgcolor=prime_color, color=light_color, on_click=add_patient)

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


import flet as ft
import json
from design import *

def search_patient(e):
    search_query = searchTextField.value.split()  # Разделяем введенные данные на имя и фамилию
    if len(search_query) < 2:
        # Если введены неполные данные, показываем сообщение
        dataBaseColumn.controls.append(ft.Text("Невідома помилка"))
        dataBaseColumn.update()
        return

    search_name = search_query[0].strip().lower()  # Имя
    search_last_name = search_query[1].strip().lower()  # Фамилия

    # Очищаем предыдущие результаты поиска
    dataBaseColumn.controls.clear()

    try:
        # Загружаем данные пациентов из JSON файла
        with open("patients.json", "r", encoding="utf-8") as file:
            patients_list = json.load(file)

        # Поиск всех пациентов с совпадающим именем и фамилией
        found_patients = []
        for patient in patients_list:
            if (patient["name"].strip().lower() == search_name and
                patient["last_name"].strip().lower() == search_last_name):
                found_patients.append(patient)

        if found_patients:
            # Если найдены пациенты, добавляем их ограниченные данные в интерфейс
            for patient in found_patients:
                # Формируем строку с основными данными пациента (имя, фамилия и дата поступления)
                patient_info = (f"{patient['name']}, {patient['last_name']}, "
                                f"Дата: {patient['date']}")
                # "name": "Alexandr",
                # "last_name": "Kior",
                # "age": "22",
                # "sex": "Чоловік",
                # "date": "08.15.2002",
                # "disorder": "Депресия",
                # "drug": "Мухоморчик",
                # "dose": "20"

                # Добавляем строку с данными пациента в колонку
                dataBaseColumn.controls.append(
                    ft.Container(
                        content=ft.Column(
                        [
                            ft.Text(f"{patient['date']}", weight=ft.FontWeight.W_600, color="grey", size=12),
                            ft.Text(f"{patient['name']}, {patient['last_name']}", weight=ft.FontWeight.W_600, color=prime_color, size=15),
                            ft.Text(f"{patient['age']}, {patient['sex']}", weight=ft.FontWeight.W_600, color="grey", size=12),
                            ft.Text(f"{patient['disorder']}", weight=ft.FontWeight.W_600, color=prime_color, size=15),
                            ft.Text(f"{patient['drug']}, {patient['dose']}", weight=ft.FontWeight.W_600, color=prime_color, size=15),
                        ]), bgcolor=light_color, border=ft.border.all(2, prime_color), border_radius=10, padding=5
                    )
                )
        else:
            # Если пациентов не найдено, выводим соответствующее сообщение
            dataBaseColumn.controls.append(ft.Text("Пацієнт не знайдений"))

    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        dataBaseColumn.controls.append(ft.Text("Файл 'patients.json' не знайдено"))

    # Обновляем интерфейс
    dataBaseColumn.update()


# Колонка для отображения данных из поиска
dataBaseColumn = ft.Column([], alignment=ft.alignment.center, scroll=True)

# Поле для ввода запроса
searchTextField = ft.TextField(label="Введіть ім'я та прізвище", width=400, border_color=prime_color, color="black")

# Кнопка для выполнения поиска
searchButton = ft.ElevatedButton("Пошук", on_click=search_patient, bgcolor=prime_color, color=light_color)

# Основная колонка экрана
findScreenMainColumn = ft.Column([
    ft.Text("ПОШУК", size=25, weight=ft.FontWeight.W_600, color=prime_color),
    ft.Row([searchTextField,searchButton],alignment=ft.MainAxisAlignment.CENTER),
    ft.Container(height=350, width=600, bgcolor="white", content=dataBaseColumn),
], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5, alignment=ft.alignment.center)

# Экран поиска
findScreen = ft.Container(
    bgcolor=light_color, 
    width=200,
    height=600,
    content=findScreenMainColumn,  
)
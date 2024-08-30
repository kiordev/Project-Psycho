import flet as ft

# Хранение результатов тестов
tests_results = []

# Функция для отображения результатов теста
def show_results(name, test_name, score):
    tests_results.append({"name": name, "test": test_name, "score": score})
    return f"Тест: {test_name}, Оценка: {score}"

# Функция для обработки нажатия кнопок тестов
def start_test(test_name, page):
    def test_handler(e):
        name = name_input.value
        if test_name == "Тест Бека":
            score = "10/27"  # Пример результата
        else:
            score = "Неизвестный тест"
        result_text.value = show_results(name, test_name, score)
        result_text.update()
        page.go_back()

    return test_handler

# Основная функция
def main(page: ft.Page):
    page.title = "Психиатрические тесты по DSM-5"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Поле для ввода имени
    name_input = ft.TextField(label="Ваше имя", width=300)
    page.add(name_input)

    # Основное поле
    main_area = ft.Column()
    result_text = ft.Text("Результаты тестов:", size=16)

    # Боковое меню
    menu = ft.Column(
        [
            ft.TextButton("Пройти тест", on_click=lambda e: show_tests(page)),
            ft.TextButton("Инструкции", on_click=lambda e: show_instructions(page)),
            ft.TextButton("База пройденных тестов", on_click=lambda e: show_results_page(page)),
        ]
    )

    page.add(menu)

def show_tests(page: ft.Page):
    test_buttons = [
        ft.TextButton("Тест Бека", on_click=start_test("Тест Бека", page)),
        ft.TextButton("Тест 2", on_click=start_test("Тест 2", page)),
        ft.TextButton("Тест 3", on_click=start_test("Тест 3", page)),
    ]
    page.add(ft.Column(test_buttons))

def show_instructions(page: ft.Page):
    instructions_text = ft.Text("Инструкции: Это приложение предназначено для помощи в установке психиатрических диагнозов по DSM-5. Пожалуйста, используйте его ответственно.")
    page.add(instructions_text)

def show_results_page(page: ft.Page):
    results_text = ft.Column([
        ft.Text("Результаты:"),
        *[ft.Text(f"{result['name']} - {result['test']} - {result['score']}") for result in tests_results]
    ])
    page.add(results_text)

# Запуск приложения
ft.app(target=main)

import flet as ft
from design import *
from rules import *

text_items = [ft.Text(rule, size=15, color=dark_color) for rule in mainrul]
# Вторичная колонка с правила
ruleScreenSecondaryColumn = ft.Column(
    controls=text_items, horizontal_alignment=ft.CrossAxisAlignment.START, spacing=10)

# Главная колонка
ruleScreenMainColumn = ft.Column([
    ft.Text("Правила до ознайомлення: ", size=30, weight=ft.FontWeight.W_600, color=prime_color),
    ruleScreenSecondaryColumn,
], horizontal_alignment=ft.CrossAxisAlignment.START, spacing=10
)

ruleScreenSecondaryContainer = ft.Container(
    content=ruleScreenMainColumn,
    bgcolor=light_color,
    margin=20,
)

ruleScreen = ft.Container(
    bgcolor=light_color, 
    width=200,
    height=600,
    content=ruleScreenSecondaryContainer,  
)


import flet as ft
from src.utils.colors import AppColors

class ChartWidget:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def build(self):
        total = self.income + self.expenses
        if total == 0:
            income_percentage = 50
            expenses_percentage = 50
        else:
            income_percentage = (self.income / total) * 100
            expenses_percentage = (self.expenses / total) * 100

        total_width = 300

        # garante que a soma sempre bate
        income_width = round((income_percentage / 100) * total_width)
        expenses_width = total_width - income_width

        row_children = []

        # só renderiza se tiver largura mínima aceitável
        if income_width > 3:
            row_children.append(
                ft.Container(
                    bgcolor=AppColors.SUCCESS,
                    height=20,
                    width=income_width,
                    border_radius=ft.border_radius.only(
                        top_left=10, bottom_left=10,
                        top_right=10 if expenses_width <= 3 else 0,
                        bottom_right=10 if expenses_width <= 3 else 0
                    )
                )
            )

        if expenses_width > 3:
            row_children.append(
                ft.Container(
                    bgcolor=AppColors.ERROR,
                    height=20,
                    width=expenses_width,
                    border_radius=ft.border_radius.only(
                        top_right=10, bottom_right=10,
                        top_left=10 if income_width <= 3 else 0,
                        bottom_left=10 if income_width <= 3 else 0
                    )
                )
            )

        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "Entradas vs Gastos",
                    color=AppColors.WHITE,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Container(height=10),

                ft.Container(
                    content=ft.Row(row_children, spacing=0),
                    width=total_width,
                    padding=0,
                    alignment=ft.alignment.center
                ),

                ft.Container(height=10),

                ft.Row([
                    ft.Row([
                        ft.Container(width=12, height=12, bgcolor=AppColors.SUCCESS, border_radius=6),
                        ft.Text(f"Entradas ({0.0 if total == 0 else income_percentage:.1f}%)", color=AppColors.WHITE, size=12)
                    ], spacing=5),
                    ft.Row([
                        ft.Container(width=12, height=12, bgcolor=AppColors.ERROR, border_radius=6),
                        ft.Text(f"Gastos ({0.0 if total == 0 else expenses_percentage:.1f}%)", color=AppColors.WHITE, size=12)
                    ], spacing=5),
                ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
            alignment=ft.alignment.center,
            padding=ft.padding.all(20),
            bgcolor=AppColors.GRAY_DARK,
            border_radius=12
        )

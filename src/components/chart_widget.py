import flet as ft
from src.utils.colors import AppColors

class ChartWidget:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def build(self):
        total = self.income + self.expenses
        if total == 0:
            income_percentage = 0
            expenses_percentage = 0
        else:
            income_percentage = (self.income / total) * 100
            expenses_percentage = (self.expenses / total) * 100
        
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
                
                # Barra de progresso visual
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            bgcolor=AppColors.SUCCESS,
                            height=20,
                            width=income_percentage * 2 if income_percentage > 0 else 1,
                            border_radius=ft.border_radius.only(top_left=10, bottom_left=10)
                        ),
                        ft.Container(
                            bgcolor=AppColors.ERROR,
                            height=20,
                            width=expenses_percentage * 2 if expenses_percentage > 0 else 1,
                            border_radius=ft.border_radius.only(top_right=10, bottom_right=10)
                        ),
                    ], spacing=0),
                    width=200,
                    alignment=ft.alignment.center
                ),
                
                ft.Container(height=10),
                
                # Legendas
                ft.Row([
                    ft.Row([
                        ft.Container(width=12, height=12, bgcolor=AppColors.SUCCESS, border_radius=6),
                        ft.Text(f"Entradas ({income_percentage:.1f}%)", color=AppColors.WHITE, size=12)
                    ], spacing=5),
                    ft.Row([
                        ft.Container(width=12, height=12, bgcolor=AppColors.ERROR, border_radius=6),
                        ft.Text(f"Gastos ({expenses_percentage:.1f}%)", color=AppColors.WHITE, size=12)
                    ], spacing=5),
                ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
            padding=ft.padding.all(20),
            bgcolor=AppColors.GRAY_DARK,
            border_radius=12
        )
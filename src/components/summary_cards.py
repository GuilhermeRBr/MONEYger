import flet as ft
from src.utils.colors import AppColors

class SummaryCards:
    def __init__(self, total_income, total_expenses, transactions_count, categories_count):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.transactions_count = transactions_count
        self.categories_count = categories_count

    def build(self):
        return ft.Column([
            ft.Row([
                self._build_summary_card(
                    "Entradas", 
                    f"R$ {self.total_income:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), 
                    AppColors.SUCCESS
                ),
                self._build_summary_card(
                    "Gastos", 
                    f"R$ {self.total_expenses:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), 
                    AppColors.ERROR
                ),
            ], spacing=10),
            
            ft.Container(height=10),
            
            ft.Row([
                self._build_summary_card("Transações", str(self.transactions_count), AppColors.PRIMARY),
                self._build_summary_card("Categorias", str(self.categories_count), AppColors.TERTIARY),
            ], spacing=10),
        ], spacing=0)

    def _build_summary_card(self, title, value, color):
        return ft.Container(
            content=ft.Column([
                ft.Text(
                    title,
                    color=AppColors.GRAY_LIGHT,
                    size=12,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    value,
                    color=color,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                )
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5),
            bgcolor=AppColors.GRAY_DARK,
            padding=ft.padding.all(12),
            border_radius=8,
            expand=True,
            border=ft.border.all(1, color)
        )
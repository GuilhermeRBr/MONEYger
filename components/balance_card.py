import flet as ft
from utils.colors import AppColors

class BalanceCard:
    def __init__(self, balance):
        self.balance = balance

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "Saldo:",
                    color=AppColors.WHITE,
                    size=18,
                    weight=ft.FontWeight.W_300
                ),
                ft.Text(
                    f"R$ {self.balance:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                    color=AppColors.get_balance_color(self.balance),
                    size=36,
                    weight=ft.FontWeight.BOLD
                )
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=5),
            bgcolor=AppColors.GRAY_DARK,
            padding=ft.padding.all(20),
            margin=ft.margin.only(left=16, right=16, top=16, bottom=8),
            border_radius=12,
            width=360
        )
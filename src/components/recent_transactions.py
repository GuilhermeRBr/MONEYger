import flet as ft
from flet import Icons
from src.utils.colors import AppColors

class RecentTransactions:
    def __init__(self, transactions):
        self.transactions = transactions

    def build(self):
        if not self.transactions:
            return ft.Container(
                content=ft.Text(
                    "Nenhuma transação recente",
                    color=AppColors.GRAY_MEDIUM,
                    size=14,
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.all(20)
            )

        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "Transações Recentes",
                    color=AppColors.WHITE,
                    size=16,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Container(height=10),
                ft.Column([
                    self._build_transaction_item(transaction)
                    for transaction in self.transactions
                ], spacing=8)
            ], spacing=0),
            bgcolor=AppColors.GRAY_DARK,
            padding=ft.padding.all(16),
            border_radius=12
        )

    def _build_transaction_item(self, transaction):
        date_str = transaction.timestamp.strftime("%d/%m")
        amount_str = f"R$ {abs(transaction.amount):.2f}".replace(".", ",")
        amount_color = AppColors.SUCCESS if transaction.amount > 0 else AppColors.ERROR
        type_icon = Icons.ARROW_DOWNWARD if transaction.amount > 0 else Icons.ARROW_UPWARD
        
        return ft.Container(
            content=ft.Row([
                ft.Icon(
                    type_icon,
                    color=amount_color,
                    size=16
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"{transaction.category} - {amount_str}",
                            color=AppColors.WHITE,
                            size=12,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            f"{date_str} - {transaction.description[:20]}{'...' if len(transaction.description) > 20 else ''}",
                            color=AppColors.GRAY_LIGHT,
                            size=10
                        )
                    ], spacing=2),
                    expand=True
                )
            ], spacing=8),
            padding=ft.padding.all(8),
            bgcolor=AppColors.BACKGROUND,
            border_radius=6
        )
import flet as ft
from flet import Icons
from src.utils.colors import AppColors

class TransactionCard:
    def __init__(self, transaction, on_delete=None, on_details=None):
        self.transaction = transaction
        self.on_delete = on_delete
        self.on_details = on_details

    def build(self):
        date_str = self.transaction.timestamp.strftime("%d/%m/%Y %H:%M")
        
        amount_str = f"R$ {abs(self.transaction.amount):.2f}".replace(".", ",")
        amount_color = AppColors.SUCCESS if self.transaction.type == 'income' else AppColors.ERROR
        type_icon = Icons.ARROW_DOWNWARD if self.transaction.type == 'income' else Icons.ARROW_UPWARD
        
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(
                        type_icon,
                        color=amount_color,
                        size=24
                    ),
                    padding=ft.padding.only(right=10)
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"{date_str} - {amount_str}",
                            color=AppColors.WHITE,
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            f"{self.transaction.type.replace('income', 'Recebi').replace('expense', 'Paguei')} - {self.transaction.category}",
                            color=AppColors.GRAY_LIGHT,
                            size=12
                        ),
                        ft.Text(
                            self.transaction.description,
                            color=AppColors.GRAY_MEDIUM,
                            size=11
                        )
                    ], spacing=2),
                    expand=True
                ),
                
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=Icons.VISIBILITY,
                            icon_color=AppColors.PRIMARY,
                            icon_size=20,
                            on_click=lambda _: self.show_details() if self.on_details else None,
                            tooltip="Ver detalhes"
                        ),
                        ft.IconButton(
                            icon=Icons.DELETE,
                            icon_color=AppColors.ERROR,
                            icon_size=20,
                            on_click=lambda _: self.confirm_delete() if self.on_delete else None,
                            tooltip="Excluir"
                        ),
                    ], spacing=0),
                    width=80
                )
            ], alignment=ft.MainAxisAlignment.START),
            bgcolor=AppColors.GRAY_DARK,
            padding=ft.padding.all(12),
            margin=ft.margin.only(bottom=8),
            border_radius=8,
            border=ft.border.all(1, AppColors.QUATERNARY)
        )

    def show_details(self):
        if self.on_details:
            self.on_details(self.transaction)

    def confirm_delete(self):
        if self.on_delete:
            self.on_delete(self.transaction.id)
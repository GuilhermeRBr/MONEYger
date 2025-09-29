import flet as ft
from src.utils.colors import AppColors
from src.components.transaction_card import TransactionCard
from src.controllers.transaction_controller import get_all_transactions, remove_transaction

class TransactionHistoryView:
    def __init__(self, data_manager, refresh_callback):
        self.data_manager = data_manager
        self.refresh_callback = refresh_callback
        self.transaction_list = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)
        self.page = None

    def refresh(self):
        transactions = get_all_transactions()
        self.transaction_list.controls.clear()
        
        if transactions:
            self.transaction_list.controls.extend([
                TransactionCard(
                    transaction=transaction,
                    on_delete=self.delete_transaction,
                    on_details=self.show_transaction_details
                ).build()
                for transaction in transactions
            ])
        else:
            self.transaction_list.controls.append(
                ft.Container(
                    content=ft.Text(
                        "Nenhuma transação encontrada",
                        color=AppColors.GRAY_MEDIUM,
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(40)
                )
            )
        if self.transaction_list.page is not None:
            self.transaction_list.update()

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text(
                        "HISTÓRICO:",
                        color=AppColors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                    padding=ft.padding.all(20),
                    alignment=ft.alignment.center_left
                ),
                ft.Container(
                    content=self.transaction_list,
                    expand=True,
                    padding=ft.padding.symmetric(horizontal=16)
                )
            ], spacing=0),
            bgcolor=AppColors.BACKGROUND,
            expand=True
        )

    def delete_transaction(self, transaction_id):
        remove_transaction(transaction_id)
        self.refresh()
        self.refresh_callback()


    def show_transaction_details(self, transaction):
        date_str = transaction.timestamp.strftime("%d/%m/%Y às %H:%M")
        amount_str = f"R$ {abs(transaction.amount):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        type_str = "Recebimento" if transaction.type == "income" else "Pagamento"

        modal = ft.AlertDialog(
            title=ft.Text(
                "Detalhes da Transação",
                color=AppColors.WHITE,
                size=18,
                weight=ft.FontWeight.BOLD
            ),
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Valor:", color=AppColors.GRAY_LIGHT, size=14),
                        ft.Text(amount_str, color=AppColors.WHITE, size=14, weight=ft.FontWeight.BOLD)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Row([
                        ft.Text("Tipo:", color=AppColors.GRAY_LIGHT, size=14),
                        ft.Text(type_str, color=AppColors.WHITE, size=14)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Row([
                        ft.Text("Categoria:", color=AppColors.GRAY_LIGHT, size=14),
                        ft.Text(transaction.category, color=AppColors.WHITE, size=14)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Row([
                        ft.Text("Data:", color=AppColors.GRAY_LIGHT, size=14),
                        ft.Text(date_str, color=AppColors.WHITE, size=14)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Divider(color=AppColors.QUATERNARY),
                    
                    ft.Text("Descrição:", color=AppColors.GRAY_LIGHT, size=14),
                    ft.Text(
                        transaction.description,
                        color=AppColors.WHITE,
                        size=14,
                        max_lines=3
                    )
                ], spacing=10),
                width=300,
                height=200
            ),
            bgcolor=AppColors.GRAY_DARK,
            actions=[
                ft.TextButton(
                    text="Fechar",
                    on_click=lambda _: self.close_modal(),
                    style=ft.ButtonStyle(color=AppColors.PRIMARY)
                )
            ]
        )
        
        print(f"Detalhes da transação: {type_str} de {amount_str} em {date_str}")

    def close_modal(self):
        pass
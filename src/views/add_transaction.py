import flet as ft
from src.utils.colors import AppColors
from datetime import datetime
from src.controllers.transaction_controller import add_transaction

class AddTransactionView:
    def __init__(self, data_manager, on_transaction_added, page):
        self.data_manager = data_manager
        self.on_transaction_added = on_transaction_added
        self.page = page
        self.setup_form()

    def setup_form(self):

        self.value_field = ft.TextField(
            label="VALOR:",
            prefix_text="R$ ",
            keyboard_type=ft.KeyboardType.NUMBER,
            color=AppColors.WHITE,
            label_style=ft.TextStyle(color=AppColors.WHITE),
            border_color=AppColors.QUATERNARY,
            focused_border_color=AppColors.PRIMARY,
            cursor_color=AppColors.PRIMARY,
            text_style=ft.TextStyle(color=AppColors.WHITE)
        )
        
        self.description_field = ft.TextField(
            label="De onde veio o dinheiro:",
            hint_text="Descrição",
            color=AppColors.WHITE,
            label_style=ft.TextStyle(color=AppColors.WHITE),
            border_color=AppColors.QUATERNARY,
            focused_border_color=AppColors.PRIMARY,
            cursor_color=AppColors.PRIMARY,
            text_style=ft.TextStyle(color=AppColors.WHITE)
        )
        
        self.category_field = ft.TextField(
            label="Categoria:",
            hint_text="Ex: Alimentação, Transporte, Salário",
            color=AppColors.WHITE,
            label_style=ft.TextStyle(color=AppColors.WHITE),
            border_color=AppColors.QUATERNARY,
            focused_border_color=AppColors.PRIMARY,
            cursor_color=AppColors.PRIMARY,
            text_style=ft.TextStyle(color=AppColors.WHITE)
        )
        

        self.transaction_type = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(
                    value="income", 
                    label="Recebi",
                    label_style=ft.TextStyle(color=AppColors.WHITE),
                    fill_color=AppColors.SUCCESS
                ),
                ft.Radio(
                    value="expense", 
                    label="Paguei",
                    label_style=ft.TextStyle(color=AppColors.WHITE),
                    fill_color=AppColors.ERROR
                ),
            ]),
            value="expense"
        )

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text(
                        "Nova Transação",
                        color=AppColors.WHITE,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    padding=ft.padding.all(20),
                    alignment=ft.alignment.center
                ),
                
                ft.Container(
                    content=ft.Column([
                        self.value_field,
                        
                        ft.Container(height=20),
                        
                        self.description_field,
                        
                        ft.Container(height=20),
                        
                        self.category_field,
                        
                        ft.Container(height=20),
                        
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    "Tipo de transação:",
                                    color=AppColors.WHITE,
                                    size=14,
                                    weight=ft.FontWeight.W_500
                                ),
                                self.transaction_type
                            ], spacing=10),
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Container(
                            content=ft.ElevatedButton(
                                text="SALVAR",
                                on_click=self.save_transaction,
                                bgcolor=AppColors.PRIMARY,
                                color=AppColors.WHITE,
                                style=ft.ButtonStyle(
                                    text_style=ft.TextStyle(
                                        size=16,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    padding=ft.padding.symmetric(horizontal=40, vertical=15)
                                )
                            ),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(top=20)
                        )
                        
                    ], spacing=0),
                    padding=ft.padding.all(20),
                    expand=True
                )
            ], spacing=0),
            bgcolor=AppColors.BACKGROUND,
            expand=True
        )

    def save_transaction(self, e):

        if not self.value_field.value or not self.description_field.value or not self.category_field.value:
            self.show_snackbar("Por favor, preencha todos os campos!", AppColors.ERROR)
            return
        
        try:
            value_text = self.value_field.value.replace(",", ".").strip()
            amount = float(value_text)
            
            if amount <= 0:
                self.show_snackbar("O valor deve ser maior que zero!", AppColors.ERROR)
                return
            
            add_transaction(amount, self.category_field.value.strip().capitalize(), self.description_field.value.strip().capitalize(), datetime.now(), self.transaction_type.value)
            
            # self.data_manager.add_transaction(
            #     amount=amount,
            #     category=self.category_field.value.strip(),
            #     description=self.description_field.value.strip(),
            #     date=datetime.now(),
            #     transaction_type=self.transaction_type.value
            # )

            self.clear_form()
            
            self.show_snackbar("Transação adicionada com sucesso!", AppColors.SUCCESS)

            self.on_transaction_added()
            
        except ValueError:
            self.show_snackbar("Valor inválido! Use apenas números.", AppColors.ERROR)

    def clear_form(self):
        self.value_field.value = ""
        self.description_field.value = ""
        self.category_field.value = ""
        self.transaction_type.value = "expense"

    def show_snackbar(self, message, color):
        snackbar = ft.SnackBar(
            content=ft.Text(message, color=AppColors.WHITE),
            bgcolor=color,
            duration=3000
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()
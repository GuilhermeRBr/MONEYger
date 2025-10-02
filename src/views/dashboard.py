import flet as ft
from src.utils.colors import AppColors
from src.components.balance_card import BalanceCard
from src.components.chart_widget import ChartWidget
from src.components.summary_cards import SummaryCards
from src.components.recent_transactions import RecentTransactions
from src.controllers.transaction_controller import *

class DashboardView:
    def __init__(self, refresh_callback):
        self.refresh_callback = refresh_callback

    def refresh(self):
        pass

    def build(self):
        balance = get_balance()
        total_income = income_total()
        total_expenses = expense_total()
        transactions_count = count_transactions()
        categories_count = count_categories()
        recent_transactions = get_all_transactions(3)
        
        
        return ft.Container(
            content=ft.Column(
                [
                    BalanceCard(balance).build(),
                    ft.Container(
                        content=ft.Column(
                            [
                                ChartWidget(total_income, total_expenses).build(),
                                ft.Divider(color=AppColors.QUATERNARY, height=20),
                                SummaryCards(
                                    total_income,
                                    total_expenses,
                                    transactions_count,
                                    categories_count
                                ).build(),
                                ft.Divider(color=AppColors.QUATERNARY, height=20),
                                RecentTransactions(recent_transactions).build()
                            ],
                            spacing=15,
                        ),
                        padding=ft.padding.all(16),
                    )
                ],
                spacing=0,
                expand=True,
                scroll=ft.ScrollMode.AUTO, 
            ),
            expand=True,
            bgcolor=AppColors.BACKGROUND,
        )

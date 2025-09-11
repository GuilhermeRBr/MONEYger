import flet as ft
from utils.colors import AppColors
from components.balance_card import BalanceCard
from components.chart_widget import ChartWidget
from components.summary_cards import SummaryCards
from components.recent_transactions import RecentTransactions

class DashboardView:
    def __init__(self, data_manager, refresh_callback):
        self.data_manager = data_manager
        self.refresh_callback = refresh_callback

    def refresh(self):
        """Atualiza os dados da dashboard"""
        pass

    def build(self):
        balance = self.data_manager.get_balance()
        total_income = self.data_manager.get_total_income()
        total_expenses = self.data_manager.get_total_expenses()
        transactions_count = self.data_manager.get_transactions_count()
        recent_transactions = self.data_manager.get_all_transactions()[:3]  # Últimas 3 transações
        
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
                                    len(self.data_manager.get_expense_categories())
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
                scroll=ft.ScrollMode.AUTO,  # << aqui que faz diferença
            ),
            expand=True,
            bgcolor=AppColors.BACKGROUND,
        )

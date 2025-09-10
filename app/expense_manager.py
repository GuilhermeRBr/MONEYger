import flet as ft
from views.dashboard import DashboardView
from views.add_transaction import AddTransactionView
from views.transaction_history import TransactionHistoryView
from components.navigation import NavigationComponent
from utils.colors import AppColors
from data.mock_data import DataManager

class ExpenseManagerApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.data_manager = DataManager()
        self.setup_page()
        self.setup_views()
        self.setup_navigation()
        self.show_dashboard()

    def setup_page(self):
        self.page.title = "MONEYger"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = AppColors.BACKGROUND
        self.page.padding = 0
        self.page.window.width = 400
        self.page.window.height = 700
        self.page.window.resizable = False

    def setup_views(self):
        self.dashboard_view = DashboardView(self.data_manager, self.refresh_data)
        self.add_transaction_view = AddTransactionView(self.data_manager, self.on_transaction_added, self.page)
        self.history_view = TransactionHistoryView(self.data_manager, self.refresh_data)
        
    def setup_navigation(self):
        self.navigation = NavigationComponent(
            on_dashboard_click=self.show_dashboard,
            on_add_click=self.show_add_transaction,
            on_history_click=self.show_history
        )

    def show_dashboard(self):
        self.page.clean()
        self.dashboard_view.refresh()
        self.page.add(
            ft.Container(
                content=ft.Column([
                    self.dashboard_view.build(),
                    self.navigation.build()
                ], spacing=0),
                expand=True
            )
        )
        self.page.update()

    def show_add_transaction(self):
        self.page.clean()
        self.page.add(
            ft.Container(
                content=ft.Column([
                    self.add_transaction_view.build(),
                    self.navigation.build()
                ], spacing=0),
                expand=True
            )
        )
        self.page.update()

    def show_history(self):
        self.page.clean()
        self.history_view.refresh()
        self.page.add(
            ft.Container(
                content=ft.Column([
                    self.history_view.build(),
                    self.navigation.build()
                ], spacing=0),
                expand=True
            )
        )
        self.page.update()

    def on_transaction_added(self):
        self.show_dashboard()
        
    def refresh_data(self):
        self.dashboard_view.refresh()
        self.history_view.refresh()
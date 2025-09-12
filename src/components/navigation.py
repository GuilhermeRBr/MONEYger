import flet as ft
from flet import Icons
from src.utils.colors import AppColors

class NavigationComponent:
    def __init__(self, on_dashboard_click, on_add_click, on_history_click):
        self.on_dashboard_click = on_dashboard_click
        self.on_add_click = on_add_click
        self.on_history_click = on_history_click

    def build(self):
        return ft.Container(
            content=ft.Row([

                ft.Container(
                    content=ft.IconButton(
                        icon=Icons.HOME,
                        icon_color=AppColors.WHITE,
                        icon_size=28,
                        on_click=lambda _: self.on_dashboard_click()
                    ),
                    expand=1,
                    alignment=ft.alignment.center,
                ),

                ft.Container(
                    content=ft.FloatingActionButton(
                        icon=Icons.ADD,
                        bgcolor=AppColors.PRIMARY,
                        foreground_color=AppColors.WHITE,
                        on_click=lambda _: self.on_add_click(),
                        mini=True,
                    ),
                    alignment=ft.alignment.center,
                ),

                ft.Container(
                    content=ft.IconButton(
                        icon=Icons.HISTORY,
                        icon_color=AppColors.WHITE,
                        icon_size=28,
                        on_click=lambda _: self.on_history_click()
                    ),
                    expand=1,
                    alignment=ft.alignment.center,
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            height=70,
            bgcolor="#444343",
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
            border_radius=ft.border_radius.only(top_left=20, top_right=20)
        )
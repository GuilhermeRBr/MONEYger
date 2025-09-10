import flet as ft
from app.expense_manager import ExpenseManagerApp

def main(page: ft.Page):
    ExpenseManagerApp(page)

if __name__ == "__main__":
    ft.app(target=main)

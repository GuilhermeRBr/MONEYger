import flet as ft
from fastapi import FastAPI
from src.app.expense_manager import ExpenseManagerApp

api = FastAPI()


def main(page: ft.Page):
    ExpenseManagerApp(page)

if __name__ == "__main__":
    ft.app(target=main)

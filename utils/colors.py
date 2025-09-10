import flet as ft

class AppColors:
    # Cores atualizadas pelo usuário
    PRIMARY = "#f64a00"      # Laranja vibrante
    SECONDARY = "#ff004f"    # Rosa/vermelho vibrante
    TERTIARY = "#00a000"     # Verde
    QUATERNARY = "#744e95"   # Roxo escuro
    BACKGROUND = "#271811"   # Marrom escuro
    
    # Cores complementares
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY_LIGHT = "#E0E0E0"
    GRAY_MEDIUM = "#9E9E9E"
    GRAY_DARK = "#3a3a3a"
    
    # Cores para estado
    SUCCESS = "#00a000"
    ERROR = "#ff004f"
    WARNING = "#FF9800"
    INFO = "#2196F3"

    @staticmethod
    def get_balance_color(balance: float) -> str:
        return AppColors.SUCCESS if balance >= 0 else AppColors.ERROR
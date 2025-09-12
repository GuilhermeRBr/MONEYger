class AppColors:
    PRIMARY = "#f64a00"     
    SECONDARY = "#db0045"    
    TERTIARY = "#00a000"     
    QUATERNARY = "#632d8f"   
    BACKGROUND = "#222020"   

    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY_LIGHT = "#E0E0E0"
    GRAY_MEDIUM = "#9E9E9E"
    GRAY_DARK = "#3a3a3a"
    
    SUCCESS = "#00a000"
    ERROR = "#db0045"
    WARNING = "#FF9800"
    INFO = "#2196F3"

    @staticmethod
    def get_balance_color(balance: float) -> str:
        return AppColors.SUCCESS if balance >= 0 else AppColors.ERROR
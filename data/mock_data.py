from datetime import datetime, timedelta
import random

class Transaction:
    def __init__(self, id, amount, category, description, date, transaction_type):
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.type = transaction_type  # 'income' ou 'expense'

class DataManager:
    def __init__(self):
        self.transactions = []
        self.next_id = 1
        self._generate_sample_data()

    def _generate_sample_data(self):
        """Gera dados de exemplo para demonstração"""
        sample_transactions = [
            (3000.0, "Trabalho", "Salário mensal", "income"),
            (-300.0, "Alimentação", "Supermercado", "expense"),
            (-1000.0, "Moradia", "Aluguel", "expense"),
            (-150.0, "Transporte", "Gasolina", "expense"),
            (500.0, "Extra", "Freelance", "income"),
            (-80.0, "Lazer", "Cinema", "expense"),
            (-200.0, "Saúde", "Farmácia", "expense"),
        ]
        
        base_date = datetime.now() - timedelta(days=7)
        
        for i, (amount, category, description, t_type) in enumerate(sample_transactions):
            transaction_date = base_date + timedelta(days=i)
            self.add_transaction(amount, category, description, transaction_date, t_type)

    def add_transaction(self, amount, category, description, date, transaction_type):
        transaction = Transaction(
            id=self.next_id,
            amount=abs(amount) if transaction_type == "income" else -abs(amount),
            category=category,
            description=description,
            date=date,
            transaction_type=transaction_type
        )
        self.transactions.append(transaction)
        self.next_id += 1
        return transaction

    def remove_transaction(self, transaction_id):
        self.transactions = [t for t in self.transactions if t.id != transaction_id]

    def get_all_transactions(self):
        return sorted(self.transactions, key=lambda x: x.date, reverse=True)

    def get_balance(self):
        return sum(t.amount for t in self.transactions)

    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    def get_total_expenses(self):
        return abs(sum(t.amount for t in self.transactions if t.amount < 0))

    def get_transactions_count(self):
        return len(self.transactions)

    def get_expense_categories(self):
        """Retorna categorias de gastos com totais para o gráfico"""
        categories = {}
        for t in self.transactions:
            if t.amount < 0:
                if t.category in categories:
                    categories[t.category] += abs(t.amount)
                else:
                    categories[t.category] = abs(t.amount)
        return categories
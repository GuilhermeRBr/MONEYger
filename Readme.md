<div align="center">
  <h1 align="center">MONEYger — Gerenciador de Finanças Pessoais</h1>
  <p align="center">
    <strong>MONEYger é uma aplicação desktop open-source para controle de finanças pessoais, desenvolvida para quem quer organizar receitas e despesas de forma simples e visual com Python, Flet e PostgreSQL.</strong>
  </p>
  <p align="center">
    <a href="#"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue"></a>
    <a href="#"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/GuilhermeRBr/MONEYger?color=green"></a>
    <a href="#"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/GuilhermeRBr/MONEYger?color=purple"></a>
  </p>
  <br />
  <p align="center">
    <img src="https://skillicons.dev/icons?i=python,postgres,fastapi" alt="Tech Stack Icons" />
  </p>
</div>

---

## Sobre o projeto

O **MONEYger** é uma aplicação desktop para **gerenciamento de finanças pessoais**, com foco em registro de transações, visualização de saldo e acompanhamento de gastos por categoria.

> Desenvolvido para quem quer ter controle total sobre o seu dinheiro, com uma interface moderna e responsiva rodando localmente com Flet e dados persistidos no PostgreSQL.

Funcionalidades:

- Dashboard com saldo atual em tempo real
- Registro de receitas e despesas com categoria e descrição
- Gráfico comparativo de receitas vs. despesas
- Cards de resumo: total de transações e categorias cadastradas
- Histórico completo de transações com detalhes e exclusão
- Visualização das transações mais recentes no dashboard
- Navegação entre telas por barra inferior

---

## Screenshots

| Dashboard | Nova Transação | Histórico |
|-----------|----------------|-----------|
| ![Dashboard](src/assets/images/homepage.png) | ![Nova Transação](src/assets/images/new_transaction.png) | ![Histórico](src/assets/images/history.png) |

---

## Tecnologias Usadas

| Tecnologia | Descrição |
|------------|-----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Linguagem principal do projeto |
| ![Flet](https://img.shields.io/badge/-Flet-000000?style=flat&logo=flutter&logoColor=white) | Framework para UI desktop com Python |
| ![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white) | ORM para acesso ao banco de dados |
| ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white) | Banco de dados relacional |
| ![python-dotenv](https://img.shields.io/badge/-dotenv-ECD53F?style=flat&logo=dotenv&logoColor=black) | Gerenciamento de variáveis de ambiente |

---

## Como rodar o projeto

### Pré-requisitos

- [Python 3.10+](https://www.python.org)
- [pip](https://pip.pypa.io)
- PostgreSQL rodando localmente (ou via Docker)

### 1. Clone o repositório

```bash
git clone https://github.com/GuilhermeRBr/MONEYger.git
cd MONEYger
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

```bash
cp .env.exemple .env
```

Edite o `.env` com a sua connection string do PostgreSQL:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/moneyger
```

### 4. Inicie a aplicação

```bash
python main.py
```

> A aplicação abrirá em uma janela desktop de 400×700px.

> **Atenção:** O banco de dados e as tabelas são criados automaticamente na primeira execução via SQLAlchemy.

---

## Estrutura de Pastas

```
MONEYger/
├── main.py
├── requirements.txt
├── .env.exemple
└── src/
    ├── app/
    │   └── expense_manager.py      # Inicialização e roteamento da app
    ├── assets/
    │   └── images/
    ├── components/
    │   ├── balance_card.py         # Card de saldo atual
    │   ├── chart_widget.py         # Gráfico receitas vs despesas
    │   ├── navigation.py           # Barra de navegação inferior
    │   ├── recent_transactions.py  # Últimas transações no dashboard
    │   ├── summary_cards.py        # Cards de resumo (total, categorias)
    │   └── transaction_card.py     # Card individual de transação
    ├── controllers/
    │   └── transaction_controller.py  # Lógica de negócio e queries
    ├── models/
    │   └── transaction.py          # Model SQLAlchemy
    ├── utils/
    │   └── colors.py               # Paleta de cores da aplicação
    └── views/
        ├── dashboard.py            # Tela principal
        ├── add_transaction.py      # Tela de nova transação
        └── transaction_history.py  # Tela de histórico
```

---

## Colaboradores

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/GuilhermeRBr.png" width="100px;" alt="Guilherme Rebouças"/>
      <br />
      <sub><b>Guilherme Rebouças</b></sub>
      <br />
      <a href="https://github.com/GuilhermeRBr" target="_blank">@GuilhermeRBr</a>
    </td>
  </tr>
</table>

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

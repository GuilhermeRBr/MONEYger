# MONEYger - Gerenciador Financeiro  

O **MONEYger** é um aplicativo desenvolvido em **Python** com **Flet** que ajuda no controle de finanças pessoais.  
Ele permite registrar receitas e despesas, calcular automaticamente o saldo disponível e manter um histórico detalhado de transações.  

## Funcionalidades  
- Registrar **recebimentos** (salários, vendas, transferências, etc.).  
- Registrar **gastos** de forma simples e organizada.  
- Exibir **saldo atualizado em tempo real**.  
- Consultar um **histórico completo de transações**.  
- Interface gráfica desenvolvida em **Flet**, responsiva e fácil de usar.  

## Tecnologias Utilizadas  
- **Python**  
- **Flet** (interface gráfica)  
- **PostgreSQL** + **SQLAlchemy** (armazenamento de dados)  

## Como Usar  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/GuilhermeRBr/moneyger.git
   cd moneyger

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Instale as dependêndias:
    ```bash
    pip install -r requirements.txt

4. Configure as variáveis de ambiente no arquivo **.env**:
    ```bash
    DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/moneyger

5. Execute o aplicativo:
    ```bash
    flet run main.py

<p align="center">
  <img src="src/assets/images/homepage.png" width="30%" style="margin-right:10px;">
  <img src="src/assets/images/new_transaction.png" width="30%" style="margin-right:10px;">
  <img src="src/assets/images/history.png" width="30%">
</p>


## Contribuição
Sinta-se à vontade para sugerir melhorias ou relatar problemas abrindo uma **issue** .

## Autor
Desenvolvido por **Guilherme**.

## Licença
Este projeto está sob a licença MIT.


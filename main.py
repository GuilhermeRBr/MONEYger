import flet as ft
from flet import Colors, Icons
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.models import Transacao
from datetime import datetime


CONN = 'sqlite:///MONEYger.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()




recebidoAll = 0
for i in session.query(Transacao).all():
    recebidoAll += i.valor 

def main(page: ft.Page):
    
    

    global recebidoAll

    home_valor = ft.Text(f"R$ {recebidoAll}", color="black", size=50)
    lista_transacoes = ft.ListView()

    def cadastrar(e):
        global recebidoAll

        recebido = (add.content.controls[1].value)
        descricao = (add.content.controls[3].value)
        radio_stats = (add.content.controls[4].value)
        print(recebido, descricao)

        if recebido.isdigit():
            time = datetime.now()
            data_formatada = time.strftime('%d/%m/%Y %H:%M:%S')
            nova_transacao = Transacao(data=data_formatada,valor=recebido, descricao=descricao)
            session.add(nova_transacao)
            session.commit()
            if radio_stats == 'recebido':
                recebidoAll += nova_transacao.valor
            else:
                recebidoAll -= nova_transacao.valor

            lista_transacoes.controls.append(ft.Text(f'{nova_transacao.data} - R$ {nova_transacao.valor} - {nova_transacao.descricao}', color='black'))
            print('Transacao salva com sucesso!')
            print(radio_stats)
            home_valor.value = f"R$ {recebidoAll}"  
            stack_main.update()



    def btn_add(e):
        stack_main.controls.clear()
        stack_main.update()

        stack_main.controls.append(add)
        stack_main.update()

    def btn_home(e):
        stack_main.controls.clear()
        stack_main.update()

        stack_main.controls.append(home)
        stack_main.update()
        
    def btn_history(e):
        stack_main.controls.clear()
        stack_main.update()
    
        stack_main.controls.append(history)
        stack_main.update()


    #pagina:
    page.title = 'MONEYger'
    page.theme_mode = 'dark'
    page.bgcolor = Colors.BLUE
    page.window.always_on_top = True
    page.window.width = 450
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=Icons.ADD,
        bgcolor=Colors.BLUE,
        shape=ft.CircleBorder(),
        width=70,
        height=70,
        on_click=btn_add,
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor= '#F6F6F6FF',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(icon=Icons.HOME, icon_color=Colors.BLUE, icon_size=29, on_click=btn_home,  padding=0,)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),
                ft.Container(width=40),
                ft.IconButton(icon=Icons.HISTORY, icon_color=Colors.BLUE, icon_size=29, on_click=lambda e:(btn_history(e))),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )



    home = ft.Container(        
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#f6f6f6ff',
        shadow=ft.BoxShadow(blur_radius=10,color=Colors.with_opacity(opacity=0.5, color='black')),
        padding=50, content=ft.Column([
            ft.Text('Saldo:', color='black', size=30),
            home_valor])
    )


    for i in session.query(Transacao).all():
        lista_transacoes.controls.append(ft.Text(f'R$ {i.valor} - {i.descricao}', color='black'))
    history = ft.Container(        
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#f6f6f6ff',
        shadow=ft.BoxShadow(blur_radius=10,color=Colors.with_opacity(opacity=0.5, color='black')),
        padding=50, 
        content=ft.Column([ft.Text('HISTÓRICO:', color='black'), lista_transacoes])
    )

    add = ft.Container(
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#f6f6f6ff',
        shadow=ft.BoxShadow(blur_radius=10,color=Colors.with_opacity(opacity=0.5, color='black')),
        padding=50,
        content=ft.Column([
            ft.Text('VALOR:', color='black'),
            ft.TextField(prefix_text='R$',
                         label='Digite o valor que você recebeu...', text_align=ft.TextAlign.LEFT,
                         width=300,
                         color='black',
                         keyboard_type=ft.KeyboardType.NUMBER,
                         input_filter=lambda c: c.isdigit(),
                         ),
            ft.Text('De onde veio esse dinheiro:', color='black'),
            ft.TextField(label='Descrição',
                         text_align=ft.TextAlign.LEFT,
                         width=300,
                         color='black',
                         ),
            ft.RadioGroup(
                content=ft.Row([
                    ft.Radio(value='recebido',
                             label='Recebi',
                             fill_color='red',
                             label_style=ft.TextStyle(color='black')),
                    ft.Radio(value='pago',
                             label='Paguei',
                             fill_color='red',
                             label_style=ft.TextStyle(color='black'))
                ])
            ),
            ft.ElevatedButton('SALVAR', on_click=cadastrar)
            ]
        ) 
    )

    stack_main = ft.Stack(controls=[home])
    
    page.add(stack_main)

ft.app(target=main)


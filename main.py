import flet as ft
from flet import Colors, Icons
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from src.models.models import Transacao
from datetime import datetime


CONN = 'sqlite:///MONEYger.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()



total = session.query(func.sum(Transacao.total)).scalar()
if total is not None:
    recebidoAll = total
else:
    recebidoAll = 0

def main(page: ft.Page):
    
    def formatar_moeda(valor):
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    global recebidoAll

    home_valor = ft.Text(f"R$ {formatar_moeda(recebidoAll)}", color="white", size=50)
    lista_transacoes = ft.ListView()

    def cadastrar(e):
        global recebidoAll

        recebido = (add.content.controls[1].value)
        descricao = (add.content.controls[3].value).capitalize()
        radio_stats = (add.content.controls[4].value)
        print(recebido, descricao)

        if recebido.isdigit():
            time = datetime.now()
            data_formatada = time.strftime('%d/%m/%Y %H:%M:%S')
            nova_transacao = Transacao(data=data_formatada,
                                       valor=recebido,
                                       descricao=descricao, status=radio_stats,
                                       
                                       )
            session.add(nova_transacao)
            session.commit()

            if radio_stats == 'Recebi':
                nova_transacao.total += nova_transacao.valor
            else:
                nova_transacao.total -= nova_transacao.valor

            session.commit()

            total = session.query(func.sum(Transacao.total)).scalar()

            home_valor.value = f"R$ {formatar_moeda(total)}"  
            stack_main.update()

            lista_transacoes.controls.append(ft.Container(
                ft.Text(f'{nova_transacao.data} - R$ {nova_transacao.valor} - {nova_transacao.status} - {nova_transacao.descricao}',
                width=370,
                color='white'),
                bgcolor='black',
                alignment=ft.alignment.center,
                padding=5,
                margin=5,
                border_radius=10,

                ) )
            

            print('Transacao salva com sucesso!')
            print(radio_stats)





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
    page.bgcolor = "#0074CC"
    page.window.always_on_top = True
    page.window.width = 450
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    #botao flutuante:
    page.floating_action_button = ft.FloatingActionButton(
        icon=Icons.ADD,
        bgcolor='#0074CC',
        shape=ft.CircleBorder(),
        width=70,
        height=70,
        on_click=btn_add,
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor= '#D2D2D2',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=Icons.HOME,                  icon_color='#0074CC',
                                icon_size=29, on_click=btn_home,  
                                padding=0,
                                )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),
                ft.Container(width=40),
                ft.IconButton(
                    icon=Icons.HISTORY, 
                    icon_color='#0074CC', 
                    icon_size=29, 
                    on_click=lambda e:(btn_history(e))
                    ),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )


    #botao home
    home = ft.Container(        
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#17181B',
        shadow=ft.BoxShadow(blur_radius=10,color=Colors.with_opacity(opacity=0.5, color='black')),
        padding=20,
        alignment=ft.alignment.center,
        content=ft.Column([
            ft.Container(
                width=370,
                height=150,
                bgcolor='black',
                border_radius=20,
                padding=15,
                alignment=ft.alignment.center,
                content=ft.Column([ 
                    ft.Text('Saldo:', color='white', size=30,),             
                    home_valor,
                    
                ])
            )
        ])
    )

    #historico:
    for i in session.query(Transacao).all():
        lista_transacoes.controls.append(
            ft.Container(
                ft.Text(f'{i.data} - R$ {i.valor} - {i.status} - {i.descricao}', color='white'),
                width=550,
                bgcolor='black',
                alignment=ft.alignment.center,
                padding=20,
                margin=5,
                border_radius=10,

                )  
            )
    history = ft.Container(        
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#17181B',
        shadow=ft.BoxShadow(blur_radius=10,color=Colors.with_opacity(opacity=0.5, color='black')),
        padding=10, 
        content=ft.Column([ft.Text('HISTÓRICO:', color='white'), lista_transacoes], scroll='auto')
    )

    #botão add
    add = ft.Container(
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#17181B',
        shadow=ft.BoxShadow(blur_radius=10,color=Colors.with_opacity(opacity=0.5, color='black')),
        padding=50,
        content=ft.Column([
            ft.Text('VALOR:', color='white'),
            ft.TextField(prefix_text='R$',
                         label='Digite o valor', text_align=ft.TextAlign.LEFT,
                         width=300,
                         color='white',
                         keyboard_type=ft.KeyboardType.NUMBER,
                         input_filter=lambda c: c.isdigit(),
                         ),
            ft.Text('De onde veio o dinheiro:', color='white'),
            ft.TextField(label='Descrição',
                         text_align=ft.TextAlign.LEFT,
                         width=300,
                         color='white',
                         ),
            ft.RadioGroup(
                content=ft.Row([
                    ft.Radio(value='Recebi',
                             label='Recebi',
                             fill_color='red',
                             label_style=ft.TextStyle(color='white')),
                    ft.Radio(value='Paguei',
                             label='Paguei',
                             fill_color='red',
                             label_style=ft.TextStyle(color='white'))
                ]),
                value='Recebi'
            ),
            ft.ElevatedButton('SALVAR', on_click=cadastrar),


            ]
        ) 
    )

    stack_main = ft.Stack(controls=[home])
    
    page.add(stack_main)

ft.app(target=main)


import flet as ft

def main(page: ft.Page):

    def cadastrar(e):
        recebido = (main.content.controls[1].value)
        descricao = (main.content.controls[3].value)
        print(recebido, descricao)

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
    page.title = 'GASTÔMETRO'
    page.theme_mode = 'dark'
    page.bgcolor = ft.colors.BLUE
    page.window.always_on_top = True
    page.window.width = 450
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.BLUE,
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
                            ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.BLUE, icon_size=29, on_click=btn_home,padding=0,),
                            ft.Text('HOME', color='black',size=15)
                        ], alignment=ft.MainAxisAlignment.CENTER
                    )
                )
                
                
                ,


                ft.Container(width=40),
                ft.IconButton(icon=ft.icons.HISTORY, icon_color=ft.colors.BLUE, icon_size=29, on_click=btn_history),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )


    home = ft.Container(        
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#f6f6f6ff',
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.5, color='black')),
        padding=50, content=ft.Column([
            ft.Text('Home', color='black'),
            ]
        )
    )

    history = ft.Container(        
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#f6f6f6ff',
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.5, color='black')),
        padding=50, content=ft.Column([
            ft.Text('Historico', color='black'),
            ]
        )
    )


    add = ft.Container(
        width=400,
        height=550,
        border_radius=20,
        bgcolor='#f6f6f6ff',
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.5, color='black')),
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
            ft.ElevatedButton('SALVAR', on_click=cadastrar)
            ]
        ) 
    )

    stack_main = ft.Stack(
        controls=[ home

        ]
    )
    
    page.add(stack_main)

ft.app(target=main, view=ft.WEB_BROWSER)


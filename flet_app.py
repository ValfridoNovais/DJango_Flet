import flet as ft
import os
import sys

# Adicione o diretório que contém o módulo 'myproject' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'django_flet_app', 'myproject')))

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.myproject.settings')
import django
django.setup()

from myproject.myapp.models import Cliente, Funcionario, Material, Produto, Veiculo

def main(page: ft.Page):
    page.title = "Django Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def navigate_to(route):
        if route == "/view1":
            content_container.content = view1()
        elif route == "/view2":
            content_container.content = view2()
        elif route == "/view3":
            content_container.content = view3()
        elif route == "/view4":
            content_container.content = view4()
        elif route == "/view5":
            content_container.content = view5()
        page.update()

    def sidebar_button(route, text):
        return ft.ElevatedButton(
            text, 
            on_click=lambda _: navigate_to(route),
            style=ft.ButtonStyle(color=ft.colors.WHITE)
        )

    content_container = ft.Container(expand=True, padding=10)

    page.add(
        ft.Row([
            ft.Container(
                ft.Column([
                    sidebar_button("/view1", "Clientes"),
                    sidebar_button("/view2", "Funcionários"),
                    sidebar_button("/view3", "Materiais"),
                    sidebar_button("/view4", "Produtos"),
                    sidebar_button("/view5", "Veículos"),
                ]),
                width=200,
                padding=10,
            ),
            ft.VerticalDivider(width=1),
            content_container
        ])
    )

    # Set initial content
    navigate_to("/view1")

def create_table_view(model_class, title):
    items = model_class.objects.all()
    rows = [ft.Row([ft.Text(field.name) for field in model_class._meta.fields])]
    for item in items:
        row = ft.Row([ft.Text(str(getattr(item, field.name))) for field in model_class._meta.fields])
        rows.append(row)
    return ft.Column([ft.Text(title), *rows])

def view1():
    return create_table_view(Cliente, "Clientes")

def view2():
    return create_table_view(Funcionario, "Funcionários")

def view3():
    return create_table_view(Material, "Materiais")

def view4():
    return create_table_view(Produto, "Produtos")

def view5():
    return create_table_view(Veiculo, "Veículos")

ft.app(target=main)

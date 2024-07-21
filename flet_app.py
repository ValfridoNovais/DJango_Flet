import flet as ft
import os
import sys
import requests

# Adicione os diretórios corretos ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'django_flet_app')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'django_flet_app', 'myproject')))

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()

from myapp.models import Cliente, Funcionario, Material, Produto, Veiculo

def main(page: ft.Page):
    page.title = "Django Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def navigate_to(route):
        try:
            response = requests.get(f'http://127.0.0.1:8000{route}')
            if response.status_code == 200:
                page.views.clear()
                page.views.append(ft.Text(response.text))
        except requests.ConnectionError as e:
            page.views.clear()
            page.views.append(ft.Text(f'Error: Could not connect to the Django server. Details: {str(e)}'))
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
                    sidebar_button("/view1/", "Clientes"),
                    sidebar_button("/view2/", "Funcionários"),
                    sidebar_button("/view3/", "Materiais"),
                    sidebar_button("/view4/", "Produtos"),
                    sidebar_button("/view5/", "Veículos"),
                ]),
                width=200,
                padding=10,
            ),
            ft.VerticalDivider(width=1),
            content_container
        ])
    )

    # Set initial content
    navigate_to("/view1/")

ft.app(target=main)

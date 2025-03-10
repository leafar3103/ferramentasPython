import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    # ft.windows.width = 800
    page.update()


ft.app(main)

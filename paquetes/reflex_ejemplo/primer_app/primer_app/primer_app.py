"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from primer_app.components.navbar import navbar
from primer_app.views.header.header import header
from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    # hstack en Reflex organiza elementos en una fila horizontal, facilitando la creación de interfaces ordenadas.
    return rx.hstack(
            navbar(),
            header()
    )



app = rx.App()
app.add_page(index)
app._compile()


import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Ignaciogovo", size="9"),
        rx.text("Hola buenas tardes, esto es una prueba")
    )
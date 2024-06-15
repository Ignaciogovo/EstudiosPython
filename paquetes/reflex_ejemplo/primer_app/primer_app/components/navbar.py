import reflex as rx






def navbar() -> rx.Component:
    # Welcome Page (Index)
    # hstack en Reflex organiza elementos en una fila horizontal, facilitando la creación de interfaces ordenadas.
    return rx.hstack(
        rx.text("Descargar vídeos en formato mp3", # Agrega un texto con el mensaje "Descargar vídeos en formato mp3"
        height="40px" # Define la altura del texto a 40px
        ),
        position="sticky", # Fija la posición del elemento para que se mantenga visible al hacer scroll
        bg="#FFC300", # Establece el color de fondo a un tono amarillo
        padding_y="16px", # Agrega un relleno vertical de 16px
        padding_x="8px", # Agrega un relleno horizontal de 8px
        z_index="999" # Establece una prioridad alta de apilamiento para mantener el elemento sobre otros
    )

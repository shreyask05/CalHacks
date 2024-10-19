"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Swarm,", size="9"),
            rx.text(
                "Test your product's user experience :-) ",
                size="5",
            ),
            rx.link(
                rx.button("Dashboard"),
                href="/dashboard",
                is_external=False,
            ),

            rx.link(
                rx.button("About"),
                href="/about",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def about():
    return rx.text("for calhacks 24'")
def dashboard():
    return rx.text("dashboard here")

app = rx.App()
app.add_page(index)
app.add_page(dashboard)
app.add_page(about)

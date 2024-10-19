"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from docutils.parsers.rst.directives.tables import align

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

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Swarm", size="7", weight="bold", color="black"

                    ),
                    align_items="left",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("yellow", shade=11),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

color = "rgb(107,99,246)"
def form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="URL",
                    name="url",
                    align="center"
                ),
                rx.upload(
                    rx.vstack(
                        rx.button(
                            "Select File",
                            color=color,
                            bg="white",
                            border=f"1px solid {color}",
                            align="center"
                        ),
                        rx.text(
                            "Drag and drop files here or click to select files"
                        ),
                        align="center"
                    ),
                    id="upload1",
                    border=f"1px dotted {color}",
                    padding="5em",
                ),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
                rx.button("Analyze UI", type="submit"),
                align_items="center",
                justify_content="center",
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
            align_items="center",
            justify_content="center",
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
        align_items="center",
        justify_content="center",
    )


def about():
    return rx.box(
        navbar(),
        rx.text("for calhacks 24'")
        )
def dashboard():

    return rx.box(
        navbar(),
        rx.divider(),
        form(),
        rx.text("the dashboard lives here")
        )

app = rx.App()
app.add_page(index)
app.add_page(dashboard)
app.add_page(about)


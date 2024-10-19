"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

class State(rx.State):
    """The app state."""

    url: str = ""
    file_content: str = ""
    file_name: str = ""

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s)."""
        for file in files:
            content = await file.read()
            # Decode the content assuming it's a text file
            self.file_content = content.decode('utf-8')
            self.file_name = file.filename

    async def handle_submit(self, form_data: dict):
        """Handle the form submission."""
        self.url = form_data.get("url", "")

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
        rx.text(text, size="4", weight="medium"), href=url, color="black"
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
        width="100%",
    )

def url_input():
    return rx.input(
        placeholder="URL",
        name="url",
        align="center"
    )

def file_upload():
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color="rgb(107,99,246)",
                    bg="white",
                    border="1px solid rgb(107,99,246)",
                ),
                rx.text(
                    "Drag and drop text file here or click to select"
                ),
            ),
            id="readme",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
            accept={".txt": []},  # Only accept .txt files
        ),
        rx.hstack(rx.foreach(rx.selected_files("readme"), rx.text)),
        rx.button(
            "Upload",
            on_click=State.handle_upload(rx.upload_files(upload_id="readme")),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("readme"),
        ),
    )

def inputs():
    return rx.vstack(
        rx.form(
            rx.vstack(
                url_input(),
                file_upload(),
                rx.button("Analyze UI", type="submit"),
                align_items="center",
                justify_content="center",
            ),
            on_submit=State.handle_submit,
            reset_on_submit=True,
            align_items="center",
            justify_content="center",
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(State.url),
        rx.cond(
            State.file_name != "",
            rx.vstack(
                rx.text("Uploaded file: " + State.file_name),
                rx.text("File content:"),
                rx.text_area(
                    value=State.file_content,
                    is_read_only=True,
                    width="100%",
                    height="200px",
                ),
            ),
        ),
        align_items="center",
        justify_content="center",
        margin_top="4em"
    )

def dashboard():
    return rx.box(
        navbar(),
        rx.divider(),
        inputs(),
    )

def about():
    return rx.box(
        navbar(),
        rx.text("for calhacks 24'")
    )

app = rx.App()
app.add_page(index)
app.add_page(dashboard)
app.add_page(about)

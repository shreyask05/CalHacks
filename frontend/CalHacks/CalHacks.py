"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from reflex import color


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

    def clear_file(self):
        """Clear the file content and name."""
        self.file_content = ""
        self.file_name = ""

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="5", weight="medium"),
        href=url,
        color="white",
        text_decoration="none",
        _hover={"text_decoration": "underline"}
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.color_mode_cond(
                    rx.image(src="/swarm.png", height="3em", width="4em", radius="20px"),
                    rx.image(src="/swarm.png", height="3em", width="4em", radius="20px"),
                ),
                rx.heading("Swarm", size="8", weight="bold", color="white"),
                spacing="4",
            ),
            rx.spacer(),
            rx.desktop_only(
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("Dashboard", "/dashboard"),
                    navbar_link("About", "/about"),
                    spacing="5",
                ),
                margin_right="4em"
            ),
            rx.mobile_and_tablet(
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            navbar_link("Home", "/"),
                            bg="white",
                            color="black",
                            _hover={"bg": "rgb(244, 191, 12)"}
                        ),
                        rx.menu.item(
                            navbar_link("Dashboard", "/dashboard"),
                            bg="white",
                            color="black",
                            _hover={"bg": "rgb(244, 191, 12)"}
                        ),
                        rx.menu.item(
                            navbar_link("About", "/about"),
                            bg="white",
                            color="black",
                            _hover={"bg": "rgb(244, 191, 12)"}
                        ),
                        bg="white",
                        border="1px solid",
                        border_color="rgb(244, 191, 12)",
                    ),
                ),
            ),
            width="100%",
            align_items="center",
        ),
        background_color="rgb(244, 191, 12)",
        padding="1em",
        width="100%",
    )

def index():
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("Welcome to Swarm", size="9"),
            rx.text(
                "Test your product's user experience with ease",
                size="5",
                color="rgb(244, 191, 12)",
                margin_bottom="2em",
            ),
            rx.divider(margin_y="2em"),
            rx.heading("Why Choose Swarm?", size="7", margin_bottom="1em"),
            rx.hstack(
                feature_card(
                    "Fast Analysis",
                    "Analyze your UI in seconds",
                    "zap"  # Using a lightning bolt icon
                ),
                feature_card(
                    "Comprehensive Reports",
                    "Get detailed insights",
                    "clipboard-list"  # Using a clipboard with list icon
                ),
                feature_card(
                    "User-Friendly",
                    "Easy to use interface",
                    "smile"  # Using a smiley face icon
                ),
                spacing="4",
                wrap="wrap",
                justify="center",
            ),
            rx.divider(margin_y="2em"),
            rx.heading("How It Works", size="7", margin_bottom="1em"),
            how_it_works_section(),
            rx.divider(margin_y="2em"),
            rx.heading("Get Started Today", size="7", margin_bottom="1em"),
            rx.link(
                rx.button(
                    "Try Swarm Now",
                    color="black",
                    background_color="rgb(244, 191, 12)",
                    size="10",
                ),
                href="/dashboard",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            align_items="center",
            min_height="85vh",
            padding_y="2em",
        ),
        rx.logo(),
    )

def how_it_works_section():
    return rx.box(
        rx.vstack(
            rx.ordered_list(
                rx.list_item(
                    rx.text("Upload your design or provide a URL for instant analysis.", font_size="lg", color="gray.700")
                ),
                rx.list_item(
                    rx.text("Our AI performs a comprehensive analysis of your UI/UX.", font_size="lg", color="gray.700")
                ),
                rx.list_item(
                    rx.text("Receive actionable insights to enhance your product.", font_size="lg", color="gray.700")
                ),
                spacing="1em",
                padding_left="1em",
            ),
            width="100%",
            max_width="800px",
            margin="0 auto",
            padding="2em",
        )
    )

def step_card(title: str, description: str, icon: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.icon(icon, color="rgb(244, 191, 12)", size=30),
            rx.heading(title, size="lg", color="rgb(244, 191, 12)", margin_top="1em"),
            rx.text(description, color="gray.700", text_align="center", margin_top="0.5em"),
            align_items="center",
        ),
        bg="rgba(244, 191, 12, 0.05)",
        border_radius="lg",
        padding="2em",
        width="30%",
        box_shadow="md",
        _hover={"transform": "translateY(-5px)", "box_shadow": "lg"},
        transition="all 0.3s ease-in-out",
    )

def feature_card(title: str, description: str, icon: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon, color="rgb(244, 191, 12)", size=35),
                bg="white",
                padding="10px",
                border_radius='50%'
            ),
            rx.heading(title, size='6', color="white", margin_top="0.5em", align="center"),
            rx.text(description, color="white",size='3.5', text_align="center"),
            align_items="center",
            spacing="3"
        ),
        bg="rgb(244, 191, 12)",
        border="1px solid",
        border_color="white",
        border_radius="20px",
        padding="1.5em",
        width="250px",
        height="250px",
        box_shadow="lg",
        _hover={
            "transform": "translateY(-12px)",
            "box_shadow": "xl",
        },
        transition="all 0.3s ease-in-out",
    )

def url_input():
    return rx.input(
        placeholder="URL",
        name="url",
        align="center",
        border="1px solid rgb(245,225,71)",
        margin_bottom='1em',
    )

def file_upload():
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color="black",
                    bg=rx.color("yellow", shade=11),
                    border="1px solid rgb(245,225,71)",
                    align="center"
                ),
                rx.text(
                    "Drag and drop text file here or click to select"
                ),
                align='center'
            ),
            id="readme",
            border="2px solid rgb(245,225,71)",
            padding="5em",
            accept={".txt": []},  # Only accept .txt files
            align="center",
            border_radius='20px'
        ),
        rx.hstack(rx.foreach(rx.selected_files("readme"), rx.text)),
        rx.hstack(
            rx.button(
                "Upload",
                on_click=State.handle_upload(rx.upload_files(upload_id="readme")),
                color="black",
                bg=rx.color("yellow", shade=11),
                margin_right='343px'
            ),
            rx.button(
                "Clear",
                color="black",
                bg=rx.color("yellow", shade=11),
                on_click=[
                    rx.clear_selected_files("readme"),
                    State.clear_file
                ],
            ),
        ),

    )

def inputs():
    return rx.vstack(
        rx.form(
            rx.vstack(
                url_input(),
                file_upload(),
                rx.button(
                    "Analyze UI",
                    type="submit",
                    color="black",
                    bg=rx.color("yellow", shade=11)
                ),
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

def team_member(name: str, role: str, image: str) -> rx.Component:
    return rx.vstack(
        rx.avatar(name=name, size="xl", src=image),
        rx.text(name, font_weight="bold"),
        rx.text(role, color="gray"),
        bg="white",
        padding="1em",
        border_radius="lg",
        box_shadow="lg",
        _hover={"transform": "scale(1.05)"},
        transition="all 0.2s ease-in-out",
    )

def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("About Swarm", size="9", margin_bottom="1em"),
            rx.text(
                "Revolutionizing UI/UX Testing with AI",
                color=rx.color("yellow", shade=11),
                font_size="2xl",
                margin_bottom="2em",
            ),
            rx.flex(
                rx.vstack(
                    rx.heading("Our Mission", size="7"),
                    rx.text(
                        "At Swarm, we're on a mission to simplify and enhance UI/UX testing. "
                        "By leveraging cutting-edge AI technology, we provide instant, "
                        "accurate, and actionable insights to improve your product's user experience.",
                        max_width="600px",
                    ),
                    align_items="start",
                    width="50%",
                ),
                rx.image(
                    src="/mission_image.jpg",  # Replace with your actual image
                    height="300px",
                    width="50%",
                    object_fit="cover",
                    border_radius="lg",
                ),
                width="100%",
                margin_bottom="3em",
            ),
            rx.divider(),
            rx.heading("Our Team", size="7", margin_y="1em"),
            rx.hstack(
                team_member("Alice Johnson", "Founder & CEO", "/alice.jpg"),
                team_member("Bob Smith", "CTO", "/bob.jpg"),
                team_member("Carol Davis", "Lead Designer", "/carol.jpg"),
                team_member("David Brown", "AI Specialist", "/david.jpg"),
                spacing="8",
                justify="center",
                wrap="wrap",
            ),
            rx.divider(),
            rx.heading("Our Approach", size="7", margin_y="1em"),
            rx.hstack(
                rx.vstack(
                    rx.icon("search", color="yellow", size=4),
                    rx.text("Analyze", font_weight="bold"),
                    rx.text("Deep dive into UI elements"),
                    padding="1em",
                    bg="rgba(244, 191, 12, 0.1)",
                    border_radius="lg",
                ),
                rx.vstack(
                    rx.icon("lightbulb", color="yellow", size=4),
                    rx.text("Innovate", font_weight="bold"),
                    rx.text("Generate creative solutions"),
                    padding="1em",
                    bg="rgba(244, 191, 12, 0.1)",
                    border_radius="lg",
                ),
                rx.vstack(
                    rx.icon("repeat", color="yellow", size=4),
                    rx.text("Iterate", font_weight="bold"),
                    rx.text("Continuous improvement"),
                    padding="1em",
                    bg="rgba(244, 191, 12, 0.1)",
                    border_radius="lg",
                ),
                spacing="4",
                margin_y="2em",
                wrap="wrap",
            ),
            rx.divider(),
            rx.vstack(
                rx.heading("Get in Touch", size="7"),
                rx.text("Have questions or want to learn more? We'd love to hear from you!"),
                rx.hstack(
                    rx.link(
                        rx.button("Contact Us", color_scheme="yellow"),
                        href="mailto:info@swarm.ai",
                    ),
                    rx.link(
                        rx.button("Documentation", variant="outline", color_scheme="yellow"),
                        href="/docs",
                    ),
                    spacing="4",
                ),
                margin_y="2em",
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="2em",
            spacing="6",
        ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index)
app.add_page(dashboard)
app.add_page(about)

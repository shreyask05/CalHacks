"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import asyncio

from CalHacks.main import UXENGINE
from CalHacks.process import get_html 
import asyncio
import groq as Groq
from reflex_text_loop import TextLoop
from reflex_motion import motion
import json

class impressionState(rx.State):
    data: list = []

    def load_data(self):
        with open("./CalHacks/first_impressions.json") as file:
            self.data = json.load(file)
            
class swarmState(rx.State):
    swarm_data: list = []
    
    def load_swarm_data():
        with open("./CalHacks/results.json", "r") as file:
            swarm_data = json.load(file)

class charState(rx.State):
    data: list = []

    def load_data(self):
        with open("./CalHacks/characters.json") as file:
            self.data = json.load(file)


class State(rx.State):
    url: str = ""
    details: str = ""
    is_loading: bool = False
    

    async def handle_submit(self, form_data: dict):
        self.url = form_data.get("url", "")
        self.details = form_data.get("details", "")
        get_html(self.url, "APP.html")
        self.is_loading = True
        return rx.redirect("/loading")

    async def finish_loading(self):
        await asyncio.sleep(3)  # Wait for 3 seconds
        self.is_loading = False  # Stop loading after waiting
        print("redirecting")
        return rx.redirect("/results")

    def clear_fields(self):
        self.url = ""
        self.details = ""

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="5", weight="medium"),
        href=url,
        color="black",
        text_decoration="none",
        _hover={"text_decoration": "underline", "color": "white"}
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(src="/swarm.png", height="6em", width="8em", radius="20px"),
                rx.heading(
                    "Swarm",
                    size="8",
                    weight="bold",
                    color="black"
                ),
                spacing="0",
                align="center"
            ),
            rx.spacer(),
            rx.desktop_only(
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("Dashboard", "/dashboard"),
                    navbar_link("About", "/about"),
                    spacing="6",
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
                            _hover={"transform": "scale(1.1)","bg": "rgb(244, 191, 12)"}
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
        width="100%",
    )

def index():
    return rx.box(
        navbar(),
        rx.vstack(
            motion(
                rx.heading(
                    "Welcome to Swarm",
                    size="9",
                    margin_top="0.8em",
                    align="center",
                ),
                while_hover={"scale": 1.2},
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),

            rx.text(
                "Test your product's UI / UX with ",
                TextLoop(
                    rx.text.strong("ease", color="rgb(244, 191, 12)"),
                    rx.text.strong("efficiency", color="rgb(244, 191, 12)"),
                    rx.text.strong("speed", color="rgb(244, 191, 12)"),
                    rx.text.strong("clarity", color="rgb(244, 191, 12)"),
                    rx.text.strong("consistency", color="rgb(244, 191, 12)"),
                ),
                margin_top="1em",
                size="5",
                color="white",
                margin_bottom="1em",
                margin_right="3em",
            ),
            rx.link(
                rx.button(
                    "Try Swarm Now",
                    color="black",
                    background_color="rgb(244, 191, 12)",
                    size="4",
                ),
                href="/dashboard",
                is_external=False
            ),
            rx.divider(margin_y="1em"),
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
            rx.heading("How It Works", size="7", margin_bottom="10px"),
            how_it_works_section(),
            rx.divider(margin_y="2em"),
            rx.heading("Get Started Today", size="7", margin_bottom="1em"),
            rx.link(
                rx.button(
                    "Try Swarm Now",
                    color="black",
                    background_color="rgb(244, 191, 12)",
                    size="4",
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
        align="center",
    )

def how_it_works_section():
    return rx.box(
        rx.vstack(
            rx.text(
                rx.text.strong("Upload"), " your design or provide a URL for instant analysis.",
                size="5",
                color="white",
                align="center",
                margin_bottom="10px"
            ),
            rx.text("Our AI performs a ", rx.text.strong("comprehensive"), " analysis of your UI/UX.",
                size="5",
                color="white",
                align="center",
                margin_bottom="10px"
            ),
            rx.text(
                "Receive actionable insights to ", rx.text.strong("enhance"), " your product.",
                size="5",
                color="white",
                align="center"
            ),
            align="center",

        ),
        align="center",
        border="1px solid",
        border_color="rgb(244, 191, 12)",
        border_radius="2em",
        padding="2em"
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
            rx.text(description, color="black",size='3.5', text_align="center"),
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
            "box_shadow": "xl"
        },
        transition="all 0.3s ease-in-out",
    )

def url_input():
    return rx.input(
        placeholder="Enter URL",
        name="url",
        align="center",
        border="1px solid rgb(244, 191, 12)",
        margin_bottom='1em',
        padding="0.5em 1em",
        border_radius="md",
    )

def large_text_input():
    return rx.text_area(
        placeholder="Enter detailed information on your target audience",
        name="details",
        align="center",
        border="1px solid rgb(244, 191, 12)",
        margin_bottom='1em',
        padding="1em",
        border_radius="md",
        width="100%",
        height="150px",
    )

def clear_button():
    return rx.button(
        "Clear",
        color="black",
        background_color="rgb(244, 191, 12)",
        on_click=State.clear_fields,  # Just clears the input fields
        padding="0.5em 2em",
        border_radius="md",
        _hover={"bg": "rgb(245,225,71)"},
    )

def inputs():
    return rx.vstack(
        rx.form(
            rx.vstack(
                url_input(),
                large_text_input(),
                rx.hstack(
                    rx.button(
                        "Analyze UI",
                        type="submit",
                        color="black",
                        background_color="rgb(244, 191, 12)",
                        padding="0.5em 2em",
                        border_radius="md",
                        _hover={"bg": "rgb(245,225,71)"},
                    ),
                    clear_button(),
                    spacing="1em"
                ),
                align_items="center",
                justify_content="center",
            ),
            on_submit=State.handle_submit,
            reset_on_submit=True,
            align_items="center",
            justify_content="center",
            width="100%",
            max_width="600px",
            padding="2em",
        ),
        rx.divider(),
        rx.heading("Results", size="6", margin_top='2em'),
        rx.text("URL: " + State.url),
        rx.text("Details: " + State.details),
        align_items="center",
        justify_content="center",
    )

def dashboard():
    return rx.box(
        navbar(),
        rx.divider(),
        inputs(),
    )

def team_member(name: str, role: str, image: str, linkedin_url: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.avatar(name=name, size="7", src=image),
            rx.text(name, font_weight="bold", color="black"),
            rx.text(role, color="black"),
            height="100%",
            bg="white",
            padding="1em",
            border_radius="lg",
            box_shadow="lg",
            _hover={"transform": "scale(1.1)"},
            transition="all 0.2s ease-in-out",
        ),
        href=linkedin_url,
        is_external=True,
        _hover={"text_decoration": "none"},
    )

def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("About Swarm", size="9", margin_bottom="1em"),
            rx.text(
                "Revolutionizing UI/UX Testing with",
                TextLoop(
                    rx.text.strong("AI", color="white"),
                    rx.text.strong("ML", color="white"),
                    rx.text.strong("NLP", color="white"),
                    rx.text.strong("LLM", color="white"),
                ),
                color="rgb(244, 191, 12)",
                font_size="1.5em",
                margin_bottom="1.2em",
            ),
            rx.flex(
                rx.vstack(
                    rx.heading("Our Mission", size="7"),
                    rx.text(
                        "At Swarm, we're on a mission to simplify and enhance UI/UX testing. "
                        "By leveraging cutting-edge AI technology, we provide instant, "
                        "accurate, and actionable insights to improve your product's user experience.",
                        max_width="600px", size="5"
                    ),
                    align_items="start",
                    width="50%",
                ),
                rx.image(src="/swarm.png", height="15em", width="20em", border_radius="20px"),
                width="100%",
                margin_bottom="3em",
            ),
            rx.divider(),
            rx.heading("Our Team", size="7", margin_y="1em"),
            rx.hstack(
                team_member("Shreyas Konanki", "Founder & CEO", "/shreyas.png", "https://www.linkedin.com/in/shreyas-konanki"),
                team_member("Rohan Bopardikar", "CTO", "/rohan.png", "https://www.linkedin.com/in/rbopardi/"),
                team_member("Harshith Senthilkumaran", "Lead Designer", "/harshith.png", "https://www.linkedin.com/in/harshith-senthilkumaran/"),
                team_member("Darsh Verma", "AI Specialist", "/darsh.png", "https://www.linkedin.com/in/darshucla/"),
                spacing="8",
                justify="center",
                wrap="wrap",
            ),
            rx.divider(),
            rx.heading("Our Approach", size="7", margin_y="0em"),
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.icon("search", color="yellow", size=20),
                        rx.text("Analyze", font_weight="bold"),
                    ),
                    rx.text("Deep dive into UI elements"),
                    padding="1em",
                    bg="rgba(244, 191, 12,0.1)",
                    border_radius="lg",
                    _hover={"transform": "scale(1.05)", "color": "rgb(244, 191, 12)"}
                ),
                rx.vstack(
                    rx.hstack(
                        rx.icon("lightbulb", color="yellow", size=20),
                        rx.text("Innovate", font_weight="bold"),
                    ),
                    rx.text("Generate creative solutions"),
                    padding="1em",
                    bg="rgba(244, 191, 12, 0.1)",
                    border_radius="lg",
                    _hover={"transform": "scale(1.05)", "color": "rgb(244, 191, 12)"}
                ),
                rx.vstack(
                    rx.hstack(
                        rx.icon("repeat", color="yellow", size=20),
                        rx.text("Iterate", font_weight="bold"),
                    ),
                    rx.text("Continuous improvement"),
                    padding="1em",
                    bg="rgba(244, 191, 12, 0.1)",
                    border_radius="lg",
                    _hover={"transform": "scale(1.05)", "color": "rgb(244, 191, 12)"}
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
                        href="https://reflex.dev/docs/getting-started/introduction/",
                        is_external=True
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

def loading_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.spinner(size="3", color="rgb(244, 191, 12)"),
            rx.text("Analyzing your UI, please wait...", font_size="2xl", margin_top="1em", color="rgb(244, 191, 12)"),
            align_items="center",
            justify_content="center",
            min_height="85vh",
        ),
        background_color="black",

    )

class AgentState(rx.State):
    feedback_modal: dict[str, bool] = {}

    def toggle_feedback(self, agent_name: str):
        for name in self.feedback_modal:
            self.feedback_modal[name] = False
        self.feedback_modal[agent_name] = not self.feedback_modal.get(agent_name, False)

def agent_card(name: str, description: str, feedback: str) -> rx.Component:
    return rx.vstack(
        rx.icon("user", color="rgb(244, 191, 12)", size=35),
        rx.text(name, font_weight="bold", color="rgb(244, 191, 12)"),
        rx.text(description, color="white", text_align="center"),
        rx.popover.root(
            rx.popover.trigger(
                rx.button(
                    "Show Feedback",
                    color="black",
                    bg="rgb(244, 191, 12)",
                    _hover={"bg": "rgba(244, 191, 12, 0.8)"}
                )
            ),
            rx.popover.content(
                rx.flex(
                    rx.heading(f"Feedback from {name}", size="lg", color="rgb(244, 191, 12)"),
                    rx.text(feedback, color="white"),
                    rx.popover.close(
                        rx.button(
                            "Close",
                            color="black",
                            bg="rgb(244, 191, 12)",
                            _hover={"bg": "rgba(244, 191, 12, 0.8)"}
                        )
                    ),
                    direction="column",
                    spacing="3",
                    bg="black",
                    border="1px solid rgb(244, 191, 12)",
                    padding="1em",
                    max_width="300px",
                )
            )
        ),
        bg="rgba(244, 191, 12, 0.2)",
        border="1px solid rgb(244, 191, 12)",
        border_radius="lg",
        padding="1em",
        width="200px",
        height="200px",
        _hover={"transform": "scale(1.05)", "bg": "rgba(244, 191, 12, 0.3)"},
        transition="all 0.2s ease-in-out",
    )

def log_card(key: str, value: str) -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(
            rx.box(
                rx.text(key, color="white", font_weight="bold"),
                bg="rgba(244, 191, 12, 0.1)",
                border="1px solid rgb(244, 191, 12)",
                border_radius="lg",
                padding="1em",
                margin_bottom="0.5em",
                cursor="pointer",
                _hover={"bg": "rgba(244, 191, 12, 0.2)"},
            )
        ),
        rx.popover.content(
            rx.flex(
                rx.text(f"Log: {key}", font_weight="bold"),
                rx.text(value),
                rx.popover.close(
                    rx.button("Close", color="black", bg="rgb(244, 191, 12)")
                ),
                direction="column",
                spacing="3",
                bg="black",
                border="1px solid rgb(244, 191, 12)",
                padding="1em",
                max_width="300px",
            )
        )
    )

def swarm_results() -> rx.Component:
    f = open("./CalHacks/results.json")
    data = json.load(f)
    f.close()
    return rx.table.body(
        rx.foreach(
            data,
            lambda row: rx.table.row(
                rx.table.cell(row["case"], color="white"),
                rx.table.cell(row["result"], color="white"),
            ),
        )
    )
    
def first_impression_results() -> rx.Component:
    f = open("./CalHacks/first_impressions.json")
    data = json.load(f)
    f.close()
    return rx.foreach(
        data,
        lambda row: rx.table.row(
            agent_card(row["name"], row["summary"], row["feedback"])
        ),
    )

def results_page() -> rx.Component:
    
    with open('log.json', 'r') as json_file:
        data = json.load(json_file)
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("Analysis Results", size="9", margin_top="1em", margin_bottom="0.5em", color="white"),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("First Impression", value="first_impression", color="black"),
                    rx.tabs.trigger("Swarm Test", value="swarm_test", color="black"),
                    background_color="rgb(244, 191, 12)",
                ),
                rx.tabs.content(
                    rx.flex(
                        # agent_card("Bonnie", "UI/UX Specialist", "The website has a clean and modern design. The layout is intuitive, but there's room for improvement in the mobile responsiveness."),
                        # agent_card("William", "Color Theory Expert", "The color scheme is cohesive and aligns well with the brand. Consider adding more contrast for better readability in some sections."),
                        # agent_card("Brian", "Usability Tester", "Navigation is straightforward, but some interactive elements could benefit from clearer visual cues for better user engagement."),
                        # agent_card("Kylie", "Accessibility Analyst", "Overall accessibility is good, but there are opportunities to enhance screen reader compatibility and keyboard navigation."),
                        first_impression_results(),
                        spacing="4",
                        justify="center",
                        wrap="wrap",
                        margin_top="10em"
                    ),
                    value="first_impression",
                ),
                rx.tabs.content(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Case", color="rgb(244, 191, 12)", font_weight="bold"),
                                rx.table.column_header_cell("Result", color="rgb(244, 191, 12)", font_weight="bold"),
                            ),
                            background_color="black",
                        ),
                        swarm_results(),
                        width="100%",
                        border="1px solid rgba(255, 255, 255, 0.2)",
                        border_radius="md",
                        overflow="hidden",
                    ),
                    rx.button("Download log", on_click=rx.download(url="/web_agent.log")),
                    value="swarm_test",
                ),
                width="100%",
            ),
            align_items="stretch",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="2em",
        ),
        background_color="black",
        min_height="100vh",
    )

app = rx.App()
app.add_page(index)
app.add_page(dashboard)
app.add_page(about)
app.add_page(loading_page, route="/loading", on_load=State.finish_loading)
app.add_page(results_page, route="/results")


'''
this is how you show the info in the results page if needed for testing
rx.box(
                rx.text("URL: " + State.url, color="white"),
                rx.text("Details: " + State.details, color="white"),
                margin_top="0em",
                margin_bottom="2em",
                padding="1em",
                border_radius="md",
                width="100%",
            )
'''
"""FixMyText — Arabic Keyboard Layout Corrector built with Reflex 0.7+."""

from rxconfig import config
import reflex as rx
import pyperclip

# -----------------------------
# 🔤 Text Conversion Dictionary
# -----------------------------
fixTextDict = {
    "a": "ش", "b": "لا", "c": "ؤ", "d": "ي", "e": "ث", "f": "ب",
    "g": "ل", "h": "ا", "i": "ه", "j": "ت", "k": "ن", "l": "م",
    "m": "ة", "n": "ى", "o": "خ", "p": "ح", "q": "ض", "r": "ق",
    "s": "س", "t": "ف", "u": "ع", "v": "ر", "w": "ص", "x": "ء",
    "y": "غ", "z": "ئ", "`": "ذ", "'": "ط", ";": "ك", "/": "ظ",
    "[": "ج", "]": "د", ".": "ز", ",": "و",
}

# -----------------------------
# 🧠 App State
# -----------------------------
class State(rx.State):
    bad_text: str = ""
    fixed_text: str = ""

    def set_text(self, value: str):
        self.bad_text = value

    def fix_my_text(self):
        """Convert English-layout Arabic letters into proper Arabic."""
        result = ""
        for ch in self.bad_text.lower():
            result += fixTextDict.get(ch, ch)
        self.fixed_text = result


# -----------------------------
# 🎨 Colors
# -----------------------------
light_blue = "#cfecf7"
normal_blue = "#54b3d6"
dark_blue = "#12282d"

# -----------------------------
# 🧩 Bottom Bar
# -----------------------------
def bottombar():
    return rx.flex(
        rx.text(
            "© 2025 Developed and Designed With 💖 by ",
            font_size="0.8em",
            font_family="Vobca-Black",
            color=light_blue,
        ),
        rx.link(
            "Osama Abd El Mohsen",
            href="https://github.com/Osama-Abd-El-Mohsen",
            color=normal_blue,
            font_family="Vobca-Black",
            font_size="0.8em",
        ),
        justify="center",
        align="center",
        direction="row",
        padding="6px",
        background_color=dark_blue,
        position="fixed",
        bottom="0",
        width="100%",
        z_index="500",
    )

# -----------------------------
# 🏠 Main Page
# -----------------------------
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Welcome To Fix My Text Website!",
                size="9",
                align="center",
                font_family="Vobca-Black",
                font_size=["1.7em", "2.5em"],
            ),
            rx.card(
                rx.vstack(
                    rx.heading(
                        "Enter Arabic text written in English layout to fix 🔧",
                        size="7",
                        font_family="Vobca-Black",
                        align="center",
                    ),
                    rx.text_area(
                        placeholder="Enter some text...",
                        size="1",
                        variant="soft",
                        font_family="Cairo",
                        on_change=State.set_text,
                        value=State.bad_text,
                        style = {"width":"100%"}
                    ),
                    rx.button(
                        "Fix Text",
                        on_click=State.fix_my_text,
                        color_scheme="cyan",
                        size="3",
                    ),
                    rx.text_area(
                        placeholder="Result...",
                        variant="soft",
                        font_family="Cairo",
                        is_read_only=True,
                        value=State.fixed_text,
                        style = {"width":"100%"}
                        
                    ),
                    rx.button(
                        "Copy Result",
                        on_click=rx.set_clipboard(State.fixed_text),
                        color_scheme="gray",
                        size="3",
                    ),
                    spacing="4",
                    align="center",
                ),
                style={"maxWidth": "800px", "width": "100%"},
                padding="2em",
            ),
            bottombar(),
            align="center",
            spacing="7",
        ),
        height="100vh",
        padding="2em",
        background=(
            "repeating-linear-gradient(45deg, #0e343a, #0e343a 5%, "
            "#12282d 5%, #12282d 40%)"
        ),

        style = {
        '@keyframes move-it': {
            '0%': {
                'background-position': 'initial'
            },
            '100%': {
                'background-position': '100px 0px'
            }
        },
        'background': 'repeating-linear-gradient(45deg, #0e343a, #0e343a 5%, #12282d 5%, #12282d 40%)',
        'background-size': '100px 100px',
        'animation': 'move-it 2s linear infinite'
    }
        
    )

# -----------------------------
# 🚀 App Configuration
# -----------------------------
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="cyan",
        radius="large",
        panel_background="translucent",
    ),
    stylesheets=[
        "/fonts/myfont.css",
        "/styles.css",
    ],
)

app.add_page(index, route="/", title="Fix My Text")


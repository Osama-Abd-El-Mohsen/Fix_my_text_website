"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
import pyperclip

fixTextDict={
    'a':'ش',
    'b':'لا',
    'c':'ؤ',
    'd':'ي',
    'e':'ث',
    'f':'ب',
    'g':'ل',
    'h':'ا',
    'i':'ه',
    'j':'ت',
    'k':'ن',
    'l':'م',
    'm':'ة',
    'n':'ى',
    'o':'خ',
    'p':'ح',
    'q':'ض',
    'r':'ق',
    's':'س',
    't':'ف',
    'u':'ع',
    'v':'ر',
    'w':'ص',
    'x':'ء',
    'y':'غ',
    'z':'ئ',
    '`':'ذ',
    "'":'ط',
    ";":'ك',
    "/":'ظ',
    "[":'ج',
    "]":'د',
    ".":'ز',
    ",":'و',
}
class TextAreaBlur(rx.State):
    text: str = ""
    fixedText = ''
    BadText=''
    
    def set_text(self, value):
        self.BadText = value
        State.alert = 2


    def FixMyText(self):
        self.fixedText = ''
        for x in self.BadText.lower() :
            if x in fixTextDict.keys():
                self.fixedText+=fixTextDict[f'{x}']
            else  :
                self.fixedText+=x



class State(rx.State):
    BadText:str =''

light_blue = '#cfecf7'
normal_blue = '#54b3d6'
dark_blue = '#12282d'

def bottombar():
    return rx.flex(
        rx.desktop_only(
            rx.center(
                rx.hstack(
                    rx.text(
                        "© 2024 Developed and Designed With 💖 by : ".upper(),
                        font_size=[".7em"],
                        font_family="Vobca-Black",
                        color=light_blue,
                    ),
                    rx.link(
                        "Osama Abd El Mohsen".upper(),
                        font_size=[".7em"],
                        href='https://github.com/Osama-Abd-El-Mohsen',
                        font_family="Vobca-Black",
                        color=normal_blue,
                    ),
                ),
                align='center'
            ),
        ),
        rx.mobile_and_tablet(
            rx.chakra.responsive_grid(
                rx.text(
                    "© 2024 Developed and Designed With 💖 by  ".upper(),
                    font_size=[".5em"],
                    font_family="Vobca-Black",
                    color=light_blue,
                    align='center'
                ),
                rx.center(
                rx.link(
                    "Osama Abd El Mohsen".upper(),
                    href='https://github.com/Osama-Abd-El-Mohsen',
                    font_size=[".5em"],
                    font_family="Vobca-Black",
                    color=normal_blue,
                    align='center'
                ),
                )
            ),
            columns=[1],
            padding="2px",
        ),
        direction='row',
        align="center",
        justify="center",
        position="fixed",
        bottom="0",
        width="100%",
        padding="2px",
        background_color='#12282d',
        z_index="500",
        color=light_blue,
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            bottombar(),
            rx.heading(
                "Welcome To Fix My Text Website!", size="9",
                align='center',
                font_family="Vobca-Black",font_size=["1.7em",'2.5em'],
                class_name='hover-text'),
            rx.card(
                rx.flex(
                    rx.heading(
                        " Enter Some ArabicText in English layout To Fix 🔧 " ,size= '7',font_family="Vobca-Black"),
                    rx.chakra.text_area(
                        placeholder="Enter Some Text....", size='5',
                        required=True,
                        variant='filled',
                        font_size=[".7em",'1em'],
                        font_family="cairo",
                        on_blur= TextAreaBlur.set_text ),
                    rx.button(
                        "Fix",
                        on_click=TextAreaBlur.FixMyText(),
                        font_size=[".7em",'1em'],
                        font_family="Vobca-Black",
                        variant = 'soft',
                        size ='3'),
                    rx.chakra.text_area(
                        placeholder="Result ....",
                        size='3',
                        font_size=[".7em",'1em'],
                        is_read_only=True,
                        variant='filled',
                        font_family="cairo",
                        value= TextAreaBlur.fixedText ),
                    rx.button(
                        "Copy Result",
                        font_size=[".7em",'1em'],
                        font_family="Vobca-Black",
                        variant = 'soft',
                        on_click=rx.set_clipboard(TextAreaBlur.fixedText),
                        size ='3'),
                    direction="column",
                    variant='soft',
                    spacing="3",
                ),
                style={"maxWidth": 1000},
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
        padding="5px",
    )

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
app = rx.App(
    style=style,
    stylesheets=[
        "/fonts/myfont.css",
        "/styles.css",
    ],
    theme=rx.theme(
        appearance="dark",
        accent_color="cyan",
        grayColor="sage",
        panel_background='translucent',
        radius="large")
)
app.add_page(index)

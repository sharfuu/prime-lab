from kivy.app import App
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


# ---------------------------------
# CUSTOM FONTS
# ---------------------------------

FONT_REGULAR = "fonts/SpaceGrotesk-Regular.ttf"
FONT_MEDIUM = "fonts/SpaceGrotesk-Medium.ttf"
FONT_SEMIBOLD = "fonts/SpaceGrotesk-SemiBold.ttf"
FONT_BOLD = "fonts/SpaceGrotesk-Bold.ttf"


LabelBase.register(
    name="SpaceGrotesk",
    fn_regular=FONT_REGULAR
)

LabelBase.register(
    name="SpaceGroteskMedium",
    fn_regular=FONT_MEDIUM
)

LabelBase.register(
    name="SpaceGroteskSemiBold",
    fn_regular=FONT_SEMIBOLD
)

LabelBase.register(
    name="SpaceGroteskBold",
    fn_regular=FONT_BOLD
)


# ---------------------------------
# DARK THEME
# ---------------------------------

Window.clearcolor = (0.055, 0.065, 0.10, 1)

BG = (0.055, 0.065, 0.10, 1)
CARD = (0.10, 0.12, 0.17, 1)

WHITE = (0.94, 0.95, 0.98, 1)
MUTED = (0.68, 0.72, 0.80, 1)

BLUE = (0.25, 0.45, 0.90, 1)
GREEN = (0.25, 0.65, 0.45, 1)
PURPLE = (0.55, 0.35, 0.85, 1)


# ---------------------------------
# PRIME FUNCTIONS
# ---------------------------------

def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:

        if n % i == 0:
            return False

        i += 2

    return True


def goldbach_pairs(n):

    pairs = []

    for p in range(2, n // 2 + 1):

        if is_prime(p) and is_prime(n - p):
            pairs.append((p, n - p))

    return pairs


def generate_primes(limit):

    primes = []

    for n in range(2, limit + 1):

        if is_prime(n):
            primes.append(n)

    return primes


def calculate_prime_gaps(primes):

    gaps = []

    for i in range(len(primes) - 1):

        p1 = primes[i]
        p2 = primes[i + 1]

        gaps.append(
            (p1, p2, p2 - p1)
        )

    return gaps


# ---------------------------------
# CARD BUTTON
# ---------------------------------

class CardButton(Button):

    def __init__(self, accent_color, **kwargs):

        super().__init__(**kwargs)

        self.font_name = "SpaceGroteskMedium"

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:

            Color(*CARD)

            self.card = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(18)]
            )

            Color(*accent_color)

            self.accent = RoundedRectangle(
                pos=self.pos,
                size=(dp(6), self.height),
                radius=[dp(18)]
            )

        self.bind(
            pos=self.update_graphics,
            size=self.update_graphics
        )

    def update_graphics(self, *args):

        self.card.pos = self.pos
        self.card.size = self.size

        self.accent.pos = self.pos

        self.accent.size = (
            dp(6),
            self.height
        )


# ---------------------------------
# PRIME LAB APP
# ---------------------------------

class PrimeLabApp(App):

    def build(self):

        self.root_layout = BoxLayout(
            orientation="vertical"
        )

        self.show_home()

        return self.root_layout


    # ---------------------------------
    # CLEAR SCREEN
    # ---------------------------------

    def clear_screen(self):

        self.root_layout.clear_widgets()


    # =================================
    # HOME
    # =================================

    def show_home(self):

        self.clear_screen()

        root = BoxLayout(
            orientation="vertical",
            padding=[
                dp(24),
                dp(28),
                dp(24),
                dp(20)
            ],
            spacing=dp(12)
        )

        root.add_widget(
            Label(
                text="PRIME LAB",
                font_name="SpaceGroteskBold",
                font_size=dp(27),
                bold=True,
                color=WHITE,
                size_hint_y=None,
                height=dp(45)
            )
        )

        root.add_widget(
            Label(
                text="Explore the mathematics of prime numbers",
                font_name="SpaceGrotesk",
                font_size=dp(14),
                color=MUTED,
                size_hint_y=None,
                height=dp(32)
            )
        )

        root.add_widget(
            Label(
                text="",
                size_hint_y=None,
                height=dp(45)
            )
        )

        # GOLDBACH

        goldbach = CardButton(
            accent_color=BLUE,
            text=(
                "GOLDBACH PRIME PAIRS\n\n"
                "Write an even number as a sum of two primes"
            ),
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            size_hint_y=None,
            height=dp(105)
        )

        goldbach.bind(
            on_release=lambda x: self.show_goldbach()
        )

        root.add_widget(goldbach)

        # GENERATOR

        generator = CardButton(
            accent_color=GREEN,
            text=(
                "PRIME GENERATOR\n\n"
                "Generate prime numbers up to a limit"
            ),
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            size_hint_y=None,
            height=dp(105)
        )

        generator.bind(
            on_release=lambda x: self.show_generator()
        )

        root.add_widget(generator)

        # GAPS

        gaps = CardButton(
            accent_color=PURPLE,
            text=(
                "PRIME GAPS\n\n"
                "Explore the gaps between consecutive primes"
            ),
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            size_hint_y=None,
            height=dp(105)
        )

        gaps.bind(
            on_release=lambda x: self.show_gaps()
        )

        root.add_widget(gaps)

        root.add_widget(
            Label(
                text="",
                size_hint_y=1
            )
        )

        root.add_widget(
            Label(
                text="Prime Lab • v1.1",
                font_name="SpaceGrotesk",
                font_size=dp(11),
                color=(0.50, 0.55, 0.63, 1),
                size_hint_y=None,
                height=dp(25)
            )
        )

        self.root_layout.add_widget(root)


    # =================================
    # GOLDBACH
    # =================================

    def show_goldbach(self):

        self.clear_screen()

        root = BoxLayout(
            orientation="vertical",
            padding=[
                dp(24),
                dp(25),
                dp(24),
                dp(18)
            ],
            spacing=dp(12)
        )

        root.add_widget(
            Label(
                text="GOLDBACH PRIME PAIRS",
                font_name="SpaceGroteskBold",
                font_size=dp(23),
                color=WHITE,
                size_hint_y=None,
                height=dp(50)
            )
        )

        root.add_widget(
            Label(
                text="Enter an even number",
                font_name="SpaceGrotesk",
                font_size=dp(14),
                color=MUTED,
                size_hint_y=None,
                height=dp(30)
            )
        )

        self.goldbach_input = TextInput(
            hint_text="Example: 100",
            font_name="SpaceGrotesk",
            font_size=dp(18),
            multiline=False,
            input_filter="int",
            foreground_color=WHITE,
            hint_text_color=MUTED,
            background_color=CARD,
            cursor_color=BLUE,
            padding=[
                dp(15),
                dp(12)
            ],
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.goldbach_input)

        calculate = Button(
            text="FIND PRIME PAIRS",
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            background_normal="",
            background_color=BLUE,
            size_hint_y=None,
            height=dp(55)
        )

        calculate.bind(
            on_release=lambda x: self.calculate_goldbach()
        )

        root.add_widget(calculate)

        self.goldbach_result = Label(
            text="",
            font_name="SpaceGrotesk",
            font_size=dp(16),
            color=WHITE,
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.goldbach_result.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1])
        )

        scroll = ScrollView()

        scroll.add_widget(self.goldbach_result)

        root.add_widget(scroll)

        root.add_widget(
            Label(
                text="",
                size_hint_y=1
            )
        )

        back = Button(
            text="<-  BACK",
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            background_normal="",
            background_color=(0.16, 0.18, 0.24, 1),
            size_hint_y=None,
            height=dp(48)
        )

        back.bind(
            on_release=lambda x: self.show_home()
        )

        root.add_widget(back)

        self.root_layout.add_widget(root)


    def calculate_goldbach(self):

        value = self.goldbach_input.text.strip()

        if not value:

            self.goldbach_result.text = (
                "Please enter an even number."
            )

            return

        n = int(value)

        if n < 4 or n % 2 != 0:

            self.goldbach_result.text = (
                "Please enter an even number >= 4."
            )

            return

        pairs = goldbach_pairs(n)

        result = (
            f"{n} = p + q\n\n"
            f"Found {len(pairs)} prime pair(s):\n\n"
        )

        for p, q in pairs:

            result += f"{p} + {q} = {n}\n"

        self.goldbach_result.text = result


    # =================================
    # PRIME GENERATOR
    # =================================

    def show_generator(self):

        self.clear_screen()

        root = BoxLayout(
            orientation="vertical",
            padding=[
                dp(24),
                dp(25),
                dp(24),
                dp(18)
            ],
            spacing=dp(12)
        )

        root.add_widget(
            Label(
                text="PRIME GENERATOR",
                font_name="SpaceGroteskBold",
                font_size=dp(23),
                color=WHITE,
                size_hint_y=None,
                height=dp(50)
            )
        )

        root.add_widget(
            Label(
                text="Generate all prime numbers up to a limit",
                font_name="SpaceGrotesk",
                font_size=dp(14),
                color=MUTED,
                size_hint_y=None,
                height=dp(30)
            )
        )

        self.generator_input = TextInput(
            hint_text="Example: 100",
            font_name="SpaceGrotesk",
            font_size=dp(18),
            multiline=False,
            input_filter="int",
            foreground_color=WHITE,
            hint_text_color=MUTED,
            background_color=CARD,
            cursor_color=GREEN,
            padding=[
                dp(15),
                dp(12)
            ],
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.generator_input)

        generate = Button(
            text="GENERATE PRIMES",
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            background_normal="",
            background_color=GREEN,
            size_hint_y=None,
            height=dp(55)
        )

        generate.bind(
            on_release=lambda x: self.calculate_primes()
        )

        root.add_widget(generate)

        self.prime_count = Label(
            text="",
            font_name="SpaceGroteskBold",
            font_size=dp(32),
            color=GREEN,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.prime_count)

        self.prime_count_description = Label(
            text="",
            font_name="SpaceGrotesk",
            font_size=dp(13),
            color=MUTED,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(25)
        )

        root.add_widget(self.prime_count_description)

        self.generator_result = Label(
            text="",
            font_name="SpaceGrotesk",
            font_size=dp(16),
            color=WHITE,
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.generator_result.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1])
        )

        scroll = ScrollView()

        scroll.add_widget(self.generator_result)

        root.add_widget(scroll)

        root.add_widget(
            Label(
                text="",
                size_hint_y=1
            )
        )

        back = Button(
            text="<-  BACK",
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            background_normal="",
            background_color=(0.16, 0.18, 0.24, 1),
            size_hint_y=None,
            height=dp(48)
        )

        back.bind(
            on_release=lambda x: self.show_home()
        )

        root.add_widget(back)

        self.root_layout.add_widget(root)


    def calculate_primes(self):

        value = self.generator_input.text.strip()

        if not value:

            self.prime_count.text = ""
            self.prime_count_description.text = ""

            self.generator_result.text = (
                "Please enter a limit."
            )

            return

        limit = int(value)

        if limit < 2:

            self.prime_count.text = ""
            self.prime_count_description.text = ""

            self.generator_result.text = (
                "Please enter a number >= 2."
            )

            return

        primes = generate_primes(limit)

        self.prime_count.text = str(len(primes))

        self.prime_count_description.text = (
            f"prime numbers up to {limit}"
        )

        self.generator_result.text = (
            ", ".join(str(p) for p in primes)
        )


    # =================================
    # PRIME GAPS
    # =================================

    def show_gaps(self):

        self.clear_screen()

        root = BoxLayout(
            orientation="vertical",
            padding=[
                dp(24),
                dp(25),
                dp(24),
                dp(18)
            ],
            spacing=dp(12)
        )

        root.add_widget(
            Label(
                text="PRIME GAPS",
                font_name="SpaceGroteskBold",
                font_size=dp(23),
                color=WHITE,
                size_hint_y=None,
                height=dp(50)
            )
        )

        root.add_widget(
            Label(
                text="Explore the gaps between consecutive primes",
                font_name="SpaceGrotesk",
                font_size=dp(14),
                color=MUTED,
                size_hint_y=None,
                height=dp(30)
            )
        )

        self.gaps_input = TextInput(
            hint_text="Example: 100",
            font_name="SpaceGrotesk",
            font_size=dp(18),
            multiline=False,
            input_filter="int",
            foreground_color=WHITE,
            hint_text_color=MUTED,
            background_color=CARD,
            cursor_color=PURPLE,
            padding=[
                dp(15),
                dp(12)
            ],
            size_hint_y=None,
            height=dp(55)
        )

        root.add_widget(self.gaps_input)

        calculate = Button(
            text="ANALYSE PRIME GAPS",
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            background_normal="",
            background_color=PURPLE,
            size_hint_y=None,
            height=dp(55)
        )

        calculate.bind(
            on_release=lambda x: self.calculate_gaps()
        )

        root.add_widget(calculate)

        self.largest_gap = Label(
            text="",
            font_name="SpaceGroteskBold",
            font_size=dp(28),
            color=PURPLE,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(50)
        )

        root.add_widget(self.largest_gap)

        self.largest_gap_detail = Label(
            text="",
            font_name="SpaceGrotesk",
            font_size=dp(13),
            color=MUTED,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(45)
        )

        root.add_widget(self.largest_gap_detail)

        self.average_gap = Label(
            text="",
            font_name="SpaceGroteskMedium",
            font_size=dp(15),
            color=WHITE,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(30)
        )

        root.add_widget(self.average_gap)

        self.gaps_result = Label(
            text="",
            font_name="SpaceGrotesk",
            font_size=dp(15),
            color=WHITE,
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.gaps_result.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1])
        )

        scroll = ScrollView()

        scroll.add_widget(self.gaps_result)

        root.add_widget(scroll)

        root.add_widget(
            Label(
                text="",
                size_hint_y=1
            )
        )

        back = Button(
            text="<-  BACK",
            font_name="SpaceGroteskMedium",
            font_size=dp(14),
            color=WHITE,
            background_normal="",
            background_color=(0.16, 0.18, 0.24, 1),
            size_hint_y=None,
            height=dp(48)
        )

        back.bind(
            on_release=lambda x: self.show_home()
        )

        root.add_widget(back)

        self.root_layout.add_widget(root)


    def calculate_gaps(self):

        value = self.gaps_input.text.strip()

        if not value:

            self.largest_gap.text = ""
            self.largest_gap_detail.text = ""
            self.average_gap.text = ""

            self.gaps_result.text = (
                "Please enter a limit."
            )

            return

        limit = int(value)

        if limit < 3:

            self.largest_gap.text = ""
            self.largest_gap_detail.text = ""
            self.average_gap.text = ""

            self.gaps_result.text = (
                "Please enter a number >= 3."
            )

            return

        primes = generate_primes(limit)

        if len(primes) < 2:

            self.gaps_result.text = (
                "At least two primes are required."
            )

            return

        gaps = calculate_prime_gaps(primes)

        largest = max(
            gap[2] for gap in gaps
        )

        largest_pairs = [
            (p1, p2)
            for p1, p2, gap in gaps
            if gap == largest
        ]

        self.largest_gap.text = (
            f"Largest gap: {largest}"
        )

        pair_text = ", ".join(
            f"{p1} -> {p2}"
            for p1, p2 in largest_pairs
        )

        self.largest_gap_detail.text = pair_text

        total_gap = sum(
            gap[2] for gap in gaps
        )

        average = total_gap / len(gaps)

        self.average_gap.text = (
            f"Average gap: {average:.2f}"
        )

        result = (
            f"Prime gaps up to {limit}\n\n"
        )

        for p1, p2, gap in gaps:

            result += (
                f"{p1} -> {p2}   gap = {gap}\n"
            )

        self.gaps_result.text = result


# ---------------------------------
# RUN
# ---------------------------------

PrimeLabApp().run()
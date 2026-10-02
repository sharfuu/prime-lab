__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen


# ---------- PRIME FUNCTIONS ----------

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


def primes_up_to(n):
    primes = []

    for x in range(2, n + 1):
        if is_prime(x):
            primes.append(x)

    return primes


# ---------- HOME SCREEN ----------

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="PRIME LAB",
            font_size=32,
            size_hint_y=None,
            height=80
        )

        subtitle = Label(
            text="Explore the world of prime numbers",
            font_size=18,
            size_hint_y=None,
            height=50
        )

        goldbach = Button(
            text="Goldbach\nPrime Pairs",
            font_size=20
        )

        generator = Button(
            text="Prime Generator",
            font_size=20
        )

        gaps = Button(
            text="Prime Gaps",
            font_size=20
        )

        goldbach.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "goldbach")
        )

        generator.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "generator")
        )

        gaps.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "gaps")
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(goldbach)
        layout.add_widget(generator)
        layout.add_widget(gaps)

        self.add_widget(layout)


# ---------- GOLDBACH ----------

class GoldbachScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        back = Button(
            text="← Back",
            size_hint_y=None,
            height=50
        )

        back.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "home")
        )

        title = Label(
            text="Goldbach Prime Pairs",
            font_size=26,
            size_hint_y=None,
            height=60
        )

        self.input_box = TextInput(
            hint_text="Enter an even number",
            input_filter="int",
            multiline=False,
            font_size=22,
            size_hint_y=None,
            height=60
        )

        button = Button(
            text="FIND PRIME PAIRS",
            font_size=20,
            size_hint_y=None,
            height=60
        )

        button.bind(on_press=self.calculate)

        self.result = Label(
            text="Enter an even number",
            font_size=18,
            halign="left",
            valign="top"
        )

        scroll = ScrollView()
        scroll.add_widget(self.result)

        layout.add_widget(back)
        layout.add_widget(title)
        layout.add_widget(self.input_box)
        layout.add_widget(button)
        layout.add_widget(scroll)

        self.add_widget(layout)

    def calculate(self, instance):

        try:
            n = int(self.input_box.text)

            if n <= 2 or n % 2 != 0:
                self.result.text = (
                    "Enter an even number greater than 2."
                )
                return

            pairs = []

            for p in range(2, n // 2 + 1):

                if is_prime(p) and is_prime(n - p):

                    pairs.append(
                        f"{n} = {p} + {n-p}"
                    )

            self.result.text = (
                f"Found {len(pairs)} representation(s):\n\n"
                + "\n".join(pairs)
            )

        except ValueError:

            self.result.text = "Please enter a number."


# ---------- PRIME GENERATOR ----------

class GeneratorScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        back = Button(
            text="← Back",
            size_hint_y=None,
            height=50
        )

        back.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "home")
        )

        title = Label(
            text="Prime Generator",
            font_size=26,
            size_hint_y=None,
            height=60
        )

        self.input_box = TextInput(
            hint_text="Generate primes up to...",
            input_filter="int",
            multiline=False,
            font_size=22,
            size_hint_y=None,
            height=60
        )

        button = Button(
            text="GENERATE",
            font_size=20,
            size_hint_y=None,
            height=60
        )

        button.bind(on_press=self.generate)

        self.result = Label(
            text="Enter a limit",
            font_size=18,
            halign="left",
            valign="top"
        )

        scroll = ScrollView()
        scroll.add_widget(self.result)

        layout.add_widget(back)
        layout.add_widget(title)
        layout.add_widget(self.input_box)
        layout.add_widget(button)
        layout.add_widget(scroll)

        self.add_widget(layout)

    def generate(self, instance):

        try:
            n = int(self.input_box.text)

            if n < 2:
                self.result.text = "Enter a number ≥ 2."
                return

            primes = primes_up_to(n)

            self.result.text = (
                f"There are {len(primes)} primes ≤ {n}.\n\n"
                + ", ".join(map(str, primes))
            )

        except ValueError:

            self.result.text = "Please enter a number."


# ---------- PRIME GAPS ----------

class GapsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        back = Button(
            text="← Back",
            size_hint_y=None,
            height=50
        )

        back.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "home")
        )

        title = Label(
            text="Prime Gaps",
            font_size=26,
            size_hint_y=None,
            height=60
        )

        self.input_box = TextInput(
            hint_text="Primes up to...",
            input_filter="int",
            multiline=False,
            font_size=22,
            size_hint_y=None,
            height=60
        )

        button = Button(
            text="CALCULATE GAPS",
            font_size=20,
            size_hint_y=None,
            height=60
        )

        button.bind(on_press=self.calculate)

        self.result = Label(
            text="Enter a limit",
            font_size=18,
            halign="left",
            valign="top"
        )

        scroll = ScrollView()
        scroll.add_widget(self.result)

        layout.add_widget(back)
        layout.add_widget(title)
        layout.add_widget(self.input_box)
        layout.add_widget(button)
        layout.add_widget(scroll)

        self.add_widget(layout)

    def calculate(self, instance):

        try:
            n = int(self.input_box.text)

            primes = primes_up_to(n)

            if len(primes) < 2:
                self.result.text = "Need at least two primes."
                return

            gaps = []

            for i in range(1, len(primes)):
                gap = primes[i] - primes[i - 1]

                gaps.append(
                    f"{primes[i-1]} → {primes[i]} : gap {gap}"
                )

            largest = max(
                primes[i] - primes[i - 1]
                for i in range(1, len(primes))
            )

            self.result.text = (
                f"Largest gap ≤ {n}: {largest}\n\n"
                + "\n".join(gaps)
            )

        except ValueError:

            self.result.text = "Please enter a number."


# ---------- APP ----------

class PrimeLab(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(name="home")
        )

        manager.add_widget(
            GoldbachScreen(name="goldbach")
        )

        manager.add_widget(
            GeneratorScreen(name="generator")
        )

        manager.add_widget(
            GapsScreen(name="gaps")
        )

        return manager


PrimeLab().run()

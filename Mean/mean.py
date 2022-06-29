import manimpango
from manim import *
config.pixel_width = 720
config.pixel_height = 1280


class Mean(Scene):
    def construct(self):
        manimpango.list_fonts()

        text1 = Text("Means", font_size=72)
        text2 = Text("A mean (or average)", font_size=72, color=BLUE)
        text3 = Text("is what you use to get", font_size=60)
        text4 = Text("useful meaning out of", font_size=60)
        text5 = Text("a bunch of numbers.", font_size=60)

        intro_text = [text1, text2, text3, text4, text5]

        text2.shift(UP * 2)
        text3.next_to(text2, DOWN, buff=0.5)
        text4.next_to(text3, DOWN, buff=0.5)
        text5.next_to(text4, DOWN, buff=0.5)

        self.add(text1)
        self.wait()
        self.play(Transform(text1, text2))
        self.wait(0.5)
        self.play(Create(text3))
        self.play(Create(text4))
        self.play(Create(text5))
        self.wait(3)
        for text in intro_text:
            self.play(FadeOut(text), run_time=0.5)

        text6 = Text("A class has 5 students with test scores", font_size=60)
        text7 = Text("Can't know how well the entire class did", font_size=60)
        text8 = Text("just by looking at a single number ", font_size=60, slant=ITALIC, color=RED)

        text6.shift(UP * 3)
        text7.shift(UP * 3)
        text8.next_to(text7, DOWN, buff=0.5)

        number1 = Text("66", font_size=36)
        number2 = Text("80", font_size=36)
        number3 = Text("85", font_size=36)
        number4 = Text("92", font_size=36)
        number5 = Text("76", font_size=36)

        numbers = [number1, number2, number3, number4, number5]

        number1.shift(DOWN * 6).shift(LEFT * 3)
        number2.next_to(number1, RIGHT, buff=1)
        number3.next_to(number2, RIGHT, buff=1)
        number4.next_to(number3, RIGHT, buff=1)
        number5.next_to(number4, RIGHT, buff=1)

        self.play(Create(text6))
        self.wait()

        for number in numbers:
            self.play(Create(number), run_time=0.25)

        self.play(number1.animate.shift(UP * 6).shift(LEFT * 2.5).scale(2))
        self.play(number2.animate.next_to(number1, RIGHT, buff=2).scale(2))
        self.play(number3.animate.next_to(number2, RIGHT, buff=2).scale(2))
        self.play(number4.animate.next_to(number3, RIGHT, buff=2).scale(2))
        self.play(number5.animate.next_to(number4, RIGHT, buff=2).scale(2))

        self.wait(1.5)

        self.play(Transform(text6, text7))
        self.wait()
        self.play(Create(text8))

        box1 = SurroundingRectangle(number1, buff=0.2)
        box2 = SurroundingRectangle(number2, buff=0.2)
        box3 = SurroundingRectangle(number3, buff=0.2)
        box4 = SurroundingRectangle(number4, buff=0.2)
        box5 = SurroundingRectangle(number5, buff=0.2)

        self.play(Create(box1))
        self.wait(0.5)
        self.play(Transform(box1, box2))
        self.wait(0.5)
        self.play(Transform(box1, box3))
        self.wait(0.5)
        self.play(Transform(box1, box4))
        self.wait(0.5)
        self.play(Transform(box1, box5))

        self.wait()
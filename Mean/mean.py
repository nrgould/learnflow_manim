import manimpango
from manim import *
config.pixel_width = 720
config.pixel_height = 1280

SMALL_TEXT = 36
MEDIUM_TEXT = 44
LARGE_TEXT = 72
HUGE_TEXT = 200

FONT = "Sora"

class Mean(Scene):
    def construct(self):
        manimpango.list_fonts()

        # section 1

        text1 = Text("Means", font_size=LARGE_TEXT, font=FONT)
        text2 = Text("A mean (or average)", font_size=LARGE_TEXT, color=BLUE, font=FONT)
        text3 = Text("is what you use to get", font_size=MEDIUM_TEXT, font=FONT)
        text4 = Text("useful meaning out of", font_size=MEDIUM_TEXT, font=FONT)
        text5 = Text("a bunch of numbers.", font_size=MEDIUM_TEXT, font=FONT)

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
        self.wait()
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4), FadeOut(text5))

        # section 2

        text_2_1 = Text("A class has 5 students with test scores", font_size=MEDIUM_TEXT, font=FONT)
        text_2_2 = Text("You can't know how well the class did", font_size=MEDIUM_TEXT, font=FONT)
        text_2_3 = Text("just by looking at a single number ", font_size=MEDIUM_TEXT, slant=ITALIC, color=RED, font=FONT)

        text_2_1.shift(UP * 3)
        text_2_2.shift(UP * 3)
        text_2_3.next_to(text_2_2, DOWN, buff=0.5)

        number1 = Text("66", font_size=SMALL_TEXT, font=FONT)
        number2 = Text("80", font_size=SMALL_TEXT, font=FONT)
        number3 = Text("85", font_size=SMALL_TEXT, font=FONT)
        number4 = Text("92", font_size=SMALL_TEXT, font=FONT)
        number5 = Text("76", font_size=SMALL_TEXT, font=FONT)

        number1.shift(DOWN * 6).shift(LEFT * 3)
        number2.next_to(number1, RIGHT, buff=1)
        number3.next_to(number2, RIGHT, buff=1)
        number4.next_to(number3, RIGHT, buff=1)
        number5.next_to(number4, RIGHT, buff=1)

        self.play(Create(text_2_1))
        self.wait()

        self.play(Create(number1), Create(number2), Create(number3), Create(number4), Create(number5), run_time=0.5)
        self.wait(0.5)

        self.play(number1.animate.shift(UP * 6).shift(LEFT * 2.5).scale(2))
        self.play(number2.animate.next_to(number1, RIGHT, buff=2).scale(2))
        self.play(number3.animate.next_to(number2, RIGHT, buff=2).scale(2))
        self.play(number4.animate.next_to(number3, RIGHT, buff=2).scale(2))
        self.play(number5.animate.next_to(number4, RIGHT, buff=2).scale(2))

        self.wait(1.5)

        self.play(text_2_1.animate.shift(UP * 5))
        self.play(Create(text_2_2))
        self.wait()
        self.play(Create(text_2_3))

        BOX_TRANSITION_TIME = 0.1
        BOX_RUN_TIME = 0.5
        BOX_BUFFER = 0.2

        box1 = SurroundingRectangle(number1, buff=BOX_BUFFER)
        box2 = SurroundingRectangle(number2, buff=BOX_BUFFER)
        box3 = SurroundingRectangle(number3, buff=BOX_BUFFER)
        box4 = SurroundingRectangle(number4, buff=BOX_BUFFER)
        box5 = SurroundingRectangle(number5, buff=BOX_BUFFER)

        question_mark = Text("?", font_size=HUGE_TEXT, color=YELLOW)
        question_mark.shift(DOWN * 3)

        self.play(Create(box1))
        self.wait(BOX_TRANSITION_TIME)
        self.play(Transform(box1, box2), run_time=BOX_RUN_TIME)
        self.wait(BOX_TRANSITION_TIME)
        self.play(Transform(box1, box3), run_time=BOX_RUN_TIME)
        self.wait(BOX_TRANSITION_TIME)
        self.play(Transform(box1, box4), run_time=BOX_RUN_TIME)
        self.wait(BOX_TRANSITION_TIME)
        self.play(Transform(box1, box5), run_time=BOX_RUN_TIME)
        self.wait(BOX_TRANSITION_TIME)
        self.play(Transform(box1, question_mark), run_time=BOX_RUN_TIME)
        self.wait()
        self.play(FadeOut(number1), FadeOut(number2), FadeOut(number3), FadeOut(number4), FadeOut(number5),
                  FadeOut(question_mark), FadeOut(box1), FadeOut(text_2_1), FadeOut(text_2_2), FadeOut(text_2_3))

        # section 3

        text_3_1 = Text("So how do we get a meaningful number?", font_size=MEDIUM_TEXT, font=FONT)
        text_3_2 = Text("If you take every number in the set", font_size=MEDIUM_TEXT, font=FONT)
        text_3_3 = Text("and divide by how many numbers", font_size=MEDIUM_TEXT, font=FONT, color=YELLOW)
        text_3_4 = Text("are in the set", font_size=MEDIUM_TEXT, font=FONT, color=YELLOW, slant=ITALIC)

        text_3_3.next_to(text_3_2, DOWN, buff=1)
        text_3_4.next_to(text_3_3, DOWN, buff=1)

        self.play(Create(text_3_1))
        self.wait()
        self.play(text_3_1.animate.shift(UP * 5))
        self.play(Create(text_3_2))
        self.play(Create(text_3_3))
        self.wait()


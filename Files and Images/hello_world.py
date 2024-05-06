from manim import *

class hello(Scene):
    def construct(self):
        text = Text("I Love MP SAMARTHA!")
        self.play(Write(text))
        self.wait(3)
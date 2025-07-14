from manim import *

class ChannelBanner(Scene):
    def construct(self):
        # Outer polygon border
        polygon = RegularPolygon(n=6, radius=3.5, color=WHITE, stroke_width=3)
        polygon2 = RegularPolygon(n=6, radius=3.5, color=WHITE, stroke_width=3)
        polygon2.rotate(-PI / 12)

        # Central Mu symbol (bold)
        integral = MathTex(r"\boldsymbol{\int}").scale(3).set_color(BLUE_E).shift(LEFT * 0.8)

        # Integral sign next to Mu (bold)
        mu = MathTex(r"\boldsymbol{\mu}").scale(5).set_color(BLUE_E).next_to(integral, RIGHT, buff=0.25)

        # Group Mu and Integral
        central_symbols = VGroup(mu, integral)

        # Add channel name below
        channel_name = Tex(
            "Intuimation", color=WHITE
        ).scale(0.8).next_to(central_symbols, DOWN, buff=0.5)

        # Combine all elements
        logo = VGroup(polygon, polygon2, central_symbols, channel_name).scale(0.5).move_to(LEFT*4)

        tex = Tex(r"$\int$"," u i ",r"$\mu$"," a t i o n ",". . .").scale(2).next_to(logo,RIGHT,buff=0.6)
        tex[0].set_color(BLUE_E)
        tex[2].set_color(BLUE_E)
        VGroup(logo,tex).scale(0.7)
        self.add(logo,tex)

import os

class ChannelBanner1(Scene):
    def construct(self):
        # Create text parts
        left_tex = Tex(r"$\int$", "  u  i  ").scale(2).move_to(LEFT*2.5 + 0.5 * DOWN)
        right_text = Tex("  a  t  i  o  n", "...").scale(2).move_to(RIGHT*2.5 + DOWN * 0.5)


        # Get full absolute path to the image
        img_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "mu_bot", "media", "images", "bot", "MuBot_ManimCE_v0.19.0.png")
        )

        img = ImageMobject(img_path).scale(0.5)

        self.add(img)
        self.add(left_tex, right_text)

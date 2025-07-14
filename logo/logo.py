from manim import *

class IntuimationLogo(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # Outer polygon border
        polygon = RegularPolygon(n=6, radius=3.5, color=WHITE, stroke_width=6)
        polygon2 = RegularPolygon(n=6, radius=3.5, color=WHITE, stroke_width=6)
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
        logo = VGroup(polygon, polygon2, central_symbols, channel_name)
        self.add(logo)

class IntuimationIntro(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # Outer polygon border
        polygon = RegularPolygon(n=6, radius=3.5, color=WHITE, stroke_width=6)
        polygon2 = RegularPolygon(n=6, radius=3.5, color=WHITE, stroke_width=6)
        # polygon2.rotate(-PI / 12)

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
        logo = VGroup(polygon, polygon2, central_symbols, channel_name)
        self.play(FadeIn(polygon),
                  polygon2.animate.rotate(-PI/12),
                  FadeIn(VGroup(integral, mu)),
                  Write(channel_name))
        self.wait(2)

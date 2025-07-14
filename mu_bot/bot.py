from manim import *


class MuBot(Scene):
    def construct(self):
        # Bot's body: μ symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil (glints)
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        
        # Group the eyes together for easier manipulation
        eyes = VGroup(
            left_eye_white, right_eye_white, 
            left_eye_pupil, right_eye_pupil,
            left_eye_glint, right_eye_glint
        )
        
        # Assemble the bot from the μ symbol and the eyes.
        # Scale the entire bot up by 1.5.
        bot_body = VGroup(mu, eyes).scale(1.5)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN *0.9 + LEFT).scale(1.5)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.5)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.5)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth)
        bot_happy = VGroup(bot_body.copy(), happy_mouth.copy())
        bot_sad = VGroup(bot_body.copy(), sad_mouth.copy())

        self.add(bot_happy)

        


class MuBotExpressions(Scene):
    def construct(self):
        # Bot's body: μ symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil (glints)
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        
        # Group the eyes together for easier manipulation
        eyes = VGroup(
            left_eye_white, right_eye_white, 
            left_eye_pupil, right_eye_pupil,
            left_eye_glint, right_eye_glint
        )
        
        # Assemble the bot from the μ symbol and the eyes.
        # Scale the entire bot up by 1.5.
        bot_body = VGroup(mu, eyes).scale(1.5)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN *0.9 + LEFT).scale(1.5)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.5)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.5)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth)
        bot_happy = VGroup(bot_body.copy(), happy_mouth.copy())
        bot_sad = VGroup(bot_body.copy(), sad_mouth.copy())
        
        # Blinking effect using fade-in and fade-out
        def blink():
            return AnimationGroup(
                FadeOut(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                FadeIn(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                lag_ratio=0.2,
            )
        
        # Intro Animation: Show bot in thinking mode
        self.play(FadeIn(bot_thinking), run_time=1.5)
        self.play(blink(), run_time=0.5)
        self.wait(1)
        
        # Transform to happy expression
        self.play(Transform(bot_thinking, bot_happy), run_time=1)
        self.play(blink(), run_time=0.5)
        self.wait(1)
        
        # Transform to sad expression
        self.play(Transform(bot_thinking, bot_sad), run_time=1)
        self.play(blink(), run_time=0.5)
        self.wait(1)

class MuBotCloud(Scene):
    def construct(self):
        # Bot's body: μ symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil (glints)
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        
        # Group the eyes together for easier manipulation
        eyes = VGroup(
            left_eye_white, right_eye_white, 
            left_eye_pupil, right_eye_pupil,
            left_eye_glint, right_eye_glint
        )
        
        # Assemble the bot from the μ symbol and the eyes.
        # Scale the entire bot up by 1.5.
        bot_body = VGroup(mu, eyes).scale(1.2)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.2)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth).to_edge(DL)
        bot_happy = VGroup(bot_body.copy(), happy_mouth).to_edge(DL)
        bot_sad = VGroup(bot_body.copy(), sad_mouth).to_edge(DL)
        
        # Blinking effect using fade-in and fade-out
        def blink():
            return AnimationGroup(
                FadeOut(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                FadeIn(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                lag_ratio=0.2,
            )
        
                # Thought bubbles (dots leading to cloud)
        dot1 = Dot(radius=0.08, color=WHITE).next_to(bot_thinking, UR, buff=0.1)
        dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
        dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

        # Thinking cloud (Rounded Rectangle)
        thinking_cloud = RoundedRectangle(width=7.5, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
        thinking_cloud.next_to(dot3, UR)
        mu_thinking = VGroup(bot_thinking, dot1,dot2,dot3, thinking_cloud).next_to(bot_thinking, UR)
        mu_thinking.shift(RIGHT + DOWN)

        tex1 = Tex("Welcome to Intuimation !!").scale(0.8).move_to(thinking_cloud.get_center())
        tex2 = Tex("Math Enthuisiasts")
        tex3 = Tex("Something Inuitive").scale(0.8).move_to(thinking_cloud.get_center())
        tex0 = Tex("Let's Learn Something fun").scale(0.8).move_to(thinking_cloud.get_center())
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(mu_thinking))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait()
        self.play(Transform(tex1, tex0))
        self.wait()
        self.play(Transform(tex1,tex3))
        self.wait(2)
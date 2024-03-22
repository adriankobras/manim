from manim import *
from numpy import sin, cos
import numpy as np
import math

config.frame_width = 14.0
config.frame_size = (1080,1920)

colors = color_gradient((GOLD, RED, MAROON, PURPLE, TEAL, GREEN, YELLOW),8)

class Taylor(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-8.0, 8.0), y_range=(-16.0, 16.0)).set_opacity(0.15)
        axes = Axes(x_range=[-6, 6], y_range=[-11, 3], y_length=14).move_to([0,-4,0])
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.add(plane)

        text = Tex("Taylor Series Approximation", color=WHITE, font_size=50).move_to([0,8.5,0])
        formula = MathTex(r"sin(x) \approx").next_to(text, 3*DOWN).set_color(BLUE).shift(3*LEFT)
        approx1 = MathTex(r"x").next_to(formula, RIGHT).set_color(colors[0])
        approx2 = MathTex(r"x - \frac{x^3}{3!}").next_to(formula, RIGHT).set_color(colors[1]).shift(0.09*UP)
        approx3 = MathTex(r"x - \frac{x^3}{3!} + \frac{x^5}{5!}").next_to(formula, RIGHT).set_color(colors[2]).shift(0.09*UP)
        approx4 = MathTex(r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}").next_to(formula, RIGHT).set_color(colors[3]).shift(0.09*UP)
        approx5 = MathTex(r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!}").next_to(formula, RIGHT).set_color(colors[4]).shift(0.09*UP)
        approx6 = MathTex(r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - \cdots").next_to(formula, RIGHT).set_color(colors[5]).shift(0.09*UP)
        approx7 = MathTex(r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - \cdots").next_to(formula, RIGHT).set_color(colors[6]).shift(0.09*UP)
        approx8 = MathTex(r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - \cdots").next_to(formula, RIGHT).set_color(colors[7]).shift(0.09*UP)
        # equation = Group(formula, approx)
        level = Variable(0, Tex("n"), var_type=Integer).next_to(text, 8*DOWN)

        def f1(x):
            return sin(x)
        def t1(x):
            return x
        def t2(x):
            return x - x**3/math.factorial(3)
        def t3(x):
            return x - x**3/math.factorial(3) + x**5/math.factorial(5)
        def t4(x):
            return x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7)
        def t5(x):
            return x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9)
        def t6(x):
            return x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11)
        def t7(x):
            return x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11) + x**13/math.factorial(13)
        def t8(x):
            return x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11) + x**13/math.factorial(13) - x**15/math.factorial(15)

        g1 = axes.plot(f1, color=BLUE)
        tay1_keep = axes.plot(t1, color=colors[0])
        tay1 = axes.plot(t1, color=colors[0])
        tay2 = axes.plot(t2, color=colors[1])
        tay3 = axes.plot(t3, color=colors[2])
        tay4 = axes.plot(t4, color=colors[3])
        tay5 = axes.plot(t5, color=colors[4])
        tay6 = axes.plot(t6, color=colors[5])
        tay7 = axes.plot(t7, color=colors[6])
        tay8 = axes.plot(t8, color=colors[7])

        self.play(Write(text), Write(axes), Write(labels))

        # self.play(Write(text))
        self.play(FadeIn(formula), FadeIn(level))

        self.play(AnimationGroup(Create(g1), lag_ratio=0.5))

        self.play(Create(tay1_keep), Write(approx1), level.tracker.animate.set_value(1), level.animate.set_color(colors[0]))
        self.add(tay1)
        self.play(Transform(tay1,tay2), Transform(approx1,approx2), level.tracker.animate.set_value(3), level.animate.set_color(colors[1]))
        self.play(Transform(tay2,tay3), Transform(approx2,approx3), level.tracker.animate.set_value(5), level.animate.set_color(colors[2]))
        self.play(Transform(tay3,tay4), Transform(approx3,approx4), level.tracker.animate.set_value(7), level.animate.set_color(colors[3]))
        self.play(Transform(tay4,tay5), Transform(approx4,approx5), level.tracker.animate.set_value(9), level.animate.set_color(colors[4]))
        self.play(Transform(tay5,tay6), Transform(approx5,approx6), level.tracker.animate.set_value(11), level.animate.set_color(colors[5]))
        self.play(Transform(tay6,tay7), Transform(approx6,approx7), level.tracker.animate.set_value(13), level.animate.set_color(colors[6]))
        self.play(Transform(tay7,tay8), Transform(approx7,approx8), level.tracker.animate.set_value(15), level.animate.set_color(colors[7]))

        self.play(FadeOut(tay1_keep), FadeOut(tay1), FadeOut(tay2), FadeOut(tay3), FadeOut(tay4), FadeOut(tay5), FadeOut(tay6), FadeOut(approx1), FadeOut(approx2), FadeOut(approx3), FadeOut(approx4), FadeOut(approx5), FadeOut(approx6))
        self.play(FadeOut(axes), FadeOut(labels), FadeOut(text), FadeOut(formula), FadeOut(tay7), FadeOut(level), FadeOut(g1), FadeOut(approx7))



        #self.play(Unwrite(axes), Unwrite(labels), Unwrite(g1))
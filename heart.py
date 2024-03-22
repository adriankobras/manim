from manim import *
from math import sin, cos

config.frame_width = 30.0
config.frame_width = 14.0
config.frame_size = (1080,1920)

class Heart(Scene):
    def construct(self):
        axes = Axes(x_range=[-10, 10], y_range=[-10, 10], x_length=12, y_length=12)
        # labels = axes.get_axis_labels(x_label="x", y_label="y")

        def heart(t):
            """Parametric function of <3."""
            return (
                0.2 * (16 * (sin(t)) ** 3) + 4.5,
                0.2 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)),
            )
        
        formula = MathTex(r"x(t) &= \begin{bmatrix} 0.2 * (16 * (sin(t)) ** 3) + 4.5 \\ 0.2 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)) \end{bmatrix}").move_to([0,8.5,0]).scale(0.6)
        text = MathTex(r"t \in [-\pi,\pi]").next_to(formula, DOWN).scale(0.6)

        # the t_range parameter determines the range of the parametric function parameter
        g1 = axes.plot_parametric_curve(heart, color=RED_E, t_range=[-PI, PI], stroke_width=5)

        self.play(Write(axes))

        self.play(Write(formula))
        self.play(Write(text))

        # self.play(AnimationGroup(Write(g1), Write(g2), lag_ratio=0.5))
        self.play(Create(g1, run_time=3))

        self.play(Unwrite(axes), Unwrite(formula), Unwrite(text))
        self.play(g1.animate.shift(2.5*LEFT).scale(2))

        # self.play(g1.animate.shift(2.5*LEFT))

        self.play(g1.animate(run_time=0.3).set_fill(RED_E, opacity=0.5).scale(0.915))

        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(1.2))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(0.88))
        self.play(g1.animate(run_time=0.4).set_opacity(0.5).scale(0.95))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(1.2))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(0.88))
        self.play(g1.animate(run_time=0.4).set_opacity(0.5).scale(0.95))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(1.2))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(0.88))
        self.play(g1.animate(run_time=0.4).set_opacity(0.5).scale(0.95))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(1.2))
        self.play(g1.animate(run_time=0.12).set_opacity(1).scale(0.88))
        self.play(g1.animate(run_time=0.4).set_opacity(0.5).scale(0.95), FadeOut(g1))
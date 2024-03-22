from manim import *

config.frame_width = 14.0
config.frame_size = (1080,1920)

class Flower(Scene):
    def construct(self):
        axes = Axes(x_range=[-10, 10], y_range=[-10, 10], x_length=12, y_length=12)

        def f(t):
            a, k = 5, 10
            x = a*np.cos(k*t+PI/2)*np.cos(t)
            y = a*np.cos(k*t+PI/2)*np.sin(t)
            return np.array((x, y, 0))
        func = ParametricFunction(f, t_range=np.array([0, 2*PI, 0.1]))
        func = func.set_color(GOLD).set_stroke(width=1).set_fill(GOLD, opacity=0.5)

        formula = MathTex(r"x(t) &= \begin{bmatrix} a*cos(k*t+\pi/2)*cos(t) \\ a*cos(k*t+\pi/2)*sin(t) \end{bmatrix}").move_to([0,8.5,0]).scale(1)
        text = MathTex(r"a = 5, k = 10").next_to(formula, 3*DOWN).scale(1)

        self.play(Write(axes), AnimationGroup(Write(formula), Write(text), lag_ratio=1))

        self.play(Create(func, run_time=10, rate_func=linear))
        
        self.play(FadeOut(axes), FadeOut(formula), FadeOut(text), func.animate.scale(1.1))

        self.play(Rotate(func, angle=15*PI, rate_func=smooth, run_time=10))

        self.play(FadeOut(func))
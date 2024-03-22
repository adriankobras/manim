from manim import *

config.frame_width = 9.0
config.frame_size = (1080,1920)

def get_internal_circumferences():
    return [Circle(radius=(1 - i / 20), color=TEAL).set_stroke(width=3) for i in range(1, 21)]


class CircleArea(Scene):
    def construct(self):
        self.main_circle = Circle(radius=1, color=PURPLE)

        radius = Line(self.main_circle.get_center(),
                      (1, 0, 0)).set_color(WHITE)

        rotate_radius = Rotate(
            radius, angle=TAU, about_point=self.main_circle.get_center())

        brace = BraceLabel(radius, text='r')

        self.play(Create(radius))
        self.play(rotate_radius, Create(self.main_circle))
        # self.play(Create(brace), run_time=0.5)
        # self.wait(1)
        # self.play(FadeOut(brace))

        # Internal circumferences
        self.int_circumferences = get_internal_circumferences()

        creations = [Create(circumference)
                     for circumference in self.int_circumferences]
        self.play(rotate_radius, *creations)

        all_circumferences = [self.main_circle, *self.int_circumferences]

        # end_point = (-3, 0, 0)
        # move_to_left = [ApplyMethod(c.shift, end_point)
        #                 for c in [radius, *all_circumferences]]

        end_point = (0, 3, 0)
        move_up = [ApplyMethod(c.shift, end_point)
                        for c in [radius, *all_circumferences]]

        self.play(*move_up)

        #self.wait(1)

        cloned_radius = Line(self.main_circle.get_center(),
                             (1, 3, 0)).set_color(WHITE)

        self.play(cloned_radius.animate.shift((-3.5, -3, 0)).rotate(PI / 2))

        self.unroll_circumferences()

        cloned_radius_brace = BraceLabel(
            cloned_radius, text='r', brace_direction=LEFT)

        unrolled_main_circle_brace = BraceLabel(
            self.unrolled_main_circle, text='2{\pi}r')

        self.play(Create(cloned_radius_brace),
                  Create(unrolled_main_circle_brace), run_time=0.5)

        #self.wait(1)

        overlayed_circle = Circle(
            radius=1, color=PURPLE).set_fill(PURPLE, opacity=0.5)

        overlayed_circle.shift(3*UP)

        fade_unrolled_circumferences_out = [
            FadeOut(uc) for uc in self.unrolled_circumferences]

        filled_triangle_points = [[-3, 0.5, 0],
                                  [-3, -0.5, 0], [-3+TAU, -0.5, 0]]

        filled_triangle_color = TEAL

        filled_triangle = Polygon(
            *filled_triangle_points, color=filled_triangle_color).set_fill(filled_triangle_color, opacity=0.5)

        self.play(Create(overlayed_circle), Create(filled_triangle), Uncreate(radius), *fade_unrolled_circumferences_out,
                  FadeOut(self.unrolled_main_circle), FadeOut(cloned_radius))

        #self.wait(1)

        self.play(overlayed_circle.animate.shift(UP * 2), self.main_circle.animate.shift(UP * 2), filled_triangle.animate.shift(
            UP * 2), cloned_radius_brace.animate.shift(UP * 2), unrolled_main_circle_brace.animate.shift(UP * 2))

        area_text = Tex(r"A( ")
        area_text.shift(DOWN, 1.5*LEFT)
        area_circle = Circle(radius=0.2, color=PURPLE).set_fill(PURPLE, opacity=0.5).shift(DOWN, LEFT)
        area_circle.next_to(area_text,RIGHT)
        area_text2 = Tex(r" ) = ")
        area_text2.next_to(area_circle,RIGHT)
        self.play(Create(area_text), Create(area_text2), Create(area_circle))

        formula = MathTex(
            r"r", r"\cdot", r"2{\pi}r", r"\over", r"2")
        formula.next_to(area_text2)
        self.play(Create(formula))
        self.wait(0.5)

        formula2 = MathTex(
            r"r", r"\cdot", r"{\pi}r")
        formula2.next_to(area_text2)
        self.play(Transform(formula, formula2))
        self.wait(0.5)

        formula3 = MathTex("{\pi}r^2")
        formula3.next_to(area_text2).shift(0.1*UP)
        self.play(Transform(formula, formula3))

        self.wait(1)

    def unroll_circumferences(self):
        l = list(enumerate(self.int_circumferences))
        l = reversed(l)
        self.unrolled_circumferences = []
        for i, circumference in l:
            i = i + 1
            unrolled = Line(
                (-3, -0.5 + i / 20, 0), ((-3 + circumference.radius * TAU, -0.5 + i / 20, 0)), stroke_width=3).set_color(TEAL)
            self.play(Transform(circumference, unrolled), run_time=0.3)
            self.unrolled_circumferences.append(circumference)

        self.unrolled_main_circle = Line(
            (-3, -0.5, 0), ((-3 + self.main_circle.radius * TAU, -0.5, 0))).set_color(PURPLE)

        self.play(TransformFromCopy(self.main_circle,
                                    self.unrolled_main_circle, run_time=0.3))
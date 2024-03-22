from manim import *

config.frame_width = 14.0
config.frame_size = (1080,1920)

number_of_lines = 2
gradient_colors = [MAROON, GOLD, GREEN] #[RED,YELLOW,BLUE]
end_value = 40 # 100
total_time = 72 # 180

class MmodNTracker(Scene):

    def construct(self):
        circle = Circle().set(height=12).set_color(GRAY)
        # circle.to_edge(RIGHT,buff=1)
        mod_tracker = ValueTracker(0)
        lines = self.get_m_mod_n_objects(circle,mod_tracker.get_value())
        lines.add_updater(
            lambda mob: mob.become(
                self.get_m_mod_n_objects(circle,mod_tracker.get_value())
                )
            )

        ftext = Tex("f( ")
        #ftext.scale(2)
        ftext.move_to([-0.7,8,0])

        decimal = DecimalNumber(
                0,
                num_decimal_places=0,
                include_sign=False,
                unit=None, 
            )
        #decimal.scale(2)
        decimal.next_to(ftext,RIGHT,buff=SMALL_BUFF).shift(0.02*UP)
        decimal.add_updater(lambda d: d.set_value(mod_tracker.get_value()))

        closetext = Tex(",800)")
        #closetext.scale(2)
        closetext.next_to(decimal,RIGHT,buff=MED_SMALL_BUFF).shift(0.03*DOWN)
        # closetext.add_updater(lambda m: m.next_to(decimal,RIGHT,buff=SMALL_BUFF))

        self.play(FadeIn(circle), FadeIn(lines), FadeIn(ftext), FadeIn(decimal), FadeIn(closetext))
        self.play(
            mod_tracker.animate.set_value(end_value),
            rate_func=linear,
            run_time=total_time
            )
        
        #self.wait()
        # self.play(FadeOut(circle), FadeOut(lines), FadeOut(ftext), FadeOut(decimal), FadeOut(closetext))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def get_m_mod_n_objects(self,circle,x,y=None):
        if y==None:
            y = number_of_lines
        lines = VGroup()
        for i in range(y):
            start_point = circle.point_from_proportion((i%y)/y)
            end_point = circle.point_from_proportion(((i*x)%y)/y)
            line = Line(start_point,end_point).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*gradient_colors)
        return lines
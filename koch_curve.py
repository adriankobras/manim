from manim import *

config.frame_width = 14.0
config.frame_size = (1080,1920)

class KochCurve(Scene):
    def construct(self):
        def KochCurve(
            n, length=14, stroke_width=8, color=(BLUE, PURPLE, BLUE)
        ):

            l = length / (3 ** n)

            LineGroup = Line().set_length(l)

            def NextLevel(LineGroup):
                return VGroup(
                    *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

            for _ in range(n):
                LineGroup = NextLevel(LineGroup)

            KC = (
                VMobject(stroke_width=stroke_width)
                .set_points(LineGroup.get_all_points())
                .set_color(color)
            )
            return KC

        level = Variable(0, Tex("n"), var_type=Integer).set_color(BLUE).scale(1.3)
        txt = (
            VGroup(Tex("Koch Curve", color=WHITE, font_size=80, tex_template=TexFontTemplates.helvetica_fourier_it), level)
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to([0,8,0]).align_on_border(LEFT, buff=1)
        )
        kc = KochCurve(0, stroke_width=15).to_edge(DOWN, buff=2.5)

        self.add(txt, kc)
        self.wait()

        for i in range(1, 8):
            if i == 6 or i ==7:
                self.play(
                    level.tracker.animate(run_time=0.5).set_value(i),
                    # kc.animate.become(
                    #     KochCurve(i, stroke_width=17 - (2 * i)).to_edge(DOWN, buff=2.5)
                    # ).scale(1+i/2*1.5).shift(i*1.5*DOWN),
                    kc.animate(run_time=0.5).become(
                        KochCurve(i, stroke_width=15 - (2 * i)).to_edge(DOWN, buff=2.5)
                    ),
                )
            else:
                self.play(
                    level.tracker.animate.set_value(i),
                    # kc.animate.become(
                    #     KochCurve(i, stroke_width=17 - (2 * i)).to_edge(DOWN, buff=2.5)
                    # ).scale(1+i/2*1.5).shift(i*1.5*DOWN),
                    kc.animate.become(
                        KochCurve(i, stroke_width=15 - (2 * i)).to_edge(DOWN, buff=2.5)
                    ),
                )
            self.wait()
            # kc.shift(3*DOWN)
            # self.wait()
            # if i==7:
            #     self.play(
            #         kc.animate.become(
            #             KochCurve(i, stroke_width=17 - (2 * i)).to_edge(DOWN)
            #         ).scale(1+(i-1)/4+4).move_to(3*DOWN),
            #     )
        
        self.play(
                kc.animate(run_time=4).scale(20).shift(38*DOWN)
        )

        self.play(
                level.tracker.animate.set_value(0),
                kc.animate.become(
                    KochCurve(0, stroke_width=15).to_edge(DOWN, buff=2.5)
                ),
            )
        self.wait()

        # for i in range(4, -1, -1):
        #     self.play(
        #         level.tracker.animate.set_value(i),
        #         kc.animate.become(
        #             KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5)
        #         ),
        #     )
        #     self.wait()
            

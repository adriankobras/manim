from manim import *

config.frame_width = 10.0
config.frame_size = (1080,1920)

class Hilbert(Scene):
    def construct(self):
        points = [LEFT + DOWN, LEFT + UP, RIGHT + UP, RIGHT + DOWN]

        hilbert = Path(points).scale(3).set_color((TEAL, GOLD))

        self.play(Write(hilbert, rate_func=rush_into))

        for i in range(1, 3):
            # length of a single segment in the curve
            new_segment_length = 1 / (2 ** (i + 1) - 1)

            # scale the curve such that it it is centered
            new_scale = (1 - new_segment_length) / 2

            # save the previous (large) curve to align smaller ones by it
            lu = hilbert.copy()
            lu, hilbert = hilbert, lu

            self.play(
                lu.animate.scale(new_scale)
                .set_color(DARK_GRAY)
                .align_to(hilbert, points[1])
            )

            ru = lu.copy()
            self.play(ru.animate.align_to(hilbert, points[2]))

            ld, rd = lu.copy(), ru.copy()
            self.play(
                ld.animate.align_to(hilbert, points[0]).rotate(-PI / 2),
                rd.animate.align_to(hilbert, points[3]).rotate(PI / 2),
            )

            new_hilbert = Path(
                list(ld.flip(LEFT).get_important_points())
                + list(lu.get_important_points())
                + list(ru.get_important_points())
                + list(rd.flip(LEFT).get_important_points())
            ).set_color((TEAL, GOLD))

            self.play(Write(new_hilbert, rate_func=rush_into, run_time=2))

            self.remove(lu, ru, ld, rd)

            hilbert = new_hilbert
        
        self.play(FadeOut(hilbert))
        #self.wait()

class Path(VMobject):
    def __init__(self, points, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.set_points_as_corners(points)

    def get_important_points(self):
        return list(self.get_start_anchors()) + [self.get_end_anchors()[-1]]
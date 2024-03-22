from manim import *

config.frame_width = 14.0
config.frame_size = (1080,1920)

class FibonacciSpiral(Scene):
    def construct(self):

        squares = VGroup(Square(1 * 0.3))
        next_dir = [RIGHT, UP, LEFT, DOWN]
        FSeq = [1, 2, 3, 5, 8, 13, 21, 34, 55]

        for j, i in enumerate(FSeq):
            d = next_dir[j % 4]
            squares.add(Square(i * 0.3).next_to(squares, d, buff=0))

        squares.center()

        direction = [1, -1, -1, 1]
        corner = [[UL, -UL], [UR, -UR]]
        spiral = VGroup()

        for j, i in enumerate(squares):
            c = corner[j % 2]
            d = direction[j % 4]
            arc = ArcBetweenPoints(
                i.get_corner(c[0]),
                i.get_corner(c[1]),
                angle=PI / 2 * d,
                color="#04d9ff",
                stroke_width=6,
            )
            if direction[j % 4] != 1:
                arc = arc.reverse_direction()
            spiral.add(arc)

        self.play(
            LaggedStart(
                FadeIn(squares, lag_ratio=1), Create(spiral, lag_ratio=1), run_time=5
            )
        )
        self.wait()

        self.play(FadeOut(squares), Uncreate(spiral[::-1]), run_time=1.5)

from manim import *
from itertools import cycle
import copy

config.frame_width = 4.0
config.frame_size = (1080,1920)

class Dragon(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        colors = [RED_A, RED_B, RED_C, RED_D, RED_E, MAROON_E, MAROON_D, MAROON_C, MAROON_B, MAROON_A]
        self.color = cycle(colors)
        path = VGroup()
        col = next(self.color)
        first_line = Line(ORIGIN, UP / 5, color=col, stroke_width=2)
        dot1 = Dot(ORIGIN, color=col, radius=0.01)
        dot2 = Dot(UP / 5, color=col, radius=0.01)
        path.add(first_line, dot1, dot2)
        path.set_color(col)

        self.add(path)
        # self.play(Create(path))
        self.camera.frame.animate.move_to(path).set(width=path.width*2)

        for i in range(17): # max 17
            print(f"==> Iteration {i+1}")
            self.duplicate_path(path, i)
            self.wait(0.3)
        self.wait()

        self.play(FadeOut(path))

    def duplicate_path(self, path, i):
        new_path = path.copy()
        new_path.set_color(next(self.color))
        self.add(new_path)
        point = self.get_last_point(path)
        path_rotated = copy.deepcopy(new_path)
        if i == 0:
            about_point = [0, 0.2, 0]
        else:
            about_point = path[-1].get_points()[point]
        print(about_point)
        path_rotated.rotate(90 * DEGREES, about_point=about_point)
        full_path = VGroup(new_path, path_rotated)
        self.play(
            Rotate(
                new_path,
                angle=90 * DEGREES,
                about_point=about_point,
                rate_func=linear
            ),
            self.camera.frame.animate.move_to(full_path).set(width=full_path.width*2),
            run_time=2.5, rate_func=smooth
        )
        self.add(new_path)
        post_path = list(reversed([*new_path]))
        path.add(*post_path)

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1

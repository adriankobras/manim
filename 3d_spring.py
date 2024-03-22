from manim import *

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        d1 = Sphere(radius=1).set_color(ORANGE)
        curve0 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                -1
            ]), color=RED, t_range = np.array([-3*TAU, 5*TAU, 0.01])
        ).set_shade_in_3d(True)
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ]), color=RED, t_range = np.array([-3*TAU, 5*TAU, 0.01])
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.play(MoveAlongPath(d1, curve0), rate_func=linear)
        self.begin_ambient_camera_rotation(rate=0.3, about="phi")
        self.play(MoveAlongPath(d1, curve1), rate_func=linear)
        #self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()
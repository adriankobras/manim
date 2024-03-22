from typing import Sequence, Tuple

from manim import *

from WaitingScene import WaitingScene

config.frame_width = 20.0
config.frame_size = (1080,1920)

def find_closest_point(point: np.ndarray, mobs: Sequence[Mobject]) -> Tuple[np.ndarray, float, Mobject]:
    closestPoint = mobs[0].get_all_points()[0]
    curDist = np.linalg.norm(closestPoint - point)
    curMob = mobs[0]
    for mob in mobs:
        for p in mob.get_all_points():
            newDist = np.linalg.norm(p - point)
            if newDist < curDist:
                closestPoint = p
                curDist = newDist
                curMob = mob
    return closestPoint, curDist, curMob


color_array = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED, MAROON, PURPLE]
colors = color_gradient(color_array, 11)


class Ball(Circle):
    def __init__(self, speed: np.ndarray = ORIGIN, **kwargs):
        self.speed = np.copy(speed)
        self.was_hit = False
        super().__init__(**kwargs)


class BounceSimulation(VGroup):
    def __init__(
            self,
            balls: Sequence[Ball],
            walls: Sequence[ParametricFunction],
            scene: Scene,
            gravity_constant: float = 0.002,
            speed_multiplier: float = 0.03,
            ball_buff: float = 1.2,
            windage: float = 0.99999,
            **kwargs
    ):
        for ball in balls:
            ball.speed *= speed_multiplier
        self.balls = balls
        self.walls = walls
        self.scene = scene
        self.gravity_constant = gravity_constant
        self.speed_multiplier = speed_multiplier
        self.ball_buff = ball_buff
        self.windage = windage
        super().__init__(*balls, *walls, **kwargs)

    def wall_collision_updater(self, ball: Ball):
        if ball.was_hit:
            return
        point, distance, mob = find_closest_point(ball.get_center(), self.walls)
        if distance <= ball.radius * self.ball_buff:
            normal = ball.get_center() - point
            normal = normal / np.linalg.norm(normal)
            ball.speed -= 2 * np.dot(ball.speed, normal) * normal
            ball.was_hit = True
            gain = np.interp(np.linalg.norm(ball.speed), [0.015, 0.15], [-40, -10])
            # self.scene.add_sound("assets/ball_hit1.wav", gain=gain)

    def gravity_updater(self, ball: Ball):
        if ball.was_hit:
            return
        ball.speed += DOWN * self.gravity_constant

    def windage_updater(self, ball: Ball):
        ball.speed *= self.windage

    @staticmethod
    def hit_updater(ball: Ball):
        ball.was_hit = False

    def simulate(self):
        for b in self.balls:
            if len(self.walls) > 0:
                b.add_updater(lambda m, dt: self.wall_collision_updater(m))
            b.add_updater(lambda m, dt: self.gravity_updater(m))
            b.add_updater(lambda m, dt: self.windage_updater(m))
            b.add_updater(lambda m, dt: self.hit_updater(m))
            b.add_updater(lambda m, dt: m.shift(m.speed))


class Bouncing(Scene):

    def func(self, t):
        return [t, t ** 2, 0]

    def construct(self):
        sim = BounceSimulation(
            [Ball(ORIGIN, radius=0.5, arc_center=UP * 6 + RIGHT * (j/100000), color=colors[j], fill_opacity=1).scale(0.95) for j in range(-5, 6)],
            [ParametricFunction(self.func, t_range=[-4, 4], use_smoothing=False, stroke_width=8).scale(11).to_edge(DOWN)],
            self,
        )
        self.add(*sim.walls)
        self.play(FadeIn(VGroup(*sim.balls)))
        # self.play(Write(VGroup(*sim.balls)), Write(Tex("Parabola").to_edge(DL)))
        # self.wait()
        sim.simulate()
        self.wait(30)


class Collision(Scene):
    def construct(self):
        sim = BounceSimulation(
            [Ball(UR, radius=0.3, arc_center=DL),
             Ball(LEFT, radius=0.3, arc_center=RIGHT)],
            [],
            self,
            gravity_constant=0,
        )
        self.add(sim)
        sim.simulate()
        self.wait(2)


class BouncingThumbnail(WaitingScene):

    def func(self, t):
        return [t, t ** 2, 0]

    def construct(self):
        self.add(ParametricFunction(self.func, t_range=[-2, 2], use_smoothing=False, stroke_width=8).scale(5).to_edge(DOWN),
                 Circle(2, stroke_width=8))
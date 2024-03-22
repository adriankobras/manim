from manim import *

config = {
    'fast': {'gravity_constant': 0.00067, 'speed': 0.0027},
    'medium': {'gravity_constant': 0.000089, 'speed': 0.0009},
    'slow': {'gravity_constant': 0.000012, 'speed': 0.0003}
}


class Planet(Dot):
    def __init__(self, mass: float, speed: np.ndarray, **kwargs):
        self.mass = mass
        self.speed = speed
        super().__init__(radius=mass ** 0.1 * 0.05 + 0.01, **kwargs)

    def move(self):
        self.shift(self.speed)


class StaticPlanet(Planet):
    def __init__(self, mass: float, speed: np.ndarray, **kwargs):
        super().__init__(mass, speed, **kwargs)

    def move(self):
        pass


class Trace(VMobject):
    def __init__(
            self,
            function,
            length: int = sys.maxsize,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.function = function
        self.length = length
        self.set_points([function()])

    @staticmethod
    def trace_updater(trace):
        edgePoints = np.append(trace.get_points()[::trace.n_points_per_cubic_curve], [trace.get_points()[-1], trace.function()], axis=0)
        if edgePoints.size > trace.length:
            edgePoints = np.delete(edgePoints, 0, 0)
        trace.set_points_smoothly(edgePoints)

    def start_trace(self) -> 'Trace':
        self.add_updater(self.trace_updater)
        return self

    def stop_trace(self) -> 'Trace':
        self.remove_updater(self.trace_updater)
        return self

    def set_length(self, length: int):
        self.length = length


class GravitySimulation(VGroup):
    def __init__(
            self,
            *planets: Planet,
            gravity_constant: float = 0.0000002,
            speed: float = 0.001,
            acceleration_law=lambda m, r: m / r ** 2,
            **kwargs
    ):
        super().__init__(*planets, **kwargs)
        for item in planets:
            item.speed *= speed
        self.acceleration_law = acceleration_law
        self.planets = planets
        self.gravity_constant = gravity_constant

    @staticmethod
    def _planet_updater(this: Planet, dt: float, simulation):
        for other in simulation.planets:
            if this == other:
                continue
            p1_center = this.get_center_of_mass()
            p2_center = other.get_center_of_mass()

            r = np.linalg.norm(p1_center - p2_center)
            dv = ((p2_center - p1_center) / r)
            this.speed += dv * dt * simulation.gravity_constant * simulation.acceleration_law(other.mass, r)
            this.move()

    def simulate(self):
        for p in self.planets:
            p.add_updater(lambda m, dt: self._planet_updater(m, dt, self) if dt != 0 else m)


class Simulation(Scene):
    def construct(self):
        planets = [
            Planet(1, UP * 10).move_to(LEFT * 2).set_color(RED),
            Planet(1, UP * 2).move_to(LEFT * 4).set_color(BLUE),
            Planet(1, DOWN * 5).move_to(RIGHT * 4).set_color(GREEN),
            Planet(1, LEFT * 10).move_to(DOWN * 2).set_color(YELLOW),
            StaticPlanet(1000, ORIGIN),
        ]
        gr = GravitySimulation(*planets, **config['fast'])
        self.add(gr)
        gr.simulate()
        self.wait(10)


class SimulationRLinear(Scene):
    def construct(self):
        planets = [
            Planet(1, UP * 15).move_to(LEFT * 3).set_color(BLUE),
            StaticPlanet(1000, ORIGIN).move_to(ORIGIN).set_color(YELLOW)
        ]
        tr = Trace(planets[0].get_center, sys.maxsize).set_color_by_gradient([PURE_BLUE, BLUE_D, WHITE])
        gr = GravitySimulation(*planets, **config['fast'], acceleration_law=lambda m, r: m / r)
        self.add(tr, gr)
        tr.start_trace()
        gr.simulate()
        self.wait(5)


class SimulationRNormal(Scene):
    def construct(self):
        planets = [
            Planet(1, UP * 17).move_to(LEFT * 3).set_color(BLUE),
            StaticPlanet(1000, ORIGIN).move_to(ORIGIN).set_color(YELLOW)
        ]
        tr = TracedPath(planets[0].get_center)
        gr = GravitySimulation(*planets, **config['fast'], acceleration_law=lambda m, r: m / r ** 2)
        self.add(tr, gr)
        gr.simulate()
        self.wait(10)


class SimulationRTriple(Scene):
    def construct(self):
        planets = [
            Planet(1, UP * 3.7).move_to(LEFT * 3).set_color(BLUE),
            StaticPlanet(1000, ORIGIN).move_to(ORIGIN).set_color(YELLOW)
        ]
        tr = Trace(planets[0].get_center)
        gr = GravitySimulation(*planets, **config['fast'], acceleration_law=lambda m, r: m / r ** 3)
        self.add(tr, gr)
        self.wait(10)


class ThumbNail(Scene):
    def construct(self):
        planets = [
            Planet(1, UP * 7.185).move_to(LEFT * 4).set_color(BLUE),
            StaticPlanet(1000, ORIGIN).move_to(LEFT * 2).set_color(YELLOW),
            StaticPlanet(1000, ORIGIN).move_to(RIGHT * 2).set_color(YELLOW),
        ]
        tr = Trace(planets[0].get_center)
        gr = GravitySimulation(*planets, **config['fast'])
        self.add(tr, gr)
        self.wait(10)
import os
from manim import *
import numpy as np

class LorenzAttractor(ThreeDScene):
    def construct(self):
        self.create_axes()
        self.create_lorenz_attractor()

    def create_axes(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)

    def lorenz_system(self, pos, sigma=10, rho=28, beta=8/3):
        x, y, z = pos
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return np.array([dx_dt, dy_dt, dz_dt])

    def rate_to_color(self, rate, min_rate, max_rate):
        rate_log = np.log(rate)
        min_rate_log = np.log(min_rate)
        max_rate_log = np.log(max_rate)
        rate_normalized = (rate_log - min_rate_log) / (max_rate_log - min_rate_log)
        return interpolate_color(BLUE, RED, rate_normalized)

    def create_lorenz_attractor(self):
        # Initial position
        pos = np.array([-1.0, 1.0, 0.0])

        # Parameters for the animation
        dt = 0.01
        steps = 5000
        scale_factor = 0.14
        dt_scaling_factor = 0.1

        # Create a curve from the initial position
        curve = ParametricFunction(
            lambda t: pos,
            t_range=[0, 1, 0.1],
            color=YELLOW,
        )

        min_rate = float("inf")
        max_rate = float("-inf")

        # Calculate min_rate and max_rate
        for _ in range(steps):
            dp = self.lorenz_system(pos) * dt
            rate = np.linalg.norm(dp)
            min_rate = min(min_rate, rate)
            max_rate = max(max_rate, rate)
            pos += dp

        # Reset initial position
        pos = np.array([-1.0, 1.0, 0.0])

        # Create segments with color based on rate of change
        for _ in range(steps):
            dp = self.lorenz_system(pos) * dt
            rate = np.linalg.norm(dp)
            segment_color = self.rate_to_color(rate, min_rate, max_rate)
            segment = Line3D(pos - dp, pos, color=segment_color, stroke_width=2)
            curve.add(segment)
            pos += dp

            # Adjust time step based on rate of change
            adaptive_dt = dt * dt_scaling_factor / rate
            pos += dp * adaptive_dt

        curve.scale(scale_factor)
        curve.move_to(ORIGIN)  # Center the curve in the scene
        self.add(curve)
        self.wait()




if __name__ == "__main__":
    script_name = f"{__file__}"
    os.system(f"manim {script_name} LorenzAttractor -pql")




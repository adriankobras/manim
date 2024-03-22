from manim import *
import numpy as np
from random import seed, uniform
from scipy import integrate

# config.frame_height = 14.222222222222221
config.frame_width = 4.0
config.frame_size = (1080,1920)

num_dots = 1

def aizawa(x, y, z, a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1):
    x_dot = (z-b) * x - d*y
    y_dot = d * x + (z-b) * y
    z_dot = c + a*z - z**3 /3 - x**2 + f * z * x**3
    return x_dot, y_dot, z_dot

def update_trajectory(traj, dot):
    new_point = dot.get_center()
    if np.linalg.norm(new_point - traj.points[-1]) > 0.01:
        traj.add_smooth_curve_to(new_point)

def update_position(dot,dt):
    x_dot, y_dot, z_dot = aizawa(dot.get_center()[0]*10, dot.get_center()[1]*10, dot.get_center()[2]*10)
    x = x_dot * dt/10
    y = y_dot * dt/10
    z = z_dot * dt/10
    dot.shift(x/10*RIGHT + y/10*UP + z/10*OUT)

class Aizawa_Attractor(ThreeDScene):
    def construct(self):
        seed(1)
        x0 = -5 + 10 * np.random.random((num_dots, 3))

        # Solve for the trajectories
        dt = 0.1
        t = np.arange(0, 10, dt)
        # t = np.linspace(0, 4, 1000)
        x_t = np.asarray([integrate.odeint(aizawa, x0i, t)
                  for x0i in x0])
        
        print(x_t)
        
        # Set up figure & 3D axis for animation
        ax = ThreeDAxes()

        # choose a different color for each trajectory
        colors = np.asarray([random_color() for i in num_dots])

        dots = VGroup(
            *[
                Sphere(radius=0.02)
                .shift(UP * uniform(-1, 1) + RIGHT * uniform(-1, 1))
                .set_color(BLUE)
                for _ in range(num_dots)
            ]
        )
        
        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES,gamma = 0*DEGREES)  
        self.begin_ambient_camera_rotation(rate=0.05)            #Start move camera

        self.add(ax,dots)

        traj = VGroup()

        for i in range(len(x_t)-1):
            a = 30
            self.remove(traj)
            traj = VGroup()
            
            if i >= 30:
                for n in range(i,i-30,-1):
                    # line1 = Line3D(x_t[])
                    line2 = Line(x2[n]*RIGHT + y2[n]*UP , x2[n-1]*RIGHT + y2[n-1]*UP).set_stroke(BLUE,width=2).set_opacity(0.03*a)
                    traj.add(line1)
                    traj.add(line2)
                    a -= 1
            
            else:
                for n in range(i,0,-1):
                    line1 = Line(x1[n]*RIGHT + y1[n]*UP , x1[n-1]*RIGHT + y1[n-1]*UP).set_stroke(YELLOW,width=2).set_opacity(0.05*a)
                    line2 = Line(x2[n]*RIGHT + y2[n]*UP , x2[n-1]*RIGHT + y2[n-1]*UP).set_stroke(BLUE,width=2).set_opacity(0.05*a)
                    traj.add(line1)
                    traj.add(line2)
                    a -= 1
            
            self.add(traj)
            self.play(
                Circle1.move_to, x1[i+1]*RIGHT + y1[i+1]*UP,
                Circle2.move_to, x2[i+1]*RIGHT + y2[i+1]*UP,
                run_time=1/30,rate_func=linear)
        
        # for i in range(num_dots):
        # traj = VMobject()
        # traj.start_new_path(dots[0].get_center())
        # traj.set_stroke(BLUE, 1.5, opacity=0.6)
        # traj.add_updater(update_trajectory(dots[0]))
        # self.add(traj)

        # dots[0].add_updater(update_position)
        # self.wait(520)
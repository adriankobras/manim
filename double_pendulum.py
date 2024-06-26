from manim import *
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 2.0  # length of pendulum 1 in m
L2 = 1.5  # length of pendulum 2 in m
M1 = 3.0  # mass of pendulum 1 in kg
M2 = 4.0  # mass of pendulum 2 in kg

# config.frame_height = 14.222222222222221
config.frame_width = 8.0
config.frame_size = (1080,1920)

class DoublePendulum(Scene):
    def construct(self):
        axes = NumberPlane(x_range=(-4.0, 4.0), y_range=(-8.0, 8.0)).set_opacity(0.2)
        self.add(axes)

        def derivs(state, t):
            dydx = np.zeros_like(state)
            dydx[0] = state[1]

            delta = state[2] - state[0]
            den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
            dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                        + M2 * G * sin(state[2]) * cos(delta)
                        + M2 * L2 * state[3] * state[3] * sin(delta)
                        - (M1+M2) * G * sin(state[0]))
                       / den1)

            dydx[2] = state[3]

            den2 = (L2/L1) * den1
            dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                        + (M1+M2) * G * sin(state[0]) * cos(delta)
                        - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                        - (M1+M2) * G * sin(state[2]))
                        / den2)

            return dydx

        # create a time array with dt steps
        dt = 0.01
        t = np.arange(0, 100, dt)

        # th1 and th2 are the initial angles (degrees)
        # w10 and w20 are the initial angular velocities (degrees per second)
        th1 = 170.0
        w1 = 0.0
        th2 = 180.0
        w2 = 0.0

        # initial state
        state = np.radians([th1, w1, th2, w2])

        # integrate your ODE using scipy.integrate.
        y = integrate.odeint(derivs, state, t)

        x1 = L1*sin(y[:, 0])
        y1 = -L1*cos(y[:, 0])

        x2 = L2*sin(y[:, 2]) + x1
        y2 = -L2*cos(y[:, 2]) + y1

        #Pendulum Motion

        Center = Dot()
        Circle1 = Dot(radius=0.04*M1).move_to(x1[0]*RIGHT+y1[0]*UP).set_color(RED)
        Circle2 = Dot(radius=0.04*M2).move_to(x2[0]*RIGHT+y2[0]*UP).set_color(BLUE)

        def update_trajectory1(self, dt):
            new_point = Circle1.get_center()
            self.add_smooth_curve_to(new_point)

        def update_trajectory2(self, dt):
            new_point = Circle2.get_center()
            self.add_smooth_curve_to(new_point)

        traj1 = VMobject()
        traj1.start_new_path(Circle1.get_center())
        traj1.set_stroke(RED, 2, opacity=0.8)
        traj1.add_updater(update_trajectory1)
        self.add(traj1)

        traj2 = VMobject()
        traj2.start_new_path(Circle2.get_center())
        traj2.set_stroke(BLUE, 2, opacity=0.8)
        traj2.add_updater(update_trajectory2)
        self.add(traj2)

        Line1 = self.getline(Center,Circle1)
        Line1.add_updater(
                        lambda mob: mob.become(
                        self.getline(Center,Circle1)
                        ))

        Line2 = self.getline(Circle1,Circle2)
        Line2.add_updater(
                        lambda mob: mob.become(
                        self.getline(Circle1,Circle2)
                        ))

        self.add(Line1,Line2,Center,Circle1,Circle2)

        for i in range(len(x1)-1):
            self.remove(Circle1,Circle2)
            self.add(Circle1,Circle2)
            self.play(
                Circle1.animate.move_to(x1[i+1]*RIGHT + y1[i+1]*UP),
                Circle2.animate.move_to(x2[i+1]*RIGHT + y2[i+1]*UP),
                run_time=1/30,rate_func=linear)

    def getline(self,Point1,Point2):
            start_point = Point1.get_center()
            end_point = Point2.get_center()
            line = Line(start_point,end_point).set_stroke(width=2) 
            return line
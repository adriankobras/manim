from manim import *
import numpy as np

class Lorenz_Attractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # axes = ThreeDAxes(x_min=-3.5,x_max=3.5,y_min=-3.5,y_max=3.5,z_min=0,z_max=6,axis_config={"include_tip": True,"include_ticks":True,"stroke_width":1})
        dot = Sphere(radius=0.05,fill_color=BLUE).move_to(0*RIGHT + 0.2*UP + 0.105*OUT)
        dot.set_color(BLUE)
        dot2 = Sphere(radius=0.05,fill_color=YELLOW).move_to(0*RIGHT + 0.1*UP + 0.105*OUT)
        dot2.set_color(YELLOW)
        dot3 = Sphere(radius=0.05,fill_color=RED).move_to(0*RIGHT + 0.05*UP + 0.105*OUT)
        dot3.set_color(RED)
        dot4 = Sphere(radius=0.05,fill_color=ORANGE).move_to(0*RIGHT + 0.15*UP + 0.105*OUT)
        dot4.set_color(ORANGE)
        dot5 = Sphere(radius=0.05,fill_color=PURPLE).move_to(0*RIGHT + 0.25*UP + 0.105*OUT)
        dot5.set_color(PURPLE)
        
        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES,gamma = 0*DEGREES)  
        self.begin_ambient_camera_rotation(rate=0.05)            #Start move camera

        dtime = 0.01
        numsteps = 30

        self.add(axes,dot,dot2,dot3,dot4,dot5)

        def lorenz(x, y, z, s=10, r=28, b=2.667):
            x_dot = s*(y - x)
            y_dot = r*x - y - x*z
            z_dot = x*y - b*z
            return x_dot, y_dot, z_dot

        def update_trajectory(self, dt):
            new_point = dot.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)

        def update_trajectory2(self, dt):
            new_point = dot2.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)

        def update_trajectory3(self, dt):
            new_point = dot3.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)
        
        def update_trajectory4(self, dt):
            new_point = dot4.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)
        
        def update_trajectory5(self, dt):
            new_point = dot5.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)

        traj = VMobject()
        traj.start_new_path(dot.get_center())
        traj.set_stroke(BLUE, 1.5, opacity=0.6)
        traj.add_updater(update_trajectory)
        self.add(traj)

        traj2 = VMobject()
        traj2.start_new_path(dot2.get_center())
        traj2.set_stroke(YELLOW, 1.5, opacity=0.6)
        traj2.add_updater(update_trajectory2)
        self.add(traj2)

        traj3 = VMobject()
        traj3.start_new_path(dot3.get_center())
        traj3.set_stroke(RED, 1.5, opacity=0.6)
        traj3.add_updater(update_trajectory3)
        self.add(traj3)

        traj4 = VMobject()
        traj4.start_new_path(dot4.get_center())
        traj4.set_stroke(ORANGE, 1.5, opacity=0.6)
        traj4.add_updater(update_trajectory4)
        self.add(traj4)

        traj5 = VMobject()
        traj5.start_new_path(dot5.get_center())
        traj5.set_stroke(PURPLE, 1.5, opacity=0.6)
        traj5.add_updater(update_trajectory5)
        self.add(traj5)

        def update_position(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot.get_center()[0]*10, dot.get_center()[1]*10, dot.get_center()[2]*10)
            x = x_dot * dt/10
            y = y_dot * dt/10
            z = z_dot * dt/10
            self.shift(x/10*RIGHT + y/10*UP + z/10*OUT)

        def update_position2(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot2.get_center()[0]*10, dot2.get_center()[1]*10, dot2.get_center()[2]*10)
            x2 = x_dot * dt/10
            y2 = y_dot * dt/10
            z2 = z_dot * dt/10
            self.shift(x2/10*RIGHT + y2/10*UP + z2/10*OUT)

        def update_position3(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot3.get_center()[0]*10, dot3.get_center()[1]*10, dot3.get_center()[2]*10)
            x3 = x_dot * dt/10
            y3 = y_dot * dt/10
            z3 = z_dot * dt/10
            self.shift(x3/10*RIGHT + y3/10*UP + z3/10*OUT)

        def update_position4(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot4.get_center()[0]*10, dot4.get_center()[1]*10, dot4.get_center()[2]*10)
            x4 = x_dot * dt/10
            y4 = y_dot * dt/10
            z4 = z_dot * dt/10
            self.shift(x4/10*RIGHT + y4/10*UP + z4/10*OUT)
        
        def update_position5(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot5.get_center()[0]*10, dot5.get_center()[1]*10, dot5.get_center()[2]*10)
            x5 = x_dot * dt/10
            y5 = y_dot * dt/10
            z5 = z_dot * dt/10
            self.shift(x5/10*RIGHT + y5/10*UP + z5/10*OUT)

        dot.add_updater(update_position)
        dot2.add_updater(update_position2)
        dot3.add_updater(update_position3)
        dot4.add_updater(update_position4)
        dot5.add_updater(update_position5)
        self.wait(520)

        # 50,4
        # 40,3
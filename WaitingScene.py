from manim import *


class WaitingScene(Scene):
    def __init__(self, wait_time: float = 0.2, **kwargs):
        super().__init__(**kwargs)
        self.wait_time = wait_time

    def play(self, *args, **kwargs):
        super().play(*args, **kwargs)
        super().play(Wait(run_time=self.wait_time))

    def play3(self, *args, **kwargs):
        self.play(AnimationGroup(*args, run_time=3), **kwargs)

    def play5(self, *args, **kwargs):
        self.play(AnimationGroup(*args, run_time=5), **kwargs)

    def get_all_vmobjects(self) -> []:
        vmobjects = []
        for item in self.mobjects:
            if isinstance(item, VMobject):
                vmobjects.append(item)
        return vmobjects
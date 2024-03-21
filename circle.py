from dataclasses import dataclass, field
from utils.log import log
from bokeh.plotting import figure, show


@dataclass
class Circle:
    radius: int

    def __post_init__(self):
        if not self.radius < 1 or not self.radius > 0:
            log.exception("Radius values is expected to be between: 0 and 1!")
            self.radius = 1

    def render_shape(self):
        p = figure(
            sizing_mode="stretch_width",
            max_width=500,
            height=500,
        )

        p.circle(
            x=1,
            y=1,
            fill_alpha=0,
            radius=self.radius,
        )

        p.xaxis.visible = False
        p.yaxis.visible = False

        return p

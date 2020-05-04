import vpython as vp
# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

vp.scene.background = vp.color.white
vp.scene.width = 600
vp.scene.height = 600
vp.scene.forward = vp.vector(-.5, -.3, -1)

vp.scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

xaxis = vp.cylinder(color=vp.vector(1, 0, 0), pos=vp.vector(
    0, 0, 0), axis=vp.vector(10, 0, 0), radius=0.3)
xlbl = vp.label(pos=vp.vector(11, 0, 0), text="X",
                color=vp.color.red, opacity=0, height=30, box=0)
yaxis = vp.cylinder(color=vp.color.green, pos=vp.vector(
    0, 0, 0), axis=vp.vector(0, 10, 0), radius=0.3)
ylbl = vp.label(pos=vp.vector(0, 11, 0), text="Y",
                color=vp.color.green, opacity=0, height=30, box=0)
zaxis = vp.cylinder(color=vp.color.blue, pos=vp.vector(
    0, 0, 0), axis=vp.vector(0, 0, 10), radius=0.3)
xlbl = vp.label(pos=vp.vector(0, 0, 11), text="Z",
                color=vp.color.blue, opacity=0, height=30, box=0)

r = vp.arrow(pos=vp.vector(0, 0, 0), axis=vp.vector(
    2, 10, 7), color=vp.color.white, shaftwidth=0.5)

import vpython as vp

# https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/program/GlowScriptObjects-VPython/edit

# This program displays most GlowScript 3D objects.

# It also illustrates key features such as mouse handling, rate, and sleep.

# Bruce Sherwood, August 2011; VPython version November 2014

s = vp.sphere(color=vp.color.magenta, radius=0.5, visible=False)
drag = False


def down(ev):
    global drag
    s.pos = vp.scene.mouse.pos
    s.visible = True
    drag = True


def move(ev):
    global drag
    if not drag:
        return
    s.pos = vp.scene.mouse.pos


def up(ev):
    global drag
    s.visible = False
    drag = False


vp.scene.bind("mousedown", down)

vp.scene.bind("mousemove", move)

vp.scene.bind("mouseup", up)

vp.scene.title = "A display of most GlowScript 3D objects"
vp.scene.width = 640
vp.scene.height = 400
#vp.scene.range = 5
vp.scene.background = vp.color.gray(0.7)
vp.scene.center = vp.vector(0, 0.5, 0)
vp.scene.forward = vp.vector(-.3, 0, -1)
gslabel = vp.label(pos=vp.vector(1.1, 2, 0), text='GlowScript',
                   xoffset=40, height=16, color=vp.color.yellow)
vp.box(pos=vp.vector(-2, 0, 0), size=vp.vector(.3, 2.5, 2.5), color=vp.color.red)
vp.box(pos=vp.vector(.25, -1.4, 0),
       size=vp.vector(4.8, .3, 2.5), color=vp.color.red)
vp.cylinder(pos=vp.vector(-2, 2, 1.25), radius=0.7,
            axis=vp.vector(0, 0, -2.5), color=vp.color.blue)
ball = vp.sphere(pos=vp.vector(2, 1, 0), radius=0.5, color=vp.color.cyan)
ptr = vp.arrow(pos=vp.vector(0, 0, 2), axis=vp.vector(
    2, 0, 0), color=vp.color.yellow)
vp.cone(pos=vp.vector(-2, 0, 0), radius=1,
        length=3, color=vp.color.green, opacity=0.3)
vp.ring(pos=vp.vector(.2, 0, 0), radius=.6, axis=vp.vector(
    1, 0, 0), thickness=0.12, color=vp.color.gray(0.4))
vp.ellipsoid(pos=vp.vector(-.3, 2, 0), color=vp.color.orange,
             size=vp.vector(.3, 1.5, 1.5))
vp.pyramid(pos=vp.vector(.3, 2, 0), color=vp.vector(
    0, 0.5, .25), size=vp.vector(0.8, 1.2, 1.2))
spring = vp.helix(pos=vp.vector(2, -1.25, 0), radius=0.3, axis=vp.vector(0, 1.8, 0),
                  color=vp.color.orange, thickness=.1)
angle = 0
da = .01

trail = vp.curve(color=vp.color.magenta, radius=.02)
trail.append(vp.vector(1, 0, 0))
trail.append(vp.vector(1, 0, 2))
trail.append(vp.vector(2, 0, 2))

while angle < 3*vp.pi/4:
    vp.rate(100)
    ptr.rotate(angle=da, axis=vp.vector(0, 0, 1), origin=ptr.pos)
    trail.append(ptr.pos+ptr.axis)
    angle += da

vp.sleep(1)  # sleep for 1 second
vp.scene.autoscale = False
vp.scene.append_to_caption("""Drag the mouse and you'll drag a sphere.
On a touch screen, press and hold, then drag.""")

t = 0
dt = .01
y0 = gslabel.pos.y
ball_yo = ball.pos.y
while t < 10:
    vp.rate(1/dt)
    ball.pos.y = ball_yo+0.5*vp.sin(-4*t)
    spring.length = ball.pos.y-spring.pos.y-ball.radius+0.15
    gslabel.yoffset = 28*vp.sin(-4*t)
    t += dt

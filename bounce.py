import vpython as vp

vp.scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = vp.box(pos=vp.vector(side, 0, 0), size=vp.vector(
    thk, s2, s3),  color=vp.color.red)
wallL = vp.box(pos=vp.vector(-side, 0, 0),
               size=vp.vector(thk, s2, s3),  color=vp.color.red)
wallB = vp.box(pos=vp.vector(0, -side, 0),
               size=vp.vector(s3, thk, s3),  color=vp.color.blue)
wallT = vp.box(pos=vp.vector(0,  side, 0), size=vp.vector(
    s3, thk, s3),  color=vp.color.blue)
wallBK = vp.box(pos=vp.vector(0, 0, -side),
                size=vp.vector(s2, s2, thk), color=vp.color.gray(0.7))

ball = vp.sphere(color=vp.color.green, radius=0.4, make_trail=True, retain=200)
ball.mass = 1.0
ball.p = vp.vector(-0.15, -0.23, +0.27)

side = side - thk*0.5 - ball.radius

dt = 0.3
while True:
    vp.rate(200)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    if not (side > ball.pos.x > -side):
        ball.p.x = -ball.p.x
    if not (side > ball.pos.y > -side):
        ball.p.y = -ball.p.y
    if not (side > ball.pos.z > -side):
        ball.p.z = -ball.p.z

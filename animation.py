import vpython as vp

ball1 = vp.sphere(pos=vp.vector(0, 0, 0), radius=0.5, color=vp.color.green)
ball2 = vp.sphere(pos=vp.vector(-3, 4, 0), radius=0.5, color=vp.color.cyan)
pointer = vp.arrow(pos=vp.vector(0, 0, 0), axis=ball2.pos -
                   ball1.pos, color=vp.color.orange)

r = vp.vector(-3, 4, 0)

while r.x < 10:
    vp.rate(1000)
    # vp.sphere(pos=r, radius=0.5, color=vp.color.cyan)
    ball2.pos = r
    r.x = r.x + 1

import vpython as vp

# pip install Vpython
# https://www.glowscript.org/docs/VPythonDocs/index.html

ball = vp.sphere(pos=vp.vector(1, 0, 0), radius=0.1, color=vp.color.red)
box = vp.box(pos=vp.vector(0, 0, 0), axis=vp.vector(
    0, 1, 1), color=vp.color.green)
arrow = vp.arrow(pos=vp.vector(-3, 0, 0),
                 axis=vp.vector(1, 1, 1), color=vp.color.cyan)
vec1 = vp.vector(-2, -2, -2)
vec2 = vp.vector(1, 1, 0)
curve = vp.curve(vec1, vec2)

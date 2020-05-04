import vpython as vp
rod = vp.cylinder(pos=vp.vector(0, 2, 1), axis=vp.vector(5, 0, 0), radius=1)
# The center of one end of this cylinder is at x=0, y=2, and z=1.
# Its axis lies along the x axis, with length 5, so that the other
# end of the cylinder is at (5,2,1).

rod.pos = vp.vector(15, 11, 9)
rod.pos.x = 15

import vpython as vp


handle = vp.cylinder(size=vp.vector(1, 0.2, 0.2),
                     color=vp.vector(0.72, 0.42, 0))
head = vp.box(size=vp.vector(0.2, 0.6, 0.2),
              pos=vp.vector(1.1, 0, 0), color=vp.color.gray(0.6))
hammer = vp.compound([handle, head])
hammer.axis = vp.vector(1, 1, 0)

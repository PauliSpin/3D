import vpython as vp

# https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/program/Gyroscope-VPython/edit

# Gyroscope sitting on a pedestal

# The analysis is in terms of Lagrangian mechanics.
# The Lagrangian variables are polar angle theta,
# azimuthal angle phi, and spin angle psi.

vp.scene.width = 800
vp.scene.height = 600
vp.scene.range = 1.2
vp.scene.title = "A precessing, nutating gyroscope"

Lshaft = 1  # length of gyroscope shaft
r = Lshaft/2  # distance from support to center of mass
Rshaft = 0.03  # radius of gyroscope shaft
M = 1  # mass of gyroscope (massless shaft)
Rrotor = 0.4  # radius of gyroscope rotor
Drotor = 0.1  # thickness of gyroscope rotor
I3 = 0.5*M*Rrotor**2  # moment of inertia of gyroscope about its own axis
# moment of inertia about a line through the support, perpendicular to the axis
I1 = M*r**2 + .5*I3
hpedestal = Lshaft  # height of pedestal
wpedestal = 0.1  # width of pedestal
tbase = 0.05  # thickness of base
wbase = 3*wpedestal  # width of base
g = 9.8
Fgrav = vp.vector(0, -M*g, 0)
top = vp. vector(0, 0, 0)  # top of pedestal

shaft = vp.cylinder(length=Lshaft, radius=Rshaft, color=vp.color.orange)
rotor = vp.cylinder(pos=vp.vector(Lshaft/2-Drotor/2, 0, 0), axis=vp.vector(Drotor, 0, 0),
                    radius=Rrotor, color=vp.color.gray(0.9))
base = vp.sphere(color=shaft.color, radius=Rshaft)
end = vp.sphere(pos=vp.vector(Lshaft, 0, 0), color=shaft.color, radius=Rshaft)
gyro = vp.compound([shaft, rotor, base, end])
gyro_center = gyro.pos
gyro.texture = vp.textures.metal
tip = vp.sphere(pos=shaft.axis, radius=shaft.radius /
                2,  make_trail=True, retain=250)
tip.trail_color = vp.color.green
tip.trail_radius = 0.15*Rshaft

pedestal = vp.box(pos=top-vp.vector(0, hpedestal/2+shaft.radius/2, 0),
                  height=hpedestal-shaft.radius, length=wpedestal, width=wpedestal, texture=vp.textures.wood)
pedestal_base = vp.box(pos=top-vp.vector(0, hpedestal+tbase/2, 0),
                       height=tbase, length=wbase, width=wbase, texture=vp.textures.wood)

theta = 0
thetadot = 0
psi = 0
psidot = 0
phi = 0
phidot = 0
pureprecession = False


def reset():
    global theta, thetadot, psi, psidot, phi, phidot
    theta = 0.3*vp.pi  # initial polar angle of shaft (from vertical)
    thetadot = 0  # initial rate of change of polar angle
    psi = 0  # initial spin angle
    psidot = 30  # initial rate of change of spin angle (spin ang. velocity)
    phi = -vp.pi/2  # initial azimuthal angle
    phidot = 0  # initial rate of change of azimuthal angle
    if pureprecession:  # Set to True if you want pure precession, without nutation
        a = (1-I3/I1)*vp.sin(theta)*vp.cos(theta)
        b = -(I3/I1)*psidot*vp.sin(theta)
        c = M*g*r*vp.sin(theta)/I1
        phidot = (-b+vp.sqrt(b**2-4*a*c))/(2*a)
    gyro.axis = gyro.length * \
        vp.vector(vp.sin(theta)*vp.sin(phi),
                  vp.cos(theta), vp.sin(theta)*vp.cos(phi))
    A = vp.norm(gyro.axis)
    gyro.pos = 0.5*Lshaft*A
    tip.pos = Lshaft*A
    tip.clear_trail()


reset()
vp.scene.waitfor('textures')

dt = 0.0001
t = 0
Nsteps = 20  # number of calculational steps between graphics updates

while True:
    vp.rate(200)
    for step in range(Nsteps):  # multiple calculation steps for accuracy
        # Calculate accelerations of the Lagrangian coordinates:
        atheta = vp.sin(theta)*vp.cos(theta)*phidot**2+(M*g*r*vp.sin(theta) -
                                                        I3*(psidot+phidot*vp.cos(theta))*phidot*vp.sin(theta))/I1
        aphi = (I3/I1)*(psidot+phidot*vp.cos(theta))*thetadot / \
            vp.sin(theta)-2*vp.cos(theta)*thetadot*phidot/vp.sin(theta)
        apsi = phidot*thetadot*vp.sin(theta)-aphi*vp.cos(theta)
        # Update velocities of the Lagrangian coordinates:
        thetadot += atheta*dt
        phidot += aphi*dt
        psidot += apsi*dt
        # Update Lagrangian coordinates:
        theta += thetadot*dt
        phi += phidot*dt
        psi += psidot*dt

    gyro.axis = gyro.length * \
        vp.vector(vp.sin(theta)*vp.sin(phi),
                  vp.cos(theta), vp.sin(theta)*vp.cos(phi))
    # Display approximate rotation of rotor and shaft:
    gyro.rotate(angle=psidot*dt*Nsteps)
    A = vp.norm(gyro.axis)
    gyro.pos = 0.5*Lshaft*A
    tip.pos = Lshaft*A
    t = t+dt*Nsteps

# Class 11 Physics — Kinematics

## Position

Position specifies where an object is located in space relative to a chosen origin and reference frame. In one dimension, position is a single coordinate x measured along a chosen axis. In two or three dimensions, position is a vector **r** = x î + y ĵ + z k̂. The choice of origin and axis orientation is arbitrary; the laws of physics are independent of this choice, but the numerical value of position depends on it. For example, a ball on a table has a different x value depending on whether you measure from the table's left edge or its right edge.

Position alone is not motion — motion requires the position to change over time. The function **r**(t) describing position at every instant is called the position vector function and contains all kinematic information about a particle. SI unit: metre (m).

## Displacement

Displacement is the change in position of an object: Δ**r** = **r**_f − **r**_i, where **r**_i and **r**_f are the initial and final position vectors. It is a vector quantity with magnitude equal to the straight-line length between start and finish, and direction pointing from initial to final position. SI unit: metre (m).

Displacement depends only on the endpoints, not on the path taken. A runner who completes one lap of a 400 m track returns to the starting line — total displacement is zero, even though she has clearly moved. In one dimension, displacement can be negative if motion is in the negative direction of the chosen axis. Displacement is not the same as distance: distance is always positive and depends on the path, while displacement is a vector that depends only on endpoints.

## Distance

Distance is the total length of the path travelled by an object, regardless of direction. It is a scalar quantity, always positive, and depends on the actual route taken. SI unit: metre (m).

For motion along a straight line in a single direction, distance equals the magnitude of displacement. If the object reverses direction, distance keeps adding up while the magnitude of displacement may decrease. A ball thrown 5 m up and falling back to your hand has travelled 10 m in distance, but 0 m in displacement.

The relationship |displacement| ≤ distance always holds; equality requires straight-line motion in a single direction without reversal. Distance is what an odometer reads in a car; displacement is what a straight-line GPS measurement gives between two points. Both quantities are useful but they answer different questions about the motion.

## Velocity

Velocity is the rate of change of displacement with time. In one dimension, v = dx/dt; in three dimensions, **v** = d**r**/dt. Velocity is a vector with both magnitude and direction. SI unit: metre per second (m/s).

Average velocity over an interval is **v**_avg = Δ**r**/Δt, where Δ**r** is the total displacement and Δt is the elapsed time. Instantaneous velocity is the limit **v** = lim(Δt→0) Δ**r**/Δt, which equals the time derivative of the position vector. Geometrically, instantaneous velocity is the slope of the position-time graph at a given instant.

In one dimension, velocity can be negative when motion is in the negative axis direction. A car driving at 60 km/h east has a different velocity from one driving 60 km/h west, even though their speeds are identical. The direction component is what distinguishes velocity from speed.

## Speed

Speed is the rate of change of distance with time, a scalar quantity with magnitude only. Average speed over an interval is the total distance divided by total time: speed_avg = distance / time. Instantaneous speed is the magnitude of the instantaneous velocity vector, |**v**|. SI unit: metre per second (m/s).

Speed is always non-negative, since both distance and time are non-negative. For motion along a straight line without reversal, average speed equals the magnitude of average velocity. When the object reverses direction, however, average speed exceeds the magnitude of average velocity, because distance keeps accumulating while displacement may shrink.

A common point of confusion: instantaneous speed equals |**v**|, but average speed does not generally equal |**v**_avg|. A runner who jogs 100 m out and 100 m back in 40 s has zero average velocity but an average speed of 5 m/s. The two coincide only for unidirectional motion.

## Acceleration

Acceleration is the rate of change of velocity with time. In one dimension, a = dv/dt; in three dimensions, **a** = d**v**/dt. It is a vector quantity. SI unit: metre per second squared (m/s²).

Acceleration occurs whenever an object's velocity changes — in magnitude, in direction, or both. A car speeding up on a straight road accelerates in the direction of motion. A car slowing down accelerates opposite to motion (often called deceleration). A car moving at constant speed around a curve still accelerates, because its direction changes; this is centripetal acceleration.

Average acceleration is **a**_avg = Δ**v**/Δt. Instantaneous acceleration is the time derivative of velocity. Acceleration is also the second derivative of position: **a** = d²**r**/dt². On a velocity-time graph, instantaneous acceleration is the slope. By Newton's second law, **F**_net = m**a**, so wherever there is acceleration there must be a net force.

## Average vs instantaneous quantities

For any time-varying kinematic quantity Q (position, velocity, acceleration), the average value over an interval [t₁, t₂] is Q_avg = ΔQ/Δt = (Q(t₂) − Q(t₁))/(t₂ − t₁), while the instantaneous value at time t is Q(t) itself, obtained in the limit as Δt → 0.

The distinction matters whenever motion is non-uniform. Driving 120 km in 2 hours gives an average velocity of 60 km/h, but the speedometer at any given instant might read anywhere from 0 (red light) to 100 km/h (highway). The average is the stretched-out picture; the instantaneous value is the snapshot.

On a position-time graph, the slope of the chord between two points equals the average velocity over that interval; the slope of the tangent at a single point equals the instantaneous velocity. As the interval shrinks, the chord rotates toward the tangent — this is the geometric meaning of the derivative.

## Equations of motion (uniform acceleration)

For motion in a straight line under constant acceleration a, with initial velocity u, the three kinematic equations relating displacement s, velocity v, and time t are:

  v = u + a t  
  s = u t + (1/2) a t²  
  v² = u² + 2 a s

These are not independent laws. They are consequences of the definitions of velocity and acceleration combined with the assumption that a is constant. The first equation follows from integrating a = dv/dt; the second from integrating v = ds/dt with v from the first; the third by eliminating t between the first two.

All three apply only when acceleration is constant in both magnitude and direction. They work for free fall (a = g downward), for a car braking with uniform deceleration, and for any other uniformly accelerated motion in one dimension. For non-uniform acceleration, one must integrate the actual a(t) function.

## Projectile motion

A projectile is an object launched into space with an initial velocity and subsequently moving only under gravity (air resistance ignored). The motion separates cleanly into two independent components: horizontal motion is uniform (constant velocity v_x = u cos θ), and vertical motion is uniformly accelerated (a_y = −g, starting with v_y = u sin θ).

The resulting trajectory is a parabola. For a projectile launched from ground level at angle θ with initial speed u, landing at the same height:

  Time of flight: T = (2 u sin θ)/g  
  Maximum height: H = (u² sin² θ)/(2 g)  
  Horizontal range: R = (u² sin 2θ)/g

The range is maximum at θ = 45°, where sin 2θ = 1. Two angles θ and (90° − θ) give the same range. At the peak of the trajectory the vertical component of velocity is zero, but the horizontal component remains v_x; the speed at the peak is u cos θ, not zero.

## Relative velocity in one dimension

Velocity is always measured relative to some reference frame. The velocity of object A as measured from the frame of object B is the relative velocity v_AB. In one dimension, with a chosen positive direction:

  v_AB = v_A − v_B

where v_A and v_B are velocities in the ground frame, each carrying a sign that indicates direction.

Two cars moving east at 60 km/h and 40 km/h respectively: v_AB = 60 − 40 = 20 km/h (A pulls away from B at 20 km/h). Two cars approaching head-on at 60 km/h and −40 km/h: v_AB = 60 − (−40) = 100 km/h (closing speed). The same physical motion looks different from different frames; this is the essence of relative motion.

Relative velocity satisfies v_AB = − v_BA. It is independent of the choice of origin but depends entirely on the choice of reference frame.

## Relative velocity in two dimensions

In two or three dimensions, relative velocity is the vector difference:

  **v**_AB = **v**_A − **v**_B

where both terms are vectors. The magnitude and direction follow from the vector triangle, or equivalently by subtracting components.

Standard example — rain. Rain falling vertically with velocity **v**_R relative to the ground, while you walk forward with velocity **v**_M, has velocity **v**_RM = **v**_R − **v**_M in your frame. The relative velocity is tilted backward, which is why you tilt the umbrella forward into the rain when walking.

Boat crossing a river. If the boat's velocity in still water is **v**_BW and the river flows with velocity **v**_W relative to the bank, the boat's velocity relative to the bank is **v**_BG = **v**_BW + **v**_W. To cross straight across, the boat must aim partly upstream so its upstream component cancels the river's flow.

## Free fall

Free fall is the motion of an object under the influence of gravity alone, with all other forces (especially air resistance) ignored. Near the Earth's surface, the acceleration is constant at g ≈ 9.8 m/s² (often taken as 10 m/s² for quick estimates), directed downward.

All objects in free fall have the same acceleration regardless of their mass — Galileo's insight, verified by dropping a feather and a hammer in vacuum. A heavy stone and a light pebble released together hit the ground at the same instant in vacuum.

The equations of motion apply with a = g. For an object dropped from rest at height h:

  v = √(2 g h)  
  t = √(2 h / g)

For an object thrown straight up with initial speed u:

  Maximum height: H = u² / (2 g)  
  Time to peak: t = u / g

In real conditions, air resistance breaks the equal-acceleration result, and a feather falls noticeably slower than a hammer.

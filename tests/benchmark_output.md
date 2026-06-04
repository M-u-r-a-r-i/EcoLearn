# Analogy Generator Benchmark

_Run at 2026-06-04 16:49:00. Model: gemini-2.5-flash. Level: Class 11._

---

## 1. Relative velocity — football

**Concept:** Relative velocity  
**Interest:** football  
**Level:** Class 11

---

1. SCENARIO
You are a defender sprinting at 7 m/s along the touchline, chasing an attacker running 10 m/s in the same direction. To the spectators in the stands, the attacker moves at 10 m/s. To you, the gap opens at only 3 m/s — the attacker drifts away slowly, not at full pace. That 3 m/s is the attacker's velocity relative to you.

    attacker's ground speed  →  v_A = 10 m/s
    your ground speed        →  v_B = 7 m/s
    perceived closing speed  →  v_AB = v_A − v_B = 3 m/s
    spectators in the stands →  ground frame of reference

The analogy breaks if the attacker cuts laterally — then v_AB becomes a vector, and the 1D subtraction no longer captures the chase.

2. FORMAL RESTATEMENT
The **relative velocity** of A with respect to B along a straight line is v_AB = v_A − v_B, where velocities are signed in a chosen positive direction. The result describes A's motion as observed from B's frame.

3. SELF-CHECK QUESTION
If you accelerate to match the attacker at 10 m/s exactly, what does v_AB become, and what would the chase look like from your point of view at that instant?

[ANALOGY_QUALITY: 5]

## 2. Relative velocity — gaming

**Concept:** Relative velocity  
**Interest:** gaming  
**Level:** Class 11

---

1. SCENARIO
Imagine you're playing a fast-paced multiplayer racing game, observing the action from a drone camera that hovers high above the track. Your opponent, "Speedster," is driving their car at a blazing 150 km/h, heading towards the finish line. Meanwhile, your own car, "Phantom," is right behind them, driving at a slightly slower 120 km/h in the same direction. From the drone's perspective, both cars are moving quickly across the track. However, from your car's perspective, Speedster isn't pulling away at 150 km/h; instead, they are only gradually gaining on you at 30 km/h. This 30 km/h is how fast Speedster appears to be moving from your car's viewpoint.

    Speedster's velocity relative to track → v_S = 150 km/h
    Phantom's velocity relative to track  → v_P = 120 km/h
    Speedster's velocity relative to Phantom → v_SP = v_S - v_P = 30 km/h
    Drone camera's perspective             → ground frame of reference

The analogy breaks down if the cars are not moving in a perfectly straight line, as real racing games involve turning and drifting, which would require vector analysis.

2. FORMAL RESTATEMENT
**Relative velocity** is the velocity of an object with respect to another object, as observed from the second object's frame of reference. For motion in one dimension, if object A has a velocity v_A and object B has a velocity v_B, both measured with respect to a common reference frame (like the ground), then the relative velocity of A with respect to B is given by the equation: v_AB = v_A − v_B. Here, v_A and v_B are signed quantities, where a consistent positive direction is chosen. If v_AB is positive, it means A is moving in the positive direction relative to B; if negative, A is moving in the negative direction relative to B.

3. SELF-CHECK QUESTION
If your car, Phantom, suddenly hits a turbo boost and accelerates to 150 km/h, matching Speedster's velocity, what would Speedster's velocity be relative to your car at that moment, and what would that look like on your in-game mini-map if it showed relative positions?

[ANALOGY_QUALITY: 5]

## 3. Average vs instantaneous velocity — football

**Concept:** Average vs instantaneous velocity  
**Interest:** football  
**Level:** Class 11

---

1. SCENARIO
Imagine you're a football coach reviewing a player's performance. You might look at the player's **average velocity** by checking how far they ran from one end of the field to the other over the entire 90-minute match. This tells you their overall pace but not what they were doing at any specific moment. To understand their **instantaneous velocity**, you'd need to watch a replay, pausing the video at exactly 23 minutes and 15 seconds to see how fast they were sprinting at that precise moment, and in what direction. They might have been standing still, jogging, or in a full sprint.

    total displacement of player  →  Δx
    total time of match           →  Δt
    overall pace over match       →  v_avg = Δx / Δt
    player's position at time t   →  x(t)
    player's velocity at time t   →  v_inst = dx/dt
    entire match duration         →  time interval
    specific moment in match      →  instant of time

The analogy breaks because a football player's velocity changes discontinuously (e.g., they stop instantly), whereas in physics, velocity is generally assumed to change smoothly over infinitesimally small time intervals.

2. FORMAL RESTATEMENT
**Average velocity** is defined as the total displacement of an object divided by the total time taken for that displacement. Mathematically, it is given by:

$v_{avg} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$

Here, $\Delta x$ represents the **displacement** (the change in position, $x_f - x_i$) and $\Delta t$ represents the **time interval** (the change in time, $t_f - t_i$). Average velocity is a vector quantity, meaning it has both magnitude and direction.

**Instantaneous velocity**, on the other hand, is the velocity of an object at a particular instant in time. It is defined as the limit of the average velocity as the time interval approaches zero. Mathematically, it is given by:

$v_{inst} = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$

Here, $\frac{dx}{dt}$ represents the **derivative** of the position function $x(t)$ with respect to time $t$. Instantaneous velocity is also a vector quantity, and its magnitude is known as **instantaneous speed**.

3. SELF-CHECK QUESTION
If a player runs 100 meters down the field in 10 seconds, then immediately turns around and runs back 50 meters in 5 seconds, how would their average velocity for the entire 15-second period compare to their instantaneous velocity at the exact moment they turn around?

Hint: Remember what displacement means for average velocity.

[ANALOGY_QUALITY: 5]

## 4. Projectile motion — football

**Concept:** Projectile motion  
**Interest:** football  
**Level:** Class 11

---

1. SCENARIO
Imagine you're taking a free kick in football. When you kick the ball, it leaves your foot with a certain speed and at an angle to the ground. Once it's in the air, the only significant force acting on it is gravity, pulling it straight downwards. This means the ball continues to move horizontally at a constant speed, because nothing is pushing it forward or backward. However, its vertical speed constantly changes: it slows down as it rises, momentarily stops at the peak of its flight, and then speeds up as it falls back towards the ground, tracing a curved path. The ball continues its journey until it hits the ground or is caught.

    kicking the ball               →  initial velocity (magnitude and angle)
    ball leaving your foot         →  launch point (origin)
    gravity pulling the ball down  →  acceleration due to gravity (g)
    ball's forward movement        →  horizontal component of velocity (v_x)
    ball's up and down movement    →  vertical component of velocity (v_y)
    path of the ball through the air →  trajectory

The analogy breaks down because real footballs experience significant air resistance, which continuously slows down their horizontal motion and also affects their vertical motion, whereas in ideal projectile motion, air resistance is neglected.

2. FORMAL RESTATEMENT
**Projectile motion** is the motion of an object thrown or projected into the air, subject only to the acceleration of gravity. When an object is launched with an initial velocity $\vec{u}$ at an angle $\theta$ above the horizontal, its motion can be analyzed by separating it into two independent components: horizontal and vertical. The horizontal motion is uniform, meaning the horizontal velocity component ($u_x = u \cos\theta$) remains constant because there is no horizontal acceleration. The vertical motion is uniformly accelerated, meaning the vertical velocity component ($u_y = u \sin\theta$) changes due to the constant downward acceleration of gravity ($a_y = -g$). The path traced by the projectile is called its **trajectory**, which is typically parabolic.

3. SELF-CHECK QUESTION
If you kick a football with the same initial speed but increase the launch angle from 30 degrees to 60 degrees, how would the time the ball spends in the air change, and why?

[ANALOGY_QUALITY: 5]

## 5. Free fall — gaming

**Concept:** Free fall  
**Interest:** gaming  
**Level:** Class 11

---

**[ERROR]** `ServerError`: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

## 6. Work done by a force — football

**Concept:** Work done by a force  
**Interest:** football  
**Level:** Class 11

---

1. SCENARIO
Imagine you're a football player trying to move a heavy tackling dummy across the practice field. If you push the dummy with a certain force, and it moves a certain distance in the direction you're pushing, you've done work. The harder you push (more force) or the further you push it (more distance), the more work you do. If you push it really hard for a short distance, or gently for a long distance, you might do the same amount of work. But if you push the dummy sideways while it's only moving forward, or if it doesn't move at all, you aren't doing any work on it in the direction of its motion.

    your push on the dummy → F (magnitude of force applied)
    distance dummy moves   → d (magnitude of displacement)
    effort to move dummy   → W (work done by the force)
    direction of push      → θ (angle between force and displacement)

The analogy breaks down because in football, you can feel tired even if you push a wall that doesn't move (zero displacement), but in physics, zero displacement means zero work done.

2. FORMAL RESTATEMENT
**Work done** by a constant force is defined as the product of the magnitude of the force, the magnitude of the displacement of the object, and the cosine of the angle between the force and displacement vectors. Mathematically, it is expressed as W = F ⋅ d = Fd cos θ. Here, **W** represents the work done in joules (J), which is a scalar quantity. **F** is the magnitude of the constant force applied, measured in newtons (N). **d** is the magnitude of the displacement of the object, measured in meters (m). **θ** is the angle between the direction of the force vector and the direction of the displacement vector. If the force and displacement are in the same direction (θ = 0°), work is maximum and positive. If they are perpendicular (θ = 90°), no work is done. If they are in opposite directions (θ = 180°), work is negative.

3. SELF-CHECK QUESTION
If you push the tackling dummy with a force of 100 N, but the dummy moves 5 meters directly opposite to the direction you are pushing (perhaps someone else is pulling it), what is the work done by your force, and how does this relate to your effort?
Hint: Consider the angle between your force and the dummy's displacement.

[ANALOGY_QUALITY: 5]

## 7. Kinetic energy — gaming

**Concept:** Kinetic energy  
**Interest:** gaming  
**Level:** Class 11

---

1. SCENARIO
Imagine you're playing a racing game, and your car is speeding down a straight track. The faster your car is moving, the more difficult it is to stop or change its direction quickly, right? It feels like your car has more "oomph" or "momentum" the faster it goes. This feeling of "oomph" that your car possesses due to its motion is like its kinetic energy. If your car is twice as heavy but moving at the same speed, it would have even more "oomph" and be harder to stop, representing a greater kinetic energy. So, the speed and weight of your car determine how much "oomph" it has.

    car's "oomph" / difficulty to stop → **kinetic energy** (KE)
    car's speed                        → **velocity** (v)
    car's weight                       → **mass** (m)

The analogy breaks down because in most games, cars have a maximum speed limit, meaning their "oomph" can't increase indefinitely, whereas in physics, kinetic energy can theoretically increase without bound as velocity increases.

2. FORMAL RESTATEMENT
**Kinetic energy** (KE) is the energy an object possesses due to its motion. It is a scalar quantity and depends on both the object's mass and its speed. The defining equation for kinetic energy is:

KE = (1/2)mv²

Here, **m** represents the **mass** of the object, measured in kilograms (kg). The mass is a measure of the amount of matter in an object and its inertia. **v** represents the **speed** of the object, measured in meters per second (m/s). Speed is the magnitude of the velocity vector. The equation shows that kinetic energy is directly proportional to the mass and proportional to the square of the speed. This means that if the speed doubles, the kinetic energy quadruples. The unit for kinetic energy is the joule (J).

3. SELF-CHECK QUESTION
If you're driving a lightweight racing drone (low mass) at a very high speed, and then switch to a much heavier tank (high mass) moving at the exact same speed, which vehicle would have a greater kinetic energy, and why?
Hint: Consider how the "oomph" changes with the car's weight in the scenario.

[ANALOGY_QUALITY: 5]

## 8. Work-energy theorem — football

**Concept:** Work-energy theorem  
**Interest:** football  
**Level:** Class 11

---

1. SCENARIO
Imagine you're a football player kicking a ball. When you kick it, you apply a force over a short distance, causing the ball to speed up. The harder you kick (more force) or the longer your foot stays in contact with the ball (more displacement), the more you change its speed. If you kick it gently, it gains less speed; if you apply the same gentle force over a longer follow-through, it gains more speed. The total "effort" you put in, which is the force you apply multiplied by the distance your foot pushes the ball, directly translates to how much the ball's speed changes.

    force applied to the ball  →  F_net (net force)
    distance your foot pushes the ball  →  d (displacement)
    total "effort" (F_net × d)  →  W_net (net work done on the ball)
    change in the ball's speed/energy  →  ΔKE = (1/2)m(v_f² − v_i²)

The analogy breaks down because in football, the ball eventually stops due to friction and air resistance, which are external forces not explicitly included in the simple kick calculation.

2. FORMAL RESTATEMENT
The **work-energy theorem** states that the **net work** done on an object by all forces acting on it is equal to the change in its **kinetic energy**. Mathematically, this is expressed as W_net = ΔKE = (1/2)mv_f² − (1/2)mv_i². Here, W_net is the net work done, measured in joules (J), and is calculated as the product of the net force (F_net) acting on the object and the displacement (d) over which that force acts, provided the force is constant and in the direction of displacement. ΔKE represents the change in kinetic energy, which is the difference between the final kinetic energy (KE_f) and the initial kinetic energy (KE_i). Kinetic energy itself is defined as KE = (1/2)mv², where m is the mass of the object in kilograms (kg) and v is its speed in meters per second (m/s).

3. SELF-CHECK QUESTION
If a footballer kicks a ball with a certain force over a specific distance, and then a second player kicks the same ball with half the force but over twice the distance, how would the change in the ball's kinetic energy compare between the two kicks?
Hint: Think about how "effort" maps to work done.

[ANALOGY_QUALITY: 5]

## 9. Power — gaming

**Concept:** Power  
**Interest:** gaming  
**Level:** Class 11

---

1. SCENARIO
Imagine you're playing a real-time strategy game, and you need to build structures. Different structures require different amounts of **resources** (like wood or gold) to be gathered. You have a team of **worker units**, and each worker unit can gather resources at a certain speed. The faster your worker units gather resources, the faster you accumulate the total resources needed to build that structure. If you have many worker units, or highly upgraded ones, your resource gathering rate is high, and you can complete the resource requirement for a big structure very quickly.

    resources needed for a structure → W (work done)
    time taken to gather resources   → t (time)
    worker unit's gathering speed    → P (power)
    amount of resources gathered     → energy transferred

The analogy breaks because in a game, resources are often discrete units that appear at specific nodes, whereas in physics, energy transfer can be continuous and occur anywhere.

2. FORMAL RESTATEMENT
**Power** is defined as the rate at which work is done or energy is transferred. Mathematically, average power P_avg is given by the equation P_avg = W/t, where **W** is the total work done or energy transferred, and **t** is the time taken to perform that work or transfer that energy. The SI unit of power is the **watt** (W), which is equivalent to one joule per second (J/s). A higher power value means that a larger amount of work is done in a shorter period, or energy is transferred more quickly.

3. SELF-CHECK QUESTION
If you need to gather 1000 units of gold for a structure, and your worker units are upgraded to gather at twice their previous rate, how would the time taken to build that structure change compared to before the upgrade?
Hint: Think about how the new gathering rate relates to the original one.

[ANALOGY_QUALITY: 5]

## 10. Conservation of energy — football

**Concept:** Conservation of energy  
**Interest:** football  
**Level:** Class 11

---

1. SCENARIO
Imagine you're a football coach, and your team is preparing for a match. You have a fixed total amount of "team energy" that can be expressed in different forms. Some of this energy is "offensive energy," like how many chances your strikers can create, or how much pressure your wingers can apply. The rest is "defensive energy," which is how well your defenders can block shots and your goalkeeper can save goals. During the game, offensive energy can transform into defensive energy, and vice-versa. For example, if your team loses possession high up the pitch (reducing offensive energy), your defenders might have to work harder to stop a counter-attack (increasing defensive energy). No matter how the game plays out, the total sum of offensive and defensive energy for your team remains constant, provided no outside influence like a red card or a lucky bounce changes the overall situation.

    total team energy  →  E_total (total mechanical energy)
    offensive energy   →  KE (kinetic energy)
    defensive energy   →  PE (potential energy)
    team's performance on the field → an object's motion
    no outside influence (e.g., no red cards, no lucky bounces) →  absence of non-conservative forces (like friction or air resistance)

The analogy breaks down because in a real football game, "team energy" can actually be lost or gained through factors like player fatigue or strategic substitutions, which don't have direct equivalents in the physics concept of conserved mechanical energy.

2. FORMAL RESTATEMENT
The **principle of conservation of mechanical energy** states that for an isolated system, where only conservative forces (like gravity or spring force) do work, the total mechanical energy remains constant. Mechanical energy (E) is the sum of an object's **kinetic energy** (KE) and its **potential energy** (PE). Mathematically, this is expressed as: E = KE + PE = constant.
Here, KE = (1/2)mv², where 'm' is the mass of the object and 'v' is its speed. Potential energy can take various forms, such as gravitational potential energy (PE_g = mgh, where 'g' is acceleration due to gravity and 'h' is height) or elastic potential energy (PE_s = (1/2)kx², where 'k' is the spring constant and 'x' is the displacement from equilibrium). The principle implies that as an object moves, kinetic energy can be converted into potential energy, and vice-versa, but their sum stays the same.

3. SELF-CHECK QUESTION
If your team's "offensive energy" dramatically increases, what must happen to its "defensive energy" if the total "team energy" is to remain constant?
Hint: Think about how the different forms of energy balance each other out in the mapping.

[ANALOGY_QUALITY: 5]


# Class 11 Physics — Work, Energy, and Power

## Work done by a constant force

When a constant force **F** acts on an object that undergoes displacement **d**, the work done by the force is:

  W = **F** · **d** = F d cos θ

where θ is the angle between the force and the displacement vectors. SI unit: joule (J), where 1 J = 1 N·m.

Work is a scalar. It is positive when force has a component along the displacement (the force speeds the object up along that direction), negative when the components oppose (the force slows the object down), and zero when force and displacement are perpendicular (no energy is transferred along the direction of motion). A waiter walking horizontally with a tray does no work on the tray, because the upward normal force is perpendicular to the horizontal displacement — even though the waiter feels tired.

Work depends on both magnitudes and the angle between vectors. It is the mechanism by which energy is transferred to or from an object.

## Work-energy theorem

The work-energy theorem states that the net work done on an object by all forces equals the change in its kinetic energy:

  W_net = ΔKE = (1/2) m v_f² − (1/2) m v_i²

where m is the object's mass, v_i is its initial speed, and v_f is its final speed.

This theorem is a direct consequence of Newton's second law combined with the definition of work. Starting from F = m a and integrating along the displacement yields ∫ F dx = ∫ m a dx = (1/2) m (v_f² − v_i²). It applies to any net force — constant or variable, conservative or not — as long as W_net accounts for every force acting on the object.

The theorem links two ideas: force-times-distance (work) and motion (kinetic energy). It is often easier than solving F = m a directly, because work and energy are scalars while force and acceleration are vectors. It is most powerful when only initial and final speeds matter, not the details of the motion in between.

## Kinetic energy

Kinetic energy is the energy an object possesses by virtue of its motion. For an object of mass m moving at speed v, kinetic energy is:

  KE = (1/2) m v²

SI unit: joule (J). KE is a scalar, always non-negative, and depends only on the magnitude of the velocity, not its direction.

The factor of 1/2 and the v² dependence both follow from the work-energy theorem. Note the quadratic dependence: doubling the speed quadruples the kinetic energy. A car moving at 60 km/h has four times the KE of the same car at 30 km/h — which is why braking distance depends on speed squared, and why a head-on collision at 100 km/h is dramatically more dangerous than one at 50 km/h.

KE depends on the reference frame. A passenger in a moving train has zero KE relative to the train but large KE relative to the ground. KE is not invariant across observers; it must be computed in a clearly stated frame.

## Potential energy

Potential energy is the energy stored in a system due to its configuration — the relative positions of its parts — when those parts interact through a conservative force. The most common forms in Class 11 are:

  Gravitational PE near Earth's surface: U = m g h (with h measured from a chosen reference height)  
  Elastic PE of an ideal spring: U = (1/2) k x² (with x the displacement from the natural length and k the spring constant)

SI unit: joule (J). Potential energy is defined only up to an additive constant; only differences ΔU are physically meaningful. The choice of "zero" height for gravitational PE is arbitrary — what matters is the change between two heights.

When a system's configuration changes such that PE decreases, the lost PE typically converts into KE, and vice versa. A ball at rest at height h has PE = m g h relative to the ground; just before hitting the ground, it has KE = m g h, in the absence of friction.

## Conservation of energy

The law of conservation of mechanical energy states that if only conservative forces (such as gravity or a spring force) act on a system, the total mechanical energy E = KE + PE remains constant:

  KE_i + PE_i = KE_f + PE_f

This is a powerful tool. It lets you relate motion at any two points without integrating the equations of motion in between. For a ball rolling down a frictionless incline of height h, m g h at the top equals (1/2) m v² at the bottom, giving v = √(2 g h) — independent of the shape of the incline.

When non-conservative forces (friction, air resistance) are present, mechanical energy is not conserved; some converts to heat, sound, or deformation. The more general principle, the law of conservation of energy, states that the total energy of an isolated system — including thermal, sound, light, chemical, and other forms — is conserved. Mechanical energy is just one piece of the total. This broader law has no known exceptions in classical or quantum physics.

## Power

Power is the rate at which work is done, or equivalently the rate at which energy is transferred:

  P_avg = W / t   (average power over an interval t)  
  P = dW/dt = **F** · **v**   (instantaneous power, with **v** the velocity)

SI unit: watt (W), where 1 W = 1 J/s. Useful conversions: 1 horsepower (hp) ≈ 746 W; 1 kilowatt-hour (kWh) = 3.6 × 10⁶ J is a unit of energy, not power.

Two engines may do the same total work but at different rates. A 100 W bulb left on for 1 hour delivers 100 × 3600 = 3.6 × 10⁵ J of energy; the same energy could be delivered in 1 second by a 360 kW source. Power tells you not how much energy was transferred but how quickly.

A car moving at constant speed v against a drag force F requires the engine to deliver P = F v just to maintain motion — even though, technically, the net work on the car is zero (since KE is constant).

## Work done by a variable force

When a force varies with position, the simple W = F d cos θ no longer applies. Instead, work is computed by integration:

  W = ∫ **F** · d**r**   (general)  
  W = ∫_{x_i}^{x_f} F(x) dx   (1D, force along the direction of motion)

Geometrically, the work done by a variable force is the area under the force-vs-position graph between the start and end positions.

The classic example is a spring obeying Hooke's law, F = −k x, where k is the spring constant and x is the displacement from natural length. The work done by the spring as it stretches from 0 to x is:

  W_spring = ∫₀^x (−k x') dx' = −(1/2) k x²

The negative sign means the spring does negative work on the object stretching it; equivalently, the stretching agent does positive work, which is stored as elastic potential energy U = (1/2) k x². The integral approach generalises to any well-defined F(x), including gravity at altitudes where g varies.

## Energy loss to friction

When two surfaces slide against each other, kinetic friction does negative work on the moving object:

  W_friction = − f · d = − μ_k N · d

where f is the friction force, μ_k is the coefficient of kinetic friction, N is the normal force, and d is the distance slid. The minus sign reflects that friction always opposes relative motion.

This "lost" mechanical energy does not vanish. It is converted into heat (and sometimes sound, deformation, or wear). A block sliding to rest on a rough floor still satisfies conservation of total energy — its lost KE shows up as a slight temperature rise of the block and floor.

Because friction depends on the path (a longer slide dissipates more energy), it is a non-conservative force. Friction is the main reason real-world systems are less efficient than idealised calculations suggest. Designing for low friction — through lubrication, ball bearings, or streamlining — is a central engineering challenge in everything from car engines to bicycle drivetrains.

## Conservative vs non-conservative forces

A conservative force is one whose work on an object depends only on the initial and final positions, not on the path taken. Equivalently, the work done by a conservative force over any closed loop is zero. Gravity and an ideal spring are the standard Class 11 examples; the electric force between static charges is another.

For a conservative force, one can define a potential energy U such that F = − dU/dx (in 1D). This is what allows the energy-conservation shortcut KE_i + PE_i = KE_f + PE_f.

A non-conservative force does work that depends on the path: friction, air drag, viscous forces, and applied pushes or pulls all qualify. Sliding a block in a closed loop on a rough surface and returning it to its starting point does zero net work for gravity but non-zero net work against friction. No potential energy function exists for a non-conservative force.

In real problems, both kinds of force are usually present. The general work-energy theorem still holds — net work equals ΔKE — but only the conservative part can be folded into a potential energy.

## Real-world examples

The work-energy framework explains phenomena across daily life. A roller-coaster gains KE as it descends, losing PE; in the absence of friction, the speed at any height is determined entirely by the height drop from the start, regardless of the track's shape. Real coasters lose energy to friction and air drag, which is why the second hill is always lower than the first.

A simple pendulum converts PE at the extremes of its swing into KE at the lowest point and back, oscillating until pivot friction and air drag damp it to rest.

In a hydroelectric dam, water at height h has gravitational PE = m g h; flowing down a pipe converts this to KE; spinning a turbine converts KE to rotational KE; the generator converts that into electrical energy. Each step is less than 100 % efficient, so the electrical output is always less than the original gravitational PE — but the total energy, including heat dissipated along the way, is conserved.

Regenerative braking in an electric car captures the car's KE as it slows and stores it back in the battery instead of wasting it as heat, illustrating how the work-energy concept maps directly onto practical engineering.

# Analogy Generator Benchmark — v3 (with RAG context)

_Run at 2026-06-07 10:48:55. Each case is fed the top 3 curriculum passages plus the top 3 interest passages as context, then asked to generate the explanation. Critic loop is intentionally disabled here so the diff against v2 isolates the RAG effect._

---

## 1. Relative velocity — football

**Concept:** Relative velocity  
**Interest:** football  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_kinematics.md :: Relative velocity in one dimension` (distance 0.596)
2. `physics_kinematics.md :: Relative velocity in two dimensions` (distance 1.022)
3. `physics_kinematics.md :: Velocity` (distance 1.090)

**Retrieved interest context (top 3):**

1. `football.md :: 9. Free kick — knuckleball` (distance 0.878)
2. `football.md :: 16. Roberto Carlos's free kick (1997)` (distance 0.949)
3. `football.md :: 1. Player sprint speeds` (distance 1.008)

---

**Generated explanation:**

*   Concept: Relative velocity (1D and 2D/3D).
    *   Student Interest: Football.
    *   Level: Class 11 (CBSE/ISC).
    *   Constraints: No filler, specific output format (Scenario, Formal Restatement, Self-Check Question), 450-650 words, no emojis, no decorative formatting, bold key terms once.
    *   Curriculum Context: $v_{AB} = v_A - v_B$ (1D), $\mathbf{v}_{AB} = \mathbf{v}_A - \mathbf{v}_B$ (Vector), rain/boat examples.
    *   Interest Context: Mbappé sprint speeds (~10 m/s), Roberto Carlos curve, knuckleballs.

    *   Need to map:
        *   Object A (Velocity $v_A$) $\rightarrow$ Attacker (e.g., Mbappé).
        *   Object B (Velocity $v_B$) $\rightarrow$ Defender.
        *   Relative Velocity $v_{AB}$ $\rightarrow$ Closing speed/gap change.
        *   Ground Frame $\rightarrow$ The pitch/spectators.
        *   Direction (Positive/Negative) $\rightarrow$ Direction of the run.
        *   Vector addition/subtraction (2D) $\rightarrow$ Cut-off angles or crossing the pitch.

    *   *Scenario Draft:*
        Imagine Kylian Mbappé sprinting toward the goal at 10 m/s while a defender chases him in the same direction at 8 m/s. To a spectator in the stands, Mbappé is moving at 10 m/s, but to the defender, Mbappé seems to be pulling away at only 2 m/s. Now imagine the defender is sprinting toward Mbappé head-on at 8 m/s to stop a pass; the closing speed feels much faster, as they approach each other at 18 m/s. If Mbappé suddenly cuts diagonally across the pitch while the defender continues straight, the defender must adjust their aim—not just their speed—to intercept him. This diagonal adjustment is like calculating the vector difference to find the relative path.

    *   *Mapping Table:*
        velocity of object A ($v_A$) $\rightarrow$ Mbappé's sprint speed
        velocity of object B ($v_B$) $\rightarrow$ defender's sprint speed
        relative velocity ($v_{AB}$) $\rightarrow$ perceived closing or separating speed
        ground frame $\rightarrow$ the football pitch/spectators
        vector subtraction $\rightarrow$ adjusting the cutoff angle for a diagonal run

    *   *Breakdown Point:* The analogy breaks down because humans can change their velocity (accelerate/decelerate) instantly via friction and muscle power, whereas the basic relative velocity formula assumes instantaneous velocities at a specific moment.

    *   *Formal Restatement:*
        **Relative velocity** is the velocity of an object as measured from a specific **reference frame**. For two objects A and B moving in one dimension, the velocity of A relative to B is given by the equation $v_{AB} = v_A - v_B$, where $v_A$ and $v_B$ are velocities relative to a common ground frame and are signed based on direction. In two or three dimensions, this is expressed as a **vector difference**: $\mathbf{v}_{AB} = \mathbf{v}_A - \mathbf{v}_B$. This means the relative velocity is the result of subtracting the velocity vector of the observer from the velocity vector of the observed object. The **magnitude** and direction of $\mathbf{v}_{AB}$ can be determined using the triangle law of vector addition. A key property is that $v_{AB} = -v_{BA}$, meaning the relative velocity of B with respect to A is equal in magnitude but opposite in direction to that of A with respect to B. The SI unit for velocity is the metre per second (m/s).

    *   *Self-Check Question:*
        If Mbappé is sprinting north at 10 m/s and a defender is sprinting south at 8 m/s, what is the relative velocity of Mbappé with respect to the defender? How does this compare to the relative velocity if both were sprinting north?
        *Hint:* Consider the signs of the velocities in the 1D equation $v_{AB} = v_A - v_B$.

    *   Check word count: Scenario (~100) + Table (~50) + Restatement (~150) + Question (~50) = ~350. I need to expand to hit the 450-650 range.
    *   Expansion: Elaborate more on the 2D aspect in the scenario. Describe the "cutoff angle" more clearly. Expand the formal restatement to explain the symbols more thoroughly.

    *   *Revised Scenario:*
        Imagine Kylian Mbappé sprinting toward the goal at 10 m/s while a defender chases him from behind in the same direction at 8 m/s. To a spectator standing on the touchline, Mbappé is moving at his full speed, but to the defender, Mbappé appears to be pulling away at only 2 m/s. Now, imagine the defender is instead sprinting head-on toward Mbappé at 8 m/s to intercept a pass; the closing speed feels much more intense, as they approach each other at 18 m/s. If Mbappé suddenly cuts diagonally across the pitch while the defender continues in a straight line, the defender cannot simply run toward where Mbappé is currently located. To intercept him, the defender must calculate a "cutoff angle," which is essentially finding the vector difference between their two velocity paths. This ensures the relative velocity vector points directly toward the attacker.

    *   *Revised Restatement:*
        **Relative velocity** is the velocity of an object as measured from a specific **reference frame**. In one dimension, with a chosen positive direction, the velocity of object A relative to object B is defined by the equation $v_{AB} = v_A - v_B$. Here, $v_A$ is the velocity of object A and $v_B$ is the velocity of object B, both measured relative to a stationary ground frame. If the objects move in opposite directions, one velocity must be negative, which mathematically results in their speeds being added. In two or three dimensions, relative velocity is treated as a **vector difference**: $\mathbf{v}_{AB} = \mathbf{v}_A - \mathbf{v}_B$. This vector subtraction accounts for both the speed and the direction of motion, allowing for the calculation of paths in a plane. The **magnitude** of this vector represents the relative speed, while its direction indicates the line of sight from the observer to the observed object. The SI unit for all these measurements is the metre per second (m/s).

    *   *Revised Question:*
        If Mbappé is sprinting north at 10 m/s and a defender is sprinting south at 8 m/s, what is the relative velocity of Mbappé with respect to the defender? If the defender suddenly turns and sprints north at 8 m/s instead, how does the relative velocity change, and what does this mean for the gap between them?
        *Hint:* Use the mapping of "north" and "south" as positive and negative signs in the equation $v_{AB} = v_A - v_B$.

    *   Check constraints:
        *   Scenario 5-7 sentences? (6 sentences). Yes.
        *   Mapping table? Yes.
        *   Breakdown sentence? Yes.
        *   Formal restatement 5-7 sentences? (6 sentences). Yes.
        *   Equation included? Yes.
        *   Symbols explained? Yes.
        *   Bold key terms once? Yes.
        *   No filler? Yes.
        *   No emojis? Yes.
        *   No decorative formatting? Yes.
        *   SI units? Yes.
        *   Word count check:
            Scenario: ~130
            Table: ~50
            Restatement: ~160
            Question: ~70
            Total: ~410. Still a bit low. Need to expand the formal restatement and scenario slightly more to ensure >450.

    *   *Further Expansion:*
        Scenario: Add a sentence about the "ground frame" explicitly.
        Restatement: Elaborate on the vector triangle or the property $v_{AB} = -v_{BA}$.

    *   *Final Polish:*
        Scenario:
        Imagine Kylian Mbappé sprinting toward the goal at 10 m/s while a defender chases him from behind in the same direction at 8 m/s. To a spectator standing on the touchline, Mbappé is moving at his full speed, but to the defender, Mbappé appears to be pulling away at only 2 m/s. Now, imagine the defender is instead sprinting head-on toward Mbappé at 8 m/s to intercept a pass; the closing speed feels much more intense, as they approach each other at 18 m/s. The touchline and the grass of the pitch serve as the fixed background against which both players' speeds are initially measured. If Mbappé suddenly cuts diagonally across the pitch while the defender continues in a straight line, the defender cannot simply run toward where

## 2. Relative velocity — gaming

**Concept:** Relative velocity  
**Interest:** gaming  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_kinematics.md :: Relative velocity in one dimension` (distance 0.596)
2. `physics_kinematics.md :: Relative velocity in two dimensions` (distance 1.022)
3. `physics_kinematics.md :: Velocity` (distance 1.090)

**Retrieved interest context (top 3):**

1. `gaming.md :: 14. 60 fps vs 30 fps in action games` (distance 0.940)
2. `gaming.md :: 13. Frame rate and perceived motion` (distance 0.952)
3. `gaming.md :: 19. Realistic vs arcade physics` (distance 1.101)

---

**Generated explanation:**

*   Concept: Relative Velocity.
    *   Student Interest: Gaming.
    *   Level: Class 11 (CBSE/ISC).
    *   Curriculum Context: Relative velocity in 1D ($v_{AB} = v_A - v_B$) and 2D/3D (vector difference $\mathbf{v}_{AB} = \mathbf{v}_A - \mathbf{v}_B$). Examples: cars, rain, boat/river.
    *   Interest Context: Frame rates (30, 60, 120+ fps), simulators vs. arcade games, iRacing/DCS/MSFS.

    *   Need a gaming scenario that maps to relative velocity.
    *   Scenario: A racing simulator (like iRacing) where two cars are moving.
    *   Case 1 (1D): Two cars racing in the same direction. Car A is faster. From the spectator's (ground) view, both are fast. From Car B's cockpit view, Car A is pulling away slowly.
    *   Case 2 (1D): Head-on collision or passing. High closing speed.
    *   Case 3 (2D/3D): A car driving through a rain effect in a simulator. If the car moves forward, the rain (falling vertically relative to the ground) appears to hit the windshield at an angle.

    *   *Drafting Scenario:*
        Imagine you are playing a high-fidelity simulator like iRacing. You are driving your car at 200 km/h, and a rival is speeding up behind you at 220 km/h. While the track-side cameras see both of you screaming past at immense speeds, your cockpit view shows the rival slowly creeping closer at only 20 km/h. If you were to turn around and drive toward them head-on, the gap would close violently at 420 km/h. Now, imagine it starts raining in the sim; as you accelerate, the raindrops, which fall straight down relative to the track, seem to slant backward across your windshield.

    *   *Mapping:*
        Velocity of car A (rival) relative to ground $\rightarrow v_A$
        Velocity of car B (you) relative to ground $\rightarrow v_B$
        Relative velocity of rival as seen from your cockpit $\rightarrow v_{AB}$
        Track-side camera $\rightarrow$ ground reference frame
        Rain falling vertically $\rightarrow$ $\mathbf{v}_R$ (velocity of rain relative to ground)
        Rain appearing slanted $\rightarrow$ $\mathbf{v}_{RM}$ (velocity of rain relative to you)

    *   *Breakdown:* The analogy breaks if the game uses "arcade" physics (like Mario Kart) where relative speeds are clamped or artificial "rubber-banding" forces the cars to stay close regardless of their actual velocities.

    *   Define **relative velocity**.
    *   1D Equation: $v_{AB} = v_A - v_B$.
    *   Explain symbols: $v_{AB}$ is velocity of A relative to B, $v_A$ and $v_B$ are velocities in the ground frame.
    *   Mention signs for direction.
    *   2D/3D Equation: $\mathbf{v}_{AB} = \mathbf{v}_A - \mathbf{v}_B$.
    *   Explain vector subtraction.
    *   Mention the rain/boat examples as per the curriculum context.

    *   Needs to require reasoning through the mapping.
    *   Question: If you are in a simulator and you match the exact speed and direction of the car next to you, what happens to $v_{AB}$ and how does the other car appear to move from your cockpit view?
    *   Hint: Look at the subtraction in the mapping.

    *   No emojis? Checked.
    *   No decorative formatting? Checked.
    *   Bold key terms once? Checked.
    *   SI units? Checked.
    *   Target length 450-650?
        *   Scenario: ~120 words.
        *   Restatement: ~150 words.
        *   Question: ~50 words.
        *   Total might be a bit low. Need to expand the Scenario and Formal Restatement to hit the 450-650 range.

    *   *Expanding Scenario:* Elaborate on the feeling of the cockpit view vs the spectator view. Describe the rain effect more vividly.
    *   *Expanding Formal Restatement:* Add more detail on the vector triangle and the specific condition of the boat crossing the river (aiming upstream).

    *   *Revised Scenario:*
        Imagine you are playing a high-fidelity simulator like iRacing. You are driving your car at 200 km/h, and a rival is speeding up behind you at 220 km/h. While the track-side cameras see both of you screaming past the asphalt at immense speeds, your cockpit view shows the rival slowly creeping closer at only 20 km/h. If you were to suddenly pivot and drive toward them head-on at your current speed, the gap would close violently at 420 km/h. Now, consider a weather event in the sim where rain falls vertically relative to the track. As you accelerate forward, the raindrops no longer seem to fall straight down; instead, they appear to slant backward across your windshield. This perceived slant is the result of your own motion subtracting from the rain's downward motion.

        rival's speed relative to track $\rightarrow$ $v_A$
        your speed relative to track $\rightarrow$ $v_B$
        rival's speed in your cockpit view $\rightarrow$ $v_{AB}$
        track-side camera $\rightarrow$ ground reference frame
        vertical rain velocity $\rightarrow$ $\mathbf{v}_R$
        slanted rain in your view $\rightarrow$ $\mathbf{v}_{RM}$

        The analogy breaks if the game uses arcade physics, such as rubber-banding, where the game artificially adjusts speeds to keep racers close regardless of the mathematical difference in their velocities.

    *   *Revised Formal Restatement:*
        **Relative velocity** is the velocity of an object as measured from a specific reference frame, meaning the motion of one object is described from the perspective of another moving object. In one dimension, the velocity of object A relative to object B is given by the equation $v_{AB} = v_A - v_B$, where $v_A$ and $v_B$ are the velocities of the two objects relative to a stationary ground frame. The signs of $v_A$ and $v_B$ are determined by a chosen positive direction; for instance, if two objects move toward each other, one must have a negative sign, leading to a higher closing speed. In two or three dimensions, relative velocity is treated as a **vector difference**, expressed as $\mathbf{v}_{AB} = \mathbf{v}_A - \mathbf{v}_B$. This vector subtraction can be visualized using a vector triangle or by subtracting individual components. A classic application is a boat crossing a river; to move straight across, the boat's velocity relative to the water ($\mathbf{v}_{BW}$) must have an upstream component that exactly cancels the river's velocity relative to the bank ($\mathbf{v}_W$), ensuring the resulting velocity relative to the ground ($\mathbf{v}_{BG}$) is perpendicular to the bank.

    *   *Self-Check Question:*
        In your simulator, if you are chasing a rival and you increase your speed until it exactly matches theirs in both magnitude and direction, what is the resulting $v_{AB}$, and how would the rival's car appear to behave from your cockpit perspective?
        Hint: Consider what happens to the result of the subtraction in the mapping when $v_A$ and $v_B$ are identical.

    *   Length check:
        Scenario: ~160 words.
        Restatement: ~210 words.
        Question: ~60 words.
        Total: ~430 words. Still slightly under 450. I will add a bit more detail to the formal restatement regarding the rain example and the definition of velocity.

    *   *Further expansion of Formal Restatement:*
        Add: Velocity is defined as the rate of change of displacement with time, denoted as $\mathbf{v} = d\mathbf{r}/dt$ in three dimensions, with the SI unit being the metre per second (m/s). This distinguishes it from speed, as velocity includes direction. In the case of rain falling vertically ($\mathbf{v}_R$) while a person walks forward ($\mathbf{v}_M$), the relative velocity $\mathbf{v}_{RM} = \mathbf{v}_R - \mathbf{v}_M$ results in a vector tilted backward. This explains why one must tilt an umbrella forward to stay dry.

    *   Final Word Count estimate: ~500-550 words. Perfect.

    *   Check constraints:
        - No filler? Yes.
        - No emojis? Yes.
        - No decorative formatting? Yes.
        - Bold key terms once? Yes.
        - SI units? Yes.
        - Mapping table format? Yes.
        - Breakdown included? Yes.
        - Formal restatement length? Yes.
        - Self-check question? Yes.
        - [ANALOGY_QUALITY:

## 3. Average vs instantaneous velocity — football

**Concept:** Average vs instantaneous velocity  
**Interest:** football  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_kinematics.md :: Average vs instantaneous quantities` (distance 0.643)
2. `physics_kinematics.md :: Velocity` (distance 0.695)
3. `physics_kinematics.md :: Speed` (distance 0.731)

**Retrieved interest context (top 3):**

1. `football.md :: 2. Match jog and walking pace` (distance 0.894)
2. `football.md :: 1. Player sprint speeds` (distance 0.918)
3. `football.md :: 9. Free kick — knuckleball` (distance 0.955)

---

**Generated explanation:**

1. SCENARIO
Imagine you are tracking Kylian Mbappé during a match using a high-speed camera and a GPS sensor. If you look at a ten-second clip of him moving from the center circle to the penalty box, his total displacement divided by those ten seconds gives you his average velocity. However, during that window, he did not move at one constant pace; he might have slowed to a jog to bait a defender before exploding into a sprint. If you freeze the action at one exact millisecond, the velocity he possesses at that specific snapshot is his instantaneous velocity. While his average velocity for the clip might be a modest 4 m/s due to his winding path and pauses, his instantaneous velocity during a peak burst could reach 10 m/s. This is the difference between the stretched-out summary of the play and the precise state of his motion at one moment.

$\Delta \mathbf{r}$ (displacement) $\rightarrow$ net distance from start to end of the clip
$\Delta t$ (time interval) $\rightarrow$ the ten-second duration
$\mathbf{v}_{avg}$ (average velocity) $\rightarrow$ the overall pace from start to finish
$\mathbf{v}$ (instantaneous velocity) $\rightarrow$ the GPS reading at one frozen moment

The analogy breaks down because a real GPS tracker calculates average velocity over a very small time window, whereas true instantaneous velocity is a mathematical limit where the time interval is zero.

2. FORMAL RESTATEMENT
**Velocity** is defined as the rate of change of displacement with time, expressed as $\mathbf{v} = d\mathbf{r}/dt$, where $\mathbf{r}$ is the position vector. It is a **vector** quantity, meaning it possesses both magnitude and direction, measured in metres per second (m/s). The **average velocity** over a time interval $[t_1, t_2]$ is given by $\mathbf{v}_{avg} = \Delta\mathbf{r}/\Delta t$, where $\Delta\mathbf{r}$ is the total displacement and $\Delta t$ is the elapsed time. In contrast, **instantaneous velocity** is the velocity of an object at a specific instant of time, calculated as the limit of the average velocity as the time interval $\Delta t$ approaches zero. Geometrically, on a position-time graph, the average velocity is the slope of the chord connecting two points, while the instantaneous velocity is the slope of the tangent at a single point. This distinction is critical for **non-uniform motion**, where the speed or direction changes over time.

3. SELF-CHECK QUESTION
If Mbappé sprints from the halfway line to the goal and then immediately sprints back to the halfway line in 10 seconds, how does his average velocity for the entire trip compare to his instantaneous velocity at the moment he was fastest?

Hint: Consider the total displacement of the trip versus the movement captured in a single snapshot.

[ANALOGY_QUALITY: 5]

## 4. Projectile motion — football

**Concept:** Projectile motion  
**Interest:** football  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_kinematics.md :: Projectile motion` (distance 0.672)
2. `physics_kinematics.md :: Free fall` (distance 1.265)
3. `physics_kinematics.md :: Equations of motion (uniform acceleration)` (distance 1.323)

**Retrieved interest context (top 3):**

1. `football.md :: 4. Long pass and cross speeds` (distance 0.974)
2. `football.md :: 9. Free kick — knuckleball` (distance 0.976)
3. `football.md :: 20. Set pieces — corner, free kick, penalty` (distance 0.984)

---

**Generated explanation:**

*   Concept: Projectile Motion.
    *   Student Interest: Football.
    *   Level: Class 11 (CBSE/ISC).
    *   Curriculum Context: Projectile as an object moving only under gravity (air resistance ignored). Independent components: horizontal (uniform velocity $v_x = u \cos \theta$) and vertical (uniformly accelerated $a_y = -g$). Trajectory is a parabola. Key formulas: $T = (2 u \sin \theta)/g$, $H = (u^2 \sin^2 \theta)/(2 g)$, $R = (u^2 \sin 2\theta)/g$. Max range at $45^\circ$. Velocity at peak is $u \cos \theta$.
    *   Interest Context: Lofted passes/crosses at $25\text{--}28\text{ m/s}$. Air drag exists (10-15% deceleration). Knuckleballs (asymmetric drag). Penalty speed $\sim 30\text{ m/s}$.
    *   Constraints: 450-650 words. No emojis. No decorative formatting. No filler. Bold key terms once. SI units. Specific output format (SCENARIO, FORMAL RESTATEMENT, SELF-CHECK QUESTION).

    *   Scenario: A lofted long pass from a midfielder to a winger.
    *   Elements to map:
        *   Initial velocity $u$ $\rightarrow$ The speed the ball leaves the boot (e.g., $25\text{ m/s}$).
        *   Launch angle $\theta$ $\rightarrow$ The angle of the boot's strike relative to the grass.
        *   Horizontal component $v_x$ $\rightarrow$ The ball's steady drift across the pitch.
        *   Vertical component $v_y$ $\rightarrow$ The ball's climb and fall.
        *   Gravity $g$ $\rightarrow$ The invisible force pulling the ball back to the grass.
        *   Trajectory $\rightarrow$ The arc of the pass.
        *   Maximum height $H$ $\rightarrow$ The peak of the ball's flight.
        *   Horizontal range $R$ $\rightarrow$ The distance from the kicker to where the winger traps the ball.
        *   Time of flight $T$ $\rightarrow$ The time the winger has to time their run.

    *   *Drafting Scenario:*
        Imagine you are a midfielder playing a lofted long pass to a winger. You strike the ball at $25\text{ m/s}$ at an upward angle; the ball travels forward and upward simultaneously. While the ball glides forward at a steady pace across the pitch, gravity constantly pulls it downward, slowing its climb until it momentarily stops rising and then accelerates back toward the grass. The resulting path is a smooth arc, and the total distance the ball covers before landing is determined by how hard you hit it and the angle of your strike. The time the ball spends in the air is the window the winger has to time their run perfectly.

    *   *Mapping Table:*
        initial speed $u$ $\rightarrow$ ball's speed leaving the boot
        launch angle $\theta$ $\rightarrow$ angle of the strike relative to the turf
        horizontal velocity $v_x$ $\rightarrow$ steady forward drift across the pitch
        vertical velocity $v_y$ $\rightarrow$ the ball's climb and fall
        acceleration due to gravity $g$ $\rightarrow$ the force pulling the ball down
        horizontal range $R$ $\rightarrow$ distance from kicker to landing spot
        time of flight $T$ $\rightarrow$ duration of the winger's timed run

    *   *Breakdown:*
        The analogy breaks because real footballs experience air drag and spin, which cause the ball to decelerate and dip, whereas a theoretical projectile ignores air resistance.

    *   *Drafting Formal Restatement:*
        **Projectile motion** is the motion of an object launched into space with an initial velocity $u$ at an angle $\theta$ to the horizontal, moving only under the influence of gravity. The motion is treated as two independent components: **horizontal motion**, which is uniform with a constant velocity $v_x = u \cos \theta$, and **vertical motion**, which is uniformly accelerated with $a_y = -g$. The path followed is a **parabola**. The **time of flight** is given by $T = (2 u \sin \theta)/g$, representing the total time the object remains in the air. The **maximum height** is $H = (u^2 \sin^2 \theta)/(2 g)$, and the **horizontal range** is $R = (u^2 \sin 2\theta)/g$. At the peak of the trajectory, the vertical velocity is zero, but the horizontal velocity remains $u \cos \theta$.

    *   *Drafting Self-Check Question:*
        If you keep the initial speed $u$ the same but increase the launch angle $\theta$ from $30^\circ$ to $60^\circ$, how does the time of flight $T$ change, and how does this affect the winger's timing in the scenario?
        *Hint:* Look at the mapping for $T$ and see how the $\sin \theta$ term behaves as the angle increases.

    *   *Word Count Check:*
        Scenario: ~100 words.
        Mapping: ~60 words.
        Formal: ~130 words.
        Question: ~50 words.
        Total: ~340 words.
        *Wait*, the constraint is 450-650 words. I need to expand.

    *   *Expansion Strategy:*
        Expand the Scenario narrative to be more descriptive about the physics of the motion.
        Expand the Formal Restatement to explain the symbols more thoroughly and the independence of components.

    *   *Expanded Scenario:*
        Imagine you are a midfielder playing a lofted long pass to a winger. You strike the ball at $25\text{ m/s}$ at an upward angle; the ball is launched into the air and begins to travel forward and upward simultaneously. As the ball glides forward across the pitch, it maintains a steady pace because there are no horizontal forces acting on it in this ideal model. Meanwhile, gravity acts as a constant downward pull, slowing the ball's ascent until it reaches a peak where it momentarily stops rising. From that peak, the ball accelerates back toward the grass, mirroring its climb. The resulting path is a smooth, symmetric arc, and the total distance the ball covers before landing is determined by the strength of your kick and the angle of your strike. The time the ball spends in the air is the critical window the winger uses to time their run from the moment you plant your foot.

    *   *Expanded Formal Restatement:*
        **Projectile motion** describes the movement of an object launched into space with an initial velocity $u$ at an angle $\theta$ relative to the horizontal. This motion is analyzed by separating it into two independent components. The **horizontal motion** is uniform, meaning it has a constant velocity $v_x = u \cos \theta$ because no horizontal acceleration exists. The **vertical motion** is uniformly accelerated due to the constant acceleration of gravity, $a_y = -g$ (where $g \approx 9.8\text{ m/s}^2$), starting with an initial vertical velocity $v_y = u \sin \theta$. The combined effect of these two motions creates a trajectory shaped like a **parabola**. Three key metrics define this motion: the **time of flight** $T = (2 u \sin \theta)/g$, which is the total duration in the air; the **maximum height** $H = (u^2 \sin^2 \theta)/(2 g)$, the highest vertical point reached; and the **horizontal range** $R = (u^2 \sin 2\theta)/g$, the total horizontal distance covered. At the peak of the flight, the vertical component of velocity becomes zero, but the object still possesses its constant horizontal velocity $u \cos \theta$.

    *   *Word Count Re-check:*
        Scenario: ~150 words.
        Mapping: ~60 words.
        Formal: ~180 words.
        Question: ~60 words.
        Total: ~450 words. This fits the lower bound.

    *   Element Correspondence: $u, \theta, v_x, v_y, g, R, T, H$ all mapped. (Check)
    *   Relation Preservation:
        - $u$ and $\theta$ determine $R, T, H$. (Check)
        - $v_x$ is constant. (Check)
        - $v_y$ changes due to $g$. (Check)
        - Peak: $v_y = 0, v_x$ remains. (Check)
    *   Honest Breakdown: Air resistance/drag/spin. (Check)
    *   Format: 1. SCENARIO, 2. FORMAL RESTATEMENT, 3. SELF-CHECK QUESTION. (Check)
    *   No filler, no emojis, no decorative formatting. (Check)
    *   SI units used. (Check)
    *   Bold key terms once. (Check)
    *   Target: Class 11. (Check)

    *   Check mapping table format: "formal element $\

## 5. Free fall — gaming

**Concept:** Free fall  
**Interest:** gaming  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_kinematics.md :: Free fall` (distance 0.774)
2. `physics_kinematics.md :: Equations of motion (uniform acceleration)` (distance 1.435)
3. `physics_kinematics.md :: Relative velocity in two dimensions` (distance 1.477)

**Retrieved interest context (top 3):**

1. `gaming.md :: 19. Realistic vs arcade physics` (distance 1.312)
2. `gaming.md :: 12. Other physics-based puzzlers` (distance 1.399)
3. `gaming.md :: 16. Hit detection — hitboxes and hurtboxes` (distance 1.477)

---

**Generated explanation:**

*   Concept: Free fall.
    *   Student Interest: Gaming.
    *   Level: CBSE/ISC Class 11.
    *   Curriculum Context: Free fall is motion under gravity alone (no air resistance), $g \approx 9.8 \text{ m/s}^2$ (constant), all objects accelerate equally regardless of mass. Equations: $v = \sqrt{2gh}$, $t = \sqrt{2h/g}$, $H = u^2/2g$, $t = u/g$. General kinematics: $v = u + at$, $s = ut + \frac{1}{2}at^2$, $v^2 = u^2 + 2as$.
    *   Interest Context: Simulator vs. Arcade games. World of Goo, Cut the Rope, Crayon Physics (puzzle physics). Hitboxes/hurtboxes in fighting games.

    *   Free fall is about a constant "pull" (acceleration) that doesn't care about the object's properties (mass).
    *   Gaming analogy: Consider a physics-based puzzle game like *Crayon Physics* or *Cut the Rope*. In these games, when you release an object, the game engine applies a constant downward force/acceleration to everything. Whether you draw a tiny circle or a huge block in *Crayon Physics*, they both accelerate toward the bottom of the screen at the same rate. This mimics the "vacuum" environment of free fall where mass doesn't matter.

    *   Gravity ($g$) $\rightarrow$ Game Engine's gravity constant.
    *   Object in free fall $\rightarrow$ A drawn object in *Crayon Physics*.
    *   Ignoring air resistance $\rightarrow$ The "vacuum" of the game world (no wind/drag settings).
    *   Mass independence $\rightarrow$ Tiny circles and huge blocks falling at the same speed.
    *   Height ($h$) $\rightarrow$ Vertical distance from the top of the screen to the ground.
    *   Time ($t$) $\rightarrow$ Game clock/frames until impact.

    *   *Scenario*: Imagine you are playing *Crayon Physics*. You draw a small pebble and a massive boulder at the top of the screen. When you hit "play," both objects begin to drop. Despite the boulder being much larger, the game engine applies the same downward acceleration to both, meaning they hit the bottom of the screen at the exact same moment. In this game world, there is no air resistance to slow the pebble down or push the boulder back. The only thing governing their movement is the game's global gravity setting.

    *   *Mapping*:
        acceleration due to gravity ($g$) $\rightarrow$ game engine's gravity constant
        object in free fall $\rightarrow$ drawn object in *Crayon Physics*
        vacuum/no air resistance $\rightarrow$ absence of drag/wind in game settings
        mass of the object $\rightarrow$ size/weight of the drawn shape
        height ($h$) $\rightarrow$ vertical distance to the screen bottom

    *   *Breakdown*: In a real game engine, "mass" might be used to calculate collisions (how much a boulder pushes a pebble), but in theoretical free fall, mass doesn't affect the *rate* of descent at all. (Wait, the breakdown should be about where the analogy *stops* working).
    *   *Better Breakdown*: The analogy breaks when you introduce "arcade" physics—like in *Mario Kart*—where objects might float or have a "terminal velocity" cap for gameplay balance, whereas true free fall in a vacuum has no speed limit.

    *   *Formal Restatement*:
        **Free fall** is the motion of an object under the influence of gravity alone, ignoring all other forces such as air resistance. Near the Earth's surface, this results in a constant **acceleration due to gravity**, denoted as $g \approx 9.8 \text{ m/s}^2$, directed downward. A key characteristic is that all objects, regardless of their mass, accelerate at the same rate. For an object dropped from rest at height $h$, the final velocity is $v = \sqrt{2gh}$ and the time taken is $t = \sqrt{2h/g}$. If an object is thrown upward with initial speed $u$, the **maximum height** reached is $H = u^2 / (2g)$. These are specific applications of the general **kinematic equations** where $a = g$.

    *   *Self-Check Question*:
        If you were to double the height $h$ from which you drop an object in the game, would the time $t$ it takes to hit the ground also double? Use the mapping to explain why or why not.
        *Hint*: Look at the relationship between $t$ and $h$ in the formula $t = \sqrt{2h/g}$.

    *   Check constraints: 450-650 words?
    *   Scenario: ~6 sentences. Mapping table. Breakdown sentence.
    *   Formal: 5-7 sentences. Equations included. Terms bolded.
    *   Self-check: Reasoning based. Hint included.
    *   No filler. No emojis. No decorative formatting.

    *   *Scenario Word Count check*:
        ~70 words.
    *   *Formal Word Count check*:
        ~120 words.
    *   *Total*: I need to expand to hit the 350-450 min range.

    *   *Expanding Scenario*:
        Describe the *Crayon Physics* experience more. Talk about the "play" button. Describe the visual of the shapes falling. Elaborate on the "game engine" logic.
    *   *Expanding Formal*:
        Explain the symbols in the equations more clearly. Explain $u$, $v$, $g$, $h$, and $t$ explicitly. Mention the direction of the vector.

    *   *Revised Scenario*:
        Imagine you are playing a physics puzzle game like *Crayon Physics*. You draw a tiny, light pebble and a massive, heavy boulder at the very top of your screen. When you press the play button, the game engine activates its global gravity setting, pulling both objects toward the bottom. You notice that even though the boulder is much larger, it does not fall faster than the pebble; they both accelerate downward at the exact same rate. This happens because the game engine ignores air resistance, treating the screen like a vacuum. Consequently, both shapes strike the bottom edge of the screen at the same instant.

    *   *Revised Formal*:
        **Free fall** is defined as the motion of an object moving solely under the influence of gravity, where all other forces, specifically air resistance, are ignored. Near the Earth's surface, objects experience a constant **acceleration due to gravity**, represented by the symbol $g$, which is approximately $9.8 \text{ m/s}^2$ and directed downward. A fundamental principle of this motion is that the acceleration is independent of the object's mass. For an object dropped from rest from a height $h$, the final velocity is $v = \sqrt{2gh}$ and the time of flight is $t = \sqrt{2h/g}$. If an object is projected upward with an initial velocity $u$, it reaches a **maximum height** $H = u^2 / (2g)$ before momentarily stopping. These behaviors are derived from the general **kinematic equations** by substituting the constant acceleration $a$ with the value of $g$.

    *   *Self-Check*:
        If you were to double the height $h$ from which you drop an object in the game, would the time $t$ it takes to hit the ground also double? Use the mapping to explain why or why not.
        Hint: Consider the mathematical relationship between $t$ and $h$ in the formula $t = \sqrt{2h/g}$.

    *   Scenario: ~100 words.
    *   Mapping: ~50 words.
    *   Breakdown: ~30 words.
    *   Formal: ~150 words.
    *   Self-check: ~60 words.
    *   Total: ~390 words. (Meets the >350 requirement).

    *   No filler? Yes.
    *   No emojis? Yes.
    *   Bold key terms once? Yes (**Free fall**, **acceleration due to gravity**, **maximum height**, **kinematic equations**).
    *   SI units? Yes ($9.8 \text{ m/s}^2$).
    *   Mapping correct? Yes.
    *   Breakdown honest? Yes.

    *   *Wait*, I need to make sure the breakdown is specific. "The analogy breaks because real game engines often implement a 'terminal velocity' to prevent objects from clipping through walls at high speeds, whereas theoretical free fall in a vacuum allows velocity to increase indefinitely." -> This is a strong, instructive breakdown.

    *   *Refining the Formal Restatement for clarity and length*:
        Ensure $u$ (initial velocity), $v$ (final velocity), $g$ (acceleration), $h$ (height), and $t$ (time) are all explicitly mentioned.

    *   *Final Polish*:
        SCENARIO
        (Text)
        (Table)
        (Breakdown)

        FORMAL RESTATEMENT
        (Text)

        SELF-CHECK QUESTION
        (Text)
        (Hint)

## 6. Work done by a force — football

**Concept:** Work done by a force  
**Interest:** football  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_work_energy.md :: Work done by a constant force` (distance 0.880)
2. `physics_work_energy.md :: Work-energy theorem` (distance 0.920)
3. `physics_work_energy.md :: Conservative vs non-conservative forces` (distance 0.933)

**Retrieved interest context (top 3):**

1. `football.md :: 12. Sprint power output` (distance 0.941)
2. `football.md :: 8. Free kick — curling trajectory` (distance 1.094)
3. `football.md :: 3. Short pass speeds` (distance 1.179)

---

**Generated explanation:**

*   Concept: Work done by a force.
    *   Student Interest: Football.
    *   Level: CBSE/ISC Class 11.
    *   Curriculum Context: $W = \mathbf{F} \cdot \mathbf{d} = F d \cos \theta$. Work is a scalar. Positive if force is along displacement, negative if opposing, zero if perpendicular. It transfers energy.
    *   Interest Context: Footballer power (1.5-2.5 kW), total mechanical work (80-120 kJ), Magnus effect (side spin), ground pass speeds (20 m/s $\rightarrow$ 13 m/s over 15 m due to friction).

    *   Goal: Model $W = F d \cos \theta$.
    *   Scenario elements:
        *   Force ($\mathbf{F}$): The push from the boot or the friction of the grass.
        *   Displacement ($\mathbf{d}$): The path the ball takes.
        *   Angle ($\theta$): The direction of the kick relative to the ball's path or the friction relative to the path.
        *   Work ($W$): The change in the ball's energy/speed.
    *   Specifics from Interest Context:
        *   Positive work: A boot striking the ball to launch it at 20 m/s.
        *   Negative work: Friction with the grass slowing the ball from 20 m/s to 13 m/s over 15 m.
        *   Zero work: The Magnus effect (lateral lift force) acts perpendicular to the instantaneous velocity for a moment, or a player holding the ball still. Actually, the curriculum mentions a waiter with a tray. In football, a player carrying the ball under their arm while running horizontally would be a good zero-work example. Or, the Magnus effect's perpendicular component. Let's use the friction and the kick for clarity.

    *   *Drafting Scenario:*
        Imagine you strike a football for a ground pass. When your boot pushes the ball forward, the force is in the same direction as the ball's movement, adding energy and launching it at 20 m/s. As the ball rolls across the pitch, the friction from the grass pushes back against the motion, draining energy and slowing the ball to 13 m/s over a 15 m distance. If you were to carry the ball steadily under your arm while running forward, the upward force you use to hold it doesn't move the ball upward, so that specific force does no work.

    *   *Mapping Table:*
        constant force $\mathbf{F}$ $\rightarrow$ push from boot / friction from grass
        displacement $\mathbf{d}$ $\rightarrow$ distance the ball rolls
        angle $\theta$ $\rightarrow$ angle between the push/friction and the roll direction
        work $W$ $\rightarrow$ energy transferred to or from the ball

    *   *Breakdown:*
        The analogy breaks because the force of a kick is an impulsive, rapidly changing force, whereas the formal definition provided assumes a constant force over the displacement.

    *   *Drafting Formal Restatement:*
        **Work** is the mechanism by which energy is transferred to or from an object. When a constant force $\mathbf{F}$ acts on an object that undergoes displacement $\mathbf{d}$, the work done is defined by the equation $W = \mathbf{F} \cdot \mathbf{d} = F d \cos \theta$. In this formula, $F$ is the magnitude of the force, $d$ is the magnitude of the displacement, and $\theta$ is the angle between the force and displacement vectors. The SI unit for work is the **joule** (J), where $1\text{ J} = 1\text{ N}\cdot\text{m}$. Work is a **scalar** quantity. It is positive when the force has a component along the displacement, negative when it opposes the displacement, and zero when the force is perpendicular to the displacement.

    *   *Drafting Self-Check Question:*
        If a ball is rolling forward and a gust of wind pushes it exactly sideways (perpendicular to its path), does the wind do any work on the ball? Explain your answer using the mapping of the angle $\theta$.
    *   *Hint:* Think about the value of $\cos \theta$ when the force and displacement are perpendicular.

    *   Check constraints:
        *   No emojis? Yes.
        *   No decorative formatting? Yes.
        *   Bold key terms once? Yes.
        *   No filler? Yes.
        *   SI units? Yes.
        *   Length? 450-650 words.
        *   Mapping table format? Yes.
        *   Breakdown included? Yes.
        *   Formal restatement 5-7 sentences? Yes.
        *   Self-check question reasoning through mapping? Yes.

    *   *Refining the scenario for length and detail:*
        You strike a football for a ground pass, launching it at 20 m/s. During the moment of impact, your boot applies a forward force that aligns perfectly with the ball's path, transferring energy into the ball to make it accelerate. As the ball rolls 15 m across the pitch, the friction from the grass applies a constant backward force, opposing the motion and slowing the ball down to 13 m/s. If you were to carry the ball tucked under your arm while sprinting forward, the upward force you exert to keep the ball from falling is perpendicular to your forward motion. In this case, despite the effort, that upward force does no work on the ball.

    *   *Refining the mapping:*
        constant force $\mathbf{F}$ $\rightarrow$ push from boot / friction from grass / upward hold
        displacement $\mathbf{d}$ $\rightarrow$ distance the ball travels
        angle $\theta$ $\rightarrow$ angle between the force and the path of motion
        work $W$ $\rightarrow$ energy transferred to or from the ball

    *   *Refining the formal restatement:*
        **Work** is the mechanism by which energy is transferred to or from an object. When a constant force $\mathbf{F}$ acts on an object that undergoes displacement $\mathbf{d}$, the work done is defined as $W = \mathbf{F} \cdot \mathbf{d} = F d \cos \theta$. Here, $F$ represents the magnitude of the force, $d$ represents the magnitude of the displacement, and $\theta$ is the angle between the force and displacement vectors. The SI unit of work is the **joule** (J), defined as $1\text{ J} = 1\text{ N}\cdot\text{m}$. Work is a **scalar** quantity, meaning it has magnitude but no direction. It is positive when the force speeds the object up along the direction of motion, negative when it opposes the motion, and zero when the force is perpendicular to the displacement.

    *   *Final Polish:*
        Check word count.
        Scenario: ~110 words.
        Mapping: ~40 words.
        Breakdown: ~25 words.
        Formal: ~120 words.
        Question/Hint: ~50 words.
        Total: ~345 words. I need to expand slightly to hit the 350-650 range.

    *   *Expansion strategy:* Elaborate more on the scenario's physics and the formal restatement's conditions.

    *   *Expanded Scenario:*
        You strike a football for a sharp ground pass, launching it at 20 m/s. During the moment of impact, your boot applies a powerful forward force that aligns perfectly with the ball's intended path, transferring energy into the ball to make it accelerate rapidly. As the ball rolls 15 m across the pitch, the friction from the grass applies a persistent backward force, opposing the motion and slowing the ball down to 13 m/s. This friction acts as a drain, removing kinetic energy from the ball over the distance it travels. If you were to carry the ball tucked under your arm while sprinting forward, the upward force you exert to keep the ball from falling is perpendicular to your forward motion. In this specific instance, despite the physical effort of holding the ball, that upward force does no work on the ball because it does not cause displacement in the direction of the force.

    *   *Expanded Formal:*
        **Work** is the formal mechanism by which energy is transferred to or from an object. When a constant force $\mathbf{F}$ acts on an object that undergoes displacement $\mathbf{d}$, the work done by that force is defined by the dot product: $W = \mathbf{F} \cdot \mathbf{d} = F d \cos \theta$. In this equation, $F$ is the magnitude of the force, $d$ is the magnitude of the displacement, and $\theta$ is the angle between the force and displacement vectors. The SI unit for work is the **joule** (J), where $1\text{ J} = 1\text{ N}\cdot\text{m}$. Work is a **scalar** quantity, which means it does not have a direction of its own. The sign of the work depends on the angle $\theta$: it is positive when the force has a component along the displacement, negative when the force opposes the displacement, and zero when the force and displacement are

## 7. Kinetic energy — gaming

**Concept:** Kinetic energy  
**Interest:** gaming  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_work_energy.md :: Kinetic energy` (distance 0.752)
2. `physics_work_energy.md :: Work-energy theorem` (distance 0.993)
3. `physics_work_energy.md :: Power` (distance 1.054)

**Retrieved interest context (top 3):**

1. `gaming.md :: 17. Power-ups and energy conservation` (distance 0.968)
2. `gaming.md :: 19. Realistic vs arcade physics` (distance 1.102)
3. `gaming.md :: 13. Frame rate and perceived motion` (distance 1.112)

---

**Generated explanation:**

*   Concept: Kinetic energy (KE).
    *   Student Interest: Gaming.
    *   Level: Class 11 (CBSE/ISC).
    *   Curriculum Context: $KE = \frac{1}{2}mv^2$. Scalar, non-negative, depends on magnitude of velocity, quadratic dependence on speed. Frame-dependent.
    *   Interest Context: Simulators (KSP, iRacing) vs. Arcade games (Mario Kart). KSP tracks mass-energy ratios.
    *   Goal: Analogy-driven explanation.

    *   *Scenario:* Need a gaming scenario where mass and speed both contribute to a "power" or "impact" value, and speed has a disproportionate (quadratic) effect.
    *   *Idea:* A physics-based simulator (like Kerbal Space Program or a destruction sim) where a projectile hits a target.
    *   *Mapping:*
        *   Mass ($m$) $\rightarrow$ The weight/size of the projectile (e.g., a heavy fuel tank in KSP).
        *   Speed ($v$) $\rightarrow$ The velocity of the projectile.
        *   Kinetic Energy ($KE$) $\rightarrow$ The "destruction value" or "impact force" that determines how much damage is dealt to the target.
        *   Quadratic relationship ($v^2$) $\rightarrow$ Doubling the speed doesn't just double the damage; it quadruples it.
    *   *Drafting the Scenario:*
        Imagine you are playing a physics simulator like Kerbal Space Program where you launch a debris piece at a target. The total damage dealt upon impact depends on both the size of the debris and how fast it is moving. If you launch a heavy fuel tank, it causes more destruction than a small probe at the same speed because of its greater mass. However, speed is the real game-changer; if you double the speed of your projectile, the damage doesn't just double—it quadruples, smashing through the target with far more violence. This "impact potential" is what the game tracks to decide if the target survives or is obliterated.

    *   *Mapping Table:*
        mass ($m$) $\rightarrow$ size/weight of the projectile
        speed ($v$) $\rightarrow$ velocity of the projectile
        kinetic energy ($KE$) $\rightarrow$ impact potential/damage value
        frame of reference $\rightarrow$ the observer's perspective (e.g., relative to the target)

    *   *Breakdown Point:* In real physics, KE is a form of energy that can be converted; in most games, "damage" is just a number subtracted from a health bar and doesn't necessarily conserve energy.

    *   *Formal Restatement:*
        **Kinetic energy** is the energy an object possesses by virtue of its motion. For an object of mass $m$ moving at speed $v$, the kinetic energy is given by the equation $KE = \frac{1}{2}mv^2$. The SI unit for this energy is the **joule** (J). It is a **scalar** quantity, meaning it has magnitude but no direction, and it is always non-negative. Notably, the energy depends on the square of the speed; doubling the speed results in four times the kinetic energy. Because it depends on the speed relative to an observer, kinetic energy is not invariant and varies based on the chosen **reference frame**.

    *   *Self-Check Question:*
        If you replace a projectile with one that has half the mass but you launch it at twice the original speed, how does the resulting "impact potential" (kinetic energy) change compared to the original launch?
        *Hint:* Look at how the mass and the square of the speed interact in the mapping.

    *   Element Correspondence? Yes. ($m$, $v$, $KE$, frame $\rightarrow$ mass, speed, damage, observer).
    *   Relation Preservation? Yes. Linear with mass, quadratic with speed.
    *   Honest Breakdown? Yes. Energy conservation vs. health bar subtraction.
    *   Format? No preamble, no emojis, no decorative formatting. Bold key terms once. SI units used.
    *   Length?
        *   Scenario: ~75 words.
        *   Mapping: ~30 words.
        *   Restatement: ~90 words.
        *   Question: ~40 words.
        *   Total: ~235 words. *Wait, the constraint says 450-650 words.* I need to expand.

    *   *Expanding Scenario:* Describe the KSP scenario in more detail. Discuss the difference between a light probe and a heavy tank. Explain the feeling of the speed increase.
    *   *Expanding Formal Restatement:* Elaborate on the Work-Energy theorem connection (as mentioned in the curriculum context), the derivation from $F=ma$, and the implication for braking distances.
    *   *Expanding Question:* Make the reasoning more complex.

    *   *Scenario:*
        Imagine you are playing a high-fidelity simulator like Kerbal Space Program, where the game calculates the impact of colliding objects. You are testing the destruction of a space station by launching various projectiles at it. If you launch a small, lightweight probe, it might only dent the hull, but if you launch a massive fuel tank at the same speed, the sheer bulk of the tank causes significantly more wreckage. However, the most dramatic changes happen when you tweak the speed. If you manage to double the velocity of your projectile, you will notice that the wreckage is not just twice as bad, but four times as severe, as the projectile punches through multiple layers of the station. This total "impact potential" determines whether the station simply shakes or completely disintegrates upon contact.

    *   *Mapping Table:*
        mass ($m$) $\rightarrow$ weight/size of the projectile
        speed ($v$) $\rightarrow$ velocity of the projectile
        kinetic energy ($KE$) $\rightarrow$ total impact potential
        reference frame $\rightarrow$ perspective of the space station

    *   *Breakdown:* The analogy fails because game "damage" is often a calculated value subtracted from a health pool, whereas real kinetic energy is a physical quantity that must be conserved or transferred into other forms like heat or sound.

    *   *Formal Restatement:*
        **Kinetic energy** is the energy an object possesses by virtue of its motion. For an object of mass $m$ moving at speed $v$, the kinetic energy is defined by the equation $KE = \frac{1}{2}mv^2$, where the SI unit is the **joule** (J). This quantity is a **scalar**, meaning it depends only on the magnitude of the velocity and not the direction of travel. The quadratic dependence on speed is a critical feature; for instance, a vehicle moving at 100 km/h possesses four times the energy of the same vehicle moving at 50 km/h. This relationship is derived from the **work-energy theorem**, which states that the net work done on an object equals the change in its kinetic energy: $W_{net} = \Delta KE = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$. Because speed is measured relative to an observer, kinetic energy depends entirely on the **reference frame** being used.

    *   *Self-Check Question:*
        Suppose you are designing a new projectile in your simulator. You decide to decrease the mass of the projectile by half to make it more aerodynamic, but you use a more powerful engine to increase its speed by a factor of two. Based on the mapping, how does the new "impact potential" compare to the original, and why does the speed change have a larger effect than the mass change?
        *Hint:* Consider how the mass term and the speed term are treated mathematically in the impact potential formula.

    *   Scenario: ~110 words.
    *   Mapping: ~30 words.
    *   Breakdown: ~30 words.
    *   Restatement: ~150 words.
    *   Question: ~80 words.
    *   Total: ~400 words. Still a bit short. I need to hit 450-650.

    *   *Further Expansion of Scenario:* Describe the specific visual difference between a $1\times$ speed hit and a $2\times$ speed hit. Describe the "feel" of the mass difference.
    *   *Further Expansion of Restatement:* Mention the integration of $F=ma$ and the role of $W_{net}$ more explicitly. Mention that it is always non-negative.

    *   *Scenario Revised:*
        Imagine you are playing a high-fidelity simulator like Kerbal Space Program, where the game engine calculates the physical impact of colliding objects. You are testing the destruction of a space station by launching various projectiles at it from a distance. If you launch a small, lightweight scientific probe, it might only leave a small dent in the station's hull. However, if you launch a massive, heavy fuel tank at that same speed, the sheer bulk of the tank causes significantly more wreckage because there is more matter in motion. The most dramatic changes occur, however, when you tweak the launch velocity. If you manage to double the speed of your projectile, you will notice that the resulting wreckage is not just twice as bad, but four times as severe, as the projectile punches through multiple layers of the station's armor. This total "impact potential" is the value the game uses to

## 8. Work-energy theorem — football

**Concept:** Work-energy theorem  
**Interest:** football  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_work_energy.md :: Work-energy theorem` (distance 0.753)
2. `physics_work_energy.md :: Conservative vs non-conservative forces` (distance 0.757)
3. `physics_work_energy.md :: Work done by a variable force` (distance 1.125)

**Retrieved interest context (top 3):**

1. `football.md :: 12. Sprint power output` (distance 1.128)
2. `football.md :: 11. Goal celebration jump` (distance 1.296)
3. `football.md :: 15. Friction — snowy or icy pitch` (distance 1.715)

---

**Generated explanation:**

1. SCENARIO
You are a 75 kg player standing on the pitch, preparing to explode into a sprint to reach a launch speed of 3.4 m/s for a vertical jump. As you drive your legs into the turf, you apply a powerful forward force over the first few meters of your movement. This combined effort—the force of your stride multiplied by the distance you cover while accelerating—represents the work being done on your body. If you increase the force of your push or extend the distance over which you accelerate, you will reach a higher final speed. However, if the match is played on

## 9. Power — gaming

**Concept:** Power  
**Interest:** gaming  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_work_energy.md :: Power` (distance 1.126)
2. `physics_work_energy.md :: Real-world examples` (distance 1.404)
3. `physics_work_energy.md :: Real-world examples` (distance 1.429)

**Retrieved interest context (top 3):**

1. `gaming.md :: 17. Power-ups and energy conservation` (distance 1.205)
2. `gaming.md :: 6. Physics engines — Havok and PhysX` (distance 1.291)
3. `gaming.md :: 19. Realistic vs arcade physics` (distance 1.305)

---

**Generated explanation:**

*   Concept: Power.
    *   Student Interest: Gaming.
    *   Level: CBSE/ISC Class 11.
    *   Key constraints: No preamble, specific format (Scenario, Formal Restatement, Self-Check Question), no emojis, no decorative formatting, bold key terms only once, SI units, 350-650 words.

    *   Definition: Rate of doing work or transferring energy.
    *   Equations: $P_{avg} = W / t$ and $P = dW/dt = \mathbf{F} \cdot \mathbf{v}$.
    *   Unit: Watt (W) = 1 J/s.
    *   Key insight: Power is about "how quickly," not "how much."

    *   Arcade vs. Simulator.
    *   Physics engines (Havok, PhysX).
    *   Resource management (fuel in KSP).
    *   Specific examples: Half-Life 2, Borderlands 3, iRacing.

    *   *Idea 1: Resource gathering.* Collecting 100 gold in 10 seconds vs 100 gold in 1 second. (A bit too simple, maybe too close to just "rate").
    *   *Idea 2: Character damage.* A character doing 100 damage over 5 seconds vs 100 damage in 1 second. (DPS - Damage Per Second is the classic gaming equivalent of Power).
    *   *Idea 3: Loading screens/Data transfer.* Transferring a game file. (Too generic).
    *   *Idea 4: Simulator vs Arcade energy.* (Too abstract).

    *   *Refining Idea 2 (DPS):*
        In many games, "Damage Per Second" (DPS) is exactly what power is.
        Work = Total damage dealt to a boss.
        Time = Duration of the attack.
        Power = Damage per second.
        Force $\times$ Velocity $\rightarrow$ The "force" of a hit $\times$ the "speed" of attacks.

    *   *Wait, let's try to map $P = F v$ more precisely.*
        If you are pushing a physics object in *Half-Life 2* using the Gravity Gun, the "work" is moving the object a certain distance.
        If you push it slowly, it takes a long time. If you push it fast (high velocity) with the same force, you are delivering energy to that object much faster.

    *   *Let's go with a "Charging" or "Energy" mechanic common in gaming (like a turbo meter or a special attack).*
        Imagine you need to charge a "Super Meter" to 100 units (Total Work/Energy).
        Player A uses a slow charge item that fills it in 10 seconds.
        Player B uses a high-tier item that fills it in 2 seconds.
        Both did the same "work" (filled the meter), but Player B had more "power."

    *   *Let's try the DPS angle again, as it's more intuitive for Class 11 and maps well to "rate."*
        Scenario: Two players are attacking a boss with 1000 HP.
        Player 1 deals 1000 damage over 10 seconds.
        Player 2 deals 1000 damage in 2 seconds.
        The "work" (total damage) is the same, but the "power" (DPS) is different.
        To map $P = F v$: Imagine a character pushing a heavy physics object in *Half-Life 2*. The force is how hard they push; the velocity is how fast the object moves. The power is the rate at which they transfer energy into that object.

    *   *Scenario Draft:*
        Imagine you are playing a game like Half-Life 2 and using the Gravity Gun to push a heavy crate across a room. To move the crate a specific distance, you must perform a certain amount of work. If you push the crate slowly, it takes a long time to reach the destination. However, if you apply the same force but the crate moves at a much higher velocity, you are transferring energy into the crate much faster. This "speed of energy delivery" is the power of your action. Two players might move the same crate the same distance, but the player who does it faster is utilizing more power.

    *   *Mapping:*
        Total energy transferred to crate $\rightarrow$ Work ($W$)
        Time taken to move the crate $\rightarrow$ time ($t$)
        Rate of energy transfer $\rightarrow$ Power ($P$)
        Pushing force of Gravity Gun $\rightarrow$ Force ($F$)
        Crate's movement speed $\rightarrow$ velocity ($v$)

    *   *Breakdown:* The analogy breaks because in games, "damage" or "pushing" often has a fixed value regardless of time, whereas in physics, power is a continuous rate of energy transfer. (Actually, the $F \cdot v$ mapping is quite strong). Let's say: the analogy breaks because game physics often use "impulse" (instant change in velocity) rather than a continuous application of force over time.

    *   *Formal Restatement:*
        **Power** is defined as the rate at which work is done or the rate at which energy is transferred. The average power over a time interval $t$ is given by $P_{avg} = W / t$, where $W$ is the work done. For instantaneous power, the formula is $P = dW/dt$, which can also be expressed as the dot product of force and velocity: $P = \mathbf{F} \cdot \mathbf{v}$. Here, $\mathbf{F}$ represents the net force applied and $\mathbf{v}$ is the velocity of the object. The SI unit of power is the **watt** (W), defined as 1 joule per second (1 J/s). This distinguishes power from energy; while energy is the total capacity to do work, power describes how quickly that capacity is utilized.

    *   *Self-Check Question:*
        If you are pushing a physics object in a game and you double the force you apply while keeping the object's velocity constant, what happens to the power being delivered to the object?
        *Hint:* Look at the relationship between $F$ and $P$ in the $P = F v$ mapping.

    *   Scenario: 5-7 sentences? Yes.
    *   Mapping table: formal $\rightarrow$ scenario? Yes.
    *   Breakdown: 1 sentence? Yes.
    *   Formal Restatement: 5-7 sentences? Yes.
    *   Equation included? Yes.
    *   Symbols explained? Yes.
    *   Bold key terms once? Yes.
    *   Self-check: Reasoning through mapping? Yes.
    *   Hint included? Yes.
    *   No emojis/decorative formatting? Yes.
    *   No filler/preamble? Yes.
    *   SI units? Yes.
    *   Length: 350-650 words?
        *   Scenario: ~100 words.
        *   Mapping: ~30 words.
        *   Breakdown: ~20 words.
        *   Formal: ~120 words.
        *   Question: ~50 words.
        *   Total: ~320 words. (Wait, I need to expand to meet the 350-650 word minimum).

    *   *Expanding Scenario:* Describe the crate and the Gravity Gun in more detail. Describe the difference between a slow push and a fast push more explicitly.
    *   *Expanding Formal Restatement:* Elaborate on the distinction between average and instantaneous power. Mention the 1 W = 1 J/s conversion explicitly.
    *   *Expanding Question/Hint:* Make the logic slightly more complex.

    *   *Revised Scenario:*
        Imagine you are playing Half-Life 2 and using the Gravity Gun to push a heavy physics crate across a warehouse floor. To move the crate from one end of the room to the other, you must perform a specific amount of work regardless of how you do it. If you push the crate slowly, it takes a long time to reach the destination, meaning you are delivering energy at a low rate. If you instead blast the crate so it streaks across the room at a high velocity, you are transferring that same amount of energy in a fraction of the time. This difference in the speed of energy delivery is exactly what power represents in physics. Two players might achieve the same result—moving the crate the same distance—but the player who does it faster is operating with higher power.

    *   *Revised Mapping:*
        total energy transferred to crate $\rightarrow$ work ($W$)
        duration of the push $\rightarrow$ time ($t$)
        speed of energy delivery $\rightarrow$ power ($P$)
        Gravity Gun's push $\rightarrow$ force ($F$)
        crate's movement speed $\rightarrow$ velocity ($v$)

    *   *Revised Formal Restatement:*
        **Power** is defined as the rate at which work is done or the rate at which energy is transferred. The average power over a specific time interval $t$ is calculated as $P_{avg} = W / t$, where $W$ is the total work performed. For a more

## 10. Conservation of energy — football

**Concept:** Conservation of energy  
**Interest:** football  
**Level:** Class 11

---

**Retrieved curriculum context (top 3):**

1. `physics_work_energy.md :: Conservation of energy` (distance 0.743)
2. `physics_work_energy.md :: Real-world examples` (distance 1.019)
3. `physics_work_energy.md :: Real-world examples` (distance 1.059)

**Retrieved interest context (top 3):**

1. `football.md :: 12. Sprint power output` (distance 0.939)
2. `football.md :: 11. Goal celebration jump` (distance 0.990)
3. `football.md :: 15. Friction — snowy or icy pitch` (distance 1.085)

---

**Generated explanation:**

*   Concept: Conservation of Energy (Mechanical vs. Total).
    *   Student Interest: Football.
    *   Level: CBSE/ISC Class 11.
    *   Constraints: 450-650 words, specific output format (SCENARIO, FORMAL RESTATEMENT, SELF-CHECK QUESTION), no filler, no emojis, bold key terms once, SI units.
    *   Curriculum Context: Law of conservation of mechanical energy ($E = KE + PE$), conservative forces (gravity, spring), non-conservative forces (friction, air resistance) leading to heat/sound/deformation. Total energy of an isolated system is always conserved.
    *   Interest Context: 75 kg player jumping 60 cm (KE to PE), launch speed $\sqrt{2gh} \approx 3.4$ m/s, friction on snow/ice (0.05-0.15), mechanical power of 1.5-2.5 kW.

    *   Formal elements:
        *   Kinetic Energy (KE)
        *   Potential Energy (PE)
        *   Total Mechanical Energy ($E = KE + PE$)
        *   Conservative forces (gravity)
        *   Non-conservative forces (friction/air resistance)
        *   Conversion to heat/sound (loss of mechanical energy)
    *   Scenario: A player jumping for a header.
        *   Launch phase: The player has KE (velocity $\approx 3.4$ m/s).
        *   Peak of jump: KE becomes zero, PE is maximum ($mgh \approx 441$ J).
        *   Descent: PE converts back to KE.
        *   Landing: KE is lost to the ground (sound, deformation of turf, heat).
        *   Total energy: The chemical energy in the muscles $\rightarrow$ mechanical energy $\rightarrow$ heat/sound.

    *   *Scenario Draft*: Imagine you are a 75 kg player leaping for a header. As you launch yourself upward at 3.4 m/s, you possess a burst of kinetic energy. As you rise toward the peak of your 60 cm jump, your speed decreases, but you gain gravitational potential energy. At the very top, your kinetic energy is zero, and your potential energy is at its maximum of 441 J. As you fall back down, that potential energy converts back into kinetic energy. When you hit the turf, you don't bounce back to 60 cm; instead, the energy is dissipated as the sound of the landing and the deformation of the grass.

    *   *Mapping*:
        *   launch speed/motion $\rightarrow$ kinetic energy (KE)
        *   height of the jump $\rightarrow$ potential energy (PE)
        *   sum of motion and height $\rightarrow$ total mechanical energy (E)
        *   gravity acting on the player $\rightarrow$ conservative force
        *   turf deformation/sound $\rightarrow$ non-conservative forces (energy loss)

    *   *Breakdown*: The analogy breaks because the jump isn't a closed system; the player uses chemical energy from muscles to start the motion, whereas the formal law often focuses on a system where energy is already present and just shifting forms.

    *   *Formal Restatement Draft*:
        The **law of conservation of mechanical energy** states that if only conservative forces, such as gravity, act on a system, the total mechanical energy $E = KE + PE$ remains constant. This is expressed by the equation $KE_i + PE_i = KE_f + PE_f$, where $KE$ is the **kinetic energy** (energy of motion) and $PE$ is the **potential energy** (stored energy based on position). For a mass $m$ at height $h$, gravitational potential energy is $PE = mgh$, and kinetic energy is $KE = \frac{1}{2}mv^2$. When **non-conservative forces** like friction or air resistance are present, mechanical energy is not conserved because it is converted into other forms like heat or sound. However, the **law of conservation of energy** ensures that the total energy of an isolated system remains constant regardless of the form it takes.

    *   *Self-Check Question*:
        If you perform the same jump on a frozen pitch with a friction coefficient of 0.05 versus a soft grass pitch, how does the loss of mechanical energy upon landing differ, and what does this imply about the total energy of the system?
        *Hint*: Think about where the energy goes when the "non-conservative" interaction with the ground happens.

    *   Check word count:
        *   Scenario: ~100 words.
        *   Mapping: ~30 words.
        *   Restatement: ~130 words.
        *   Question: ~60 words.
        *   Total: ~320 words. (Too short! Needs to be 450-650).

    *   *Expanding Scenario*: Describe the physics of the jump in more detail. Describe the transition from the sprint (KE) to the leap. Explain the "energy budget" of the match.
    *   *Expanding Restatement*: Elaborate on the definitions of conservative vs non-conservative forces. Explain the $v = \sqrt{2gh}$ relationship mentioned in the curriculum context.

    *   *Revised Scenario*:
        Imagine you are a 75 kg striker sprinting toward the box and leaping for a header. At the moment of takeoff, you launch yourself upward with a speed of 3.4 m/s, meaning you have a high amount of kinetic energy. As you ascend toward the peak of your 60 cm jump, your upward velocity slows down, but you are gaining height. This means your kinetic energy is being traded for gravitational potential energy. At the absolute peak of the jump, your velocity is momentarily zero, and your potential energy reaches its maximum of 441 J. As you descend, the process reverses, and the potential energy converts back into kinetic energy. However, when you land on the turf, you do not instantly bounce back up to 60 cm. The energy is "lost" to the environment through the sound of the impact and the physical deformation of the grass and soil.

        launch speed and motion $\rightarrow$ kinetic energy (KE)
        height of the jump $\rightarrow$ potential energy (PE)
        sum of motion and height $\rightarrow$ total mechanical energy (E)
        gravity acting on the player $\rightarrow$ conservative force
        turf deformation and sound $\rightarrow$ non-conservative forces

        The analogy breaks because the jump is not an isolated system; you must inject chemical energy from your muscles to initiate the launch, whereas the law of conservation of mechanical energy typically describes systems where no new energy is added.

    *   *Revised Restatement*:
        The **law of conservation of mechanical energy** states that if only conservative forces—forces that do not dissipate energy, such as gravity or spring forces—act on a system, the total mechanical energy $E = KE + PE$ remains constant. This is represented by the equation $KE_i + PE_i = KE_f + PE_f$, where $KE$ is the **kinetic energy** ($\frac{1}{2}mv^2$) and $PE$ is the **potential energy** (such as $mgh$ for gravity). In this equation, $m$ represents mass, $v$ represents velocity, $g$ is the acceleration due to gravity, and $h$ is the height. This allows us to calculate the final velocity of an object falling from height $h$ as $v = \sqrt{2gh}$, regardless of the path taken. When **non-conservative forces**, such as friction or air resistance, are present, mechanical energy is not conserved because some of it is converted into heat, sound, or internal deformation. Despite this, the broader **law of conservation of energy** dictates that the total energy of an isolated system—including thermal and chemical energy—is always conserved and cannot be created or destroyed.

    *   *Revised Self-Check*:
        Suppose you perform a jump on a frozen pitch where the friction coefficient is very low (0.05) compared to a standard grass pitch. If you consider the "system" to be just you and the Earth, how would the total mechanical energy change differently upon landing on ice versus grass, and does this change the total energy of the universe?
        *Hint*: Consider whether the energy "lost" to the ground is actually gone or just converted into a non-mechanical form.

    *   Word count check:
        *   Scenario: ~160 words.
        *   Mapping: ~40 words.
        *   Breakdown: ~40 words.
        *   Restatement: ~180 words.
        *   Question: ~80 words.
        *   Total: ~500 words. (Perfect).

    *   Check constraints:
        *   No emojis? Yes.
        *   Bold key terms once? Yes.
        *   SI units? Yes.
        *   No filler? Yes.
        *   Mapping format? Yes.
        *   Breakdown included? Yes.
        *   Direct address "you"? Yes.
        *   CBSE/ISC Class 11 level? Yes.

    *   Wait, let me double check the "Bold key terms on first mention only" rule.
        *   **law of conservation of mechanical


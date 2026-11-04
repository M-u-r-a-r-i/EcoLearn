# Interest corpus — Gaming

Short, physics-relevant passages about video games. Used by the analogy generator to ground concept explanations in concrete, accurate domain detail.

## 1. Racing game acceleration — simulators

Modern simulation racers like Forza Motorsport and iRacing model real-car acceleration curves. A Porsche 911 GT3 RS reaches 100 km/h from rest in about 3.2 s in-game, matching its real-world figure. The simulation tracks engine torque, gear ratio, traction loss, and weight transfer. A player who upshifts too early before peak torque sees the same acceleration penalty as in real life — the game is solving Newton's second law moment by moment, not playing a pre-recorded animation.

## 2. Racing game top speed

The Bugatti Chiron in Forza Horizon 5 reaches around 490 km/h with maximum tuning — close to the real car's Super Sport variant. Asphalt 9 takes a different route: arcade physics let hypercars exceed 600 km/h with stacked nitro, far above anything physical. Both models are internally consistent, but only one is trying to be Newtonian. Choosing between a simulator and an arcade racer is, at root, choosing which physics rules the game obeys.

## 3. FPS projectile — hitscan

In Counter-Strike 2, most rifle shots are "hitscan": when the player clicks, the game traces a straight line from the muzzle through the crosshair to whatever it hits, applying damage instantly. There is no bullet travel time, no drop, and no wind. This is a simplification — real bullets take milliseconds to reach a target even at short range — but it keeps the game responsive on a 64 or 128 tick server. The cost is that hitscan weapons cannot be dodged or led.

## 4. FPS projectile — bullet drop and travel time

Battlefield and Arma simulate projectile flight properly. A sniper round in Battlefield 2042 leaves the barrel near 850 m/s and is subject to gravity (g ≈ 9.8 m/s²), so over a 600 m shot it drops roughly 2.5 m. A skilled sniper holds aim above the target by an amount proportional to range — exactly as in real-world long-range shooting. The result is that engagements feel ballistic, with leading targets and dialling for distance.

## 5. Physics engines — what they simulate

A physics engine handles forces, collisions, and motion of objects in a game. It typically simulates rigid-body dynamics (mass, velocity, angular momentum), constraints (joints, hinges), and contact (friction, restitution). It does not usually simulate fluid dynamics or large-scale destruction — those need specialised systems. The engine runs at a fixed timestep (often 60 or 120 Hz), updating positions by integrating Newton's laws over each step.

## 6. Physics engines — Havok and PhysX

Havok powered Half-Life 2 (2004), where the Gravity Gun let players manipulate physics objects with believable mass, drag, and angular response. NVIDIA's PhysX, integrated into Unreal Engine, handles cloth, soft bodies, and particles in games like Borderlands 3 and Mirror's Edge. Unity ships with its own physics layer based on PhysX. The choice of engine determines which physical effects developers can use cheaply and which require custom code.

## 7. MOBA mana

In Dota 2 and League of Legends, mana is a resource that caps ability use. Heroes start with a mana pool (often 200–800) that regenerates slowly (1–10 per second) and is drained by spell costs. Mana scales with level and item upgrades. Strategically, mana is a soft limit on combat tempo: a hero who burns spells too fast becomes harmless until the pool refills. Some heroes use alternate resources (rage, energy, charges) with the same gating role.

## 8. RPG stamina

In Dark Souls and Elden Ring, stamina caps almost every active action — attacking, dodging, blocking, sprinting. The bar regenerates at roughly 30–45 units per second when the player is not acting, and is fully drained by a heavy combo. Combat becomes a rhythm of action and recovery, forcing patience. Real combat sports have a similar dynamic — high-intensity bursts followed by recovery — and stamina-based games are imitating that pacing, not energy in a strict physics sense.

## 9. Asphalt 9 — nitro mechanics

Asphalt 9 has three nitro tiers. A normal tap gives a moderate acceleration spike. A "shockwave" nitro, triggered by tapping a second time when a blue zone appears on the bar, applies a far stronger forward impulse, briefly bending the camera and effectively warping the car forward. Nitro is recharged by drifts, perfect launches, near-misses, and stunts. The reward loop incentivises risky driving, since playing safe leaves you stranded on the lowest tier.

## 10. Asphalt 9 — drifting

Drift in Asphalt 9 is initiated by tapping the brake while turning. The car snaps into a slide and the rear wheels lose traction; the player steers into the curve to maintain the line. Unlike a true simulator, A9 ignores tyre wear, weight transfer, and most real friction physics. Drift duration directly fills the nitro bar, so a longer drift through a sweeping bend converts the kinetic energy of the turn into stored boost — an arcade-game energy accounting that is fun but not Newtonian.

## 11. Angry Birds — projectile motion

Angry Birds is a clean projectile-motion game. The launch slingshot sets initial velocity (magnitude and angle); gravity is constant downward; the resulting trajectory is a parabola identical in shape to physics-textbook examples. Players quickly internalise the range relation intuitively: shallow angles bounce short, 45° shots go furthest, steep angles drop almost vertically. Special birds break the simple rule by adding one extra effect each — a mid-flight tap triggers a second burst, an in-air split, or a homing pull.

## 12. Other physics-based puzzlers

World of Goo, Cut the Rope, and Crayon Physics each build a game around one piece of physics. World of Goo balances tensile and compressive forces in growing structures; Cut the Rope uses gravity, ropes, and bubble buoyancy; Crayon Physics lets the player draw rigid bodies that fall and roll. None tries to be a simulator — each picks a subset of Newtonian mechanics and turns it into a puzzle space. The constraints make the games solvable; the rules make them feel real.

## 13. Frame rate and perceived motion

A game renders one frame at a time. At 30 frames per second, each frame is shown for about 33 ms; at 60 fps, for 16.7 ms. Fast-moving objects skip further between frames at lower frame rates, breaking the illusion of smooth motion. Competitive players favour 144 Hz or higher monitors because reduced inter-frame motion improves aim and reaction time. Frame rate also affects input lag — the time between pressing a key and seeing the result on screen.

## 14. 60 fps vs 30 fps in action games

A racing game at 30 fps shows the next frame 33 ms after the current one. At 200 km/h (≈ 55 m/s) the car moves 1.8 m between frames — a noticeable jump. At 60 fps the jump halves to 0.9 m, and motion looks smooth. Competitive shooters target 120+ fps because targets crossing the screen can be missed entirely in a single 30 fps frame. Frame rate is not gameplay realism, but it is perceptual realism.

## 15. Hit detection — collision volumes

A character in a 3D game is rendered as a detailed mesh, but collisions are checked against a simplified volume — usually a capsule or a small set of boxes around the body. When a projectile or melee swing crosses this volume, the engine registers a hit. Capsule colliders are cheap to compute and feel forgiving to players; tight box colliders feel precise but less generous. The choice trades CPU cost against game feel.

## 16. Hit detection — hitboxes and hurtboxes

Fighting games like Street Fighter and Tekken define each attack with a "hitbox" (the region that damages opponents) and each character with "hurtboxes" (regions that can be hit). The two only interact during the attack's active frames. High-level play involves whiffing attacks so the hitbox passes outside the opponent's hurtbox while their counter passes through your now-vulnerable frame. Modern fighting games visualise these boxes in training mode to teach the player exactly what the game checks.

## 17. Power-ups and energy conservation

Most arcade games ignore energy conservation: a mushroom in Mario doubles Mario's size and bouncing power with no mass-energy accounting. Simulation-leaning games sometimes track it strictly — Kerbal Space Program enforces real rocket-fuel mass ratios, so heavier payloads need exponentially more fuel. The contrast is a deliberate design choice: arcade titles trade physical consistency for player power fantasy; simulators trade some fun for the satisfaction of solving a real constraint problem.

## 18. In-game speed comparisons

Walking in most third-person games is around 2 m/s, sprinting around 5–6 m/s — slightly faster than reality, since players cannot sustain a real-world sprint for long. Vehicle speeds vary widely: a horse in The Witcher 3 reaches about 15 m/s, a sports car in GTA V about 55 m/s, a hypercar in Asphalt 9 over 150 m/s. Even when the numbers are realistic, ground textures rarely scale convincingly, so 200 km/h often feels slower than expected — a known visual problem in racing games.

## 19. Realistic vs arcade physics

A simulator (iRacing, DCS World, Microsoft Flight Simulator) tries to reproduce real equations of motion, so the player feels resistance — overcorrecting in a slide ends in a spin, just as in real life. An arcade game (Mario Kart, Burnout) replaces equations with feel: drifting recharges turbo, bumping a wall barely costs anything, and air time triggers stunts. Neither approach is wrong; they are answering different design questions, and pretending an arcade is a simulator (or vice versa) leads to frustrated players.

## 20. Pathfinding in real-time games

A character following a player, or a unit moving across a map, uses pathfinding — typically the A* algorithm on a navigation mesh. The engine pre-computes walkable polygons and then searches for a shortest route between start and goal. Smoothing and dynamic obstacle avoidance run on top. Pathfinding is not physics, but it interacts with physics: collisions with moving units force the path to be re-planned in real time, and large unit groups can stall on each other when the path solver cannot reconcile their goals.

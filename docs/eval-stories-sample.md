# Personal-story AI evaluation
Models: gemini-3.1-flash-lite. 6 cases on a temporary database.

| Measure | Result |
|---|---|
| Stories ready (shown to a student) | 6 of 6 (100%) |
| Ready on the first draft | 4 of 6 |
| Writer declined (no honest link to the hobby) | 0 |
| Failed all drafts (lesson's own story shown) | 0 |
| Model errors | 0 |
| Time per story, median / p95 | 12 s / 32 s |
| Model calls per story | 2.8 (failed calls: 0) |
| Tokens per story (in / out) | 3289 / 812 |
| Cost per story at the reference price | Rs 0.27 |

## Where drafts failed
- critic: 2
- format: 1

## Most common reasons
- 1x The analogy incorrectly equates 'total distance run' with 'speed' (distance is a quantity,
- 1x The analogy incorrectly equates 'velocity' with 'where you end up' (displacement), rather 
- 1x The analogy incorrectly equates 'distance traveled' with 'speed' (distance is a scalar qua
- 1x The limit sentence is irrelevant to the analogy provided; the analogy is about the player'
- 1x Not a JSON object (142 characters): '{ "fit": true, "story": "Arjun watches the shuttle dr

## Stories to read by hand
**cricket student, hobby basketball, concept velocity**
> Arjun dribbles the basketball from the center of the court all the way to the opponent's hoop. He stops, realizes he is blocked, and quickly pivots, dribbling the ball right back to the center line. His teammates cheer for his agility, noting how much ground he covered during the sprint. Later, looking at his fitness tracker, Arjun is confused. It shows he ran a significant distance, yet his overall displacement for the entire play is marked as zero. If he was moving the entire time, how can his final velocity for the play possibly be nothing?
> Analogy: The basketball court acts as your coordinate system. Your total distance represents how much ground you covered while dribbling back and forth. Your velocity, however, cares only about where you started and where you ended. When you return to the center line, your change in position is zero, making your average velocity zero, regardless of how hard you sprinted.
> Limit: This analogy assumes the court is a straight line, which ignores the actual curves and zig-zags of a real basketball game.

**football student, hobby basketball, concept velocity**
> Arjun dribbles down the court, weaving past defenders toward the basket. He sprints forward, then suddenly retreats to the three-point line to reset the play. His teammates cheer for his hustle, seeing him cover so much ground. Later, looking at the game footage, Arjun notices something strange. He spent almost the same amount of effort running back as he did moving forward, yet his position barely shifted. If he ran so hard and covered so much ground, why does his net movement look like he hardly moved at all? This is the puzzle velocity solves.
> Analogy: In this game, your total distance covered divided by time is like your speed, tracking every step you take. However, your velocity is like the scoreboard's perspective: it tracks how quickly your position changes relative to the basket, considering both how fast you move and which direction you are heading.
> Limit: The analogy breaks down because velocity tracks your position change over time, while the scoreboard only tracks points, which do not directly measure how fast or in what direction a player moves.

**gaming student, hobby badminton, concept velocity**
> Arjun stands on the badminton court, his racket ready. He watches the shuttlecock soar high, deep into the backcourt. He dashes backward to reach it, smashing it hard just before it touches the ground. The shuttle zooms forward, straight across the net, landing exactly where his opponent started. Arjun smiles, thinking his game was intense because he covered so much ground across the court. But as he walks back to the center line to reset, he wonders: if he ends up exactly where he began, does his total movement really count for anything, or is there a different way to measure how he actually changed his position?
> Analogy: Your total path across the court represents distance, while your displacement is just the straight-line change from your starting spot. Your average speed tracks how fast you covered that total path, while your average velocity only tracks how quickly your net position changed from start to finish.
> Limit: This analogy stops being true if you consider that the player is not a single point mass, but an extended object moving in complex ways that are not perfectly captured by a simple coordinate.


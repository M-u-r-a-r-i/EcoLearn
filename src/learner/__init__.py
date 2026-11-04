"""What EcoLearn knows about each learner, and what it recommends from that.

* diagnostic.py — the starting check taken after signup (layer 1).
* plan.py       — personal recommendations from the check and from lesson
                  answers (layer 2): skip what they know, fix mix-ups first.

Neither calls a model. See PROJECT_HISTORY.md §9zc for the three layers.
"""

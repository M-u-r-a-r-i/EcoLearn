"""Where the project lives on disk.

Every module that reads data/, prompts/ or chroma_db/ imports PROJECT_ROOT from here
instead of counting `Path(__file__).parents[N]` itself. Moving a module to another folder
then can't silently point it at the wrong directory.
"""

from pathlib import Path

# src/ecolearn/paths.py -> parents[0]=ecolearn, [1]=src, [2]=the repo root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

"""Terminal rock, paper, scissors — uses shared rps_core logic."""

from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from rps_core import DISPLAY, empty_score, parse_move, play_round  # noqa: E402

print(
    """Rock, Paper, Scissors
- Rock beats scissors.
- Paper beats rock.
- Scissors beats paper.
"""
)

score = empty_score()

while True:
    print(f"{score['wins']} Wins, {score['losses']} Losses, {score['ties']} Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
    raw = input("> ")
    try:
        if raw.strip().upper() == "Q":
            print("Thanks for playing!")
            break
        move = parse_move(raw)
    except ValueError:
        print("Type one of R, P, S, or Q.")
        continue

    print(f"{DISPLAY[move]} versus...")
    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")
    time.sleep(0.25)

    result = play_round(move, score["wins"], score["losses"], score["ties"])
    score = {"wins": result["wins"], "losses": result["losses"], "ties": result["ties"]}
    print(result["computer_label"])
    time.sleep(0.5)
    print(result["message"])

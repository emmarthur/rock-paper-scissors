"""
Rock, paper, scissors — shared logic for CLI and web.

Mirrors Al Sweigart's win/loss/tie rules (rock beats scissors, paper beats rock,
scissors beats paper).
"""

from __future__ import annotations

import random
from typing import Any, Literal

Move = Literal["rock", "paper", "scissors"]
Outcome = Literal["win", "lose", "tie"]

MOVES: tuple[Move, ...] = ("rock", "paper", "scissors")

DISPLAY: dict[Move, str] = {
    "rock": "ROCK",
    "paper": "PAPER",
    "scissors": "SCISSORS",
}

PLAYER_WINS: frozenset[tuple[Move, Move]] = frozenset(
    {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
)


def random_computer_move() -> Move:
    return random.choice(list(MOVES))


def judge_round(player: Move, computer: Move) -> Outcome:
    if player == computer:
        return "tie"
    if (player, computer) in PLAYER_WINS:
        return "win"
    return "lose"


def outcome_message(outcome: Outcome) -> str:
    if outcome == "win":
        return "You win!"
    if outcome == "lose":
        return "You lose!"
    return "It's a tie!"


def parse_move(raw: str) -> Move:
    token = raw.strip().lower()
    aliases: dict[str, Move] = {
        "r": "rock",
        "rock": "rock",
        "p": "paper",
        "paper": "paper",
        "s": "scissors",
        "scissors": "scissors",
    }
    if token not in aliases:
        raise ValueError("Choose rock, paper, or scissors.")
    return aliases[token]


def play_round(
    player_move: Move,
    wins: int = 0,
    losses: int = 0,
    ties: int = 0,
) -> dict[str, Any]:
    computer_move = random_computer_move()
    outcome = judge_round(player_move, computer_move)

    if outcome == "win":
        wins += 1
    elif outcome == "lose":
        losses += 1
    else:
        ties += 1

    return {
        "player_move": player_move,
        "player_label": DISPLAY[player_move],
        "computer_move": computer_move,
        "computer_label": DISPLAY[computer_move],
        "outcome": outcome,
        "message": outcome_message(outcome),
        "wins": wins,
        "losses": losses,
        "ties": ties,
    }


def empty_score() -> dict[str, int]:
    return {"wins": 0, "losses": 0, "ties": 0}

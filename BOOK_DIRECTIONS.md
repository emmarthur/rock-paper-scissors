# Book directions — Rock Paper Scissors

**Catalog #501** · Al Sweigart, *The Big Book of Small Python Projects*, **Project #59** — Rock Paper Scissors

- Packt / Invent with Python: [project59.html](https://inventwithpython.com/bigbookpython/project59.html)
- Upstream: [rockpaperscissors.py](https://github.com/asweigart/the-big-book-of-small-python-projects/blob/main/rockpaperscissors.py)
- Local reference: [`reference/rockpaperscissors.py`](./reference/rockpaperscissors.py)
- Shared logic: [`rps_core.py`](./rps_core.py)

## What the book asks you to build

A looped terminal game:

1. Track **wins**, **losses**, and **ties**.
2. Accept **R / P / S** (or quit with **Q**).
3. Pick a random computer move (1–3 → rock, paper, scissors).
4. Pause with a **1… 2… 3…** countdown before revealing the computer move.
5. Apply standard rules and print win / lose / tie.

## Web version (`web/` — FastAPI, port **3020**)

| Book step | Web equivalent |
|-----------|----------------|
| Score counters | Session score in browser; `POST /api/reset` |
| Player move R/P/S | Rock / Paper / Scissors buttons |
| Random opponent | `rps_core.random_computer_move` in `POST /api/play` |
| Countdown suspense | Client-side delays in `app.js` before reveal |
| Win/loss/tie logic | `rps_core.judge_round` / `play_round` |

CLI: [`reference/run_cli.py`](./reference/run_cli.py)

"""
FastAPI app — Rock, Paper, Scissors vs the computer.

Run: uvicorn main:app --reload --port 3020
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

_DEMO_ROOT = Path(__file__).resolve().parent.parent
if str(_DEMO_ROOT) not in sys.path:
    sys.path.insert(0, str(_DEMO_ROOT))

from rps_core import empty_score, play_round  # noqa: E402

app = FastAPI(title="Rock Paper Scissors")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")


class PlayRequest(BaseModel):
    move: Literal["rock", "paper", "scissors"]
    wins: int = Field(0, ge=0)
    losses: int = Field(0, ge=0)
    ties: int = Field(0, ge=0)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html")


@app.get("/help", response_class=HTMLResponse)
async def help_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "help.html")


@app.post("/api/reset")
async def api_reset() -> JSONResponse:
    return JSONResponse(empty_score())


@app.post("/api/play")
async def api_play(body: PlayRequest) -> JSONResponse:
    try:
        result = play_round(body.move, body.wins, body.losses, body.ties)
        return JSONResponse(result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

# Rock Paper Scissors (catalog #501)

Al Sweigart — *The Big Book of Small Python Projects*, Project #59.

| Artifact | Path |
|----------|------|
| Book steps | [`BOOK_DIRECTIONS.md`](./BOOK_DIRECTIONS.md) |
| Upstream script | [`reference/rockpaperscissors.py`](./reference/rockpaperscissors.py) |
| CLI | [`reference/run_cli.py`](./reference/run_cli.py) |
| Shared logic | [`rps_core.py`](./rps_core.py) |
| Web (FastAPI) | [`web/`](./web/) — port **3020** |

## Run the web demo

```powershell
Set-Location "c:\Users\emmak\Desktop\Content\CodingProjects\PortProjects\demos\rock-paper-scissors\web"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 3020
```

Open [http://127.0.0.1:3020/](http://127.0.0.1:3020/).

## Run the CLI

```powershell
Set-Location "c:\Users\emmak\Desktop\Content\CodingProjects\PortProjects\demos\rock-paper-scissors"
pip install -r web/requirements.txt
python reference\run_cli.py
```

Portfolio wiring: [`PORTFOLIO_INTEGRATION.md`](./PORTFOLIO_INTEGRATION.md).

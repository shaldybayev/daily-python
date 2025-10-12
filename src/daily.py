from datetime import datetime
from pathlib import Path

LOG = Path(__file__).resolve().parents[1] / "log.txt"
LOG.parent.mkdir(parents=True, exist_ok=True)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG, "a", encoding="utf-8") as f:
    f.write(f"{now} — practiced Python today\n")

print("✅ Logged today's practice!")

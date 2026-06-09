import json
from pathlib import Path

sessions = [
    "session_01",
    "session_02",
    "session_03"
]

all_results = []

for session in sessions:

    path = Path(
        f"results/tables/{session}_signal_comparison.json"
    )

    if not path.exists():
        continue

    with open(path, "r") as f:
        data = json.load(f)

    all_results.extend(data)

output_path = Path(
    "results/tables/all_sessions_signal_comparison.json"
)

with open(output_path, "w") as f:
    json.dump(
        all_results,
        f,
        indent=4
    )

print(
    f"Saved to {output_path}"
)
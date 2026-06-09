import json
from pathlib import Path

sessions = [
    "session_01",
    "session_02",
    "session_03"
]

all_results = []

for session in sessions:
    path = Path(f"results/tables/{session}_delta_offset.json")

    if not path.exists():
        print(f"Missing file: {path}")
        continue

    with open(path, "r") as f:
        data = json.load(f)

    for row in data:
        all_results.append(row)

for row in all_results:
    print(row)

output_path = Path("results/tables/all_sessions_delta_offset.json")

with open(output_path, "w") as f:
    json.dump(all_results, f, indent=4)

print(f"Saved combined results to {output_path}")
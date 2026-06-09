import json
from pathlib import Path
import numpy as np

summary = {}

# ======================
# Experiment 2
# ======================

signal_path = Path(
    "results/tables/all_sessions_signal_comparison.json"
)

if signal_path.exists():

    with open(signal_path) as f:
        signal_data = json.load(f)

    signal_scores = {}

    for row in signal_data:

        signal = row["signal_type"]

        signal_scores.setdefault(
            signal,
            []
        )

        signal_scores[signal].append(
            row["correlation_score"]
        )

    summary["signal_comparison"] = {}

    for signal, scores in signal_scores.items():

        summary["signal_comparison"][signal] = {
            "mean_correlation":
            float(np.mean(scores)),
            "std":
            float(np.std(scores))
        }

# ======================
# Save
# ======================

output = Path(
    "results/tables/experiment_summary.json"
)

with open(output, "w") as f:
    json.dump(
        summary,
        f,
        indent=4
    )

print(summary)
print(f"Saved to {output}")
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import json
import numpy as np

from src.evaluation.evaluate_3d import bone_length_variance

session = "session_02"

pose3d = np.load(f"data/processed/pose3d/{session}_pose3d.npy")

score = bone_length_variance(pose3d)

result = {
    "session": session,
    "bone_length_variance": score
}

output_path = Path(f"results/tables/{session}_3d_metrics.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w") as f:
    json.dump(result, f, indent=4)

print(result)
print(f"Saved metrics to {output_path}")
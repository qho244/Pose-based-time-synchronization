import json
from pathlib import Path

session = "session_02"

sync_path = Path(f"results/tables/{session}_sync_metrics.json")
pose3d_path = Path(f"results/tables/{session}_3d_metrics.json")

with open(sync_path, "r") as f:
    sync_data = json.load(f)

with open(pose3d_path, "r") as f:
    pose3d_data = json.load(f)

result = {
    "session": session,
    "estimated_offset_frames": sync_data["estimated_offset_frames"],
    "estimated_offset_ms": sync_data["estimated_offset_ms"],
    "correlation_score": sync_data["correlation_score"],
    "bone_length_variance": pose3d_data["bone_length_variance"]
}

output_path = Path(f"results/tables/{session}_summary.json")

with open(output_path, "w") as f:
    json.dump(result, f, indent=4)

print(result)
print(f"Saved summary to {output_path}")
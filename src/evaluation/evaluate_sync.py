import json
from pathlib import Path
import numpy as np


def frames_to_ms(offset_frames: int, fps: int = 30) -> float:
    return abs(offset_frames) / fps * 1000


def evaluate_sync(offset_file: str, session: str, output_path: str, fps: int = 30):
    offset_data = np.load(offset_file, allow_pickle=True).item()

    offset_frames = offset_data["estimated_offset_frames"]
    correlation_score = offset_data["correlation_score"]
    offset_ms = frames_to_ms(offset_frames, fps)

    result = {
        "session": session,
        "estimated_offset_frames": int(offset_frames),
        "estimated_offset_ms": float(offset_ms),
        "correlation_score": float(correlation_score),
        "fps": fps
    }

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print(result)
    print(f"Saved sync metrics to {output_path}")

    return result
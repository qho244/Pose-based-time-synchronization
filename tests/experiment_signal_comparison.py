import sys
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.motion_signal.compute_signal import (
    compute_velocity_signal,
    compute_energy_signal,
    compute_selected_joint_signal
)
from src.motion_signal.filters import moving_average, normalize_signal
from src.synchronization.estimate_offset import estimate_offset


def prepare_signal(signal):
    signal = moving_average(signal, window_size=5)
    signal = normalize_signal(signal)
    signal = np.nan_to_num(signal, nan=0.0)
    return signal


def run_experiment(session="session_02"):
    cam1_kp = np.load(f"data/processed/keypoints/{session}_cam1_keypoints.npy")
    cam2_kp = np.load(f"data/processed/keypoints/{session}_cam2_keypoints.npy")

    signal_methods = {
        "velocity": compute_velocity_signal,
        "energy": compute_energy_signal,
        "selected_joint": compute_selected_joint_signal
    }

    results = []

    for name, func in signal_methods.items():
        signal1 = prepare_signal(func(cam1_kp))
        signal2 = prepare_signal(func(cam2_kp))

        offset, score = estimate_offset(
            signal1,
            signal2,
            max_lag=80
        )

        result = {
            "session": session,
            "signal_type": name,
            "estimated_offset_frames": int(offset),
            "correlation_score": float(score)
        }

        results.append(result)
        print(result)

    output_dir = Path("results/tables")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"{session}_signal_comparison.json"

    with open(json_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Saved signal comparison to {json_path}")

    fig_dir = Path("results/figures")
    fig_dir.mkdir(parents=True, exist_ok=True)

    signal_names = [r["signal_type"] for r in results]
    scores = [r["correlation_score"] for r in results]

    plt.figure(figsize=(8, 5))
    plt.bar(signal_names, scores)
    plt.title(
        f"Motion Signal Comparison - {session}"
    )
    plt.xlabel("Signal Type")
    plt.ylabel("Correlation Score")
    plt.grid(axis="y")
    plt.tight_layout()

    fig_path = fig_dir / f"{session}_signal_comparison.png"
    plt.savefig(fig_path)
    plt.show()

    print(f"Saved plot to {fig_path}")


if __name__ == "__main__":
    run_experiment("session_01")
    run_experiment("session_02")
    run_experiment("session_03")
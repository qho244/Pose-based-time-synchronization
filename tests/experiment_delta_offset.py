import sys
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.synchronization.align_frames import align_keypoints
from src.reconstruction.triangulation import triangulate_sequence
from src.reconstruction.camera_model import create_default_camera_matrices

from src.evaluation.evaluate_3d import (
    bone_length_variance,
    temporal_smoothness_error
)


def run_experiment(session="session_02"):

    cam1 = np.load(
        f"data/processed/keypoints/{session}_cam1_keypoints.npy"
    )

    cam2 = np.load(
        f"data/processed/keypoints/{session}_cam2_keypoints.npy"
    )

    offset_data = np.load(
        f"data/processed/aligned/{session}_offset.npy",
        allow_pickle=True
    ).item()

    estimated_offset = offset_data["estimated_offset_frames"]

    deltas = [
        -30,
        -20,
        -10,
        0,
        10,
        20,
        30
    ]

    P1, P2 = create_default_camera_matrices()

    results = []

    for delta in deltas:

        offset = estimated_offset + delta

        aligned1, aligned2 = align_keypoints(
            cam1,
            cam2,
            offset
        )

        if len(aligned1) < 10 or len(aligned2) < 10:
            print(f"Skip offset {offset}: not enough frames")
            continue

        pose3d = triangulate_sequence(
            aligned1,
            aligned2,
            P1,
            P2
        )

        variance = bone_length_variance(
            pose3d
        )

        smoothness = temporal_smoothness_error(
            pose3d
        )

        row = {
            "offset": offset,
            "delta": delta,
            "bone_length_variance": float(
                variance
            ),
            "temporal_smoothness_error": float(
                smoothness
            )
        }

        results.append(row)

        print(row)

    Path(
        "results/tables"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        f"results/tables/{session}_delta_offset.json",
        "w"
    ) as f:

        json.dump(
            results,
            f,
            indent=4
        )

    # Plot 1

    x = [
        r["delta"]
        for r in results
    ]

    y = [
        r["bone_length_variance"]
        for r in results
    ]

    plt.figure(
        figsize=(8,5)
    )

    plt.plot(
        x,
        y,
        marker="o"
    )

    plt.axvline(
        0,
        linestyle="--"
    )

    plt.title(
        f"{session}: Delta Offset vs Bone Variance"
    )

    plt.xlabel(
        "Delta from Estimated Offset"
    )

    plt.ylabel(
        "Bone Length Variance"
    )

    plt.grid(True)

    plt.savefig(
        f"results/figures/{session}_delta_offset_variance.png"
    )

    plt.show()

    # Plot 2

    y = [
        r["temporal_smoothness_error"]
        for r in results
    ]

    plt.figure(
        figsize=(8,5)
    )

    plt.plot(
        x,
        y,
        marker="o"
    )

    plt.axvline(
        0,
        linestyle="--"
    )

    plt.title(
        f"{session}: Delta Offset vs Temporal Smoothness"
    )

    plt.xlabel(
        "Delta from Estimated Offset"
    )

    plt.ylabel(
        "Temporal Smoothness Error"
    )

    plt.grid(True)

    plt.savefig(
        f"results/figures/{session}_delta_offset_smoothness.png"
    )

    plt.show()


if __name__ == "__main__":
    run_experiment("session_01")
    run_experiment("session_02")
    run_experiment("session_03")
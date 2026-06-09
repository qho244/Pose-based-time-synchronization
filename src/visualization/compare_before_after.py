import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def align_signal(signal: np.ndarray, offset: int) -> np.ndarray:
    """
    Align signal2 based on estimated offset.
    
    offset > 0: cam2 is delayed, remove first offset frames from cam2
    offset < 0: cam2 is ahead, remove last abs(offset) frames from cam2
    offset = 0: no shift
    """
    if offset > 0:
        return signal[offset:]

    if offset < 0:
        return signal[:offset]

    return signal


def compare_before_after(
    signal1_path: str,
    signal2_path: str,
    offset: int,
    output_path: str
):
    """
    Plot motion signals before and after synchronization.
    """
    signal1 = np.load(signal1_path)
    signal2 = np.load(signal2_path)

    signal2_aligned = align_signal(signal2, offset)

    min_len = min(len(signal1), len(signal2_aligned))
    signal1_after = signal1[:min_len]
    signal2_after = signal2_aligned[:min_len]

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(signal1, label="Camera 1")
    plt.plot(signal2, label="Camera 2")
    plt.title("Motion Signals Before Synchronization")
    plt.xlabel("Frame")
    plt.ylabel("Normalized Motion")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(signal1_after, label="Camera 1")
    plt.plot(signal2_after, label="Camera 2 Aligned")
    plt.title(f"Motion Signals After Synchronization (Offset = {offset} frames)")
    plt.xlabel("Frame")
    plt.ylabel("Normalized Motion")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

    print(f"Saved before-after comparison: {output_path}")


if __name__ == "__main__":
    compare_before_after(
        "data/processed/signals/session_03_cam1_signal.npy",
        "data/processed/signals/session_03_cam2_signal.npy",
        offset=0,
        output_path="results/figures/session_03_before_after.png"
    )
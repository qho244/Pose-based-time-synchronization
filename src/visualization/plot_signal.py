import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def plot_signals(signal1_path: str, signal2_path: str, output_path: str):
    signal1 = np.load(signal1_path)
    signal2 = np.load(signal2_path)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 5))
    plt.plot(signal1, label="Camera 1")
    plt.plot(signal2, label="Camera 2")
    plt.title(f"Motion Signals")
    plt.xlabel("Frame")
    plt.ylabel("Normalized Motion")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

    print(f"Saved signal plot: {output_path}")


if __name__ == "__main__":
    plot_signals(
        "data/processed/signals/session_01_cam1_signal.npy",
        "data/processed/signals/session_01_cam2_signal.npy",
        "results/figures/session_01_signals.png"
    )
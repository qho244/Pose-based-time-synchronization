import numpy as np
from pathlib import Path


def estimate_offset(signal1: np.ndarray, signal2: np.ndarray, max_lag: int = 60):
    signal1 = np.nan_to_num(signal1)
    signal2 = np.nan_to_num(signal2)

    best_lag = 0
    best_score = -np.inf

    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            s1 = signal1[-lag:]
            s2 = signal2[:len(s1)]
        elif lag > 0:
            s1 = signal1[:-lag]
            s2 = signal2[lag:]
        else:
            min_len = min(len(signal1), len(signal2))
            s1 = signal1[:min_len]
            s2 = signal2[:min_len]

        min_len = min(len(s1), len(s2))
        s1 = s1[:min_len]
        s2 = s2[:min_len]

        if len(s1) < 2:
            continue

        score = np.corrcoef(s1, s2)[0, 1]

        if np.isnan(score):
            continue

        if score > best_score:
            best_score = score
            best_lag = lag

    return best_lag, best_score


def estimate_offset_from_files(signal1_path: str, signal2_path: str, output_path: str):
    signal1 = np.load(signal1_path)
    signal2 = np.load(signal2_path)

    offset, score = estimate_offset(signal1, signal2)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    result = {
        "estimated_offset_frames": int(offset),
        "correlation_score": float(score)
    }

    np.save(output_path, result)

    print("Estimated offset:", offset)
    print("Correlation score:", score)
    print(f"Saved result: {output_path}")

    return result


if __name__ == "__main__":
    estimate_offset_from_files(
        "data/processed/signals/session_01_cam1_signal.npy",
        "data/processed/signals/session_01_cam2_signal.npy",
        "data/processed/aligned/session_01_offset.npy"
    )
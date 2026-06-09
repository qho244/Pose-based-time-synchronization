import numpy as np
from pathlib import Path
from src.motion_signal.filters import moving_average, normalize_signal

def safe_nanmean(array, axis=1):
    valid_count = np.sum(~np.isnan(array), axis=axis)
    safe_array = np.nan_to_num(array, nan=0.0)

    summed = np.sum(safe_array, axis=axis)

    result = np.divide(
        summed,
        valid_count,
        out=np.zeros_like(summed, dtype=float),
        where=valid_count != 0
    )

    return result

def compute_velocity_signal(keypoints: np.ndarray):
    velocity = np.diff(keypoints, axis=0)
    speed = np.linalg.norm(velocity, axis=2)
    signal = safe_nanmean(speed, axis=1)
    signal = np.nan_to_num(signal, nan=0.0)
    return signal


def compute_energy_signal(keypoints: np.ndarray):
    velocity = np.diff(keypoints, axis=0)
    speed_squared = np.sum(velocity ** 2, axis=2)
    signal = safe_nanmean(speed_squared, axis=1)
    signal = np.nan_to_num(signal, nan=0.0)
    return signal


def compute_selected_joint_signal(keypoints: np.ndarray, joint_indices=None):
    if joint_indices is None:
        joint_indices = [15, 16, 27, 28]  # wrists + ankles in MediaPipe

    selected = keypoints[:, joint_indices, :]
    velocity = np.diff(selected, axis=0)
    speed = np.linalg.norm(velocity, axis=2)
    signal = safe_nanmean(speed, axis=1)
    signal = np.nan_to_num(signal, nan=0.0)
    return signal


def save_motion_signal(
    keypoints_path: str,
    output_path: str,
    signal_type: str = "velocity",
    smoothing: bool = True,
    normalize: bool = True
):
    keypoints_path = Path(keypoints_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    keypoints = np.load(keypoints_path)

    if signal_type == "velocity":
        signal = compute_velocity_signal(keypoints)
    elif signal_type == "energy":
        signal = compute_energy_signal(keypoints)
    elif signal_type == "selected_joint":
        signal = compute_selected_joint_signal(keypoints)
    else:
        raise ValueError(f"Unknown signal type: {signal_type}")

    if smoothing:
        signal = moving_average(signal, window_size=5)

    if normalize:
        signal = normalize_signal(signal)

    np.save(output_path, signal)

    print(f"Saved motion signal: {output_path}")
    print(f"Shape: {signal.shape}")


if __name__ == "__main__":
    save_motion_signal(
        "data/processed/keypoints/session_01_cam1_keypoints.npy",
        "data/processed/signals/session_01_cam1_signal.npy",
        signal_type="velocity"
    )

    save_motion_signal(
        "data/processed/keypoints/session_01_cam2_keypoints.npy",
        "data/processed/signals/session_01_cam2_signal.npy",
        signal_type="velocity"
    )
    
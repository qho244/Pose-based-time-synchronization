import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import numpy as np

from src.motion_signal.compute_signal import (
    compute_velocity_signal,
    compute_energy_signal,
    compute_selected_joint_signal
)


def test_velocity_signal_stationary_pose():
    keypoints = np.zeros((10, 33, 2), dtype=np.float32)

    signal = compute_velocity_signal(keypoints)

    assert signal.shape == (9,)
    assert np.allclose(signal, 0)


def test_velocity_signal_linear_motion():
    keypoints = np.zeros((10, 33, 2), dtype=np.float32)

    for t in range(10):
        keypoints[t, :, 0] = t
        keypoints[t, :, 1] = t

    signal = compute_velocity_signal(keypoints)

    assert signal.shape == (9,)
    assert np.all(signal > 0)


def test_energy_signal_stationary_pose():
    keypoints = np.zeros((10, 33, 2), dtype=np.float32)

    signal = compute_energy_signal(keypoints)

    assert signal.shape == (9,)
    assert np.allclose(signal, 0)


def test_selected_joint_signal_shape():
    keypoints = np.zeros((10, 33, 2), dtype=np.float32)

    signal = compute_selected_joint_signal(keypoints)

    assert signal.shape == (9,)


def test_signal_with_nan_does_not_crash():
    keypoints = np.zeros((10, 33, 2), dtype=np.float32)
    keypoints[3, :, :] = np.nan

    signal = compute_velocity_signal(keypoints)

    assert signal.shape == (9,)
    assert not np.any(np.isinf(signal))
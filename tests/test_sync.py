import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import numpy as np

from src.synchronization.estimate_offset import estimate_offset
from src.synchronization.align_frames import align_keypoints


def test_estimate_offset_no_shift():
    signal1 = np.array([0, 1, 2, 3, 2, 1, 0], dtype=float)
    signal2 = signal1.copy()

    offset, score = estimate_offset(signal1, signal2, max_lag=3)

    assert offset == 0
    assert score > 0.99


def test_estimate_offset_with_shift():
    signal1 = np.array([0, 0, 1, 3, 1, 0, 0], dtype=float)
    signal2 = np.array([0, 0, 0, 0, 1, 3, 1, 0, 0], dtype=float)

    offset, score = estimate_offset(signal1, signal2, max_lag=5)

    assert abs(offset) > 0
    assert score > 0.8


def test_align_keypoints_no_offset():
    kp1 = np.zeros((10, 33, 2), dtype=np.float32)
    kp2 = np.ones((10, 33, 2), dtype=np.float32)

    a1, a2 = align_keypoints(kp1, kp2, offset=0)

    assert a1.shape == (10, 33, 2)
    assert a2.shape == (10, 33, 2)


def test_align_keypoints_positive_offset():
    kp1 = np.zeros((10, 33, 2), dtype=np.float32)
    kp2 = np.ones((10, 33, 2), dtype=np.float32)

    a1, a2 = align_keypoints(kp1, kp2, offset=3)

    assert a1.shape == (7, 33, 2)
    assert a2.shape == (7, 33, 2)


def test_align_keypoints_negative_offset():
    kp1 = np.zeros((10, 33, 2), dtype=np.float32)
    kp2 = np.ones((10, 33, 2), dtype=np.float32)

    a1, a2 = align_keypoints(kp1, kp2, offset=-3)

    assert a1.shape == (7, 33, 2)
    assert a2.shape == (7, 33, 2)
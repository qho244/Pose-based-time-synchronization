import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import numpy as np

from src.reconstruction.triangulation import triangulate_sequence
from src.reconstruction.camera_model import create_default_camera_matrices


def test_triangulation_output_shape():
    n_frames = 5
    n_joints = 33

    cam1 = np.random.rand(n_frames, n_joints, 2).astype(np.float32)
    cam2 = np.random.rand(n_frames, n_joints, 2).astype(np.float32)

    P1, P2 = create_default_camera_matrices()

    pose3d = triangulate_sequence(cam1, cam2, P1, P2)

    assert pose3d.shape == (n_frames, n_joints, 3)


def test_triangulation_no_inf():
    cam1 = np.random.rand(3, 33, 2).astype(np.float32)
    cam2 = np.random.rand(3, 33, 2).astype(np.float32)

    P1, P2 = create_default_camera_matrices()

    pose3d = triangulate_sequence(cam1, cam2, P1, P2)

    assert not np.any(np.isinf(pose3d))


def test_triangulation_single_frame():
    cam1 = np.random.rand(1, 33, 2).astype(np.float32)
    cam2 = np.random.rand(1, 33, 2).astype(np.float32)

    P1, P2 = create_default_camera_matrices()

    pose3d = triangulate_sequence(cam1, cam2, P1, P2)

    assert pose3d.shape == (1, 33, 3)
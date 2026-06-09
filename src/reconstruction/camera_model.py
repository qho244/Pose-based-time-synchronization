import numpy as np


def create_default_camera_matrices(
    focal_length: float = 1000,
    cx: float = 320,
    cy: float = 240,
    baseline: float = 0.5
):
    K = np.array([
        [focal_length, 0, cx],
        [0, focal_length, cy],
        [0, 0, 1]
    ], dtype=np.float32)

    R1 = np.eye(3, dtype=np.float32)
    t1 = np.array([[0], [0], [0]], dtype=np.float32)

    R2 = np.eye(3, dtype=np.float32)
    t2 = np.array([[-baseline], [0], [0]], dtype=np.float32)

    P1 = K @ np.hstack((R1, t1))
    P2 = K @ np.hstack((R2, t2))

    return P1, P2
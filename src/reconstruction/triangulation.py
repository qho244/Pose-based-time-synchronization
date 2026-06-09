import cv2
import numpy as np
from pathlib import Path
from src.reconstruction.camera_model import create_default_camera_matrices


def triangulate_frame(kp1: np.ndarray, kp2: np.ndarray, P1: np.ndarray, P2: np.ndarray):
    points_3d = np.full((kp1.shape[0], 3), np.nan, dtype=np.float32)

    valid_mask = ~np.isnan(kp1).any(axis=1) & ~np.isnan(kp2).any(axis=1)

    if valid_mask.sum() == 0:
        return points_3d

    pts1 = kp1[valid_mask].T.astype(np.float32)
    pts2 = kp2[valid_mask].T.astype(np.float32)

    points_4d = cv2.triangulatePoints(P1, P2, pts1, pts2)
    points = (points_4d[:3] / points_4d[3]).T

    points_3d[valid_mask] = points

    return points_3d


def triangulate_sequence(kp1_seq: np.ndarray, kp2_seq: np.ndarray, P1: np.ndarray, P2: np.ndarray):
    min_len = min(len(kp1_seq), len(kp2_seq))
    kp1_seq = kp1_seq[:min_len]
    kp2_seq = kp2_seq[:min_len]

    pose3d_sequence = []

    for i in range(min_len):
        pose3d = triangulate_frame(kp1_seq[i], kp2_seq[i], P1, P2)
        pose3d_sequence.append(pose3d)

    return np.array(pose3d_sequence, dtype=np.float32)


def triangulate_from_files(kp1_path: str, kp2_path: str, output_path: str):
    kp1 = np.load(kp1_path)
    kp2 = np.load(kp2_path)

    P1, P2 = create_default_camera_matrices()

    pose3d = triangulate_sequence(kp1, kp2, P1, P2)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    np.save(output_path, pose3d)

    print(f"Saved 3D pose: {output_path}")
    print("Shape:", pose3d.shape)


if __name__ == "__main__":
    triangulate_from_files(
        "data/processed/aligned/session_01_cam1_aligned.npy",
        "data/processed/aligned/session_01_cam2_aligned.npy",
        "data/processed/pose3d/session_01_pose3d.npy"
    )
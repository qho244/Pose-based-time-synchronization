import numpy as np
from pathlib import Path


def align_keypoints(kp1: np.ndarray, kp2: np.ndarray, offset: int):
    if offset > 0:
        kp1_aligned = kp1[:-offset]
        kp2_aligned = kp2[offset:]

    elif offset < 0:
        offset_abs = abs(offset)
        kp1_aligned = kp1[offset_abs:]
        kp2_aligned = kp2[:-offset_abs]

    else:
        min_len = min(len(kp1), len(kp2))
        kp1_aligned = kp1[:min_len]
        kp2_aligned = kp2[:min_len]

    min_len = min(len(kp1_aligned), len(kp2_aligned))
    return kp1_aligned[:min_len], kp2_aligned[:min_len]


def align_keypoints_from_files(
    kp1_path: str,
    kp2_path: str,
    offset: int,
    output1_path: str,
    output2_path: str
):
    kp1 = np.load(kp1_path)
    kp2 = np.load(kp2_path)

    kp1_aligned, kp2_aligned = align_keypoints(kp1, kp2, offset)

    output1_path = Path(output1_path)
    output2_path = Path(output2_path)

    output1_path.parent.mkdir(parents=True, exist_ok=True)
    output2_path.parent.mkdir(parents=True, exist_ok=True)

    np.save(output1_path, kp1_aligned)
    np.save(output2_path, kp2_aligned)

    print(f"Saved aligned cam1: {output1_path}")
    print(f"Saved aligned cam2: {output2_path}")
    print("Aligned shape:", kp1_aligned.shape, kp2_aligned.shape)


if __name__ == "__main__":
    align_keypoints_from_files(
        "data/processed/keypoints/session_01_cam1_keypoints.npy",
        "data/processed/keypoints/session_01_cam2_keypoints.npy",
        offset=0,
        output1_path="data/processed/aligned/session_01_cam1_aligned.npy",
        output2_path="data/processed/aligned/session_01_cam2_aligned.npy"
    )
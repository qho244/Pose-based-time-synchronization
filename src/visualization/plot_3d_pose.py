import numpy as np
import matplotlib.pyplot as plt


POSE_CONNECTIONS = [
    (11, 12),
    (11, 13),
    (13, 15),
    (12, 14),
    (14, 16),
    (11, 23),
    (12, 24),
    (23, 24),
    (23, 25),
    (25, 27),
    (24, 26),
    (26, 28)
]


def plot_3d_pose(pose3d_path: str, frame_idx: int = 0):
    pose3d_seq = np.load(pose3d_path)
    pose = pose3d_seq[frame_idx]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    valid = ~np.isnan(pose).any(axis=1)
    ax.scatter(pose[valid, 0], pose[valid, 1], pose[valid, 2])

    for start, end in POSE_CONNECTIONS:
        if valid[start] and valid[end]:
            xs = [pose[start, 0], pose[end, 0]]
            ys = [pose[start, 1], pose[end, 1]]
            zs = [pose[start, 2], pose[end, 2]]
            ax.plot(xs, ys, zs)

    ax.set_title(f"3D Pose - Frame {frame_idx}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_3d_pose(
        "data/processed/pose3d/session_01_pose3d.npy",
        frame_idx=0
    )
import sys

from src.pose_extraction.extract_pose import extract_pose_from_video
from src.motion_signal.compute_signal import save_motion_signal
from src.synchronization.estimate_offset import estimate_offset_from_files
from src.synchronization.align_frames import align_keypoints_from_files
from src.reconstruction.triangulation import triangulate_from_files
from src.visualization.plot_signal import plot_signals
from src.visualization.plot_3d_pose import plot_3d_pose
from src.visualization.compare_before_after import compare_before_after


def main():
    session = sys.argv[1] if len(sys.argv) > 1 else "session_02"

    cam1_video = f"data/raw/{session}/cam1.mp4"
    cam2_video = f"data/raw/{session}/cam2.mp4"

    cam1_kp = f"data/processed/keypoints/{session}_cam1_keypoints.npy"
    cam2_kp = f"data/processed/keypoints/{session}_cam2_keypoints.npy"

    cam1_signal = f"data/processed/signals/{session}_cam1_signal.npy"
    cam2_signal = f"data/processed/signals/{session}_cam2_signal.npy"

    offset_file = f"data/processed/aligned/{session}_offset.npy"

    cam1_aligned = f"data/processed/aligned/{session}_cam1_aligned.npy"
    cam2_aligned = f"data/processed/aligned/{session}_cam2_aligned.npy"

    pose3d_output = f"data/processed/pose3d/{session}_pose3d.npy"

    signal_plot = f"results/figures/{session}_signals.png"

    print("Step 1: Extracting 2D pose...")
    extract_pose_from_video(cam1_video, cam1_kp)
    extract_pose_from_video(cam2_video, cam2_kp)

    print("Step 2: Computing motion signals...")
    save_motion_signal(cam1_kp, cam1_signal, signal_type="selected_joint")
    save_motion_signal(cam2_kp, cam2_signal, signal_type="selected_joint")

    print("Step 3: Estimating time offset...")
    result = estimate_offset_from_files(cam1_signal, cam2_signal, offset_file)
    offset = result["estimated_offset_frames"]

    print("Step 4: Aligning frames...")
    align_keypoints_from_files(
        cam1_kp,
        cam2_kp,
        offset,
        cam1_aligned,
        cam2_aligned
    )

    print("Step 5: Triangulating 3D pose...")
    triangulate_from_files(
        cam1_aligned,
        cam2_aligned,
        pose3d_output
    )

    print("Step 6: Plotting signals...")
    plot_signals(cam1_signal, cam2_signal, signal_plot)
    
    print("Step 6.1: Comparing signals before and after sync...")
    compare_before_after(
        cam1_signal,
        cam2_signal,
        offset,
        f"results/figures/{session}_before_after.png"
    )

    print("Step 7: Plotting 3D pose...")
    plot_3d_pose(pose3d_output, frame_idx=0)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
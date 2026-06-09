import cv2
import numpy as np
import mediapipe as mp
from pathlib import Path


mp_pose = mp.solutions.pose


def extract_pose_from_video(video_path: str, output_path: str):
    video_path = Path(video_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {video_path}")

    pose = mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    all_keypoints = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb_frame)

        if result.pose_landmarks:
            frame_keypoints = []

            for lm in result.pose_landmarks.landmark:
                x = lm.x * w
                y = lm.y * h
                frame_keypoints.append([x, y])

            all_keypoints.append(frame_keypoints)

        else:
            all_keypoints.append([[np.nan, np.nan] for _ in range(33)])

    cap.release()
    pose.close()

    all_keypoints = np.array(all_keypoints, dtype=np.float32)
    np.save(output_path, all_keypoints)

    print(f"Saved keypoints: {output_path}")
    print(f"Shape: {all_keypoints.shape}")


if __name__ == "__main__":
    extract_pose_from_video(
        "data/raw/session_01/cam1.mp4",
        "data/processed/keypoints/session_01_cam1_keypoints.npy"
    )

    extract_pose_from_video(
        "data/raw/session_01/cam2.mp4",
        "data/processed/keypoints/session_01_cam2_keypoints.npy"
    )
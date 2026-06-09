# Pose-based Time Synchronization for Low-Cost Multi-View Motion Capture

## Overview

This project investigates a pose-based temporal synchronization method for low-cost multi-view motion capture systems.

The main objective is to estimate and compensate for temporal offsets between unsynchronized cameras using motion signals extracted from 2D human poses, thereby improving the quality of 3D pose reconstruction.

The project focuses on:

- 2D pose extraction from monocular videos
- Motion signal generation from pose sequences
- Temporal offset estimation between multiple views
- Frame alignment
- 3D pose reconstruction through triangulation
- Quantitative evaluation of synchronization quality

---

## Research Motivation

Existing synchronization methods have several limitations:

### Pose-based Synchronization
- Mostly evaluates time delay estimation only.
- Limited analysis of impact on 3D reconstruction.

### Event-based Synchronization
- Requires observable synchronization events.
- Often ignores final 3D pose quality.

### Coded-Light Synchronization
- Requires additional hardware.
- Not suitable for low-cost systems.

This project aims to investigate whether more stable motion signals extracted from human pose can improve synchronization accuracy and consequently improve 3D pose reconstruction quality.

---

## Pipeline

```text
Video (Camera 1)
                \
                 \
                  → 2D Pose Extraction
                 /
Video (Camera 2)
                /

        ↓

Motion Signal Generation

        ↓

Time Offset Estimation

        ↓

Frame Alignment

        ↓

3D Triangulation

        ↓

Visualization & Evaluation
```

---

## Project Structure

```text
Pose-based-time-synchronization/

├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── results/
│   ├── figures/
│   └── tables/
│
├── src/
│   ├── pose_extraction/
│   ├── motion_signal/
│   ├── synchronization/
│   ├── reconstruction/
│   ├── visualization/
│   ├── evaluation/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── config.yaml
└── README.md
```

---

## Dataset

The dataset is collected using two smartphones:

- iPhone 15 Plus
- iPhone 12 Pro Max

Video settings:

- Resolution: 1920 × 1080
- FPS: 30
- Lens: 1×
- HDR: OFF

Example actions:

- Clap
- Hand wave
- Walk in place
- Sit-stand
- Jump

Dataset structure:

```text
data/raw/

session_01/
├── cam1.mp4
└── cam2.mp4

session_02/
├── cam1.mp4
└── cam2.mp4
```

---

## Installation

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Pipeline

Execute the complete pipeline:

```bash
python -m src.main
```

Pipeline steps:

1. Pose Extraction
2. Motion Signal Generation
3. Time Offset Estimation
4. Frame Alignment
5. 3D Reconstruction
6. Visualization
7. Evaluation

---

## Evaluation Metrics

### Synchronization Metrics

- Estimated Offset (frames)
- Estimated Offset (milliseconds)
- Correlation Score

Example:

```json
{
  "estimated_offset_frames": 57,
  "estimated_offset_ms": 1900,
  "correlation_score": 0.3846
}
```

### 3D Reconstruction Metrics

- Bone Length Variance

Example:

```json
{
  "bone_length_variance": 1.7586
}
```

---

## Test

Run all tests:

```bash
pytest tests/
```

Current tests:
- test_eval.py
- test_sync_eval.py
- collect_results.py
- test_motion_signal.py
- test_sync.py
- test_triangulation.py

---

## Outputs

Generated figures:

```text
results/figures/

session_02_signals.png

session_02_before_after.png

session_02_pose3d.png
```

Generated metrics:

```text
results/tables/

session_02_sync_metrics.json

session_02_3d_metrics.json

session_02_summary.json
```

---

## Team

Project Topic:

**Pose-based Time Synchronization for Low-Cost Multi-View Motion Capture**

Contributors:

- Hồ Minh Quốc 2353024
- Trịnh Lương Nhất Quân 2353017
- Phạm Anh Quân 2353011
- Bùi Thanh Tuyền

---

## Future Work

- Camera calibration using checkerboard
- Improved motion signal design
- Robust synchronization under occlusion
- Evaluation on larger datasets
- Multi-camera (>2 views) synchronization

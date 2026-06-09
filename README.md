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
- Experimental analysis

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

## Pipeline Structure

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

session_03/
├── cam1.mp4
└── cam2.mp4
```

---
## Pipeline

The synchronization pipeline performs the following steps:

### Step 1 — 2D Pose Extraction

MediaPipe Pose is used to extract 33 body keypoints from each frame.

Output:

```text
data/processed/keypoints/
```

---

### Step 2 — Motion Signal Generation

Three motion signal types are supported:

* velocity
* energy
* selected_joint

Signals are optionally smoothed and normalized.

Output:

```text
data/processed/signals/
```

---

### Step 3 — Temporal Offset Estimation

Cross-correlation is applied to estimate frame offsets between camera streams.

Output:

```text
data/processed/aligned/*_offset.npy
```

---

### Step 4 — Frame Alignment

The estimated offset is used to synchronize the two keypoint sequences.

Output:

```text
data/processed/aligned/
```

---

### Step 5 — 3D Pose Reconstruction

Aligned 2D keypoints are reconstructed into 3D poses using triangulation.

Output:

```text
data/processed/pose3d/
```

---

### Step 6 — Visualization

Generated visualizations include:

* Motion signals
* Before/after synchronization comparison
* 3D pose visualization

Output:

```text
results/figures/
```

---

## Evaluation Metrics

### Synchronization

* Estimated Offset
* Correlation Score

### 3D Reconstruction

* Bone Length Variance
* Temporal Smoothness Error

---

## Experiments

### Experiment 1 — Delta Offset Analysis

Artificial temporal offsets are introduced around the estimated offset.

Purpose:

* Analyze synchronization sensitivity
* Observe effects on 3D reconstruction quality

Output:

```text
results/tables/*_delta_offset.json
```

---

### Experiment 2 — Motion Signal Comparison

Comparison between:

* Velocity Signal
* Energy Signal
* Selected Joint Signal

Metric:

* Correlation Score

Output:

```text
results/tables/*_signal_comparison.json
```

---

## Installation

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Run Pipeline Only

Execute a single session pipeline:

```bash
python -m src.main session_01
```

or

```bash
python -m src.main session_02
```

or

```bash
python -m src.main session_03
```

This runs:

1. Pose Extraction
2. Motion Signal Generation
3. Offset Estimation
4. Frame Alignment
5. Triangulation
6. Visualization

---

### Run Full Project

Execute all sessions and experiments:

```bash
python -m src.run_all
```

This runs:

* All pipeline stages
* Experiment 1
* Experiment 2
* Result aggregation

Outputs are automatically saved into:

```text
results/figures/
results/tables/
```

---

## Dependencies

```text
numpy==1.26.4
opencv-python==4.10.0.84
mediapipe==0.10.14
matplotlib==3.9.2
pytest==9.0.3
PyYAML==6.0.2
```

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
### Institution

Vietnam National University, Ho Chi Minh City
Ho Chi Minh City University of Technology (HCMUT)
Faculty of Computer Science and Engineering

### Course

**Multidisciplinary Project**

Project Topic:

**Pose-based Time Synchronization for Low-Cost Multi-View Motion Capture**

Contributors:

- Hồ Minh Quốc 2353024
- Trịnh Lương Nhất Quân 2353017
- Phạm Anh Quân 2353011
- Bùi Thanh Tuyền

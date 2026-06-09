# POSE-BASED TIME SYNCHRONIZATION FOR LOW-COST MULTI-VIEW MOTION CAPTURE

## 1. Introduction

Motion capture (MoCap) systems are widely used in animation, virtual reality, sports analysis, healthcare, and human-computer interaction. Traditional motion capture systems often rely on specialized hardware and synchronized cameras, resulting in high deployment costs and complex setup procedures.

With the rapid development of computer vision and pose estimation techniques, low-cost multi-view motion capture systems based on consumer devices such as smartphones have become increasingly feasible. However, one major challenge in such systems is temporal synchronization between cameras. Even a small time offset can significantly affect the accuracy of 3D pose reconstruction.

This project investigates a pose-based temporal synchronization approach for low-cost multi-view motion capture systems. Instead of relying on dedicated synchronization hardware or coded light signals, synchronization is estimated directly from motion information extracted from human body poses.

---

## 2. Problem Statement

In a multi-view motion capture system, cameras often start recording at slightly different times, leading to temporal misalignment between video streams.

This temporal offset causes:

* Inconsistent observations across views
* Incorrect correspondence between frames
* Reduced accuracy of 3D reconstruction
* Increased instability in reconstructed poses

Existing approaches present several limitations:

### Pose-Based Synchronization

* Primarily focuses on estimating temporal delay.
* Limited evaluation of the impact on 3D pose reconstruction.

### Event-Based Synchronization

* Requires visible synchronization events.
* Not always applicable in natural recordings.

### Coded-Light Synchronization

* Requires additional hardware.
* Increases deployment cost.

Therefore, a software-based synchronization method suitable for low-cost systems remains an important research problem.

---

## 3. Objectives

The objectives of this project are:

### Main Objective

Develop a pose-based synchronization pipeline for low-cost multi-view motion capture systems and evaluate its impact on 3D pose reconstruction quality.

### Specific Objectives

* Extract 2D human poses from multi-view videos.
* Generate motion signals from pose sequences.
* Estimate temporal offsets between cameras.
* Align pose sequences based on estimated offsets.
* Reconstruct 3D poses using triangulation.
* Evaluate synchronization quality using quantitative metrics.
* Analyze the relationship between synchronization accuracy and 3D reconstruction quality.

---

## 4. Proposed Methodology

The proposed pipeline consists of the following stages:

### Stage 1: Video Acquisition

Videos are captured simultaneously using two smartphones positioned at different viewpoints.

Example devices:

* iPhone 15 Plus
* iPhone 12 Pro Max

Recorded actions include:

* Hand clapping
* Hand waving
* Walking
* Standing and sitting
* Jumping

---

### Stage 2: 2D Pose Extraction

Human body keypoints are extracted using MediaPipe Pose.

Output:

```text
cam1_keypoints.npy
cam2_keypoints.npy
```

Each frame contains:

* 33 body landmarks
* 2D coordinates (x, y)

---

### Stage 3: Motion Signal Generation

Motion signals are generated from pose trajectories.

Current implementation:

* Selected-joint motion signal
* Velocity-based representation

Selected joints:

* Left wrist
* Right wrist
* Left ankle
* Right ankle

The generated signal represents body movement intensity over time.

---

### Stage 4: Temporal Offset Estimation

Temporal offsets are estimated using cross-correlation between motion signals extracted from different cameras.

Output:

```text
estimated_offset_frames
correlation_score
```

---

### Stage 5: Frame Alignment

Pose sequences are temporally aligned according to the estimated offset.

Output:

```text
cam1_aligned.npy
cam2_aligned.npy
```

---

### Stage 6: 3D Reconstruction

Aligned 2D keypoints are reconstructed into 3D coordinates using triangulation.

Output:

```text
pose3d.npy
```

---

### Stage 7: Evaluation

Synchronization quality is evaluated using:

#### Synchronization Metrics

* Estimated Offset (frames)
* Estimated Offset (milliseconds)
* Correlation Score

#### 3D Reconstruction Metrics

* Bone Length Variance

Lower variance indicates more stable and physically consistent reconstructed poses.

---

## 5. System Architecture

```text
Videos
   ↓
Pose Extraction
   ↓
Motion Signal Generation
   ↓
Time Offset Estimation
   ↓
Frame Alignment
   ↓
3D Reconstruction
   ↓
Visualization
   ↓
Evaluation
```

---

## 6. Tools and Technologies

### Programming Language

* Python

### Libraries

* MediaPipe
* OpenCV
* NumPy
* Matplotlib
* PyTest

### Development Environment

* Visual Studio Code
* Git
* GitHub

---

## 7. Expected Outcomes

The project is expected to produce:

### Software

* Complete synchronization pipeline
* Motion signal generation module
* Temporal alignment module
* 3D reconstruction module
* Visualization and evaluation tools

### Experimental Results

* Synchronization metrics
* 3D reconstruction metrics
* Comparative analysis between synchronized and unsynchronized sequences

### Documentation

* Source code repository
* Technical report
* Experimental results
* Final presentation slides

---

## 8. Implementation Plan

### Week 1

* Dataset collection
* Pose extraction
* Motion signal generation
* Basic 3D reconstruction

### Week 2

* Offset estimation
* Frame alignment
* Visualization
* Evaluation metrics

### Week 3

* Experimental evaluation
* Multiple action datasets
* Result analysis

### Week 4

* Final report writing
* Presentation preparation
* Repository refinement

---

## 9. Expected Contribution

This project contributes a software-based synchronization approach that:

* Does not require specialized synchronization hardware.
* Can be implemented using consumer smartphones.
* Provides quantitative evaluation of synchronization impact on 3D reconstruction quality.
* Serves as a foundation for future low-cost multi-view motion capture systems.

---

## 10. References

[1] MediaPipe Pose Documentation.

[2] OpenCV Documentation.

[3] Hartley, R., & Zisserman, A. Multiple View Geometry in Computer Vision.

[4] Human Pose Estimation and Motion Capture Research Papers.

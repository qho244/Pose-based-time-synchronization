# WEEKLY IMPLEMENTATION PLAN

## Project

**Pose-based Time Synchronization for Low-Cost Multi-View Motion Capture**

---

# Week 1: Pipeline Development

## Objectives

Build a complete baseline pipeline from video input to 3D reconstruction.

## Tasks

### Dataset Collection

* Record videos using two smartphones.
* Capture videos from different viewpoints.
* Include several human actions:

  * Clap
  * Hand wave
  * Walk
  * Sit-stand
  * Jump

### Pose Extraction

* Install MediaPipe.
* Extract 2D body keypoints from videos.
* Save extracted keypoints into NumPy files.

### Motion Signal Generation

* Generate motion signals from selected body joints.
* Test multiple signal representations:

  * Velocity Signal
  * Energy Signal
  * Selected-Joint Signal

### Basic 3D Reconstruction

* Implement triangulation.
* Reconstruct 3D poses from synchronized frames.
* Visualize reconstructed poses.

## Deliverables

* Pose extraction module
* Motion signal module
* Basic triangulation module
* Initial dataset

---

# Week 2: Synchronization Module

## Objectives

Develop and evaluate temporal synchronization methods.

## Tasks

### Offset Estimation

* Implement cross-correlation.
* Estimate temporal offset between camera streams.

### Frame Alignment

* Align pose sequences using estimated offsets.
* Generate synchronized keypoint sequences.

### Visualization

* Plot motion signals.
* Compare synchronization results:

  * Before synchronization
  * After synchronization

### Evaluation

* Compute:

  * Offset (frames)
  * Offset (milliseconds)
  * Correlation Score

## Deliverables

* Synchronization module
* Alignment module
* Synchronization metrics
* Visualization results

---

# Week 3: Experimental Evaluation

## Objectives

Evaluate the impact of synchronization on 3D reconstruction quality.

## Tasks

### Dataset Expansion

* Record additional sessions.
* Include multiple actions and movement speeds.

### Controlled Offset Experiments

Create artificial temporal offsets:

* 0 frames
* 10 frames
* 20 frames
* 30 frames
* 40 frames

### 3D Quality Evaluation

Evaluate:

* Bone Length Variance

Compare:

* Synchronized reconstruction
* Unsynchronized reconstruction

### Result Analysis

Analyze:

* Offset vs Correlation Score
* Offset vs Bone Length Variance

## Deliverables

* Experimental dataset
* Evaluation tables
* Performance analysis

---

# Week 4: Documentation and Presentation

## Objectives

Finalize project deliverables.

## Tasks

### Documentation

* Complete README
* Complete technical report
* Organize source code

### Result Compilation

Prepare:

* Tables
* Charts
* Visualizations

### Presentation

* Create presentation slides
* Prepare project demonstration
* Rehearse final defense

### Repository Refinement

* Clean project structure
* Update documentation
* Final GitHub submission

## Deliverables

* Final report
* Presentation slides
* Demo video
* GitHub repository

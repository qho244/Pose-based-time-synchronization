import numpy as np


BONES = [
    (11, 13),
    (13, 15),
    (12, 14),
    (14, 16),
    (23, 25),
    (25, 27),
    (24, 26),
    (26, 28)
]


def bone_length_variance(pose3d):
    variances = []

    for a, b in BONES:
        lengths = np.linalg.norm(
            pose3d[:, a, :] - pose3d[:, b, :],
            axis=1
        )

        lengths = lengths[~np.isnan(lengths)]

        if len(lengths) < 5:
            continue

        # remove extreme outliers
        q1 = np.percentile(lengths, 25)
        q3 = np.percentile(lengths, 75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        lengths = lengths[
            (lengths >= lower) &
            (lengths <= upper)
        ]

        if len(lengths) < 5:
            continue

        mean_len = np.mean(lengths)

        if mean_len == 0:
            continue

        normalized_lengths = lengths / mean_len
        variances.append(np.var(normalized_lengths))

    if len(variances) == 0:
        return np.nan

    return float(np.mean(variances))

def temporal_smoothness_error(pose3d):
    velocity = np.diff(pose3d, axis=0)
    acceleration = np.diff(velocity, axis=0)

    acceleration_norm = np.linalg.norm(acceleration, axis=2)
    acceleration_norm = acceleration_norm[~np.isnan(acceleration_norm)]

    if len(acceleration_norm) == 0:
        return np.nan

    return float(np.mean(acceleration_norm))
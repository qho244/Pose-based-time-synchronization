import numpy as np


def moving_average(signal: np.ndarray, window_size: int = 5):
    if window_size <= 1:
        return signal

    kernel = np.ones(window_size) / window_size
    return np.convolve(signal, kernel, mode="same")


def normalize_signal(signal: np.ndarray):
    mean = np.nanmean(signal)
    std = np.nanstd(signal)

    if std == 0 or np.isnan(std):
        return signal - mean

    return (signal - mean) / std
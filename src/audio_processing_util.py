import numpy as np
from scipy.signal import resample_poly
from math import gcd

TARGET_SR = 16000

def to_mono_float32(audio: np.ndarray) -> np.ndarray:
    if audio.ndim == 2:
        audio = audio.mean(axis=1)          # stereo -> mono
    audio = audio.astype(np.float32, copy=False)
    return audio

def resample_to_16k(audio: np.ndarray, sr: int) -> np.ndarray:
    if sr == TARGET_SR:
        return audio.astype(np.float32, copy=False)
    g = gcd(sr, TARGET_SR)
    up = TARGET_SR // g
    down = sr // g
    return resample_poly(audio, up, down).astype(np.float32)
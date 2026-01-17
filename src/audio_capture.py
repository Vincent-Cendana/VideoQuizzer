import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile

REC_DURATION = 35
SAMPLE_RATE = 48000.0
CHANNELS = 2
DEVICE = 10

def record_numpy():
    print(f"Starting recording for {REC_DURATION} seconds...")
    result = sd.rec(int(REC_DURATION * SAMPLE_RATE), channels=CHANNELS, device=DEVICE)
    sd.wait()
    result *= 6.0
    return result 

def record_wav():
    print(f"Starting recording for {REC_DURATION} seconds...")
    file, filename = tempfile.mkstemp(suffix=".wav", prefix="audio_capture_", dir=".")
    result = sd.rec(int(REC_DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, device=DEVICE)
    sd.wait()
    result *= 6.0
    sf.write(filename, result, SAMPLE_RATE, subtype="PCM_16")
    return result
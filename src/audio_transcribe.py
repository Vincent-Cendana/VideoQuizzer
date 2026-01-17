import numpy as np
import whisper
import sounddevice as sd
import audio_processing_util as autil

model = None

def init():
    global model
    model = whisper.load_model("base")

def transcribe_audio(audio):
    transcription = model.transcribe(audio, verbose=True)

def transcribe_numpy(audio):
    mono_audio = autil.to_mono_float32(audio)
    mono_audio16 = autil.resample_to_16k(mono_audio, 48000)
    output = model.transcribe(mono_audio16, verbose=False, fp16=False)
    return output["text"]
import sounddevice
import wavio
from scipy.io.wavfile import write
frequency = 44100 # 44100 frames per second (audio)
duration = 3# in seconds
print("Recording...")
recordingAudio = sounddevice.rec(int(duration * frequency), samplerate=frequency, channels=2)
sounddevice.wait()
write("recording.wav", frequency, recordingAudio)


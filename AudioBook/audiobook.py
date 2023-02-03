from gtts import gTTS
from playsound import playsound
bookText = open(r"AudioBook\bookText.txt").read()
audio = gTTS(bookText)
audio.save("audio.mp3")
playsound("audio.mp3")
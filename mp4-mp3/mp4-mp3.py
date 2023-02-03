import moviepy
import moviepy.editor
video = moviepy.editor.VideoFileClip(r"mp4-mp3\video.mp4")
audio = video.audio
audio.write_audiofile("audiovideo.mp3")
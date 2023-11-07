from moviepy.editor import *

# Input MP4 video file
input_video_file = "voice_assistant/samplevideo.mp4"

# Output MP3 audio file
output_audio_file = "sample.mp3"

# Load the video file
video_clip = VideoFileClip(input_video_file)

# Extract the audio from the video
audio_clip = video_clip.audio

# Save the extracted audio as an MP3 file
audio_clip.write_audiofile(output_audio_file)

# Close the audio clip
audio_clip.close()

print(f"Conversion complete: {output_audio_file}")
print("Saved in sample.mp3")

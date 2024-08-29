import os
import subprocess
import whisper


# Step 1: Extract audio using FFmpeg
def extract_audio(video_path, audio_path):
    command = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "copy", audio_path]
    subprocess.run(command, check=True)


# Step 2: Transcribe audio using OpenAI Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Load the Whisper model
    result = model.transcribe(audio_path)
    return result["text"]


# Main function
if __name__ == "__main__":
    video_file = "../../calorie.mp4"  # Path to your video file
    audio_file = "output_audio.aac"  # Path to save the extracted audio

    # Extract audio from video
    extract_audio(video_file, audio_file)

    # Transcribe the extracted audio
    transcription = transcribe_audio(audio_file)
    print("Transcription:\n", transcription)

    # Optionally, clean up the audio file
    os.remove(audio_file)

import os
import subprocess
import whisper
import random
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


# Step 1: Extract audio using FFmpeg
def extract_audio(video_path, audio_path):
    try:
        command = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "copy", audio_path]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error extracting audio: {e}")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise e


# Step 2: Transcribe audio using OpenAI Whisper
def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("base")  # Load the Whisper model
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        raise e


# Main function
def extractTextFromVideo(video_file):
    audio_file = f"{random.randint(10000000, 99999999)}output_audio.aac"  # Path to save the extracted audio

    try:
        # Extract audio from video
        extract_audio(video_file, audio_file)

        # Transcribe the extracted audio
        transcription = transcribe_audio(audio_file)
        logging.info("Transcription:\n" + transcription)
        return transcription
    except Exception as e:
        logging.error(f"Error processing video: {e}")
        raise e
    finally:
        # Clean up the audio file
        try:
            os.remove(audio_file)
        except Exception as e:
            logging.warning(f"Failed to remove audio file: {e}")

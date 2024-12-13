from moviepy.editor import VideoFileClip, AudioFileClip
import os
from datetime import datetime
from utils.config import DEFAULT_SAVE_DIR

def combine_audio_video(video_path, audio_path):
    """Combine video and audio files into final MP4 output."""
    # Create output directory if it doesn't exist
    os.makedirs(DEFAULT_SAVE_DIR, exist_ok=True)
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(DEFAULT_SAVE_DIR, f"recording_{timestamp}.mp4")
    
    # Load video and audio
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    
    # Combine and save
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_path)
    
    # Close clips
    video.close()
    audio.close()
    
    return output_path
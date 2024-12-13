import threading
import os
import shutil
from recorder.video_recorder import VideoRecorder
from recorder.audio_recorder import AudioRecorder
from utils.video_processor import combine_audio_video

class ScreenRecorder:
    """Main recorder class that coordinates video and audio recording."""
    
    def __init__(self):
        self.video_recorder = VideoRecorder()
        self.audio_recorder = AudioRecorder()
        self.video_thread = None
        self.audio_thread = None
        self.temp_video = None
        self.temp_audio = None
        self.recording_region = None
        
    def start_recording(self, width, height):
        """Start both video and audio recording."""
        if self.video_recorder.recording or self.audio_recorder.recording:
            return
            
        # Start recorders and get temporary file paths
        self.temp_video = self.video_recorder.start(width, height)
        self.temp_audio = self.audio_recorder.start()
        
        # Create and start recording threads
        self.video_thread = threading.Thread(
            target=self._record_video_thread,
            args=(width, height)
        )
        self.audio_thread = threading.Thread(
            target=self.audio_recorder.record_audio
        )
        
        self.video_thread.start()
        self.audio_thread.start()
        
    def _record_video_thread(self, width, height):
        """Video recording thread function."""
        writer = self.video_recorder.get_writer(width, height)
        while self.video_recorder.recording:
            self.video_recorder.record_frame(width, height, writer)
        writer.release()
        
    def stop_recording(self):
        """Stop recording and combine video and audio."""
        if not (self.video_recorder.recording or self.audio_recorder.recording):
            return
            
        # Stop recorders
        self.video_recorder.stop()
        self.audio_recorder.stop()
        
        # Wait for threads to finish
        self.video_thread.join()
        self.audio_thread.join()
        
        # Combine video and audio
        output_path = combine_audio_video(self.temp_video, self.temp_audio)
        
        # Clean up temporary files
        os.remove(self.temp_video)
        os.remove(self.temp_audio)
        
        return output_path
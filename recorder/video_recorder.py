"""Video recording functionality."""
import cv2
import numpy as np
import pyautogui
from utils.config import FRAME_RATE
from utils.exceptions import VideoDeviceError
from utils.file_manager import generate_temp_filepath

class VideoRecorder:
    """Handles video recording functionality."""
    
    def __init__(self):
        self.recording = False
        self.output_file = None
        self.region = None
        
    def start(self, width, height):
        """Start video recording with specified dimensions."""
        try:
            self.output_file = generate_temp_filepath('.avi')
            self.recording = True
            return self.output_file
        except Exception as e:
            raise VideoDeviceError(f"Failed to start video recording: {str(e)}")
        
    def record_frame(self, width, height, writer):
        """Record a single frame."""
        try:
            screen = pyautogui.screenshot(region=(0, 0, width, height))
            frame = np.array(screen)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            writer.write(frame)
        except Exception as e:
            raise VideoDeviceError(f"Failed to record frame: {str(e)}")
        
    def get_writer(self, width, height):
        """Create and return a video writer object."""
        try:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            return cv2.VideoWriter(self.output_file, fourcc, FRAME_RATE, (width, height))
        except Exception as e:
            raise VideoDeviceError(f"Failed to create video writer: {str(e)}")
        
    def stop(self):
        """Stop video recording."""
        self.recording = False
        return self.output_file
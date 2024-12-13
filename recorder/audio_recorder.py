"""Audio recording functionality."""
import sounddevice as sd
import soundfile as sf
from utils.config import AUDIO_SAMPLE_RATE, AUDIO_CHANNELS
from utils.exceptions import AudioDeviceError
from utils.file_manager import generate_temp_filepath

class AudioRecorder:
    """Handles audio recording functionality."""
    
    def __init__(self):
        self.recording = False
        self.output_file = None
        self.sample_rate = AUDIO_SAMPLE_RATE
        self.channels = AUDIO_CHANNELS
        
    def start(self):
        """Start audio recording."""
        try:
            self.output_file = generate_temp_filepath('.wav')
            self.recording = True
            return self.output_file
        except Exception as e:
            raise AudioDeviceError(f"Failed to start audio recording: {str(e)}")
        
    def record_audio(self):
        """Record audio to file."""
        try:
            with sf.SoundFile(self.output_file, mode='w',
                             samplerate=self.sample_rate,
                             channels=self.channels) as audio_file:
                with sd.InputStream(samplerate=self.sample_rate,
                                  channels=self.channels) as stream:
                    while self.recording:
                        audio_data, overflowed = stream.read(1024)
                        audio_file.write(audio_data)
        except Exception as e:
            raise AudioDeviceError(f"Failed to record audio: {str(e)}")
                    
    def stop(self):
        """Stop audio recording."""
        self.recording = False
        return self.output_file
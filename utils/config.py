"""Configuration settings for the screen recorder application."""
import os

# Available recording resolutions
RESOLUTIONS = [
    "800x400",
    "1024x576",
    "1280x720",
    "1920x1080"
]

# Default directory for saving recordings
DEFAULT_SAVE_DIR = os.path.join(os.path.expanduser("~"), "ScreenRecordings")

# Recording settings
FRAME_RATE = 20
AUDIO_SAMPLE_RATE = 44100
AUDIO_CHANNELS = 2

# UI Colors
COLORS = {
    'background': "#1a1a2e",
    'text': "#ffffff",
    'start_button': "#000080",
    'stop_button': "#f44336",
    'region_button': "#2196F3",
    'selection_border': "#ff0000"
}

# UI Font settings
FONTS = {
    'title': ("Helvetica", 24, "bold"),
    'normal': ("Helvetica", 12),
    'small': ("Helvetica", 10),
    'credits': ("Helvetica", 8)
}
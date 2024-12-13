"""File management utilities for the screen recorder."""
import os
import shutil
from datetime import datetime
from utils.config import DEFAULT_SAVE_DIR
from utils.exceptions import FileError

def ensure_dir_exists(directory):
    """Create directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)

def generate_temp_filepath(suffix):
    """Generate a temporary file path with the given suffix."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"temp_recording_{timestamp}{suffix}"
    return os.path.join(DEFAULT_SAVE_DIR, filename)

def move_file(src, dst):
    """Move file from source to destination."""
    try:
        shutil.move(src, dst)
    except Exception as e:
        raise FileError(f"Failed to move file: {str(e)}")

def remove_file(filepath):
    """Safely remove a file if it exists."""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        raise FileError(f"Failed to remove file: {str(e)}")
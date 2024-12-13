"""Custom exceptions for the screen recorder application."""

class RecordingError(Exception):
    """Base exception for recording-related errors."""
    pass

class AudioDeviceError(RecordingError):
    """Raised when there are issues with audio devices."""
    pass

class VideoDeviceError(RecordingError):
    """Raised when there are issues with video capture."""
    pass

class FileError(Exception):
    """Raised when there are issues with file operations."""
    pass
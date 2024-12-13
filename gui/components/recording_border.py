import tkinter as tk

class RecordingBorder:
    """Shows a border around the recording area."""
    
    def __init__(self):
        self.border_windows = []
        
    def show_border(self, x, y, width, height):
        """Show red border around recording area."""
        # Create windows for each border edge
        positions = [
            (x, y, width, 2),                    # Top
            (x, y + height - 2, width, 2),       # Bottom
            (x, y, 2, height),                   # Left
            (x + width - 2, y, 2, height)        # Right
        ]
        
        for pos in positions:
            window = tk.Tk()
            window.overrideredirect(True)
            window.attributes('-topmost', True, '-alpha', 0.8)
            window.geometry(f"{pos[2]}x{pos[3]}+{pos[0]}+{pos[1]}")
            
            frame = tk.Frame(window, bg='red')
            frame.pack(fill='both', expand=True)
            
            self.border_windows.append(window)
            
    def hide_border(self):
        """Hide the recording border."""
        for window in self.border_windows:
            window.destroy()
        self.border_windows.clear()
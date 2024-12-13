import tkinter as tk

def create_control_buttons(parent, start_callback, stop_callback):
    """Create and return the control buttons frame with start/stop buttons."""
    buttons_frame = tk.Frame(parent, bg="#1a1a2e")
    
    start_button = tk.Button(
        buttons_frame,
        text="Start Recording",
        command=start_callback,
        bg="#4CAF50",
        fg="white",
        font=("Helvetica", 12),
        width=15,
        height=2
    )
    start_button.pack(side=tk.LEFT, padx=10)
    
    stop_button = tk.Button(
        buttons_frame,
        text="Stop Recording",
        command=stop_callback,
        bg="#f44336",
        fg="white",
        font=("Helvetica", 12),
        width=15,
        height=2,
        state=tk.DISABLED
    )
    stop_button.pack(side=tk.LEFT, padx=10)
    
    return buttons_frame, start_button, stop_button
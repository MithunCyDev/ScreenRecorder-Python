import tkinter as tk
from tkinter import ttk
from utils.config import RESOLUTIONS

def create_resolution_selector(parent):
    """Create and return the resolution selector frame with combobox."""
    resolution_frame = tk.Frame(parent, bg="#1a1a2e")
    
    resolution_label = tk.Label(
        resolution_frame,
        text="Select Resolution:",
        font=("Helvetica", 12),
        bg="#1a1a2e",
        fg="white"
    )
    resolution_label.pack(side=tk.LEFT, padx=5)
    
    resolution_var = tk.StringVar(value="800x400")
    resolution_combo = ttk.Combobox(
        resolution_frame,
        textvariable=resolution_var,
        values=RESOLUTIONS,
        state="readonly",
        width=15
    )
    resolution_combo.pack(side=tk.LEFT, padx=5)
    
    return resolution_frame, resolution_var
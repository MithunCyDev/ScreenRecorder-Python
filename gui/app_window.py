import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import shutil
from recorder.screen_recorder import ScreenRecorder
from gui.components.buttons import create_control_buttons
from gui.components.resolution_selector import create_resolution_selector
from gui.components.screen_selector import ScreenSelector
from gui.components.recording_border import RecordingBorder
import pyautogui

class RecorderApp:
    """Main application window class."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")
        self.root.geometry("400x350")
        self.root.configure(bg="#1a1a2e")
        
        self.recorder = ScreenRecorder()
        self.screen_selector = ScreenSelector()
        self.recording_border = RecordingBorder()
        self.recording_region = None
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Developer credit with 20% opacity
        developer_label = tk.Label(
            main_frame,
            text="Developed By MithunCy",
            font=("Helvetica", 8),
            bg="#1a1a2e",
            fg="#6d6d6d"
        )
        developer_label.pack(pady=(0, 5))
        # Using tk.NORMAL and tk_focusFollowsMouse to achieve opacity effect
        developer_label.bind('<Enter>', lambda e: e.widget.configure(fg="#333333"))
        developer_label.bind('<Leave>', lambda e: e.widget.configure(fg="#6d6d6d"))
        
        # Title
        title = tk.Label(
            main_frame,
            text="Screen Recorder",
            font=("Helvetica", 24, "bold"),
            bg="#1a1a2e",
            fg="white"
        )
        title.pack(pady=20)
        
        # Resolution selector
        self.resolution_frame, self.resolution_var = create_resolution_selector(main_frame)
        self.resolution_frame.pack(pady=10)
        
        # Region selection button
        self.region_button = tk.Button(
            main_frame,
            text="Select Region",
            command=self.select_region,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 12)
        )
        self.region_button.pack(pady=10)
        
        # Control buttons with navy blue start button
        self.buttons_frame = tk.Frame(main_frame, bg="#1a1a2e")
        self.buttons_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            self.buttons_frame,
            text="Start Recording",
            command=self.start_recording,
            bg="#1a308c",  # Navy blue color
            fg="white",
            font=("Helvetica", 12),
            width=15,
            height=2
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(
            self.buttons_frame,
            text="Stop Recording",
            command=self.stop_recording,
            bg="#d4000a",
            fg="#f0f0f0",
            font=("Helvetica", 12),
            width=15,
            height=2,
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)
            
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Ready to record",
            font=("Helvetica", 10),
            bg="#1a1a2e",
            fg="white"
        )
        self.status_label.pack(pady=10)
        
    def select_region(self):
        """Handle region selection."""
        self.root.iconify()  # Minimize main window
        self.screen_selector.show_selection_window()
        self.recording_region = self.screen_selector.get_coordinates()
        self.root.deiconify()  # Restore main window
        
        if self.recording_region:
            self.status_label.config(
                text=f"Selected region: {self.recording_region[2]}x{self.recording_region[3]}"
            )
        
    def start_recording(self):
        """Handle start recording button click."""
        try:
            # Use full screen if no region selected
            if not self.recording_region:
                screen_size = pyautogui.size()
                self.recording_region = (0, 0, screen_size[0], screen_size[1])
            
            # Show recording border
            self.recording_border.show_border(*self.recording_region)
            
            # Start recording
            self.recorder.start_recording(*self.recording_region[2:])
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.region_button.config(state=tk.DISABLED)
            self.status_label.config(text="Recording...")
            
        except Exception as e:
            self.recording_border.hide_border()
            messagebox.showerror("Error", str(e))
            
    def stop_recording(self):
        """Handle stop recording button click."""
        try:
            self.recording_border.hide_border()
            temp_path = self.recorder.stop_recording()
            
            # Show save dialog
            file_path = filedialog.asksaveasfilename(
                defaultextension=".mp4",
                filetypes=[("MP4 files", "*.mp4")],
                initialfile=f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4",
                title="Save Recording As"
            )
            
            if file_path:
                # Move the temporary file to the selected location
                shutil.move(temp_path, file_path)
                self.status_label.config(text=f"Recording saved to: {file_path}")
                messagebox.showinfo("Success", f"Recording saved to:\n{file_path}")
            else:
                # If user cancels, delete the temporary file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                self.status_label.config(text="Recording discarded")
            
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.region_button.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
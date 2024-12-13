import tkinter as tk
import pyautogui

class ScreenSelector:
    """Handles screen region selection with visual feedback."""
    
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.selection_window = None
        
    def show_selection_window(self):
        """Show a fullscreen transparent window for region selection."""
        self.selection_window = tk.Tk()
        self.selection_window.attributes('-fullscreen', True, '-alpha', 0.3)
        self.selection_window.configure(bg='black')
        
        # Bind mouse events
        self.selection_window.bind('<Button-1>', self._on_mouse_down)
        self.selection_window.bind('<B1-Motion>', self._on_mouse_drag)
        self.selection_window.bind('<ButtonRelease-1>', self._on_mouse_up)
        
        # Add escape key binding to cancel
        self.selection_window.bind('<Escape>', lambda e: self.selection_window.destroy())
        
        self.selection = tk.Canvas(self.selection_window, highlightthickness=0)
        self.selection.pack(fill='both', expand=True)
        
        self.selection_window.mainloop()
        
    def _on_mouse_down(self, event):
        """Handle mouse button press."""
        self.start_x = event.x
        self.start_y = event.y
        
    def _on_mouse_drag(self, event):
        """Handle mouse drag to draw selection rectangle."""
        self.selection.delete('selection')
        self.selection.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline='red', width=2, tags='selection'
        )
        
    def _on_mouse_up(self, event):
        """Handle mouse button release to finalize selection."""
        self.end_x = event.x
        self.end_y = event.y
        self.selection_window.destroy()
        
    def get_coordinates(self):
        """Return the selected region coordinates."""
        if not all([self.start_x, self.start_y, self.end_x, self.end_y]):
            return None
            
        x1, x2 = sorted([self.start_x, self.end_x])
        y1, y2 = sorted([self.start_y, self.end_y])
        return (x1, y1, x2 - x1, y2 - y1)
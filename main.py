import tkinter as tk
from gui.app_window import RecorderApp

def main():
    """Application entry point."""
    root = tk.Tk()
    app = RecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
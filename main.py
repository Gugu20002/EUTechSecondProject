from gui import BackupApp
import tkinter as tk
from logger import setup_logger

if __name__ == "__main__":
    setup_logger()
    root = tk.Tk()
    app = BackupApp(root)
    root.mainloop()
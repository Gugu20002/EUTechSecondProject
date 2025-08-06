import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from backup import BackupManager

CONFIG_FILE = "config.json"

class BackupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Backup Logger")
        self.root.geometry("500x320")
        self.root.configure(bg="#f0f4f8")

        self.config = self.load_config()

        # Widgets
        self.source_label = tk.Label(root, text="Source Folder:", bg="#f0f4f8", fg="#333", font=("Arial", 10, "bold"))
        self.source_entry = tk.Entry(root, width=50)
        self.source_button = tk.Button(root, text="Browse", command=self.select_source, bg="#4CAF50", fg="white")

        self.dest_label = tk.Label(root, text="Destination Folder:", bg="#f0f4f8", fg="#333", font=("Arial", 10, "bold"))
        self.dest_entry = tk.Entry(root, width=50)
        self.dest_button = tk.Button(root, text="Browse", command=self.select_destination, bg="#4CAF50", fg="white")

        self.version_label = tk.Label(root, text="Version:", bg="#f0f4f8", fg="#333", font=("Arial", 10, "bold"))
        self.version_entry = tk.Entry(root)

        self.zip_var = tk.BooleanVar()
        self.zip_check = tk.Checkbutton(root, text="ZIP Backup", variable=self.zip_var, bg="#f0f4f8", font=("Arial", 10))

        self.backup_button = tk.Button(root, text="Start Backup", command=self.run_backup, bg="#2196F3", fg="white", font=("Arial", 11, "bold"))

        # Layout
        self.source_label.pack(pady=5)
        self.source_entry.pack()
        self.source_button.pack(pady=5)

        self.dest_label.pack(pady=5)
        self.dest_entry.pack()
        self.dest_button.pack(pady=5)

        self.version_label.pack(pady=5)
        self.version_entry.pack(pady=5)

        self.zip_check.pack(pady=5)
        self.backup_button.pack(pady=10)

        # Load saved config
        self.source_entry.insert(0, self.config.get("last_source", ""))
        self.dest_entry.insert(0, self.config.get("last_destination", ""))
        self.version_entry.insert(0, self.config.get("version", "1.0.0"))
        self.zip_var.set(self.config.get("zip_enabled", False))

    def select_source(self):
        path = filedialog.askdirectory()
        if path:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, path)

    def select_destination(self):
        path = filedialog.askdirectory()
        if path:
            self.dest_entry.delete(0, tk.END)
            self.dest_entry.insert(0, path)

    def run_backup(self):
        source = self.source_entry.get()
        dest = self.dest_entry.get()
        version = self.version_entry.get()
        zip_enabled = self.zip_var.get()

        try:
            manager = BackupManager(source, dest, version, zip_enabled)
            manager.run_backup()
            messagebox.showinfo("Success", "Backup completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

        self.config["last_source"] = source
        self.config["last_destination"] = dest
        self.config["version"] = version
        self.config["zip_enabled"] = zip_enabled
        self.save_config()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=4)
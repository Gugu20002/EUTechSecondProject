import shutil
import os
from zipfile import ZipFile
from datetime import datetime
import logging

class BackupManager:
    def __init__(self, source, destination, version="1.0.0", zip_enabled=False):
        self.source = source
        self.destination = destination
        self.version = version
        self.zip_enabled = zip_enabled

    def get_backup_name(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        version_tag = f"v{self.version.replace('.', '-')}"
        return f"backup_{timestamp}_{version_tag}"

    def run_backup(self):
        if not os.path.exists(self.source):
            raise FileNotFoundError("Source folder does not exist")

        backup_name = self.get_backup_name()
        final_backup_path = os.path.join(self.destination, backup_name)

        if self.zip_enabled:
            zip_path = f"{final_backup_path}.zip"
            self._create_zip_backup(zip_path)
            logging.info(f"Zipped backup completed: {zip_path}")
        else:
            shutil.copytree(self.source, final_backup_path)
            logging.info(f"Backup completed: {final_backup_path}")

    def _create_zip_backup(self, zip_path):
        with ZipFile(zip_path, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(self.source):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, self.source)
                    zipf.write(filepath, arcname)
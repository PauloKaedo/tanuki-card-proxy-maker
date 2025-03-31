import os

from configs.config import Config

class FolderCleaner:
    
    @staticmethod
    def clean_raw_folder():
        for file in os.listdir(Config.INPUT_FOLDER_RAW):
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'webm', 'webp')):
                path = os.path.join(Config.INPUT_FOLDER_RAW, file)
                os.remove(path)
import os

from PIL import Image
from typing import List
from configs.config import Config

class ImageResizerService:

    @staticmethod
    def execute() -> List[tuple[str, Image.Image]]:
        images: List[tuple[str, Image.Image]] = []
        config = Config()
        for filename in os.listdir(config.INPUT_FOLDER_RAW):
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'webm')):
                input_path = os.path.join(config.INPUT_FOLDER_RAW, filename)
                
                with Image.open(input_path) as img:
                    resized = img.resize((config.RESIZED_WIDTH, config.RESIZED_HEIGHT), Image.LANCZOS)
                    images.append((filename, resized))

        return images

    #Duplicate images for tests
    def duplicate(qtd_copies: int):
        config = Config()

        for filename in os.listdir(config.INPUT_FOLDER_RAW):
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'wemb')):
                input_path = os.path.join(config.INPUT_FOLDER_RAW, filename)

                with Image.open(input_path) as img:
                    for row in range(qtd_copies):
                        name, extension = os.path.splitext(filename)
                        new_name = f"{name}-{row:02}{extension}"
                        output_path = os.path.join(config.INPUT_FOLDER_RAW, new_name)
                        img.save(output_path)
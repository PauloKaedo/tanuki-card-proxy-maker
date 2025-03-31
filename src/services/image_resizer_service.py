import os

from PIL import Image
from typing import List
from configs.config import Config
from enums.proxy_pattern_enum import ProxyPatternEnum

class ImageResizerService:

    @staticmethod
    def execute(proxyPattern: ProxyPatternEnum = ProxyPatternEnum.DEFAULT) -> List[tuple[str, Image.Image]]:
        images: List[tuple[str, Image.Image]] = []
        config = Config()
        config.set_proxy_pattern(proxyPattern)
        for filename in os.listdir(config.INPUT_FOLDER_RAW):
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'webm', 'webp')):
                input_path = os.path.join(config.INPUT_FOLDER_RAW, filename)
                
                with Image.open(input_path) as img:
                    resized = img.resize((config.RESIZED_WIDTH, config.RESIZED_HEIGHT), Image.LANCZOS)
                    images.append((filename, resized))

        return images
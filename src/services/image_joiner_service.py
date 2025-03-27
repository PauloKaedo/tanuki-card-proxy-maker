import os

from math import floor
from typing import List
from PIL import Image
from configs.config import Config

class ImageJoinerService:
    
    @staticmethod
    def execute(images: List[tuple[str, Image.Image]]):
        config = Config()

        total_sheets = (len(images) + config.MAX_CARDS -1) // config.MAX_CARDS
        total_sheets = 3
        idx = 0
        for page in range(total_sheets):
            idx += 1
            a3_sheet = Image.new("RGB", (config._A3_WIDTH_PX, config._A3_HEIGHT_PX), "white")
            final_filename = os.path.join(config.OUTPUT_FOLDER_RESIZED, f"resized_cards_{idx+1:02}.png")
            a3_sheet.save(final_filename, dpi=(config.DPI, config.DPI))
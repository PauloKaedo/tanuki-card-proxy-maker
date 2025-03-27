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

        print(f"Salvando {len(images)} imagens num total de {total_sheets} paginas A3")

        for page in range(total_sheets):
            a3_sheet = Image.new("RGB", (config._A3_WIDTH_PX, config._A3_HEIGHT_PX), "white")

            start_index = page * config.MAX_CARDS
            end_index = start_index + config.MAX_CARDS
            image_to_join = images[start_index:end_index]
            
            for idx, (filename, image) in enumerate(image_to_join):
                row = idx // config.MAX_COLUMNS
                column = idx % config.MAX_COLUMNS

                offset_x = int(column * config.CARD_PRINT_WIDTH + config.MARGIN_CM * config._PIXELS_PER_CM)
                offset_y = int(row * config.CARD_PRINT_HEIGHT + config.MARGIN_CM * config._PIXELS_PER_CM)

                a3_sheet.paste(image, (offset_x, offset_y))
                print(f"Anexando a imagem {filename} na pagina {page}.")

               
            final_filename = os.path.join(config.OUTPUT_FOLDER_RESIZED, f"resized_cards_{idx+1:02}.png")
            a3_sheet.save(final_filename, dpi=(config.DPI, config.DPI))
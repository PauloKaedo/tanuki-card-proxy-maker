import os

from math import floor
from typing import List
from PIL import Image
from configs.config import Config
from enums.proxy_pattern_enum import ProxyPatternEnum
from enums.sheet_type_enum import SheetType

class ImageJoinerService:
    
    @staticmethod
    def execute(images: List[tuple[str, Image.Image]], proxyPattern: ProxyPatternEnum = ProxyPatternEnum.DEFAULT, sheetType: SheetType = SheetType.A3_SHEET):
        config = Config()
        config.configure_proxy(proxyPattern, sheetType)

        total_sheets = (len(images) + config.MAX_CARDS -1) // config.MAX_CARDS

        print(f"Salvando {len(images)} imagens num total de {total_sheets} paginas")

        for page in range(total_sheets):
            single_sheet = Image.new("RGB", (config.SHEET_WIDTH_PX, config.SHEET_HEIGTH_PX), "white")

            start_index = page * config.MAX_CARDS
            end_index = start_index + config.MAX_CARDS
            image_to_join = images[start_index:end_index]
            
            for idx, (filename, image) in enumerate(image_to_join):
                row = idx // config.MAX_COLUMNS
                column = idx % config.MAX_COLUMNS

                offset_x = int(config._SHEET_MARGIN_PX + column * config.CARD_PRINT_WIDTH)
                offset_y = int(config._SHEET_MARGIN_PX + row * config.CARD_PRINT_HEIGHT)

                single_sheet.paste(image, (offset_x, offset_y))
                print(f"Anexando a imagem {filename} na pagina {page}.")

               
            final_filename = os.path.join(config.OUTPUT_FOLDER_RESIZED, f"proxy_cards_{page+1:02}.png")
            single_sheet.save(final_filename, dpi=(config.DPI, config.DPI))
import argparse

from PIL import Image
from typing import List
from services.image_resizer_service import ImageResizerService
from services.image_joiner_service import ImageJoinerService
from enums.proxy_pattern_enum import ProxyPatternEnum
from enums.sheet_type_enum import SheetType
from scraping.one_piece_scraper import OnePieceScrap


def main():
    parser = argparse.ArgumentParser(description="Tanuki Card Proxy Maker")
    
    parser.add_argument(
        "--pattern", "-p",
        type=str,
        choices=[e.value for e in ProxyPatternEnum],
        default="default",
        help="Escolha o padrão de tamanho da carta (default, yugioh). Para TCG padrões = default, para Yu-gi-oh = yugioh"
    )
    
    parser.add_argument(
        "--sheet", "-s",
        type=str,
        choices=[e.value for e in SheetType],
        default="a3",
        help="Escolha o tamanho da folha (a3, a4). A folha A4 cabem 9 cartas. A Folha A3 cabem 16 cartas"
    )
    
    args = parser.parse_args()
    
    pattern_enum = ProxyPatternEnum(args.pattern)
    sheet_enum = SheetType(args.sheet)
    
    images: List[tuple[str, Image.Image]] = ImageResizerService.execute(pattern_enum)
    ImageJoinerService.execute(images, pattern_enum, sheet_enum)

if __name__ == "__main__":
    #main()
    op_scraper = OnePieceScrap()
    print(op_scraper.fetch_src_image("""2xEB01-018"""))

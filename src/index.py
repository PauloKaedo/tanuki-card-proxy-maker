import argparse

from PIL import Image
from typing import List
from services.image_resizer_service import ImageResizerService
from services.image_joiner_service import ImageJoinerService
from enums.proxy_pattern_enum import ProxyPatternEnum
from enums.sheet_type_enum import SheetType
from enums.clean_folder_enum import CleanFolderEnum
from scraping.one_piece_spellmana_scraper import OnePieceSpellmanaScrap
from tools.image_downloader import ImageDownloader
from tools.folder_cleaner import FolderCleaner


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
    
    parser.add_argument(
        "--clean", "-c",
        type=str,
        choices=[e.value for e in CleanFolderEnum],
        default="none",
        help="Limpa a pasta de imagens de cartas unitárias Antes ou Depois do processo. Pode também SOMENTE limpar a pasta com o Just Clean. (st = Start, ed = End, jcn = Just Clean)"
    )
    
    parser.add_argument(
        "--link", "-l",
        type=str,
        help="Adiciona um link de deck do SpellMana"
    )
    
    args = parser.parse_args()
    link = args.link
    pattern_enum = ProxyPatternEnum(args.pattern)
    sheet_enum = SheetType(args.sheet)
    clean_enum = CleanFolderEnum(args.clean)
    
    if  clean_enum != CleanFolderEnum.JUST_CLEAN:
        if args.clean == CleanFolderEnum.START:
            FolderCleaner.clean_raw_folder()
            print("A pasta de imagens unitárias foi limpa no inicio do processo")
            
        if link:
            card_dict = OnePieceSpellmanaScrap.fetch_src_image(link)
            ImageDownloader.download_image(card_dict)
        
        images: List[tuple[str, Image.Image]] = ImageResizerService.execute(pattern_enum)
        ImageJoinerService.execute(images, pattern_enum, sheet_enum)
        
        if clean_enum == CleanFolderEnum.END:
            FolderCleaner.clean_raw_folder()
            print("A pasta de imagens unitárias foi limpa no fim do processo")
            
    elif clean_enum == CleanFolderEnum.JUST_CLEAN:
         FolderCleaner.clean_raw_folder()
         print("A pasta de imagens unitárias foi limpa. Finalizando processo")
        

if __name__ == "__main__":
    main()

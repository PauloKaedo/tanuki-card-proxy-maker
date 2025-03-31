import requests
import os

from typing import Dict
from configs.config import Config
from urllib.parse import urlparse

class ImageDownloader:
    
    @staticmethod
    def download_image(cards_url: Dict[str, int]):
        for url, quantity in cards_url.items():
            image = ImageDownloader._download_image(url)
            filename, extension = ImageDownloader._extract_path_name(url)
            
            for index in range(1, quantity + 1):
                path = os.path.join(Config.INPUT_FOLDER_RAW, f"{filename}-{index:02}{extension}")
                print(f"Salvando imagem no caminho: {path}")
                with open(path, "wb") as file:
                    file.write(image)
        

    @staticmethod
    def _download_image(url: str) -> bytes:
        try:
            image = requests.get(url, timeout=10000)
            if image.status_code == 200:
                return image.content
            return None
                
        except Exception as e:
            print(f"Erro ao baixar a imagem do link: {url} -> {e}")
            return None
        
    @staticmethod   
    def _extract_path_name(url: str) -> str:
        path = urlparse(url).path
        base = os.path.basename(path)
        name, extension = os.path.splitext(base)
        
        return name, extension
    
    
    
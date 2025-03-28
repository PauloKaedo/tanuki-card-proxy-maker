from abc import ABC, abstractmethod
from typing import Optional


class BaseScraper(ABC):
    
    @abstractmethod
    def fetch_src_image(self, card_name: str) -> Optional[str]:
        pass
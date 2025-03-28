from typing import List
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper
from playwright.sync_api import sync_playwright
from tools.one_piece_decklist_parser import OnePieceDecklistParser
from .scrap_config import ScrapConfig


class OnePieceScrap(BaseScraper):
    
    def fetch_src_image(self, card_codes: str):
        card_dict = OnePieceDecklistParser.code_to_dict(card_codes)
        card_codes = [key for key, _ in card_dict.items()]
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            response = page.goto("https://onepiece-cardgame.dev/cards")
            
            if response.status != 200:
                print("Erro ao conectar com a página")
                browser.close()
                return None
            
            page.wait_for_selector("img[src*='/images/cards/']")
            
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")
            
            fetched_srcs = [img.get("src") for img in soup.find_all("img") if "/images/cards/" in img.get("src")]
            
            filtred_card_srcs = [src for src in fetched_srcs if any(card_code in src for card_code in card_codes)]

            browser.close()
            return filtred_card_srcs
        
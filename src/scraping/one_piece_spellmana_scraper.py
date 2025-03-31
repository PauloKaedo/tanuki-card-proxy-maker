from typing import List
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper
from playwright.sync_api import sync_playwright
from tools.one_piece_decklist_parser import OnePieceDecklistParser
from .scrap_config import ScrapConfig


class OnePieceSpellmanaScrap(BaseScraper):
    
    @staticmethod
    def fetch_src_image(deck_url: str):
        
        deck_anchor = "zoro"
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(deck_url, wait_until="domcontentloaded", timeout=60000)
           
            deck_page = page.locator(f"h2#{deck_anchor}")
            xpath = "xpath=following-sibling::div[contains(@class, 'deck-viewer-grid')]"
            main_container = deck_page.locator(xpath).first
            viewer_container = main_container.locator("div.deck-viewer-container")
            cards_container = viewer_container.locator("div.deck-viewer-cards")
            div_cards = cards_container = cards_container.locator("div.card")
            
            cards_dict = {}
            
            for index in range(div_cards.count()):
                element = div_cards.nth(index)
                
                img_tag = element.locator("img")
                img_src = img_tag.get_attribute("data-src")
                
                qtd_text = element.locator("div.quantity-box").inner_text()
                qtd_number = int(qtd_text.strip() if qtd_text else 1)
                
                cards_dict[img_src] = qtd_number

            browser.close()
            return cards_dict
        
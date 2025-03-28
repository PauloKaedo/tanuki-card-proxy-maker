from enums.proxy_pattern_enum import ProxyPatternEnum
from enums.sheet_type_enum import SheetType

class Config:
    INPUT_FOLDER_RAW = "assets/images/raw_cards"
    OUTPUT_FOLDER_RESIZED = "assets/images/proxies"
    

    #Print Pattern
    DPI = 300
    INCH_PATTERN = 2.54
    SHEET_MARGIN_CM = 0.5
    CARD_SPACING_CM = 0.3


    #Default TCG Size Pattern
    DEFAULT_TARGET_WIDTH_CM = 6.35
    DEFAULT_TARGET_HEIGHT_CM = 8.88


    #YUGI TCG Pattern
    YUGIOH_TARGET_WIDTH_CM = 5.9
    YUGIOH_TARGET_HEIGHT_CM = 8.6


    #Sheet Unity Pattern
    _PIXELS_PER_CM = DPI / INCH_PATTERN
    _SHEET_MARGIN_PX = int(SHEET_MARGIN_CM * _PIXELS_PER_CM)
    _CARD_SPACING_PX = int(CARD_SPACING_CM * _PIXELS_PER_CM)


    #Sheet Page Pattern
    SHEET_WIDTH_PX = 0
    SHEET_HEIGTH_PX = 0
    
    
    _A3_WIDTH_PX = int(29.7 * DPI / INCH_PATTERN)
    _A3_HEIGHT_PX = int(42 * DPI / INCH_PATTERN)

    _A4_WIDTH_PX = int(21 * DPI / INCH_PATTERN)
    _A4_HEIGHT_PX = int(29.7 * DPI / INCH_PATTERN)

    
    def configure_proxy(self,  proxyPattern: ProxyPatternEnum, sheetType: SheetType):
        self.set_proxy_pattern(proxyPattern)
        self.set_sheet_size(sheetType)
    
    def set_proxy_pattern(self, proxy_pattern: ProxyPatternEnum):
        if proxy_pattern == ProxyPatternEnum.DEFAULT:
            self.RESIZED_WIDTH = int(self.DEFAULT_TARGET_WIDTH_CM * self._PIXELS_PER_CM)
            self.RESIZED_HEIGHT = int(self.DEFAULT_TARGET_HEIGHT_CM * self._PIXELS_PER_CM)

        elif proxy_pattern == ProxyPatternEnum.YUGIOH:
            self.RESIZED_WIDTH = int(self.YUGIOH_TARGET_WIDTH_CM * self._PIXELS_PER_CM)
            self.RESIZED_HEIGHT = int(self.YUGIOH_TARGET_HEIGHT_CM * self._PIXELS_PER_CM)

        self.CARD_PRINT_WIDTH = self.RESIZED_WIDTH + self._CARD_SPACING_PX * 2
        self.CARD_PRINT_HEIGHT = self.RESIZED_HEIGHT + self._CARD_SPACING_PX * 2
        
    
    def set_sheet_size(self, sheetType: SheetType):
        if sheetType == SheetType.A3_SHEET:
            self.MAX_COLUMNS = self._A3_WIDTH_PX // self.CARD_PRINT_WIDTH
            self.MAX_ROWS = self._A3_HEIGHT_PX // self.CARD_PRINT_HEIGHT
            self.MAX_CARDS = self.MAX_COLUMNS * self.MAX_ROWS
            self.SHEET_WIDTH_PX = self._A3_WIDTH_PX
            self.SHEET_HEIGTH_PX = self._A3_HEIGHT_PX
            
        elif sheetType == SheetType.A4_SHEET:
            self.MAX_COLUMNS = self._A4_WIDTH_PX // self.CARD_PRINT_WIDTH
            self.MAX_ROWS = self._A4_HEIGHT_PX // self.CARD_PRINT_HEIGHT
            self.MAX_CARDS = self.MAX_COLUMNS * self.MAX_ROWS
            self.SHEET_WIDTH_PX = self._A4_WIDTH_PX
            self.SHEET_HEIGTH_PX = self._A4_HEIGHT_PX


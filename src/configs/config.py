from enums.pattern_enum import PatternEnum

class Config:
    INPUT_FOLDER_RAW = "assets/images/raw"
    OUTPUT_FOLDER_RESIZED = "assets/images/resized"
    PROXY_PATTERN = PatternEnum.DEFAULT
    
    #Print Pattern
    DPI = 300
    INCH_PATTERN = 2.54
    MARGIN_CM = 0.3
    _PIXELS_PER_CM = DPI / INCH_PATTERN

    #Default TCG Size Pattern
    DEFAULT_TARGET_WIDTH_CM = 6.2
    DEFAULT_TARGET_HEIGHT_CM = 8.65


    #YUGI TCG Pattern
    YUGIOH_TARGET_WIDTH_CM = 5.8
    YUGIOH_TARGET_HEIGHT_CM = 8.45


    #Sheet Pattern
    _A3_WIDTH_PX = int(29.7 * DPI / INCH_PATTERN)
    _A3_HEIGHT_PX = int(42 * DPI / INCH_PATTERN)

    _A4_WIDTH_PX = int(21 * DPI / INCH_PATTERN)
    _A4_HEIGHT_PX = int(29.7 * DPI / INCH_PATTERN)

    def __init__(self):
        self.define_pattern()


    def define_pattern(self):
        if self.PROXY_PATTERN == PatternEnum.DEFAULT:
            self.RESIZED_WIDTH = int(self.DEFAULT_TARGET_WIDTH_CM * self._PIXELS_PER_CM)
            self.RESIZED_HEIGHT = int(self.DEFAULT_TARGET_HEIGHT_CM * self._PIXELS_PER_CM)

        elif self.PROXY_PATTERN == PatternEnum.YUGIOH:
            self.RESIZED_WIDTH = int(self.YUGIOH_TARGET_WIDTH_CM * self._PIXELS_PER_CM)
            self.RESIZED_HEIGHT = int(self.YUGIOH_TARGET_HEIGHT_CM * self._PIXELS_PER_CM)

        self.CARD_PRINT_WIDTH = int(self.RESIZED_WIDTH + self.MARGIN_CM * 2)
        self.CARD_PRINT_HEIGHT = int(self.RESIZED_HEIGHT + self.MARGIN_CM * 2)
        self.MAX_COLUMNS = self._A4_WIDTH_PX // self.CARD_PRINT_WIDTH
        self.MAX_ROWS = self._A4_HEIGHT_PX // self.CARD_PRINT_HEIGHT
        self.MAX_CARDS = self.MAX_COLUMNS * self.MAX_ROWS


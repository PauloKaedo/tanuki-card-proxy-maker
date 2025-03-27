from src.enum.pattern_enum import PatternEnum

class Config:
    INPUT_FOLDER_RAW = "assets/images/raw"
    OUTPUT_FOLDER_RESIZED = "assets/images/resized"
    
    DPI = 300

    PROXY_PATTERN = PatternEnum.DEFAULT

    #Default TCG Size Pattern
    DEFAULT_TARGET_WIDTH_CM = 6.2
    DEFAULT_TARGET_HEIGHT_CM = 8.65

    #YUGI TCG Pattern
    YUGIOH_TARGET_WIDTH_CM = 5.8
    YUGIOH_TARGET_HEIGHT_CM = 8.45
    
    
    def __init__(self):
        self.define_pattern(self)


    def define_pattern(self):
        if self.PROXY_PATTERN == PatternEnum.DEFAULT:
            self.RESIZED_WIDTH = int(self.DEFAULT_TARGET_WIDTH_CM * self.DPI / 2.54)
            self.RESIZED_HEIGHT = int(self.DEFAULT_TARGET_HEIGHT_CM * self.DPI / 2.54)

        elif self.PROXY_PATTERN == PatternEnum.YUGIOH:
            self.RESIZED_WIDTH = int(self.YUGIOH_TARGET_WIDTH_CM * self.DPI / 2.54)
            self.RESIZED_HEIGHT = int(self.YUGIOH_TARGET_HEIGHT_CM * self.DPI / 2.54)
    
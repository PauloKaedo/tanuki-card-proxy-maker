class Config:
    INPUT_FOLDER_RAW = "assets/images/raw"
    OUTPUT_FOLDER_RESIZED = "assets/images/resized"
    
    DPI = 300
    TARGET_WIDTH_CM = 6.2
    TARGET_HEIGHT_CM = 8.65
    
    def __init__(self):
        self.RESIZED_WIDTH = int(self.TARGET_WIDTH_CM * self.DPI / 2.54)
        self.RESIZED_HEIGHT = int(self.TARGET_HEIGHT_CM * self.DPI / 2.54)
    
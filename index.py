import os

from PIL import Image
from config import Config


def resize_images():
    config = Config()
    for filename in os.listdir(config.INPUT_FOLDER_RAW):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'webm')):
            input_path = os.path.join(config.INPUT_FOLDER_RAW, filename)
            output_path = os.path.join(config.OUTPUT_FOLDER_RESIZED, filename)
            
            with Image.open(input_path) as img:
                resized = img.resize((config.RESIZED_WIDTH, config.RESIZED_HEIGHT), Image.LANCZOS)
                resized.save(output_path)
            

if __name__ == "__main__":
    resize_images()
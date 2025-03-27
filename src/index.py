from PIL import Image
from typing import List
from services.image_resizer_service import ImageResizerService
from services.image_joiner_service import ImageJoinerService


if __name__ == "__main__":
    images: List[tuple[str, Image.Image]] = ImageResizerService.execute()
    filename, image = images[0]
    ImageJoinerService.execute(images)

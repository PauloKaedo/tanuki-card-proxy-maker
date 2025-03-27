from PIL import Image
from typing import List
from services.image_resizer_service import ImageResizerService
from services.image_joiner_service import ImageJoinerService


if __name__ == "__main__":
    #If need duplicate cards for tests: 
    #ImageResizerService.duplicate(15)

    images: List[tuple[str, Image.Image]] = ImageResizerService.execute()
    ImageJoinerService.execute(images)

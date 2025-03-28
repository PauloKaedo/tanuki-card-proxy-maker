from PIL import Image
from typing import List
from services.image_resizer_service import ImageResizerService
from services.image_joiner_service import ImageJoinerService
from enums.sheet_type_enum import SheetType


if __name__ == "__main__":
    images: List[tuple[str, Image.Image]] = ImageResizerService.execute()
    ImageJoinerService.execute(images, SheetType.A3_SHEET)

import sys

sys.path.append("../")

from source.image_convert import ImageConvert


def test_answer():
    # Test the class

    formats = [
        "png",
        "webp",
        "jpeg",
        "jpg",
        "pdf",
        "gif",
        "bmp",
        "eps",
        "tiff",
    ]  # supported formats

    for format in formats:
        image = ImageConvert("./example_image.png", format)
        assert image.convert_image() == 0

"""
    File with image conversion class, this class converts a desired image to another desired image format.
"""

from PIL import Image
from pathlib import Path
from os.path import join, getmtime
from os import utime
from datetime import datetime
from time import mktime


class ImageConvert:
    def __init__(self, IMAGE_NAME: str, NEW_IMAGE_FORMAT: str) -> None:
        """[Convert the desired image to the desired format.]

        Args:
            IMAGE_NAME ([str]): [Name of the image to be converted]
            NEW_IMAGE_FORMAT ([str]): [Format the image will be saved]
        """
        self.__verify_if_converted_image_directory_exists()
        self.__IMAGE_SAVE_DIRECTORY = join(Path().absolute(), "converted_images")
        self.__name = IMAGE_NAME
        self.__NEW_IMAGE_FORMAT = NEW_IMAGE_FORMAT
        self.__IMAGE_FORMAT = self.__verify_extension_file()

    def convert_image(self) -> int:
        """[Convert the desired image.]

        Returns:
            [Int]: [Returns 0 if the conversion is successful, otherwise returns 1.]
        """
        try:
            with Image.open(self.__name) as im:
                self.__modify_date = self.__get_image_modify_date()
                self.__name = self.__name.replace(
                    self.__IMAGE_FORMAT, self.__NEW_IMAGE_FORMAT
                ).split("/")[-1]
                try:
                    im.convert("RGBA").save(
                        f"{self.__IMAGE_SAVE_DIRECTORY}/{self.__name}"
                    )  # Convert to RGBA and save image
                except Exception:  # case the format don't support transparency
                    im.convert("RGB").save(
                        f"{self.__IMAGE_SAVE_DIRECTORY}/{self.__name}"
                    )  # Convert to RGB and save image
                finally:
                    self.set_image_modify_date()
                    return 0
        except:
            return 1

    def __verify_extension_file(self) -> str:
        """[Check the image extension and return it.]

        Args:
            IMAGE_NAME ([str]): [image name]

        Returns:
            [str]: [Image extension]
        """
        return self.__name.lower().split(".")[-1]

    def __verify_if_converted_image_directory_exists(self) -> None:
        """[Checks if the folder where the converted images will be saved exists, if not, this function will create the folder.]"""
        if not (Path("converted_images").exists()):
            Path("converted_images").mkdir()

    def __get_image_modify_date(self) -> float:
        """[Get the image modify date]

        Returns:
            float: [mktime date of the image]
        """
        date = getmtime(self.__name)
        date = datetime.fromtimestamp(date)
        return mktime(date.timetuple())

    def set_image_modify_date(self) -> None:
        """[Set the image modify date]"""
        utime(
            f"{self.__IMAGE_SAVE_DIRECTORY}/{self.__name}",
            (self.__modify_date, self.__modify_date),
        )

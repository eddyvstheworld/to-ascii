import numpy as np
from app.models.Errors import ImageTooSmallError, InvalidImageTypeError, InvalidImageTypeError


class ImageConverter:
    def __init__(self):
        self.gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        self.gscale2 = "@%#*+=-:. "
        self.maximum_brightness = 255
        self.whitelist = ['JPG', 'JPEG', 'GIF', 'PNG']

    def __getAverageBrightness(self, image, inversed):
        """Returns an average grayscale value given a PIL image. 

        Parameters:
            image (PIL): The PIL image which is to be calculated
            inversed (bool): Whether the contrast of the average_brightness should be reversed            

        Returns:
            average_brightness (float): The average brightness for the given image
        """
        image_array = np.array(image)
        width, height = image_array.shape
        average_brightness = np.average(image_array.reshape(width * height))
        return self.maximum_brightness - average_brightness if inversed else average_brightness

    def covertImageToAscii(self, image, cols, scale, inverse, more_levels):
        """Turns a x*y list of ASCII converted cropped images, given the PIL image and dimensions

        Parameters:
            image (PIL): The PIL image to be converted
            cols (int): The number of columns the converted list should have
            scale (float): The height scale of the resulting conversion
            inverse (bool): Whether the contrast of the resulting image should be reversed or not
            more_levels (bool): Whether the calculation should use the grayscale with more levels

        Returns:
            aimg (list): The ASCII result of the conversion
        """
        if image.format not in self.whitelist:
            raise InvalidImageTypeError
        image = image.convert("L")
        W, H = image.size[0], image.size[1]
        w = W/cols
        h = w/scale
        rows = int(H/h)
        if cols > W or rows > H:
            raise ImageTooSmallError
        aimg = []
        for j in range(rows):
            y1 = int(j*h)
            y2 = int((j+1)*h)
            if j == rows-1:
                y2 = H
            aimg.append("")
            for i in range(cols):
                x1 = int(i*w)
                x2 = int((i+1)*w)
                if i == cols-1:
                    x2 = W
                img = image.crop((x1, y1, x2, y2))
                avg = int(self.__getAverageBrightness(img, inverse))
                gsval = self.gscale1[int(
                    (avg*69)/255)] if more_levels else self.gscale2[int((avg*9)/255)]
                aimg[j] += gsval
        return aimg

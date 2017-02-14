"""
1. Base64 编码
2. ScaleImage
3. 常见的图片的其他操作,加水印之类,切分9图,拼图
4. 基本的验证码识别
"""
import io
import os

import requests
from PIL import Image


def image_url_to_string(url):
    from pytesseract import pytesseract
    image = Image.open(io.BytesIO(requests.get(url, timeout=20).content))
    return pytesseract.image_to_string(image)


def image_to_string(path):
    from pytesseract import pytesseract
    return pytesseract.image_to_string(Image.open(path))


import imghdr


def is_bmp(filename):
    return imghdr.what(file=filename) == 'bmp'


def is_png(filename):
    return imghdr.what(file=filename) == 'png'


def is_jpg(filename):
    return imghdr.what(file=filename) == 'jpeg'


def is_gif(filename):
    return imghdr.what(file=filename) == 'gif'


def convert_image(path_1, path_2):
    Image.open(path_1).save(path_2)


def crop_image(path, input, height, width, k, page, area):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            try:
                o = a.crop(area)
                o.save(os.path.join(path, "PNG", "%s" % page, "IMG-%s.png" % k))
            except:
                pass
            k += 1


def scale_image(width, height, zoom_level, padding=False):
    # TODO: 1.
    pass

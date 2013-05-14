"""GD module is an interface to the GD library written by Thomas Bouttel.
It allows your code to quickly draw images complete with lines, arcs,
text, multiple colors, cut and paste from other images, and flood fills,
and write out the result as a .PNG, .JPEG, or .WBMP file. This is
particularly useful in World Wide Web applications, where .JPEG is
universally supported and PNG is the up-and-coming format used for
inline images. It has been extended in some ways from the original GD
library."""

import _gd
from _gd import *
del image

# proxy the _gd.image type as a class so we can override it.

class image:

    def __init__(self, *args):
        if isinstance(args[0], image):
            args = list(args)
            args[0] = args[0]._image
        self.__dict__["_image"] = _gd.image(*args)

    def __getattr__(self, name):
        return getattr(self._image, name)

    def __setattr__(self, name, value):
        return setattr(self._image, name, value)

    def lines(self, points, color):
        "draw a line along the sequence of points in the list or tuple using color"
        prev = tuple(points[0])
        for p in points[1:]:
            p = tuple(p)
            self._image.line(prev, p, color)
            prev = p

    def copyTo(self, im, *args):
        return self._image.copyTo(im._image, *args)

    def copyResizedTo(self, im, *args):
        return self._image.copyResizedTo(im._image, *args)

    def copyResampledTo(self, im, *args):
        return self._image.copyResampledTo(im._image, *args)

    def copyMergeTo(self, im, *args):
        return self._image.copyMergeTo(im._image, *args)

    def copyMergeGrayTo(self, im, *args):
        return self._image.copyMergeGrayTo(im._image, *args)

    def copyPaletteTo(self, im, *args):
        return self._image.copyPaletteTo(im._image, *args)

    def compare(self, im, *args):
        return self._image.compare(im._image, *args)

    def setBrush(self, im, *args):
        return self._image.setBrush(im._image, *args)

    def setTile(self, im, *args):
        return self._image.setTile(im._image, *args)

# end of file.

class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidImageTypeError(Error):
    """To be raised when the file format is not whitelisted"""
    pass


class ImageTooSmallError(Error):
    """To be raised when the image is too small for the specified columns"""
    pass

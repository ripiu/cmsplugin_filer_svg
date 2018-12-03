from filer.fields.file import FilerFileField

from .filemodels import SVG


class FilerSVGField(FilerFileField):
    """A model field holding an SVG file"""

    default_model_class = SVG

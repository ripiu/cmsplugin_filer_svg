import os

from filer.models.filemodels import File

# from filer import settings as filer_settings


class SVG(File):
    """An SVG file"""

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        """Match an svg file by its extension"""
        ext = os.path.splitext(iname)[1].lower()
        return ext == '.svg'

    _icon = 'svg'

    @property
    def contents(self):
        """SVG file contents"""
        data = ''
        try:
            data = self.file.read().decode()
            self.file.close()
        except IOError:
            pass
        return data

import os

from filer.models.filemodels import File

from django.utils.translation import gettext_lazy as _


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

    class Meta:
        verbose_name = _('SVG file')
        verbose_name_plural = _('SVG files')

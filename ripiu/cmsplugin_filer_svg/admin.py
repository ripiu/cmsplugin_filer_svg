from filer.admin.fileadmin import FileAdmin

from django.contrib import admin

from .models import SVG

# use the standard FileAdmin
admin.site.register(SVG, FileAdmin)

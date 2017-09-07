from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import FilerSvgImagePluginModel

class FilerSvgImagePlugin(CMSPluginBase):
    model = FilerSvgImagePluginModel
    name = _("SVG image")
    module = 'Filer'
    render_template = 'ripiu/cmsplugin_filer_svg/ref.html'
    allow_children = False

plugin_pool.register_plugin(FilerSvgImagePlugin)

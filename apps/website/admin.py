# Librerias Django
from django.contrib import admin

# Librerias en carpetas locales
from .submodels.website_config import WebsiteConfig

admin.site.register(WebsiteConfig)

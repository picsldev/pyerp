try:
    INSTALLED_APPS += 'apps.chat'
except:
    import logging; logging.getLogger(__name__).warn('Faltan las installed_apps del settings.py')

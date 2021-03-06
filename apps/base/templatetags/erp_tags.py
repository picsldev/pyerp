# Librerias Django
from django import template

# Librerias en carpetas locales
from ..models import BaseConfig, PyApp

# from apps.home.models import WebsiteConfig

register = template.Library()


@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter
def get_online(obj):
    try:
        return BaseConfig.objects.get(pk=1).online
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_name(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.name
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_email(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.email
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_slogan(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.slogan
    except BaseConfig.DoesNotExist:
        return None



@register.filter
def get_company_rut(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.rut
    except BaseConfig.DoesNotExist:
        return None



@register.filter
def get_company_facebook(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_facebook
    except BaseConfig.DoesNotExist:
        return None



@register.filter
def get_company_instagram(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_instagram
    except BaseConfig.DoesNotExist:
        return None


@register.filter
def get_company_linkedin(obj):
    try:
        return BaseConfig.objects.get(pk=1).main_company_id.social_linkedin
    except BaseConfig.DoesNotExist:
        return None



@register.filter
def get_sidebar_collapse(obj):
    return BaseConfig.objects.get(pk=1).open_menu



@register.filter
def currency_symbol(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.currency_id.symbol


@register.filter
def currency_position(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.currency_id.position


@register.filter
def get_app_list(obj):
    apps = PyApp.objects.all().filter(installed=True).order_by('sequence')
    return [app.name.lower() + "/menu.html" for app in apps]

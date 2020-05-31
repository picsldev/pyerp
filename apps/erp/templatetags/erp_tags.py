# Librerias Django
from django import template

# Librerias en carpetas locales
from ...base.models import BaseConfig
from ...website.models import WebsiteConfig

register = template.Library()


@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter
def get_online(obj):
    return BaseConfig.objects.get(pk=1).online


@register.filter
def get_company_name(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.name


@register.filter
def get_company_email(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.email

@register.filter
def get_company_slogan(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.slogan

@register.filter
def get_company_rut(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.rut

@register.filter
def get_company_facebook(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.social_facebook

@register.filter
def get_company_instagram(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.social_instagram

@register.filter
def get_company_linkedin(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.social_linkedin

@register.filter
def get_sidebar_collapse(obj):
    return BaseConfig.objects.get(pk=1).open_menu


# WEB
@register.filter
def web_show_blog(obj):
    return WebsiteConfig.objects.get(pk=1).show_blog

@register.filter
def web_show_price(obj):
    return WebsiteConfig.objects.get(pk=1).show_price

@register.filter
def web_chat(obj):
    return WebsiteConfig.objects.get(pk=1).show_chat

@register.filter
def web_show_shop(obj):
    return WebsiteConfig.objects.get(pk=1).show_shop

@register.filter
def web_under_construction(obj):
    return WebsiteConfig.objects.get(pk=1).under_construction

# Moneda
@register.filter
def currency_symbol(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.currency_id.symbol

@register.filter
def currency_position(obj):
    return BaseConfig.objects.get(pk=1).main_company_id.currency_id.position

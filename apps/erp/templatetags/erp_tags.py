from django import template
from ...base.models import BaseConfig

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

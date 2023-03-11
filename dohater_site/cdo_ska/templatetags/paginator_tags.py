from django import template
from django.core.paginator import Paginator
from django.http import QueryDict

register = template.Library()

@register.simple_tag
def get_filter_cheked(context: list, field_name: str, field_id: str):
    field_name += str(field_id)
    for key in context:
        if key == field_name:
            return 'checked'
    return ''

@register.simple_tag
def get_proper_elided_page_range(p, number, on_each_side=2, on_ends=1):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(
        number=number, 
        on_each_side=on_each_side,
        on_ends=on_ends
    )

@register.simple_tag
def replace(querydict, argument, value):
    querydict = querydict.copy()
    if querydict.get(argument):
        querydict.pop(argument)
    querydict.appendlist(argument, value)
    return querydict.urlencode()

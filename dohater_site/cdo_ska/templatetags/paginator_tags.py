from django import template
from django.core.paginator import Paginator
from re import IGNORECASE, compile, escape as rescape

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

@register.filter
def highlight(string: str, substring: str):
    rgx = compile(rescape(substring), IGNORECASE)
    return rgx.sub(
            lambda m: f"<span>{substring}</span>",
            string
        )


def highlight(string, substring):
    rgx = compile(rescape(substring), IGNORECASE)
    return rgx.sub(
            lambda m: f'<span class="highlight">{substring}</span>',
            string
        )

@register.filter
def find_and_highlight(question, substring: str):
    """
    сделать выбор нужного вопроса, а то сейчас выводится первый попавшийся
    """
    print(type(question))
    print(dir(question))
    
    question = question.values()
    
    print(question)
    
    if len(question) > 0:
        question = question.values()[0]
    else:
        return ""
    string = question.get("question").lower()
    string_lower = string.lower()
    substring_lower = substring.lower()
    if string_lower.find(substring_lower) == -1:
        string = question.get("answer")
    
    print(string, substring)
    
    return highlight(string, substring)

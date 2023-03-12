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
def find_and_highlight(questions, substring: str):
    """
    сделать выбор нужного вопроса, а то сейчас выводится первый попавшийся
    """
    print(type(questions))
    print(dir(questions))
    
    questions = questions.values()
    substring_lower = substring.lower()
    for question in questions:
        string = question['question']
        string_lower = string.lower()
        if string_lower.find(substring_lower) != -1:
            return highlight(string, substring)
        string = question['answer']
        string_lower = string.lower()
        if string_lower.find(substring_lower) != -1:
            return highlight(string, substring)
    return ""

@register.filter
def ru_pluralize(string, variants):
    variants = variants.split(",")
    value = abs(int(string))
    
    if value % 100 in (11, 12, 13, 14):
        variant = 0
    elif value % 10 == 1:
        variant = 1
    elif value % 10 in (2, 3, 4):
        variant = 2
    else:
        variant = 0

    return variants[variant]

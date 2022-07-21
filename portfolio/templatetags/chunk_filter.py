import itertools

from django import template

register = template.Library()


@register.filter
def chunks(value, chunk_length):
    """
    Breaks a list up into a list of lists of size <chunk_length>
    """
    chunk_len = int(chunk_length)
    i = iter(value)
    while True:
        chunk = list(itertools.islice(i, chunk_len))
        if chunk:
            yield chunk
        else:
            break

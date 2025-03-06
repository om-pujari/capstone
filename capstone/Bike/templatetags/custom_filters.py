from django import template

register = template.Library()

@register.filter
def dict_key(dictionary, key):
    """Fetches a value from a dictionary safely."""
    return dictionary.get(key, "N/A") if isinstance(dictionary, dict) else "N/A"

@register.filter
def get_item(dictionary, key):
    """Returns the value from a dictionary safely"""
    return dictionary.get(key, "N/A") if isinstance(dictionary, dict) else "N/A"

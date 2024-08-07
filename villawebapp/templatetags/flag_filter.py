from django import template

register = template.Library()

FLAG_EMOJIS = {
    'en': '🇬🇧',
    'fr': '🇫🇷',
    'de': '🇩🇪',
    'it': '🇮🇹',
    'sq': '🇦🇱',
    'ru': '🇷🇺',
    'nl': '🇳🇱',
    'ja': '🇯🇵',
    'es': '🇪🇸',
    'pt': '🇵🇹',
    'tr': '🇹🇷',
    'el': '🇬🇷',
    'pl': '🇲🇨',

    # Add more language codes and flags here
}

@register.filter
def flag(value):
    return FLAG_EMOJIS.get(value, '')
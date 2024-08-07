from modeltranslation.translator import register, TranslationOptions
from .models import Portfolio

##########################################################################################################################################
@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'paragraph',
        'paragraph2',
    )
##########################################################################################################################################

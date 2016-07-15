# Django REST Case Converter
This module maps Django REST response data from underscore to camel case and maps Django REST request data from camel case to underscore. This allows both Python and JavaScript developers to use their respective variable naming best practices.

## Installation
`pip install django-case-converter`

## Global Use
If you would like to do case conversions on all Django REST responses and requests then add the `renderer` and `parser` to your Django settings

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'case_converter.renderer.UnderscoreJSONRenderer',
            # Other global renderers...
        ),

        'DEFAULT_AUTHENTICATION_CLASSES': (
            'case_converter.parser.CamelCaseJSONParser',
            # Other global parsers...
        ),
    }

## Isolated Use
If you would like to only do case conversions on specified Django REST responses and requests then add the `renderer` and `parser` to your views as decorators.

    from case_converter.renderer import UnderscoreJSONRenderer
    from case_converter.parser import CamelCaseJSONParser

    @api_view()
    @renderer_classes((UnderscoreJSONRenderer, # Other isolated renderers...))
    @parser_classes((CamelCaseJSONParser, # Other isolated parsers...))
    def my_view(request):
        # Your view logic
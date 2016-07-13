from rest_framework.renderers import JSONRenderer
from .utils import convert_to_camel_case


class UnderscoreJSONRenderer(JSONRenderer):
    def render(self, data, *args, **kwargs):
        return super(UnderscoreJSONRenderer, self).render(convert_to_camel_case(data), *args, **kwargs)
import json

from rest_framework.parsers import JSONParser, ParseError, six
from django.conf import settings
from .utils import convert_to_underscore


class CamelCaseJSONParser(JSONParser):
    def parse(self, stream, media_type=None, context=None):
        try:
            data = stream.read()
            return convert_to_underscore(json.loads(data))
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
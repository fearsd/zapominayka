# Register your factory methods here.

from app.testing import register
from app.testing.types import FactoryProtocol
from authors.models import Author


@register
def author(self: FactoryProtocol, **kwargs: dict) -> Author:
    return self.mixer.blend('authors.Author', **kwargs)

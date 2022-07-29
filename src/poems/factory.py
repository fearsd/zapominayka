from app.testing import register
from app.testing.types import FactoryProtocol
from poems.models import Poem
from poems.models import Screen


@register
def poem(self: FactoryProtocol, **kwargs: dict) -> Poem:
    return self.mixer.blend('poems.Poem', **kwargs)


@register
def screen(self: FactoryProtocol, **kwargs: dict) -> Screen:
    return self.mixer.blend('poems.Screen', **kwargs)

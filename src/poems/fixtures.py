import pytest
from typing import TYPE_CHECKING

from poems.models import Poem
from poems.models import Screen

if TYPE_CHECKING:
    from app.testing.factory import FixtureFactory


@pytest.fixture
def poem(factory: 'FixtureFactory', author) -> Poem:
    return factory.poem(author=author)


@pytest.fixture
def screen(factory: 'FixtureFactory', poem) -> Screen:
    return factory.screen(poem=poem)

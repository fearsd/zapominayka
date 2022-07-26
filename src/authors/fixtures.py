# Register your project-wide fixtures here.

import pytest
from typing import TYPE_CHECKING

from authors.models import Author

if TYPE_CHECKING:
    from app.testing.factory import FixtureFactory


@pytest.fixture
def author(factory: 'FixtureFactory') -> Author:
    return factory.author()

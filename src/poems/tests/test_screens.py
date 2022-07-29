import pytest

pytestmark = [pytest.mark.django_db]


def test_ok_get_screens_with_registered_user(as_user, screen):
    result = as_user.get('/api/v1/poems/screens/')

    assert result['count'] == 1
    assert result['next'] is None
    assert result['previous'] is None
    assert result['results'][0]['id'] == screen.pk
    assert result['results'][0]['poem'] == screen.poem.pk
    assert result['results'][0]['text'] == screen.text
    assert result['results'][0]['image'] is None


def test_ok_get_screens_with_anon_user(as_anon, screen):
    result = as_anon.get('/api/v1/poems/screens/')

    assert result['count'] == 1
    assert result['next'] is None
    assert result['previous'] is None
    assert result['results'][0]['id'] == screen.pk
    assert result['results'][0]['poem'] == screen.poem.pk
    assert result['results'][0]['text'] == screen.text
    assert result['results'][0]['image'] is None


def test_ok_get_screen_with_registered_user(as_user, screen):
    result = as_user.get(f'/api/v1/poems/screens/{screen.pk}/')

    assert result['id'] == screen.pk
    assert result['poem'] == screen.poem.pk
    assert result['text'] == screen.text
    assert result['image'] is None


def test_ok_get_screen_with_anon_user(as_anon, screen):
    result = as_anon.get(f'/api/v1/poems/screens/{screen.pk}/')

    assert result['id'] == screen.pk
    assert result['poem'] == screen.poem.pk
    assert result['text'] == screen.text
    assert result['image'] is None

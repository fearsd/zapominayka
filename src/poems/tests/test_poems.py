import pytest

pytestmark = [pytest.mark.django_db]


def test_ok_get_poems_with_registered_user(as_user, poem):
    result = as_user.get('/api/v1/poems/')

    assert result['count'] == 1
    assert result['next'] is None
    assert result['previous'] is None
    assert result['results'][0]['id'] == poem.pk
    assert result['results'][0]['author'] == poem.author.pk
    assert result['results'][0]['title'] == poem.title
    assert result['results'][0]['image'] is None


def test_ok_get_poems_with_anon_user(as_anon, poem):
    result = as_anon.get('/api/v1/poems/')

    assert result['count'] == 1
    assert result['next'] is None
    assert result['previous'] is None
    assert result['results'][0]['id'] == poem.pk
    assert result['results'][0]['author'] == poem.author.pk
    assert result['results'][0]['title'] == poem.title
    assert result['results'][0]['image'] is None


def test_ok_get_poem_with_registered_user(as_user, poem):
    result = as_user.get(f'/api/v1/poems/{poem.pk}/')

    assert result['id'] == poem.pk
    assert result['title'] == poem.title
    assert result['author'] == poem.author.pk
    assert result['image'] is None


def test_ok_get_poem_with_anon_user(as_anon, poem):
    result = as_anon.get(f'/api/v1/poems/{poem.pk}/')

    assert result['id'] == poem.pk
    assert result['title'] == poem.title
    assert result['author'] == poem.author.pk
    assert result['image'] is None

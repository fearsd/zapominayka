import pytest

pytestmark = [pytest.mark.django_db]


def test_ok_get_authors_with_registered_user(as_user, author):
    result = as_user.get('/api/v1/authors/')

    assert result['count'] == 1
    assert result['next'] is None
    assert result['previous'] is None
    assert result['results'][0]['id'] == author.pk
    assert result['results'][0]['name'] == author.name


def test_ok_get_authors_with_anon_user(as_anon, author):
    result = as_anon.get('/api/v1/authors/')

    assert result['count'] == 1
    assert result['next'] is None
    assert result['previous'] is None
    assert result['results'][0]['id'] == author.pk
    assert result['results'][0]['name'] == author.name


def test_ok_get_author_with_registered_user(as_user, author):
    result = as_user.get(f'/api/v1/authors/{author.pk}/')

    assert result['id'] == author.pk
    assert result['name'] == author.name


def test_ok_get_author_with_anon_user(as_anon, author):
    result = as_anon.get(f'/api/v1/authors/{author.pk}/')

    assert result['id'] == author.pk
    assert result['name'] == author.name

from http import client
from django.contrib.auth import get_user_model
import pytest
from django.urls import reverse

from alakufar.kufar.models import Post


@pytest.fixture()
def user():
    return get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
    )


@pytest.fixture()
def post():
    return Post.objects.create(
        title='A good title',
        info='Nice info content',
        price=12,
        author=user,
    )


@pytest.mark.django_db
def test_string_representation():
    post = Post(title='This is title')
    assert str(post) == post.title


@pytest.mark.django_db
def test_get_absolute_url():
    assert post.get_absolute_url() == '/products/1/'


@pytest.mark.django_db
def test_post_content():
    assert f'{post.title}' == 'A good title'
    assert f'{post.author}' == 'testuser'
    assert f'{post.info}' == 'Nice info content'
    assert f'{post.price}' == 12


@pytest.mark.django_db
def test_post_list_view():
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'Nice info content' in response
    # assertTemplateUsed(response, 'home.html')


@pytest.mark.django_db
def test_post_detail_view():
    response = client.get('/products/2/')
    no_response = client.get('/products/100000/')
    assert response.status_code == 200
    assert no_response.status_code == 404
    assert 'A good title' in response
    # self.assertTemplateUsed(response, 'prod_detail.html')


@pytest.mark.django_db
def test_post_create_view():
    response = client.post(reverse('prod_new'), {
        'title': 'New title',
        'info': 'New text',
        'author': user,
        'price': 100,
    })
    assert response.status_code == 200
    assert 'New title' in response
    assert 'New text' in response
    assert 100 in response


@pytest.mark.django_db
def test_post_update_view():
    response = client.post(reverse('prod_edit', args='7'), {
        'title': 'Updated title',
        'info': 'Updated text',
        'price': 101,
    })
    for post in Post.objects.all():
        print(f"---{post.pk}---")
    assert response.status_code == 302


@pytest.mark.django_db
def test_post_delete_view():
    response = client.post(
        reverse('prod_delete', args='6'))
    assert response.status_code == 302

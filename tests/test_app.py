import pytest
from app import app


@pytest.fixture()
def client():
    context = app.app_context()
    client = app.test_client()
    context.push()
    yield client
    context.pop()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    post_response = client.post('/', data={'text': '我有一只鸡但你有一只鸭'})
    assert post_response.status_code == 200
    data = post_response.get_data(as_text=True)
    print(data)
    assert '我有一只鸡但你有一只鸭' in data


def test_api(client):
    response = client.get('/api?word=啥')
    assert response.status_code == 200
    data = response.get_data(as_text=True)
    assert data == '什么'

import requests
url='http://127.0.0.1:5000/'

def test_login():
    response=requests.get(url)
    assert response.status_code==200
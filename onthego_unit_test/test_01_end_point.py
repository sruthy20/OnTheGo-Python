import requests
#import onthego.onthegoconfig
from OnTheGo-Python-1.onthego import onthegoconfig
#url='http://127.0.0.1:5000/'
url=onthegoconfig.END_POINT_URL

def test_index():
    response=requests.get(url)
    assert response.status_code==200
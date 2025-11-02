import requests

GO_SERVER_BASE_URL = 'http://gocore:8080'

def ping():
    try:
        res = requests.get(f'{GO_SERVER_BASE_URL}/ping', timeout=3)
        res.raise_for_status()
        return res.json()
    
    except requests.RequestException as e:
        return {'error': str(e)}
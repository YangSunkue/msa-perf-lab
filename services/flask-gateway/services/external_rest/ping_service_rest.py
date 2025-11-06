import requests
import utils.rest_vs_grpc as util

GO_SERVER_BASE_URL = 'http://gocore:8080'

def ping_rest_service(size: int):
    """end_to_end/rest_vs_grpc/k6_rest.js
    
    Go Rest 서버에 ping 요청을 보냅니다.
    
    Args:
        payload_size (int): 요청 페이로드 크기
    """    
    try:
        payload = util.generate_random_message(size)
        res = requests.post(f'{GO_SERVER_BASE_URL}/ping', json={'payload': payload})
        res.raise_for_status()

        return res.json()
    
    except requests.RequestException as e:
        return {'error': str(e)}


import random, string

def generate_random_message(size: int) -> str:
    """
    size만큼 랜덤 문자열을 생성합니다.
    """
    if size <= 0:
        return "Hello from Flask (gRPC client)"
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))
from utils.cpu_heavy import heavy_calculation

def cpu_heavy_service(complexity_level: int) -> int:
    """복잡한 연산을 하는 함수를 호출합니다.

    Args:
        complexity_level (int): 연산 난이도

    Returns:
        int: 연산 결과
    """
    result = heavy_calculation(complexity_level=complexity_level)
    return result
def heavy_calculation(complexity_level: int) -> int:
    """CPU를 점유하는 복잡한 연산을 수행합니다.

    Args:
        complexity_level (int): 연산 난이도

    Returns:
        int: 연산 결과
    """
    BASE_LOOP = 100_000
    loop_count = complexity_level * BASE_LOOP

    sum_val = 0
    for i in range(loop_count):
        sum_val += i * i % 1_000 + 1
    
    return sum_val
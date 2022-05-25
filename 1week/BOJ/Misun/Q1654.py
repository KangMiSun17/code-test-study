def solution():
    k, n = map(int, input().split())
    # k번 만큼 입력받아서 정수 형태로 리스트에 추가하기
    len = [int(input()) for _ in range(k)]
    min_len = 1
    max_len = max(len)
    
    while  min_len <= max_len:
        mid = (min_len + max_len) // 2
        cnt = 0
        for i in len:
            cnt += i // mid
        
        if cnt >= n:
            min_len = mid + 1
        else:
            max_len = mid - 1
    return max_len

print(solution())
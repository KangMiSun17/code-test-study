from collections import Counter
import sys
input = sys.stdin.readline

#input은 개행문자 "\n"까지 읽어들이기 때문에 .rstrip()으로 지워야한다.
n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
mid = (n+1)//2

#산술평균
print(round(sum(arr) / n))
#중앙값
arr.sort()
print(arr[mid-1])
#최빈값
def fine(list):
    lst = Counter(list).most_common()
    max_cnt = lst[0][1]
    result = []
    for num in lst:
        if num[1] == max_cnt:
            result.append(num[0])
    return result
if len(fine(arr)) >= 2:
    print(fine(arr)[1])
else:
    print(fine(arr)[0])
#범위
print(max(arr)-min(arr))

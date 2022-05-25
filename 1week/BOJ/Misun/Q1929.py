# 시간 초과 코드
'''import sys
input = sys.stdin.readline
print = sys.stdout.write

m, n = map(int, input().rstrip().split())
nums = []

for i in range(m, n+1):
    result = []
    for j in range(1, i+1):
        if i % j == 0:
            result.append(j)
    if len(result) == 2:
        nums.append(i)

for i in nums:
    print("%s\n" % i)'''

# 해결 (i의 제곱근까지만 검사하면 이후는 검사하나 마나여서..)
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
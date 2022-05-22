k,n = map(int,input().split())
arr = []
for _ in range(k):
  len = int(input())
  arr.append(len)

lower,upper = 1,max(arr)
result = 0

while lower <= upper :
  mid = (lower+upper)//2
  cut_sum = sum([(i//mid)for i in arr])

  #잘라낸 개수가 기준보다 많다면, 더 큰 단위로 잘라서 개수를 줄이기
  if cut_sum >= n:
    result = mid
    lower = mid+1

  #잘라낸 개수가 기준보다 적다면, 더 작은 단위로 잘라서 개수 늘리기
  elif cut_sum <n:
    upper = mid -1
print(result)
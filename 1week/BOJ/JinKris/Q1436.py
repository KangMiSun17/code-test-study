n = int(input())

rank=1
num=666
checkCode='666'
while True:
  if(n==rank):
    print(num)
    break
  num+=1
  if(checkCode in str(num)):
    rank+=1
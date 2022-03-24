n = int(input())
nums = map(int, input(). split())
cnt = 0

for i in nums:
  x = 0
  if i > 1:
    for j in range(2, int(i**0.5)+1):
      if i % j ==0:
        x += 1
    if x == 0:
      cnt += 1

print(cnt)
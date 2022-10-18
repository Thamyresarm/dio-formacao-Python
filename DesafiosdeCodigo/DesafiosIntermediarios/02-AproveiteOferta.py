T = int(input())

for i in range(T):
  
  N, K = input().split()
  N = int(N)
  K = int(K)
  
  if N > 0 and N <= 10000 and K >= 1:
    total = int(int(N / K) + int(N % K))
    
  print(total)
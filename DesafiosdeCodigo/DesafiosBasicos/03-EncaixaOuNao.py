N = input()

n = int(N)

while n > 0:
  
  A, B = input().split()
  
  if A[-len(B)::] == B:
    print("encaixa")
  else:
    print("nao encaixa")
  n -= 1
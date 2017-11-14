def fib(x):
  y, j = 1, 1
  for i in range(x - 1):
    y, j = j, y + j
  return j

print(fib(6))
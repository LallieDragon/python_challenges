def fib(x):
  i, j = 1, 1
  for i in range(x-1):
    i, j = j, i + j
  return i

print(fib(100))
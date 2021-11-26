def print_till_zero(n):
  if n >= 1:
    print(n)
    print_till_zero(n - 1)
print_till_zero(10)

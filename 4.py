def max_in(lst):
  if len(lst) <= 1:
    return lst[0]
  else:
    m = max_in(lst[1:])
    if m > lst[0]:
      return m
    return lst[0]
print(max_in([1, 4, 3]))

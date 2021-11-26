def is_palindrome(s):
  if len(s) == 0:
    return s
  else:
    return is_palindrome(s[1:]) + s[0]
print(is_palindrome('123'))

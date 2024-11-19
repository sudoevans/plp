def large_power(base, exponent):
  #I    f wastes time. As long as result is less than 5k that means it low power, so wont return.
  result = base ** exponent
  return result > 5000

base=int(input('enter base'))
exponent=int(input('enter exponent'))

result=large_power(base,exponent)
print(result)
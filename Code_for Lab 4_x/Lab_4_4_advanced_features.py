foo = [1, 2, 3, 4, 5]

# List  return true for odd numbers, filter add number to result list if get True
odd_foo = [x for x in foo if x % 2 == 1]

# lambda return true for odd numbers, filter add number to result list if get True
odd_foo = filter(lambda x: x % 2 == 1, foo)  
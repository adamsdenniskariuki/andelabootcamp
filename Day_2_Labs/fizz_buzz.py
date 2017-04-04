# fizz buzz class

def fizz_buzz(n):
  
  if ((n % 3) == 0 and(n % 5) != 0):
    return "Fizz"
  
  elif((n % 5) == 0 and (n % 3) != 0):
    return "Buzz"
  
  elif((n % 3) == 0 and (n % 5) == 0):
    return "FizzBuzz"
  
  elif((n % 3) != 0 or (n % 5) != 0):
    return n

print fizz_buzz(8)
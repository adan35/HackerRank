# sieve of eratosthenes algo

def sieve_of_eratosthenes(num):
  num = int(num)
  # initialize list of all trues
  prime = [True]*1000000
  p = 2
  # run loop to the square root of len(prime)
  while p*p <= len(prime): # or condition can be p <= len(prime) ** 0.5
    # if it is prime number false all its multiples
    if prime[p]:
      for i in range(p*p, len(prime), p):
        prime[i] = False
    p += 1
  # list of all primes
  primes = []
  for i in range(2, len(prime)):
    if prime[i]:
      primes.append(i)
  # required prime number
  return primes[num - 1]

print(sieve_of_eratosthenes(input("Enter nth num: ")))




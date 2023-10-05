"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
        raise ValueError(f'Number of primes = {number_of_primes} should have been 1 or more.')
    list.append(2)  
    num = 3
    while len(list) < number_of_primes:
        isPrime = False
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime:
            list.append(num)
        num += 1 
        
         
        

    return list



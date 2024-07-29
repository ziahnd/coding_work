def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def find_prime(series):
    primes = []
    for number in series:
        if is_prime(number):
            primes.append(number)
        return primes


def gen_list(limit):
    num_list = [number for number in range(limit)]
    return num_list
print("_" * 30)

limit = int(input("Please enter a number"))
my_list = gen_list(limit)
print(my_list)
prime_num = find_prime(my_list)
print("the required prime numbers are = ", prime_num)
print(prime_num)
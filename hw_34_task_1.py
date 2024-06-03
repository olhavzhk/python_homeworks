import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def prime_checker(number) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def threads_prime_filter(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(prime_checker, numbers))
    return [number for number, primes in zip(numbers, results) if prime_checker]


def processes_prime_filter(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(prime_checker, numbers))
    return [number for number, primes in zip(numbers, results) if prime_checker]


NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

if __name__ == '__main__':
    start = time.time()
    primes_threads = threads_prime_filter(NUMBERS)
    end = time.time()
    print(f"ThreadPoolExecutor: {primes_threads}")
    print(f"Time taken with ThreadPoolExecutor: {end - start} seconds")

    start = time.time()
    primes_processes = processes_prime_filter(NUMBERS)
    end = time.time()
    print(f"ProcessPoolExecutor: {primes_processes}")
    print(f"Time taken with ProcessPoolExecutor: {end - start} seconds")

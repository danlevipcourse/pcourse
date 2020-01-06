from contextlib import contextmanager
import time
import json
import orjson
from itertools import islice, count


class TimedClass(object):
    def __init__(self, funcName):
        self._funcName = funcName
        self._start = time.process_time_ns()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = (time.process_time_ns() - self._start) / 1e6
        print(f'{self._funcName} took {duration:.6f}ms')


@contextmanager
def Timed(funcName):
    # enter
    start = time.process_time_ns()
    yield
    # exit
    duration = (time.process_time_ns() - self._start) / 1e6
    print(f'{funcName} took {duration:.6f}ms')


def benchmark():
    with TimedClass('list comprehension'):
        lc = [str(i) for i in range(10000000)]
    with TimedClass('map'):
        m = list(map(str, range(10000000)))
    with TimedClass('jsonlc'):
        json.loads(json.dumps(lc))
    with TimedClass('orjsonlc'):
        orjson.loads(orjson.dumps(lc))
    with TimedClass('jsonm'):
        json.loads(json.dumps(m))
    with TimedClass('orjsonm'):
        orjson.loads(orjson.dumps(m))
    with TimedClass('jsonm'):
        json.loads(json.dumps({'sd': 1}))
    with TimedClass('orjsonm'):
        orjson.loads(orjson.dumps({'sd': 1}))


#benchmark()


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(number ** 0.5 + 2)):
        if number % i == 0:
            return False
    return True

def getNextPrime():
    integers = count(1)  # infinite generator
    return filter(is_prime, integers)

def print_first_primes(N):
    gen = getNextPrime()
    for i in range(N):
        print(next(gen))

#print_first_primes(100)

def print_primes(start, stop):
    gen = getNextPrime()
    for i in range(start):
        next(gen)
    l = islice(gen, stop-start)
    for prime in l:
        print(prime)

print_primes(100, 110)

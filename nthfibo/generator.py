from collections import defaultdict
import timeit

class FibCache(defaultdict):
    def __init__(self, fn):
	self.fn = fn

    def __missing__(self, num):
	self[num] = self.fn(num, self)
	print self
	return self[num]

def fib(num, cache):
    if num == 0:
	return 0
    elif num == 1:
	return 1
    else:
	return cache[num -1] + cache[num - 2]

'''
def calculate_n(n):
    fib_cache = FibCache(fib)
'''
fib_cache = FibCache(fib)


from itertools import ifilter
from helpers import fibonacci

print sum(ifilter(lambda x : x % 2 == 0, fibonacci(4E6)))

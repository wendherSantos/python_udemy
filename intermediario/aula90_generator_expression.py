import sys

# Generator expression, Iterables and Iterator in Python

iterable = ['I','Have', '__iter__']
# iterator = iterable.__iter__ # have __iter__ and __next__
iterator = iter(iterable) # have __iter__ and __next__

list_ = [n for n in range(100000)]
generator = (n for n in range(100000))
print(sys.getsizeof(list_))
print(sys.getsizeof(generator))

print(generator[0])
print(len(generator))

# for n in generator:
#     print(n)
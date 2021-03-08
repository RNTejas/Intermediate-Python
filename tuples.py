# Tuple: ordered, immutable, allows duplicate elements
import timeit
print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,0,'Hello']", number=100000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,0,'Hello')", number=100000000))
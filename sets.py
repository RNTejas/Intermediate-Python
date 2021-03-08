# Sets: unordered, mutable, no duplicates
my_set_ = {1, 2, 3}
# print(my_set_)

my_set_no_dipl = {1, 2, 3, 1, 2}
# print(my_set_no_dipl)

my_set_create_str = set("Hello")
my_set_create = set([1,2,3,3,4,7])

# if you want an empty set
my_dict = {}     # this is a dict
my_set = set()  # this is a set

my_set.add(1)
my_set.add(2)
my_set.add(3)

my_set.remove(2)
# my_set.discard(2) # no error

# my_set.clear()
# my_set.pop()
# for i in my_set:
#     print(i)

# print(my_set)
print("*"*40)
even = {2,4,6,8}
odd = {1,3,5,7,9}
prime = {2,3,5,7}

u = even.union(odd)
print(u)


#set operations
set_a = {1,2,3,4,5,21,21,45}
set_b ={10,1,2,3,4}

# note : in set operatons the array does not consider the duplicates

#AND Or Intersection operation
print(set_a & set_b)

#OR or union operations
print(set_a | set_b)

set_a.add(100)
print(set_a)
#pop remove the first element
set_a.pop()
print(set_a)
# remove , we need to specify the element to be removed
set_a.remove(2)
print(set_a)

#set a minus set b
print(set_a.difference(set_b))

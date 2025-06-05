x={1,2}
print(x)
print(id(x))
del x # delete the reference variable x but int object is not deleted from private heap space
import gc
gc.collect()  # WHen garbage collector runs id of [1,34] changes since a new object is created as previous one forcefully get released by garbage collector but this behavior is only witness with list for other there is no change in id after garbage collection also
y={1,2}
print(id(y)) # here y is pointing to same object which is previously pointed by x

# object have only id
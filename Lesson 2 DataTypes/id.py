# This program check whether id() return memory address in cpython
import ctypes

x = 42
print(id(x))  # Python's unique identifier
print(ctypes.cast(id(x), ctypes.py_object).value)  # Access object using memory address

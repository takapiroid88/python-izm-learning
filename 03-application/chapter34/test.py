# dir
print(dir())
print('------------')
python_dir = "python-izm"
print(dir())
print('------------')
import sys
print()
for val in dir(sys):
    print(val)

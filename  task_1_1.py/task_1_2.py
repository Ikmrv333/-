import mymodule
from mymodule import circle_area, VERSION
import mymodule as mm
from mymodule import circle_len as perimeter

print(mymodule.circle_area(5))
print(circle_area(5))
print(mm.circle_area(5))
print(perimeter(3))

print("dir(my_module) -> ", [n for n in dir(mymodule) if not n.startswith("__")])
print("mymodule.__name__ =", mymodule.__name__)
print("mymodule.__file__ =", mymodule.__file__)

print("mm._helper()", mm._helper()) 

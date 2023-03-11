from people_info import *
from calculator import add, minus, multiple, divide

print("add:", add(55, 55))
print("minus:", minus(55, 55))
print("multiply:", multiple(55, 55))
print("divide:", divide(55, 55))
print("===========================")
search_name = "Kitty"
search_info = "gender"
search_result = people(search_name, search_info)
print("===========================")


if "__name__" == "__main__":
    print("main.py: {}".format(__name__))

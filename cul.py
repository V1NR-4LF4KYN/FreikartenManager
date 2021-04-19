# cul.my 

import sys

# Usage
# -c to capitalize the arguments
# -u to convert the arguments to uppercase
# -l to convert the argument to lowercase


def x():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if "-c" in opts:
        print(" ".join(arg.capitalize() for arg in args))
    elif "-u" in opts:
        print(" ".join(arg.upper() for arg in args))
    elif "-l" in opts:
        print(" ".join(arg.lower() for arg in args))
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")

# example
import json

y = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(y))
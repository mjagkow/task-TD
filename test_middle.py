import sys
from middle import middle


assert middle(1, 2, 3) == 2
assert middle(1, 3, 2) == 2
assert middle(2, 1, 3) == 2
assert middle(2, 3, 1) == 2
assert middle(3, 1, 2) == 2
assert middle(3, 2, 1) == 2

assert middle(3, 2, 3) == 3
assert middle(3, 3, 2) == 3
assert middle(2, 3, 3) == 3
assert middle(1, 2, 1) == 1
assert middle(1, 1, 2) == 1
assert middle(2, 1, 1) == 1

assert middle(2, 2, 2) == 2
assert middle(0, 0, 0) == 0

assert middle(sys.maxsize, sys.maxsize, -sys.maxsize) == sys.maxsize
assert middle(sys.maxsize, -sys.maxsize, -sys.maxsize) == -sys.maxsize
assert middle(sys.maxsize, 0, -sys.maxsize) == 0
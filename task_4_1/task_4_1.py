
import six
print("six.__version__ =", six.__version__)
print("six.__file__    =", six.__file__)

print("PY2?", six.PY2, "| PY3?", six.PY3)
print("six.moves.range(3) ->", list(six.moves.range(3)))

import sys
print("sys.path[0] =", sys.path[0])

import site
print("site-packages:", site.getsitepackages())
import six
import sys
import site


print("six.__version__ =", six.__version__)
print("six.__file__    =", six.__file__)

print("PY2?", six.PY2, "| PY3?", six.PY3)
print("six.moves.range(3) ->", list(six.moves.range(3)))


print("sys.path[0] =", sys.path[0])


for path in site.getsitepackages():
    print("Путь к site-packages:", path)
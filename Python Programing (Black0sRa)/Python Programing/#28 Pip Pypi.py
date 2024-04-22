# Pip Pypi
from pathlib import Path

path = Path()
#print(path.exists())
#print(path.mkdir())
#print(path.rmdir())
for i in path.glob("*.py"):
    print(i)
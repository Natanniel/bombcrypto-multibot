#!/usr/bin/python
from subprocess import Popen

while True:
    print("\nLynx inicializando")
    p = Popen("python index.py", shell=True)
    p.wait()
""" test models in the distribution

"""
import os
import unittest
from fnmatch import fnmatch
import opensim as om
root = os.getcwd()
pattern = "*.osim"

osimpaths = list()
modelNames = list()

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            osimpaths.append(os.path.join(path, name))
            modelNames.append(name)

len(osimpaths)

for i in range(0 , len(osimpaths) - 1):
    try:
        model = om.Model(osimpaths[i])
        s = model.initSystem()
    except:
        print("Oops, Model Failed: " + modelNames[i])
        




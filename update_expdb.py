# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 17:27:44 2017

@author: Ian
"""
# Automatically updates and uploads packages to the cloud
import os, sys, subprocess, conda
# Search for the package
search = subprocess.check_output(['conda', 'search', 'gladio'])

# Take version number from package
#v = [int(s) for s in search.split() if s.isdigit()]

v = search.split(".")

lastLine = v[len(v)-1]

oldVersionNumber = int(lastLine.split()) 

newVer = int(oldVersionNumber[0] + 1)

f = open("meta.yaml")

oldMeta = f.read()

splitUp = oldMeta.split(".")

newMeta = splitUp[0] + str(newVer)+"\""+splitUp[1].split("\"")[1]

print(newMeta)

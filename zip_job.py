#!/usr/bin/env python
import zipfile
letters = ["a","b","c","d"]
try:
    for letter in letters:
            with open(letter+".txt","w+") as file:
                file.write("")
#            with  ZipFile(letter + "_" + ENV + ".zip", "w+") as zipObj:
#                zipObj.write(file)
except:
    print ("something fails with txt files")

try:
    for letter in letters:
        with zipfile.ZipFile('{0}_1.2.0.zip'.format(letter), "w") as zipObj:
           zipObj.write("{0}.txt".format(letter))
except:
    print ("something fails with zip files")

print ("success")

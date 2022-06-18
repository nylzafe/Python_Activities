#f = open("pythonessay.txt", "r")
#print(f.read())
#print(f.readline())

#for x in f:
#    print(x)

import os
if os.path.exists("pythonessay.txt"):
    os.remove("pythonessay.txt")
else:
    print("The File does not exist")
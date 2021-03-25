#!/usr/bin/python3
import sys 

hungry= sys.argv[1].replace(" ", "")  ###removes spaces from string
imhungry = hungry.lower() ###makes string lowercase

print(imhungry)
print("The length is", len(imhungry))
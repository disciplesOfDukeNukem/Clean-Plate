#This file will parse the rawBlast and return the text

#opening the rawBlast

with open("rawBlast.txt", 'r') as f:
    raw_blast = f.read()

print(raw_blast)
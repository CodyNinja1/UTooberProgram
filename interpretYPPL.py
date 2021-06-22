import argparse as ap

parser = ap.ArgumentParser(description="The offical YPPL interpreter.")
parser.add_argument("-f", "--file", help="Interprets the given file.")
parser.add_argument("-l", "--length", help="Set the length of the variable strip.", type=int)
info = parser.parse_args()

fileName = info.file
if info.length == None:
    cellLength = 100
else:
    cellLength = int(info.length)

programEnded = False
weJumping = False
cells = []

for _ in range(cellLength):
    cells.append(0)

cellPos = int(cellLength/2)

file = open(fileName, "r")
lines = file.readlines()
cutLines = lines

while not programEnded:
    if weJumping:
        cutLines = lines[args-1:]
        weJumping = False
    
    for lineCount in range(len(cutLines)):
        Fline = cutLines[lineCount]
        if Fline == "" or Fline == "\n":
            continue
        else:
            line = str(cutLines[lineCount]).split() 

        command = line[0]
        if command != "GOTOTHEDESCRIPTION" and command != "GOTOTHEDESCRIPTIONN" and command != "COMMENTDOWNBELOWN" and command != "COMMENTDOWNBELOW" and command != "LOOKATTHECARDINTHEUPPERRIGHTCORNER" and command != "LOOKATTHECARDINTHEUPPERLEFTCORNER" and command != "THX4WATCHING" and command != "EDITORNOTE":
            args = int(line[1])

        if command == "LOOKATTHECARDINTHEUPPERRIGHTCORNER":
            cellPos += 1
        if command == "LOOKATTHECARDINTHEUPPERLEFTCORNER":
            cellPos -= 1
        if command == "GOTOTHEDESCRIPTION":
            print(chr(cells[cellPos]), end="")
        if command == "GOTOTHEDESCRIPTIONN":
            print(str(cells[cellPos]), end="")
        if command == "THX4WATCHING":
            programEnded = True
            break
        if command == "COMMENTDOWNBELOW":
            cells[cellPos] = ord(input())
        if command == "COMMENTDOWNBELOWN":
            cells[cellPos] = int(input())
        if command == "ADDTHISVIDEOTOYOURPLAYLIST":
            cells[cellPos] += int(args)
        if command == "REMOVETHISVIDEOFROMYOURPLAYLIST":
            cells[cellPos] -= int(args)
        if command == "ADDLIKEALOT":
            cells[cellPos] *= int(args)
        if command == "SUBTRACTLIKEALOT":
            cells[cellPos] /= int(args)
        if command == "EDITORNOTE":
            continue
        if command == "JUMPTOIFYOUGOT>0":
            if cells[cellPos] > 0:
                weJumping = True
                break
        if command == "JUMPTOIFYOUWANTTO":
            weJumping = True
            break
        if command == "JUMPTOIFYOUGOT<=0":
            if cells[cellPos] <= 0:
                weJumping = True
                break

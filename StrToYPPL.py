inp = input()
out = ""
for char in inp:
    n = ord(char)
    a = f"ADDTHISVIDEOTOYOURPLAYLIST {n}\nGOTOTHEDESCRIPTION\nLOOKATTHECARDINTHEUPPERRIGHTCORNER\n"
    out = out + a
out += "EDITORNOTE This program was created using the StrToYPPL.py tool"
print(out)

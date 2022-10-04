import os
import sys

prevcmd = ""

while (1):
    print("shellthon :> ", end = "")
    inp = input()

    if inp == "exit":
        sys.exit()
        ref = False
        break
    elif inp == "prevcmd":
        inp = last
    else:
        prevcmd = inp

    print(os.system(inp))

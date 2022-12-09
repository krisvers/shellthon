#!/usr/bin/env python3
import os, sys

version = "1.1.0"

def get_prompt():
    user = os.environ.get('USER')
    if user == None:
        return str(os.environ.get('PWD').replace(os.environ.get('HOME'), "~"))+" -> "
    return str(user+" : "+str(os.environ.get('PWD').replace(os.environ.get('HOME'), "~")))+" -> "

def internal_cmd(cmd):
    if not len(cmd) > 0:
        return True

    argv = cmd.split()
    argc = len(argv)
    if (argv[0] == "version" or argv[0] == "ver"):
        print("shellthon version: "+str(version))

        return True
    elif (argv[0] == "cd"):
        if (argc == 2):
            if (argv[1].startswith("~")):
                try:
                    os.chdir(argv[1].replace("~", os.environ.get('HOME')))
                    os.environ['PWD'] = argv[1].replace("~", os.environ.get('HOME'))
                except FileNotFoundError as e:
                    print("cd: no such file or directory found")

                return True

            try:
                os.chdir(argv[1])
                os.environ['PWD'] = argv[1]
            except FileNotFoundError as e:
                print("cd: "+argv[1]+": no such file or directory found")
        else:
            try:
                os.chdir(os.environ.get('HOME'))
                os.environ['PWD'] = os.environ.get('HOME')
            except FileNotFoundError as e:
                print("cd: no home directory found")

        return True
    elif (argv[0] == "quit" or argv[0] == "exit"):
        sys.exit()
    else:
        return False

def main():
    inp = str()

    while (True):
        print(get_prompt(), end="")
        try:
            inp = input()
            if not internal_cmd(inp):
                print(os.system(inp))
        except EOFError as e:
            print(e)
        except KeyboardInterrupt as e:
            print(e)

main()

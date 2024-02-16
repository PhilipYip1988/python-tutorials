import sys
ncommands = len(sys.argv)

print(f'Command 0 The Script File: {sys.argv[0]}')

if ncommands >= 2:
    print(f'Command 1: {sys.argv[1]}')
    
if ncommands >= 3:
    print(f'Command 2: {sys.argv[2]}')

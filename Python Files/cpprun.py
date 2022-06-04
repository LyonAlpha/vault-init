import os
try:
    os.system('gcc -o main.exe  main.cpp -lstdc++')
    os.system('.\main.exe')
except Exception as e:
    os.system('echo The Exception Is The Following: ')
    print(e)
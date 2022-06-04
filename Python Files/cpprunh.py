import os
try:
    headerDirectoryAndFile = input("Enter The Header File Name => ")
    os.system(f'gcc -o main.exe  main.cpp {headerDirectoryAndFile} -lstdc++')
    os.system('.\main.exe')
except Exception as e:
    os.system('echo The Exception Is The Following: ')
    print(e)
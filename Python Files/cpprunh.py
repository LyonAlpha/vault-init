import os
try:
    # Same Thing As cpprun.py But With The Header File
    header_file_directory = input("Enter The Header File Name => ")
    os.system(f'gcc -o main.exe  main.cpp {header_file_directory} -lstdc++')
    os.system('.\main.exe')
except Exception as e:
    os.system('echo The Exception Is The Following: ')
    print(e)
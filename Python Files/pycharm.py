import os

def main():
    base_path = os.getcwd()
    os.chdir(f'{base_path}/venv')
    file = 'pyvenv.cfg'
    with open(file, 'w') as f:
        f.writelines('''home = C:\Python310
implementation = CPython
version_info = 3.10.4.final.0
virtualenv = 20.13.0
include-system-site-packages = false
base-prefix = C:\Python310
base-exec-prefix = C:\Python310
base-executable = C:\Python310\python.exe
''')
        
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
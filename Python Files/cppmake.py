import os, time
try:
    # Functions
    def clearTerminal():
        os.system('cls' if os.name == 'nt' else 'clear') # Clears The Terminal

    def joinPath(parentPath, path):
        newPath = os.path.join(parentPath, path)
        return newPath

    # Main Code
    clearTerminal()
    os.system('cmdblue')
    project_name = input("Enter A Project Name => ")
    project_files_folder_name = input("Enter A Project Dependency Name => ")
    if project_files_folder_name == "":
        project_files_folder_name = "code"
    base_dir = os.getcwd()
    newPath = joinPath(base_dir, project_name)
    os.mkdir(newPath)
    os.chdir(project_name)
    currentPath = os.getcwd()
    src = 'src'
    src_path = f'{currentPath}/{src}'
    os.mkdir(src_path)    
    os.chdir(src)
    with open('main.cpp', 'w') as f:
        f.write('')
    dependencyPathBase = joinPath(currentPath, src) 
    dependencyPath = joinPath(dependencyPathBase,project_files_folder_name)
    os.mkdir(dependencyPath)
    os.system('cmdreset')
    # time.sleep(5)
    clearTerminal()
    
except Exception as e:
    print(e)
import os

def create_dir():

    # Directory
    directory = input("Enter A Project Name => ")
    
    # Parent Directory path
    parent_dir = os.getcwd()
    
    # Path
    path = os.path.join(parent_dir, directory)
    

    os.mkdir(path)
    print("")
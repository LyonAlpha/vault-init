import os
import re
from sys import exit
import projectbase

# Parent Directory path
parent_dir = os.getcwd()

split_dir = re.split(r'\\|!|\\', parent_dir)



startup = input("""

Enter A Type Of File

[1] - Addons
[2] - Main File

=> """)

if startup == "1":

    answer = input("""

Enter An Application Type

[1] - C# Class
[2] - Python
[3] - Java
[4] - JavaScript
[5] - HTMl
[6] - CSS
[7] - C
[8] - C++

=> """)

    print("")



    if answer == "1":

        

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.cs"


        with open(os.path.join(parent_dir, file), 'w') as fp:
            fp.writelines(    
    f"""

    namespace {split_dir[2]} \u007b

        class {file_name} \u007b




        \u007d

    \u007d

            

            
    """)

    if answer == "2":

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.py"

        with open(os.path.join(parent_dir, file), 'w') as fp:

            fp.writelines("")

        number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
        
        while True: 
        
            if number_of_imports == "0":
                break

            elif number_of_imports == "1":

                print("Enter Import")

                import_1 = input("=> ")
                
                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(f'import {import_1}')
                
                break

            if number_of_imports == "2":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}''')

                break

            elif number_of_imports == "3":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                print("Enter Import #3")

                import_3 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}
import {import_3}''')

                break

            if number_of_imports == "4":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                print("Enter Import #3")

                import_3 = input("=> ")

                print("Enter Import #4")

                import_4 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}''')

                break

            elif number_of_imports == "5":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                print("Enter Import #3")

                import_3 = input("=> ")

                print("Enter Import #4")

                import_4 = input("=> ")

                print("Enter Import #5")

                import_5 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}''')

                break

    if answer == "3":

        print("Enter A Java Addon")

        print("")

        print("[1] - Class")
        print("[2] - Interface")
        print("[3] - Record")
        print("[4] - Enum")
        print("[5] - Annotation")

        print("")

        application_name = input("=> ")

        if application_name == "2":

            file_name = input("Enter A File Name => ")

            file = f"{file_name}.java"

            package_name = input("Enter A Package Name => ")
        
            with open(os.path.join(parent_dir, file), 'w') as fp:

                fp.writelines(
                    
                f"""package {package_name}

    public interface {file_name} \u007b

        

            // Enter Your Code Here
            


    \u007d 

                """
                )

            number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
            
            while True: 
            
                if number_of_imports == "0":
                    break

                elif number_of_imports == "1":

                    print("Enter Import")

                    import_1 = input("=> ")
                    
                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(f'import {import_1}\n' + old)
                    
                    break

                if number_of_imports == "2":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}\n''' + old)

                    break

                elif number_of_imports == "3":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}\n''' + old)

                    break

                if number_of_imports == "4":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}\n''' + old)

                    break

                elif number_of_imports == "5":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    print("Enter Import #5")

                    import_5 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}\n''' + old)

                    break

        if application_name == "1":

            file_name = input("Enter A File Name => ")

            file = f"{file_name}.java"

            package_name = input("Enter A Package Name => ")
        
            with open(os.path.join(parent_dir, file), 'w') as fp:

                fp.writelines(
                    
                f"""package {package_name}

    public class {file_name} \u007b

        

            // Enter Your Code Here
            


    \u007d 

                """
                )

            number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
            
            while True: 
            
                if number_of_imports == "0":
                    break

                elif number_of_imports == "1":

                    print("Enter Import")

                    import_1 = input("=> ")
                    
                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(f'import {import_1}\n' + old)
                    
                    break

                if number_of_imports == "2":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}\n''' + old)

                    break

                elif number_of_imports == "3":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}\n''' + old)

                    break

                if number_of_imports == "4":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}\n''' + old)

                    break

                elif number_of_imports == "5":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    print("Enter Import #5")

                    import_5 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}\n''' + old)

                    break

        if application_name == "3":

            file_name = input("Enter A File Name => ")

            file = f"{file_name}.java"

            package_name = input("Enter A Package Name => ")
        
            with open(os.path.join(parent_dir, file), 'w') as fp:

                fp.writelines(
                    
                f"""package {package_name}

    public record {file_name} \u007b

        

            // Enter Your Code Here
            


    \u007d 

                """
                )

            number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
            
            while True: 
            
                if number_of_imports == "0":
                    break

                elif number_of_imports == "1":

                    print("Enter Import")

                    import_1 = input("=> ")
                    
                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(f'import {import_1}\n' + old)
                    
                    break

                if number_of_imports == "2":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}\n''' + old)

                    break

                elif number_of_imports == "3":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}\n''' + old)

                    break

                if number_of_imports == "4":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}\n''' + old)

                    break

                elif number_of_imports == "5":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    print("Enter Import #5")

                    import_5 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}\n''' + old)

                    break

        if application_name == "4":

            file_name = input("Enter A File Name => ")

            file = f"{file_name}.java"

            package_name = input("Enter A Package Name => ")
        
            with open(os.path.join(parent_dir, file), 'w') as fp:

                fp.writelines(
                    
                f"""package {package_name}

    public enum {file_name} \u007b

        

            // Enter Your Code Here
            


    \u007d 

                """
                )

            number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
            
            while True: 
            
                if number_of_imports == "0":
                    break

                elif number_of_imports == "1":

                    print("Enter Import")

                    import_1 = input("=> ")
                    
                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(f'import {import_1}\n' + old)
                    
                    break

                if number_of_imports == "2":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}\n''' + old)

                    break

                elif number_of_imports == "3":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}\n''' + old)

                    break

                if number_of_imports == "4":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}\n''' + old)

                    break

                elif number_of_imports == "5":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    print("Enter Import #5")

                    import_5 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}\n''' + old)

                    break

        if application_name == "5":

            file_name = input("Enter A File Name => ")

            file = f"{file_name}.java"

            package_name = input("Enter A Package Name => ")
        
            with open(os.path.join(parent_dir, file), 'w') as fp:

                fp.writelines(
                    
                f"""package {package_name}

    public @interface {file_name} \u007b

        

            // Enter Your Code Here
            


    \u007d 

                """
                )

            number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
            
            while True: 
            
                if number_of_imports == "0":
                    break

                elif number_of_imports == "1":

                    print("Enter Import")

                    import_1 = input("=> ")
                    
                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(f'import {import_1}\n' + old)
                    
                    break

                if number_of_imports == "2":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}\n''' + old)

                    break

                elif number_of_imports == "3":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}\n''' + old)

                    break

                if number_of_imports == "4":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}\n''' + old)

                    break

                elif number_of_imports == "5":

                    print("Enter Import #1")

                    import_1 = input("=> ")

                    print("Enter Import #2")

                    import_2 = input("=> ")

                    print("Enter Import #3")

                    import_3 = input("=> ")

                    print("Enter Import #4")

                    import_4 = input("=> ")

                    print("Enter Import #5")

                    import_5 = input("=> ")

                    with open(os.path.join(parent_dir, file), 'r+') as fp:
                        old = fp.read()
                        fp.seek(0)
                        fp.writelines(
                            
                        f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}\n''' + old)

                    break
    
    if answer == "4":

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.js"

        with open(os.path.join(parent_dir, file), 'w') as fp:

            fp.writelines("")

    if answer == "5":

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.html"

        with open(os.path.join(parent_dir, file), 'w') as fp:

            fp.writelines("")

    if answer == "6":

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.css"

        with open(os.path.join(parent_dir, file), 'w') as fp:

            fp.writelines("")

    if answer == "7":

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.c"

        with open(os.path.join(parent_dir, file), 'w') as fp:
            fp.writelines("")

    if answer == "8":

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.cpp"

        with open(os.path.join(parent_dir, file), 'w') as fp:
            fp.writelines("")

        





if startup == "2":

    answer = input("""

Enter An Application Type

[1] - Bundle - [HTML, JS, CSS]
[2] - Python

=> """)

    print("")


    

    
    if answer == "2":

        projectbase.create_dir()

        file_name = input("Enter A File Name => ")

        file = f"{file_name}.py"

        with open(os.path.join(parent_dir, file), 'w') as fp:

            fp.writelines("")

        number_of_imports = input("Enter A Number Of Imports [MAX = 5] => ")
        
        while True: 
        
            if number_of_imports == "0":
                break

            elif number_of_imports == "1":

                print("Enter Import")

                import_1 = input("=> ")
                
                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(f'import {import_1}')
                
                break

            if number_of_imports == "2":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}''')

                break

            elif number_of_imports == "3":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                print("Enter Import #3")

                import_3 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}
import {import_3}''')

                break

            if number_of_imports == "4":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                print("Enter Import #3")

                import_3 = input("=> ")

                print("Enter Import #4")

                import_4 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}''')

                break

            elif number_of_imports == "5":

                print("Enter Import #1")

                import_1 = input("=> ")

                print("Enter Import #2")

                import_2 = input("=> ")

                print("Enter Import #3")

                import_3 = input("=> ")

                print("Enter Import #4")

                import_4 = input("=> ")

                print("Enter Import #5")

                import_5 = input("=> ")

                with open(os.path.join(parent_dir, file), 'w') as fp:
                    fp.writelines(
                        
                    f'''import {import_1}
import {import_2}
import {import_3}
import {import_4}
import {import_5}''')

                break


            

            
        
    if answer == "1":

        directory = input("Enter A Project Name => ")
    
        # Parent Directory path
        parent_dir = os.getcwd()
        
        # Path
        path = os.path.join(parent_dir, directory)
        

        os.mkdir(path)

                
        file1 = "index.html"

        with open(os.path.join(path, file1), 'w') as fp:

            fp.writelines("")

        print("")

        file2 = "index.js"

        with open(os.path.join(path, file2), 'w') as fp2:

            fp2.writelines("")

        print("")

        file3 = "style.css"

        with open(os.path.join(path, file3), 'w') as fp3:

            fp3.writelines("")
                
                

        
        
        

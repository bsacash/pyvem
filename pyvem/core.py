import pathlib
import os

import subprocess






def shell_type():
    shell = os.environ["SHELL"]
    return shell

def add_function():
    pass



# Verifiies there is a .pyvem directory and tries to create one if one does not exist
def health_check():
    home = str(pathlib.Path.home())
    path = os.path.join(home, ".pyvem")



    if not os.path.exists(path):
        print( "-------------------------------------------")
        print( "It looks like you just installed PyVEM.")
        print(f"Creating environment directory: {path} ")
        print("--> You will need to add a helper function to your bash profile.")
        print("--> Please add the following code.")
        print("""
        # PyVEM
        pyvem(){
            command=$1
            argument=$2

            if [ "$1" == "activate" ]; then
                source $HOME"/.pyvem/"$2"/bin/activate"
            elif [ "$command" = "deactivate" ]; then
                deactivate
            else
                command pyvem "$@"
            fi
        }
        """)
        print("\n")
        print("You will need to restart you console for PyVEM to work properly.")
        print("-----------------------------------------")
        try:
            os.mkdir(path)
            healthy = True
        except:
            print(f"Could not create PyVEM directory in '{home}'")
            healthy = False
    else:
        healthy = True

    return healthy


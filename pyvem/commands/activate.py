"""List all PyVEM virtual environments"""
import os
from .base import Base

class Activate(Base):
    def run(self):
        print("""
        It looks like you still need to configure PyVEM.
        In order for the 'activate' command to work within PyVEM
        you will need to add the following code to you bash profile.""")

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
"""Create a requirments.txt file for the current environment"""
import os
import subprocess
from .base import Base

class Req(Base):
    def run(self):

        #TODO next line breaks if not in env (I think its the pip/pip3 issue)
        proc = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
        if proc.returncode == 0:
            output = proc.stdout #byte string

            try:
                with open("requirements.txt", "w") as text_file:
                    output = output.decode("utf-8")
                    for line in output.split("\n"):
                        print(line, file=text_file)
            except:
                print("There was an issue creating your requirements file.")
        else:
            print(f"There was an issue finding your requirements. Return code: {proc.returncode}")

"""Creates a new virtual environment"""
import os
import subprocess

from .base import Base


class Create(Base):
    def run(self):

        # get a list of all environments in .pyvem
        def list_environments():
            return [
                d
                for d in os.listdir(self.path)
                if os.path.isdir(os.path.join(self.path, d))
            ]

        venv_name = self.options["<name>"]
        python_interpreter = self.options["--python"]

        if venv_name in list_environments():
            print("An environment with the name '{}' already exists.".format(venv_name))
        else:
            venv = os.path.join(self.path, venv_name)
            return_value = subprocess.run(
                [python_interpreter, "-m", "venv", os.path.join(self.path, venv_name)]
            )
            if return_value.returncode == 0:
                print("Environment '{}' created successfully.".format(venv_name))
            else:
                print(
                    "Environment could not be created. Return code: {}".format(
                        return_value.returncode
                    )
                )

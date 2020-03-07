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
        if venv_name in list_environments():
            print(f"An environment with the name '{venv_name}' already exists.")
        else:
            venv = os.path.join(self.path, venv_name)
            return_value = subprocess.run(
                ["virtualenv", os.path.join(self.path, venv_name)]
            )
            if return_value.returncode == 0:
                print(f"Environment '{venv_name}' created successfully.")
            else:
                print(
                    f"Environment could not be created. Return code: {return_value.returncode}"
                )

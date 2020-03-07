# PyVEM

The Python Virtual Enviroment Manager is a wrapper around the `virtualenv` library, providing a command line interface that better organizes Python environments. It provides quick access to the most commonly used aspects of virtual enviroments.

## Getting Started
```
pip install pyvem
```

After PyVEM is installed you will need to add a function to your `.bash_profile` in order to create a more seamless experience for activating environments. You will need to restart your console after adding this function. This first time you try to activate an environment you will be provided the function.
PyVEM will create a hidden directory in your home directry to store all PyVEM environments.

## The Basics
Create a new virtual environment.
```
$ pyvem create my_env
```
See all of your PyVEM environemnts.
```
$ pyvem list
```
Activate an environment.
```
$ pyvem activate my_env
```
Deactivate your environment
```
$ pyvem deactivate
```
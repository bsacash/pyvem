# PyVEM

The Python Virtual Enviroment Manager is a wrapper around the `virtualenv` library, providing a command line interface that better organizes Python environments. It provides quick access to the most commonly used aspects of virtual enviroments.

## Getting started
```
pip install pyvem
```

When PyVEM is installed it will add a function to your `.bash_profile` in order to create a more seamless experience for activating environments. You will need to restart your console after you install PyVEM.
PyVEM will create a hidden directory in your home directry to store all PyVEM environments.

## The basics
Create a new virtual environment.
```
pyvem create my_env
```
See all of your PyVEM environemnts.
```
pyvem list
```
Activate an environment.
```
pyvem activate my_env
```
Deactivarte your environment
```
pyvem deactivate
```



## Jupyter
PyVEM makes it easy to add enviroments as kernels into Jupyter Notebooks.
```
pyvem jupyter --add my_env
```




pyvem create <name> -t tag_name -d this is a description

create from requirments.txt
pyvem build <name> - uses the requirments.txt it sees (like a Dockerfile build)
pyvem remove <name>



# Jupyter
pyvem jupyter --add  --drop <name>  - add kernel


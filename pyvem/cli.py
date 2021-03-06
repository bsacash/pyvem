"""
Usage:
  pyvem create [-p py | --python py] <name> 
  pyvem activate <name>
  pyvem deactivate
  pyvem list
  pyvem req
  pyvem -h | --help
  pyvem --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Commands:
  activate                          Activate an existing PyVEM virtual environment.
  create                            Create a new PyVEM  virtual environment.
  deactivate                        Deactivate a virtual environment.
  list                              See all available PyVEM virtual environments.
  req                               Create a requirments.txt file for the active PyVEM environment.

Optional Arguments:
  -p py, --python py                Target interpreter for which to create a virtual environment (either absolute path or identifier string) [default: python3].

Examples:
  pyvem create -p python3 my_env

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/bsacash/pyvem
"""


from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

from .core import health_check


def main():

    if not health_check():
        print("Something went wrong.")

    """Main CLI entrypoint."""
    import pyvem.commands

    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(pyvem.commands, k) and v:
            module = getattr(pyvem.commands, k)
            pyvem.commands = getmembers(module, isclass)
            command = [
                command[1] for command in pyvem.commands if command[0] != "Base"
            ][0]
            command = command(options)
            command.run()

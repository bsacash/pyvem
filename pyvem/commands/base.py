import pathlib
import os

"""The base command."""


class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

        self.home = str(pathlib.Path.home())
        self.path = os.path.join(self.home, ".pyvem")

    def run(self):
        raise NotImplementedError("You must implement the run() method yourself!")

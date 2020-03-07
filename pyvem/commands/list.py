"""List all PyVEM virtual environments"""
import os
from .base import Base

class List(Base):
    def run(self):
        # get a list of all environments in /.pyvem
        print([d for d in os.listdir(self.path) if os.path.isdir(os.path.join(self.path,d))])
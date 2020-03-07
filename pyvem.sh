#!/bin/bash



# PyVEM - Python Virtual Environment Manager
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




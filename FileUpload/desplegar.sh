#!/bin/bash
# Comprobar si el archivo existe
if [ ! -f /opt/lampp/manager-linux-x64.run ]; then
  echo "El archivo /opt/lampp/manager-linux-x64.run no existe."
  exit 1
fi
# Comprobar si el usuario tiene permisos para ejecutar el archivo
if [ ! -x /opt/lampp/manager-linux-x64.run ]; then
  echo "El usuario no tiene permisos para ejecutar el archivo /opt/lampp/manager-linux-x64.run."
  exit 1
fi
# Ejecutar el archivo
sudo /opt/lampp/manager-linux-x64.run

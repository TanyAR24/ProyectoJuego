# Proyecto de personajes

## Descripción
Este proyecto simula una batalla entre personajes con los siguientes atributos: nombre, vida, fuerza, defensa y ataque_sorpresa
Se implementa en Python y se realizan pruebas unitarias con unittest

Se crea un requirements.txt con:
pip freeze > requirements.txt
# Instalación
Hay que tener python 3.10.12 instalado en el sistema. 
unittest viene incluido en esta versión de python
Luego instalar las dependencias con:
pip install -r requirements.txt


## Cómo ejecutar las pruebas
Las pruebas están organizadas en la carpeta ./tests dentro del proyecto. Para ejecutar las pruebas tenés que estar en la raíz del proyecto y luego ejecutarse el siguiente comando:
python3 -m unittest discover -s tests

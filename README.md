# ProjectUML

Este es el proyecto realizado durante mi TFG. Este repositorio incluye los archivos necesarios para poder desplegar una aplicación en Django llamada Gymkhana App. 

Se trata de una sencilla aplicación web para uso docente y estudiantil a través de la cual alumnos de tempranas edades puedan aprender y familiarizarse con actividades que impliquen de alguna manera el entender y analizar diagramas UML para extraer información de estos y conseguir resolver diferentes retos y juegos. 

### Pre-requisitos 

Python 3.7.3 o superior. 

Tener acceso a una terminal de comandos y poder instalar paquetes en un entorno de desarrollo. 

### Instalación
```
git clone https://github.com/jorgedepablo/ProjectUML.git 
cd ProjectUML 
pip install -r requirements.txt --user
python manage.py runserver
```
Por defecto la aplicación corre en localhost, el el puerto 8000. 


### Funcionamiento esperado

Una vez dentro de la aplicación, se podrán cargar en la base de datos usuarios, retos y juegos. El objetivo es que los usuarios naveguen a través de los menús para seleccionar el reto o juego deseado. 

Los retos consisten en resolver un acertijo o cuestión que esté relacionado con una imagen en la que se muestra un diagrama UML, indicando de que tipo es y una breve descripción del mismo. El usuario debe cumplimentar su respuesta en una caja de formulario y se comprobará si es correcta para poder avanzar. 

Se puede ver una versión desplegada de este repositorio, con una base de datos rellena para pruebas en este [enlace](https://project-uml.herokuapp.com/)
## Autores

* **Jorge De Pablo Martínez** - https://github.com/jorgedepablo - [LinkedIn](https://www.linkedin.com/in/jorge-de-pablo-mart%C3%ADnez-45291117a/)

Ver también lista de  [contribuidores](https://github.com/jorgedepablo/ProjectUML/network/dependencies) que han participado en este proyecto.

## License 

Este proyecto se ha hecho bajo una licencia GNU General Public License v3.0 - ver el archivo [LICENSE](LICENSE) para más detalles.
# Guia básica para usar git y github  

*Primer paso:* clonar la rama main
Existen 2 maneras de llevar el repositorio de github a tu repositorio local (el de tu compu) Elegi UNA.

La primera es a traves del comando clone:

git init

git clone https://github.com/LourdesIR/IntegradorTSIT4.0_1.git

(el link https lo encontras en github en el boton "code" lo copias y lo pegas talcual esta -- termina siempre en .git) Esta manera te crea la carpeta tal cual esta en la rama main

La segunda manera es con la conexion remota:

creamos una carpeta en nuestra compu y la abrimos en el visual studio code en la terminal que viene en visual estudio nos posicionamos en esa carpeta entonces ponemos:

git init git remote add origin https://github.com/LourdesIR/IntegradorTSIT4.0_1.git git pull origin main

*Segundo paso:* creamos nuestra rama (tambien existen varias maneras)
1 - La primera forma y mas sencilla es usando el siguiente comando: git checkout -b nombreRama Este comando copia la rama actual en la que estamos (main) y nos genera una nueva - en este caso la rama se llamara 'nombreRama'

2 - Una segunda forma: git branch nombreRama (se crea la rama pero aun estas ubicadx en main) git checkout nombreRama (debes moverte a la rama creada)

*Tercer paso:* Creamos los archivos
Crea todos los que necesitemos con las funciones que debemos realizar. Puede ser uno por cada funcion o uno para las que te toquen. *** Si necesitas usar una funcion de otro archivo solo debes importarla y llamarla ***

import nombreArchivoQueTieneLaFuncion: para usarla debes poner: archivo.nombrefuncion

*Cuarto paso:* Guardamos los cambios que realizamos
Una vez culminada la tarea, guardamos los cambios primero vemos que cambios tenemos hecho y que archivos modificamos o creamos. para eso usamos git status (los archivos en rojo son los NO guardados) para agregar esos cambios lo mejor de todo es ir viendolos uno por uno usamos git add -p ponemos 'y' para los que queremos guardar y 'n' para los que queremos rechasar. este formato muchas veces no te agrega los archivos creados desde cero. asique verifica con git status nuevamente . Si no queres ver uno por uno los cambios y estas MUY segurx de lo que hiciste podes poner directamente git add . esto te agrega absolutamente todos los cambios generados.

*Quinto paso:* Subir los cambios a github.
Como creaste una rama nueva, la manera de subir los cambios difiere un poco. Debes poner: git push origin nombreRama y ya casi estamos

*Sexto paso:* Pull request
Como hicimos rama nueva y queremos tener todo lo "entregable" en una sola rama, debemos enviar nuestros cambios a pull request con la rama main. (la rama main sera la rama base) Vas a la solapa "pull requests" pones "new pull request" y te aparecen 2 desplegables para elegir ramas.

La rama base debe ser main (como esta por defecto) la otra rama debe ser la que vos acabas de subir. una vez elegidas pones "create pull request" (podes cambiar el titulo y poner un comentario de los cambios)


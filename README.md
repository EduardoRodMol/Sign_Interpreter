# SignInterpreter

## Descripción

Creación del juego clasico de "piedra, papel o tijeras" a través del modelo de machine learning de mediapipe "Hands", que sea capaz de reconocer tres gestos básicos como serían la mano abierta (papel), la mano cerrada (piedra) y dedos índice y corazón levantados (tijera), para posteriormente ampliarlo al abecedario del lenguaje de signos y gestos.

El Objetivo es desplegar la aplicacion en una web que sea capaz de activar la webcam y reconocer los gestos.

## Developers

Eduardo Rodriguez => https://github.com/EduardoRodMol



## Dataset

El dataset ha sido creado directamente por nosotros usando mediapipe y opencv, capturando la imagen de las manos y almacenándola con su correspondiente label.

## Fuentes

- https://google.github.io/mediapipe/solutions/hands.html
- https://developers.googleblog.com/2021/04/signall-sdk-sign-language-interface-using-mediapipe-now-available.html
- https://laptrinhx.com/mediapipe-hand-gesture-based-volume-controller-in-python-w-o-gpu-1503882022/
- https://medium.com/analytics-vidhya/mediapipe-fingers-counting-in-python-w-o-gpu-f9494439090c
- https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe/blob/main/README_EN.md

## Uso web

Si quieres usar nuestra app directamente visitando un enlace web, ¡Estás de suerte!, hemos desplegado nuestra aplicación en la plataforma Heroku, asi que clica en este enlace. Ahora te guiaré a través de las diferentes páginas que puedes seleccionar en la columna de la izquierda.

### Main Page

Aquí puedes encontrar un breve resumen del proyecto, información sobre el dataset y nuestras cuentas de github.

### Game

Aquí ya puedes jugar al piedra, papel o tijera contra la máquina.
Primero clica en el botón run, se te abrirá una ventana donde debes dar a SELECT DEVICE, después permite el uso de tu cámara al navegador, tras esto podrás elegir que cámara quieres usar. Cuando la tengas haz click en DONE, volverás a la pantalla inicial, clica en START, ahí empezarás a ver tu imagen en la pantalla y el juego comenzará.
Cuando quieras dejar de jugar solo clica en STOP y se cerrará la cámara.

### How does it work?

Aquí explicamos como funciona Mediapipe, que es el framework que hemos utilizado para captar los keypoints de la mano y así saber la posición de los dedos e identificar las diferentes opciones de piedra, papel y tijeras.



## Uso local

Para realizar uso de la aplicación en tu dispositivo local empieza por clonar el repositorio, después necesitarás una cámara web e instalar estas librerías.

``` shell
pip install tensorflow numpy opencv-python scikit-learn
```
Una vez que hayas completado estos pasos, podrás usar las funciones de nuestra aplicación.

### Crear Dataset

Una de las funciones que puedes realizar es aumentar el dataset, grabando tu mismo las imágenes para el modelo de machine learning. Para esto debes moverte dentro de la carpeta SignInterpreter, y ejecutar este comando.

``` shell
python getdata.py
```

A continuación se abrirá una ventana con la imagen de tu cámara, y comenzará la secuencia de grabación de frames, en pantalla verás si es piedra, papel o tijera y el número del frame en el que te encuentras, solo tendrás que colocar la mano en la posición requerida.

Cuando el proceso finalice se cerrará la ventana automáticamente, y podrás ver que se ha creado una carpeta nueva por cada elección dentro de MP_Data nombrada con la fecha y la hora de realización, donde están almacenados los valores que has creado.

## Entrenar el modelo

Esta función no requiere que hagas nada salvo correr este comando, ya que el dataset ya está almacenado y la red neural creada. Cuando finalice el entrenamiento, visualizarás una confusion matrix y el accuracy score del modelo.

``` shell
python training_model.py
```

### Probar el modelo

Para probar el modelo entrenado, prepara tu cámara y corre este comando.

``` shell
python testing_model.py
```

Se abrirá una ventana con la imagen de tu cámara y ya podrás colocar tu mano en una de las tres opciones y ver como el modelo saca por pantalla la predicción de lo que has elegido. Para dejar de probar el modelo pulsa la tecla "q" o cierra el programa con ctrl+c desde la terminal.

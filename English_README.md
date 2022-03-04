# SignInterpreter

## Summary

This project would provide an efficient sign interpreter through your camera device. Our first goal consists of developing the classic game "Rock, paper, scissors", thanks to the framework
mediapipe which benefits from machine learning to recognise hand's gestures and convert them to a message.

Once we accomplish this objetive, we want to escalate our project for being able to recognise sign language and display the message on the screen in real time. This would be an
awesome tool for people who are unable to use verbal communication to make themself understood easier.


## Developers

Eduardo Rodriguez => https://github.com/EduardoRodMol

Borja Espés => https://github.com/BorjaEACode

## Dataset
The dataset has been created by us, using mediapipe and opencv, capturing the images of both hands and storing them which its matching label.

## Sources

- https://google.github.io/mediapipe/solutions/hands.html
- https://developers.googleblog.com/2021/04/signall-sdk-sign-language-interface-using-mediapipe-now-available.html
- https://laptrinhx.com/mediapipe-hand-gesture-based-volume-controller-in-python-w-o-gpu-1503882022/
- https://medium.com/analytics-vidhya/mediapipe-fingers-counting-in-python-w-o-gpu-f9494439090c
- https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe/blob/main/README_EN.md

# Local Use

For using this application on your local device, first of all clone the repository, next you will need to install these libraries and a functional webcam.

``` shell
pip install tensorflow numpy opencv-python scikit-learn
```
Once you had fulfilled these requirements, you will be able to use our application.

## Creating Dataset

One of the features which you can execute is augmenting the dataset, recording yourself the images for the machine learning model. For this purpose you should place yourself inside SignInterpreter folder, and run this command.

``` shell
python getdata.py
```

Hereafter, a window will pop up showing the footage of your webcam, and begin the sequence of collecting frames, on the screen you should see if the choice is rock, paper or scissors and which frame you are recording, you just have to show your hand in the requered position.

When this process finish the window will close automatically, and you could see that a folder has been created for each choice inside MP_Data folder named with the date and time when has been made, where the created values are stored.

## Model training

This feature does not require anything but running this command, since the dataset is already stored and the neural network trained. When the training is finished, you will see the confussion matrix and the accuracy score.

``` shell
python training_model.py
```

## Model testing

For testing the trained model, get your camera ready and run this command.

``` shell
python testing_model.py
```
A window will pop up with the camera's footage, now you can show your hand with one of the three options and seeing how the model predicts your choice and print on screen your choice predicted. For stopping the function, just press "q" or ctrl+c in the terminal.
Para probar el modelo entrenado, prepara tu cámara y corre este comando.

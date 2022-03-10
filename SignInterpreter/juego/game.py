#va a recibir la prediccion, aleatoriamente sacara piedra papel o tijera, y actualizara label y un marcador. 
#This class is going to recevice the prediction, will select a randow between stone, paper and scissors, and update the label with the winner.
import random

gesto = ['stone','paper','scissors']

def selecciona_random(gesto):
   
    return random.choice(gesto)

def traductor(predict):
    texto= "scissors"
    if predict == "piedra":
        texto = "stone"
    if predict == "papel":
        texto = "paper"
    return texto

def juego (predict):    
    machine = selecciona_random(gesto)  
    texto = traductor(predict)
    resultado  = ""  
    if texto == machine:
        resultado = "Draw"
        resultado= resultado +" player: " + texto + " manchine: " + machine
        return resultado
    if texto == "stone":
            if machine =="paper":
                resultado="game over"
            else:
                resultado="humans wins"
    if texto ==  "paper":
            if machine == "scissors":
                resultado="game over"             
            else:
                resultado="humans wins"               
    if texto ==  "scissors":
            if machine == "stone":
                resultado="game over"
            else:
                resultado="humans wins"
    resultado= resultado +" player: " + texto + " manchine: " + machine
    return resultado
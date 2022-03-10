#va a recibir la prediccion, aleatoriamente sacara piedra papel o tijera, y actualizara label y un marcador. 
#This class is going to recevice the prediction, will select a randow between stone, paper and scissors, and update the label with the winner.
import random

gesto = ['piedra','papel','tijera']

def selecciona_random(gesto):
   
    return random.choice(gesto)


def juego (predict):    
    machine = selecciona_random(gesto)    
    if predict == machine:
        return "empate " + "jugador: "+predict + " maquina prediccion: " + machine    
    if predict == "piedra":
            if machine =="papel":
                return "game over " + "jugador: "+predict + " maquina prediccion: " + machine
            else:
                return "humans wins " + "jugador: "+predict +  " maquina prediccion: " + machine
    if predict ==  "papel":
            if machine == "tijera":
                return "game over " + "jugador: "+predict + " maquina prediccion: " + machine
            else:
                return "humans wins " + "jugador: "+predict + " maquina prediccion: " + machine
    if predict ==  "tijera":
            if machine == "piedra":
                return "game over jugador: "+ predict + " maquina prediccion: " + machine
            else:
                return "humans wins " + "jugador: "+predict + " maquina prediccion: " + machine


    
                

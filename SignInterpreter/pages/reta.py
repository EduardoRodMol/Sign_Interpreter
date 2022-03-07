from juego.game import juego, gesto, selecciona_random

for i in range (10):
    predict =  selecciona_random(gesto)
    print(juego (predict))
   
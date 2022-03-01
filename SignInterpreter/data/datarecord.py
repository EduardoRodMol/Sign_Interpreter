import os
import numpy as np
from datetime import datetime

DATA_PATH = os.path.join(os.getcwd(),"MP_Data") 

# Actions that we try to detect
actions = np.array(["piedra", "papel", "tijeras"])

#Create folder when dataset was created
datadate = (datetime.now()).strftime("%d-%m-%Y %H-%M-%S")

# Thirty videos worth of data
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 30


def create_folder():
    for action in actions: 
        for sequence in range(no_sequences):
            try: 
                os.makedirs(os.path.join(DATA_PATH, action, datadate, str(sequence)))
            except:
                pass



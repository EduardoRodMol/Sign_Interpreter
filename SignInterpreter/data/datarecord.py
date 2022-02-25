import os
import numpy as np

DATA_PATH = os.path.join(os.getcwd()+'/MP_Data') 

# Actions that we try to detect
actions = np.array(['piedra', 'papel', 'tijeras'])

# Thirty videos worth of data
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 30



for action in actions: 
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass



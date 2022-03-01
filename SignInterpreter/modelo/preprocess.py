import tensorflow
from sklearn.model_selection import train_test_split
from data.datarecord import actions, no_sequences, sequence_length, DATA_PATH
import numpy as np
import os


def labeling():
    label_map = {label:num for num, label in enumerate(actions)}

    sequences, labels = [], []
    for action in actions:
        for dir in os.listdir(os.path.join(DATA_PATH, action)):
            for sequence in range(no_sequences):
                window = []
                for frame_num in range(sequence_length):
                    res = np.load(os.path.join(DATA_PATH, action, dir, str(sequence), "{}.npy".format(frame_num)))
                    window.append(res)
                sequences.append(window)
                labels.append(label_map[action])

    X = np.array(sequences)
    y = tensorflow.keras.utils.to_categorical(labels).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    return X_train, X_test, y_train, y_test

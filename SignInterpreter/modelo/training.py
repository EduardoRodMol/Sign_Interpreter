from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Dense
from tensorflow.python.keras.callbacks import TensorBoard
from sklearn.metrics import  multilabel_confusion_matrix, accuracy_score
from data.datarecord import actions
from modelo.preprocess import labeling
import numpy as np
import os

def fitting():
    X_train, X_test, y_train, y_test = labeling()

    log_dir = os.path.join(os.getcwd(),"Logs")
    tb_callback = TensorBoard(log_dir=log_dir)
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation="relu", input_shape=(30,126)))
    model.add(LSTM(128, return_sequences=True, activation="relu"))
    model.add(LSTM(64, return_sequences=False, activation="relu"))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(actions.shape[0], activation="softmax"))

    model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["categorical_accuracy"])
    model.fit(X_train, y_train, epochs=500, callbacks=[tb_callback])


    model.save(os.getcwd()+"/action.h5")

    model.load_weights("action.h5")
    y_pred = model.predict(X_test)
    y_test = np.argmax(y_test, axis=1).tolist()
    y_pred = np.argmax(y_pred, axis=1).tolist()
    print(multilabel_confusion_matrix(y_test,y_pred))
    print(accuracy_score(y_test,y_pred))

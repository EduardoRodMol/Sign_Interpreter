from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
from data.datarecord import actions
from modelo.preprocess import labeling
import os

def fitting():
    X_train, X_test, y_train, y_test = labeling()

    log_dir = os.path.join(os.getcwd()+'Logs')
    tb_callback = TensorBoard(log_dir=log_dir)
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(actions.shape[0], activation='softmax'))

    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    model.fit(X_train, y_train, epochs=200, callbacks=[tb_callback])


    model.save(os.getcwd()+'action.h5')
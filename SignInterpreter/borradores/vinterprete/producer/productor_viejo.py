#import sys
#sys.path.append("../")
from aiokafka import AIOKafkaProducer
import asyncio
import json
#import videoprocesador
from interprete.producer.utils.configuracion import *
#from utils.scraper import getdatapoint
import os
from tensorflow.python.keras.models import load_model
from data.keypoints import mp_holistic, mediapipe_detection, draw_styled_landmarks
from data.values import extract_keypoints
from data.datarecord import actions


def serializer(value):
    return json.dumps(value).encode()



async def send(loteimg,holistic):
    print("enviando...")
    producer = AIOKafkaProducer(
        bootstrap_servers=bootstrap_servers_url, # Our Kafka Connection
        value_serializer=serializer) # So JSON can be sent as messages
    await producer.start()
    print("connected")
    model = load_model("action.h5")

    try:
        for img in loteimg:
            image, results = mediapipe_detection(img, holistic)
            draw_styled_landmarks(image, results)
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-10:]
            #self.contador = self.contador +1
            
            print(keypoints)

            if len(sequence) == 10:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                label = actions[np.argmax(res)]
                print(label)

            await 62.send_and_wait(topic_name, label) # Define a topic when you send a message
                                                          # This way, they can be sorted by different consumers
    finally:
        await producer.stop()


#import sys
#sys.path.append("../")
from aiokafka import AIOKafkaProducer
#import asyncio
import json
#import videoprocesador
from interprete.producer.utils.configuracion import *
#from utils.scraper import getdatapoint
import os
def serializer(value):
    return json.dumps(value).encode()

def vari(loquesea):
    for l in loquesea:
        print(l)

async def send(sequence):
    
    
    producer = AIOKafkaProducer(
        bootstrap_servers=bootstrap_servers_url, # Our Kafka Connection
        value_serializer=serializer) # So JSON can be sent as messages
    await producer.start()
    print("connected")
    try:
        for keypoint in sequence:
        
            await producer.send_and_wait(topic_name, keypoint) # Define a topic when you send a message
                                                          # This way, they can be sorted by different consumers
    finally:
        await producer.stop()


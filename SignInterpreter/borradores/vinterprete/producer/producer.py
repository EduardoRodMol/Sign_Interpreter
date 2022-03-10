from aiokafka import AIOKafkaProducer
import asyncio
import json


def serializer(value):
    return json.dumps(value).encode()


async def send(label):
    print("enviando...")
    producer = AIOKafkaProducer(
        bootstrap_servers=bootstrap_servers_url, # Our Kafka Connection
        value_serializer=serializer) # So JSON can be sent as messages
    await producer.start()
    print("connected")
    
    keypoint = extraerkeypoints
    try:           
        await producer.send_and_wait(topic_name, label) # Define a topic when you send a message
                                                          # This way, they can be sorted by different consumers
    finally:
        await producer.stop()

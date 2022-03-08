import pickle
from aiokafka import AIOKafkaProducer
import json
from config import BOOTSTRAP_SERVERS, TOPIC
import asyncio
global producer


def serializer(value):
    return pickle.dumps(value)
    # return json.dumps(value).encode()


async def connect_kafka():
    global producer
    print(f"Connecting to topic {TOPIC}...")
    producer = AIOKafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,  # Our Kafka Connection
        value_serializer=serializer)  # So JSON can be sent as messages
    await producer.start()
    print(f"Kafka ready {BOOTSTRAP_SERVERS}")


async def local_send_frame(img):
    print("Sending frame")
    try:
        await producer.send_and_wait(TOPIC, img)
    except Exception as e:
        print(e)
    print("Frame sent to kafka")


def send_frame_kafka(img):
    frame_data = img.to_ndarray()

    # Extract keypoints
    # ...

    # Run the task
    loop = asyncio.get_running_loop()
    task = loop.create_task(local_send_frame(frame_data))
    # print(task)

    print(f"Frame keypoints sent to kafka topic {TOPIC}")

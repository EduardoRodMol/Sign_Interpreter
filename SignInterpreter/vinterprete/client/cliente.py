
from tokenize import group
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer


# Connect to a kafka broker to produce and consume messages
BROKERS = ["localhost:29092"]

# This is the default topic to produce and consume messages
DEFAULT_TOPIC = "hand_keypoints"


def get_producer():
    return AIOKafkaProducer(bootstrap_servers=BROKERS)


def get_consumer(group_id, topic=DEFAULT_TOPIC,auto_offset_reset="latest"):
    return AIOKafkaConsumer(
        topic,
        bootstrap_servers=BROKERS,
        group_id=group_id, auto_offset_reset=auto_offset_reset)

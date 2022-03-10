import os


bootstrap_servers_url = os.getenv("KAFKA_BOOTSTRAP_URL", 'localhost:29092')
topic_name = os.getenv("TOPIC_NAME", "hand_keypoints")
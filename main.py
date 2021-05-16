from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import os
from dotenv import load_dotenv,find_dotenv

import modules.BackRequest as BR
import modules.SlackMessage as SM


load_dotenv(find_dotenv())


print("Start MongoDB Consumer Server!")


# Kafka Config
consumer = KafkaConsumer(
    os.environ.get("KAFKA_TOPIC"),
    bootstrap_servers=[os.environ.get("BOOTSTRAP_SERVERS")],
    auto_offset_reset=os.environ.get("AUTO_OFFSET_RESET"),
    enable_auto_commit=os.environ.get("enable_auto_commit"),
    group_id=os.environ.get("group_id"),
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Mongo Config
client = MongoClient(os.environ.get("MONGO_CLIENT"), username=os.environ.get("MONGO_USERNAME"), password= os.environ.get("MONGO_PASSWORD"))
collection = client.admin.packets

for message in consumer:
    print("\nnew message!")
    print("topic=%s partition=%d offset=%d: key=%s value=%s" % (message.topic, message.partition,
                                                                message.offset, message.key,
                                                                message.value))
    # Parsing
    message = message.value
    trapId = message["SPU"]["MPU"]["trapId"]
    cmd = message["SPU"]["MPU"]["cmd"]
    if cmd == '2':
        BR.send_message_to_backend(trapId, cmd)
        slackText = "TrapId: " + trapId + "Warning!." + "Command is" + cmd + "."
        SM.send_message_to_slack(slackText, "ghost")

    print("Trapid: %s, cmd : %s" % (trapId, cmd))
    isRead = {
        'is_read': False
    }
    message.update(isRead)
    if collection.insert_one(message):
        print("data inserted to mongoDB.")
    else:
        print("Error. Data not inserted.")



import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# Back request
def send_message_to_backend(trap_id, command):
    backUrl = os.environ.get("BACK_URL")
    sendData = {'trapId': trap_id, 'item': command}
    requests.post(backUrl, data=sendData)

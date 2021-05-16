# Slack method
import time
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def send_message_to_slack(text,item):
    now = time.localtime()
    if item == 4:
        title = "Warning Alert"
        color = "#ffd400"
        text = "Something got caught in the trap" + "\n" + "TrapId: " + text
    else:
        title = "Error Alert"
        color = "#f55354"
        text = "There was an error in the trap" + "\n" + "TrapId: " + text

    slack_url = os.environ.get("SLACK_URL")
    payload = {
        "attachments": [
            {
                "title": title,
                "text" : text,
                "color": color,
                "attachment_type": "default",
                 "actions": [
                    {
                        "name": "check",
                        "text": "PestPlan.com",
                        "type": "button",
                        "url": "https://naver.com"
                    }
                ],
                "thumb_url": "https://i.postimg.cc/23pSYzN7/Kakao-Talk-Photo-2021-04-06-16-18-17.png",
                "footer": "Pest Plan" + " | " + "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),
                # "footer_icon": logo
            }
        ]
    }
    requests.post(
        slack_url, json=payload,
        headers={'Content-Type': 'application/json'})

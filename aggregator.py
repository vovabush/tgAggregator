from telethon import TelegramClient, events
import json


chats = None
aggregatorChannel = None
api_id = None
api_hash = None

try:
  with open('config.json') as json_file:
    config = json.load(json_file)
    chats = tuple((config["channels"]))
    aggregatorChannel = config["aggregator"]
    api_id = config["api_id"]
    api_hash = config["api_hash"]
except Exception as e:
  print(str(e))

client = TelegramClient("session_name", api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=chats))
async def my_event_handler(event):
  sender = await event.get_sender()
  await client.forward_messages(aggregatorChannel, event.message)

with client:
    client.run_until_disconnected()

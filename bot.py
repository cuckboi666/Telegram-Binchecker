import requests 
from telethon import events, Button, TelegramClient 
import os 
import logging
import json 

logging.basicConfig(level=logging.INFO)

API_ID = "7930366"
API_HASH = "7824ee12eff77f10ad932ce51c45ec53"
TOKEN = "1936824372:AAH38ptyTIEnMes_UC_PB0zpNVPHfEg3rPs"


try:
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None) 
    TOKEN = os.environ.get("TOKEN", None) 

except ValueError:
    print("You forgot to fullfill constants....") 
    print("Bot is quitting brodi....") 
    exit() 

except Exception as e:
    print (f"Error - {str(e)}") 
    print("Bot is quitting....") 
    exit() 

except ApiIdInvalidError:
    print("Your API_ID or API_HASH is Invalid") 
    print("Bot is quitting") 
    exit() 

bot = TelegramClient('bin', API_ID, API_HASH) 
bin = bot.start(bot_token=TOKEN) 

@bin.on(events.NewMessage(pattern="^[!?/]start$")) 
async def start(event): 
    if event.is_group:
        await event.reply("**Bin-Checker is Alive**") 
        return 
    await event.reply(f"**Heya {event.sender.first_name}**\nHeya I'ma Bin-Checker Bot to Check your dirtyass bins", buttons=[
        [Button.url("My source code", "https://github.com/TgxBotz/Bin-Checker")] 
    ])

@bin.on(events.NewMessage(pattern="^[!?/]help$")) 
async def help(event): 
    text = """
**Welcome to HelpMenu Brodies:**

- /start - To start me up 
- /help - To get help 
- /bin - To check those goodies brodi

"""
    

@bin.on(events.NewMessage(pattern="^[!?/]bin")) 
async def binc(event): 
    xx = await event.reply("`Processsing......`") 
    try: 
        input = event.text.split(" ", maxsplit=1)[1] 

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}") 
        res = url.json() 
        vendor = res['data']['vendor'] 
        type = res['data']['type'] 
        level = res['data']['level'] 
        bank = res['data']['bank']
        country = res['data']['country']
        me = (await event.client.get_me()).username 

        valid = f"""
<b> Valid Bin:</b> 

<b>Bin -</b> <code>{input}</code>
<b>Status -</b> <code>Valid Bin</code> 
<b>Vendor -</b> <code>{vendor}</code>
<b>Type -</b> <code>{type}</code> 
<b>Level -</b> <code>{level}</code> 
<b>Bank -</b> <code>{bank}</code> 
<b>Country -</b> <code>{country}</code>

<b>Checked By - @{me}</b> 
<b>User-ID - {event.sender_id}</b>
"""

        await xx.edit(valid, parse_mode="HTML") 
    except IndexError: 
        await xx.edit("Brodi... Please provide that bin to check\n__`/bin yourbin`__")
    except KeyError: 
        me = (await event.client.get_me()).username 
        await xx.edit(f"**➤ Invalid Bin:**\n\n**Bin -** `{input}`\n**Status -** `Invalid Bin`\n\n**Checked By -** @{me}\n**User-ID - {event.sender_id}**")

print ("Successfully Started") 
bin.run_until_disconnected() 

        
        
        
        
       
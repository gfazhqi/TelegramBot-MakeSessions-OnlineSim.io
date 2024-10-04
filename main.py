# In the name of God | Oh bug, be ashamed, I'm under Abbas's protection | coded with love by @Sardar_Cybery
# -------------------------------------------------- Import -------------------------------------------------
try:
    from telethon.sync import TelegramClient
    from telethon.events import NewMessage, CallbackQuery
except ImportError:
    print('Please wait')
    system('pip install telethon')
    print('Telethon installed')
from asyncio import sleep
from Api.Api import Request
from os import system
from json import loads
from KeyBoard.KeyBoard import AllButtons
from os import remove
from Sessinos.SessionCreator import Cr
import logging
logging.basicConfig(filename="log.txt", filemode="a",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------------------------------------- Bot Config ------------------------------------------------

Data = loads(open('Config/Config.json', 'r').read())
client = TelegramClient("main", Data["ApiID"], Data["ApiHash"]).start(
    bot_token=Data["Token"])
# -------------------------------------------------- Bot Body --------------------------------------------------


async def cancel_and_remove(Status):
    remove(f"{Status[1]['number']}.session")
    await sleep(300)
    await Request().cancel(Status[1]["tzid"])


# /start
@client.on(NewMessage(pattern='/start', func=lambda e: e.is_private and e.sender_id in Data["Admins"]))
async def StartMenu(event):
    await client.send_message(event.sender_id, "Hello, welcome to the bot", buttons=AllButtons.admin_buttons)


# get balance
@client.on(CallbackQuery(data='balance', func=lambda e: e.is_private and e.sender_id in Data["Admins"]))
async def GetBalance(event):
    await event.edit("Please wait a moment...")
    await event.edit(f"🔺 Well, let's see how much money we have. It looks like the panel balance is = **{await Request().balance()} dollars**\nHope it's 999999 😍👌", buttons=AllButtons.admin_buttons)


# send country menu
@client.on(CallbackQuery(data='create', func=lambda e: e.is_private and e.sender_id in Data["Admins"]))
async def SendCountryMenu(event):
    await event.edit("😀 Which country's session should I create for you, my master? 🤖", buttons=AllButtons.country_name_buttons)


# select country and request for create session
@client.on(CallbackQuery(func=lambda e: e.is_private and e.sender_id in Data["Admins"]))
async def SelectCountry(event: CallbackQuery.Event):
    CountryID = event.data.decode('utf-8')
    if CountryID.isnumeric():

        await event.edit("Please wait a moment...")
        Status = await Cr(int(CountryID)).try_for_create()

        if len(Status) == 2 and Status[0] == "True":
            await client.send_file(event.sender_id, f"{Status[1]['number']}.session", caption="Here you go, dear master")
            await Request().change_status(6, Status[1]["tzid"])

        if Status == "NO_NUMBER":
            await event.delete()
            await client.send_message(event.sender_id, "💢 Doctor, the site says we don't have numbers for this country 😐\nIf you'd like, try another country and hopefully you'll get what you want 😂😂\n\n🤖Here's your admin panel 😄", buttons=AllButtons.admin_buttons)

        elif Status == "WARNING_LOW_BALANCE":
            await event.delete()
            await client.send_message(event.sender_id, "💸 Doctor, our balance isn't enough for the purchase. Reach into your blessed pocket and top up 💰", buttons=AllButtons.admin_buttons)

        elif Status == "BAD_SERVICE":
            await event.delete()
            await client.send_message(event.sender_id, "❌ Doctor, this number we tried no longer has Telegram service. We got played badly ❌", buttons=AllButtons.admin_buttons)

        elif Status == "ERROR_WRONG_KEY":
            await event.delete()
            await client.send_message(event.sender_id, "❌ Doctor, did you see what happened?\nIt says the APIKEY is wrong 🥹\n\n🔺 How to change it: First go to the API folder, then open the Api.py file and replace the self.APIKEY value with a new Api Key, it's that simple 🤍", buttons=AllButtons.admin_buttons)

        elif len(Status) == 2 and Status[0] == "PhoneNumberBannedError":
            await event.delete()
            await client.send_message(event.sender_id, f"🤭 Doctor, the site played us badly\nThe number I got was banned, those rascals 😂\n\n⭕️ I'll cancel the number purchase myself, no worries 💢\n\n📞 Number: {Status[1]['number']}\n🔋 Purchase code: {Status[1]['tzid']}", buttons=AllButtons.admin_buttons)
            await cancel_and_remove(Status)

        elif len(Status) == 2 and Status[0] == "NotSendCode":
            await event.delete()
            await client.send_message(event.sender_id, f"🤨 Doctor, this one won't send a code\n😅 I'll cancel the purchase so the balance returns to the account 🤙\n\n📞 Number: {Status[1]['number']}\n🔋 Purchase code: {Status[1]['tzid']}", buttons=AllButtons.admin_buttons)
            await cancel_and_remove(Status)

        elif len(Status) == 2 and Status[0] == "PhoneNumberInvalidError":
            await event.delete()
            await client.send_message(event.sender_id, f"🤨 Doctor, Telegram won't accept this number I got\nSo I'll cancel the purchase so the balance returns 😎\n\n📞 Number: {Status[1]['number']}\n🔋 Purchase code: {Status[1]['tzid']}", buttons=AllButtons.admin_buttons)
            await cancel_and_remove(Status)

        elif len(Status) == 2 and Status[0] == "NotSMS":
            await event.delete()
            await client.send_message(event.sender_id, f"🕯 Doctor, unfortunately this number I got didn't come as an SMS and there might be something fishy, so I'll cancel the purchase for the balance to return 😀\n\n📞 Number: {Status[1]['number']}\n🔋 Purchase code: {Status[1]['tzid']}", buttons=AllButtons.admin_buttons)
            await cancel_and_remove(Status)

        elif len(Status) == 2 and Status[0] == "TRY_AGAIN_LATER":
            await event.delete()
            await client.send_message(event.sender_id, "😄 The site is not responding and says to try again later\nI'll cancel the purchase so the balance returns 🤨", buttons=AllButtons.admin_buttons)
            await cancel_and_remove(Status)

        elif len(Status) == 2 and Status[0] == "FloodWaitError":
            await event.delete()
            await client.send_message(event.sender_id, f"🤡 The number I got has been requested for codes so many times it's gone bad\nI'll cancel the purchase and you can get another number\n\n📞 Number: {Status[1]['number']}\n🔋 Purchase code: {Status[1]['tzid']}", buttons=AllButtons.admin_buttons)
            await cancel_and_remove(Status)

print('Bot is online')
client.run_until_disconnected()

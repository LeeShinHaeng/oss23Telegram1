import asyncio
from aiogram import Bot, Dispatcher, types
import datetime

async def send_time():
    #TOKEN : token of your chatbot
    #NAME : name of your channel, start with @
    	#example : @chat_name
    token = "TOKEN"
    public_chat_name = "NAME"

    bot = Bot(token=token)
    dispatcher = Dispatcher(bot=bot)
    
    # 시간을 보내는 함수
    async def job():
        #현재시간 및 회피 시간 설정
        now = datetime.datetime.now()
        if now.hour >= 23 or now.hour < 6:
            return
        text = "현재 시간: "+ now.strftime('%H:%M:%S')
        await bot.send_message(chat_id=public_chat_name, text=text)
    
    # 대기 시간 설정(초단위)
    while True:
        await job()
        await asyncio.sleep(1800)  

async def main():
    await send_time()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

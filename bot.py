import os
import sys
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from dataclasses import dataclass
from configparser import ConfigParser
from middlewares.antiflood import rate_limit, ThrottlingMiddleware
# Configure logging
logging.basicConfig(level=logging.INFO)


@dataclass
class Passport:
    tg_admin: int
    tg_bot_token: str
    antiflood_timer: int
    

def load_config():
    try: 
        config = Passport(tg_admin=os.getenv('TG_ADMIN'),
                        tg_bot_token=os.getenv('TOKEN'),
                        antiflood_timer=os.getenv('ANTIFLOOD'))
    except:
        sys.exit('Config error!')
        
    return config
        

# Initialize bot and dispatcher
config = load_config()
bot = Bot(token=config.tg_bot_token)
dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(ThrottlingMiddleware())

@dp.message_handler(content_types=types.ContentType.ANY)
@rate_limit(int(config.antiflood_timer))
async def sink_hole(message: types.Message):
    await message.answer_chat_action('typing')
    await message.reply(f'Ваше сообщение принято!\nСледующая отправка будет доступна через {config.antiflood_timer} секунд')
    await message.forward(chat_id=config.tg_admin)

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
import os
import sys
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from dataclasses import dataclass
from middlewares.antiflood import rate_limit, ThrottlingMiddleware
# Configure logging
logging.basicConfig(level=logging.INFO)


@dataclass
class Passport:
    tg_admin: int
    tg_bot_token: str
    tg_promo: str
    antiflood_timer: int
    

def load_config():
    try:
        config = Passport(tg_admin=int(os.getenv('TG_ADMIN')),
                          tg_bot_token=os.getenv('TOKEN'),
                          tg_promo=os.getenv('PROMO'),
                          antiflood_timer=int(os.getenv('ANTIFLOOD')) or 5,
                          )
    except:
        sys.exit('Config error. Terminating...')
    return config
        

# Initialize bot and dispatcher
config = load_config()
bot = Bot(token=config.tg_bot_token)
dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(ThrottlingMiddleware())


@dp.message_handler(commands=['start'])
@rate_limit(10)
async def hello(message: types.Message):
    await message.reply(f'Привет! Это предложка канала {config.tg_promo}')
    
    
@dp.message_handler(content_types=types.ContentType.ANY)
@rate_limit(int(config.antiflood_timer))
async def sink_hole(message: types.Message):
    await message.answer_chat_action('typing')
    await message.reply(f'''Ваше сообщение принято!\nСледующая отправка будет доступна через {config.antiflood_timer} секунд''')
    await message.forward(chat_id=config.tg_admin)

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
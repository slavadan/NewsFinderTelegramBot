from aiogram import Bot
from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from bot.DBController import *
from bot.config import BOT_TOKEN, DATABASE

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
executor = Executor(dp)
database_connection = DBController(DATABASE)
help_message = "/kfcpromotions -  акции kfc\n" \
               "/bkingpromotions -  акции Burger King\n" \
               "/findStopGameNews - поиск новостей на сайте gtopgame.ru\n" \
               "/findLentaNews - поиск новостей на сайте lenta.ru\n"\
                "/start - регистрация пользователя для использования бота"

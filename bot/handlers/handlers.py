from aiogram.dispatcher.filters import Command
from bot.keyboards.callbacks_datas import read_stopgame_callback, read_lenta_callback, read_kfc_callback
from bot.other import database_connection, dp, help_message
from aiogram import types
from bot.parsers.kfc_parser import KfcParser
from bot.parsers.stopgame_parser import StopGameParser
from bot.parsers.lenta_parser import LentaParser
from bot.parsers.bk_parser import BurgerKingParser
from bot.keyboards import lentakb, stopgamekb, kfckb


@dp.message_handler(Command("start"))
async def start(msg: types.Message):
    if database_connection.check_user(msg.from_user.id):

        await msg.answer("Вы уже зарегистрированны!")

    else:

        database_connection.add_user(msg.from_user.id)

        await msg.answer("Спасибо за регистрацию!")


@dp.message_handler(Command("kfcpromotions"))
async def kfcpromotions(msg: types.Message):
    if database_connection.check_user(msg.from_user.id):

        await msg.answer("Выберите категорию", reply_markup=kfckb.kfc_choice)

    else:
        await msg.answer("Вы не зарегистрированы!\nДля регистрации используйте команду /start")


@dp.message_handler(Command("bkingpromotions"))
async def bkingpromotions(msg: types.Message):
    if database_connection.check_user(msg.from_user.id):

        links = BurgerKingParser().parse()

        for link in links:
            await msg.answer(link)


@dp.message_handler(Command("help"))
async def help(msg: types.Message):
    await msg.answer(help_message)


@dp.message_handler(Command("findStopGameNews"))
async def find_stopgame_news(msg: types.Message):
    if database_connection.check_user(msg.from_user.id):

        await msg.answer("Выберите категорию!", reply_markup=stopgamekb.stopgame_choice)

    else:

        await msg.answer("Вы не зарегистрированы!\nДля регистрации используйте команду /start")


@dp.message_handler(Command("findLentaNews"))
async def find_lenta_news(msg: types.Message):
    if database_connection.check_user(msg.from_user.id):

        await msg.answer("Выберите категорию", reply_markup=lentakb.lenta_choice)

    else:

        await msg.answer("Вы не зарегистрированы!\nДля регистрации используйте команду /start")


@dp.message_handler(Command("findTokinyPromo"))
async def find_tokiny_promo(msg: types.Message):
    pass


@dp.callback_query_handler(read_stopgame_callback.filter())
async def read_stopgame_news(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    stopgame_parser = StopGameParser()
    stopgame_parser.set_category(callback_data.get('category'))

    print(stopgame_parser.URL)
    links = stopgame_parser.parse()

    if len(links) == 0:

        await call.message.answer(f"Новостей в категории {callback_data.get('category')} за сегодня еще нету!")

    else:

        for link in links:
            await call.message.answer(link)


@dp.callback_query_handler(read_lenta_callback.filter())
async def read_lenta_news(call: types.CallbackQuery, callback_data: dict):
    lenta_parser = LentaParser()
    lenta_parser.set_category(callback_data.get('category'))

    links = lenta_parser.parse()

    if len(links) == 0:

        await call.message.answer(f"Новостей в категории {callback_data.get('category')} за сегодня еще нету!")

    else:

        for link in links:
            await call.message.answer(link)


@dp.callback_query_handler(read_kfc_callback.filter())
async def read_kfc(call: types.CallbackQuery, callback_data: dict):
    pass

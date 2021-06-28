from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.callbacks_datas import read_stopgame_callback

stopgame_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="All news", callback_data=read_stopgame_callback.new(
                category="All"
            )),
            InlineKeyboardButton(text="Pc news", callback_data=read_stopgame_callback.new(
                category="PC"
            )),
            InlineKeyboardButton(text="Xbox one news", callback_data=read_stopgame_callback.new(
                category="XboxOne"
            ))
        ],
        [
            InlineKeyboardButton(text="Xbox series X news", callback_data=read_stopgame_callback.new(
                category="XboxX"
            )),
            InlineKeyboardButton(text="PlayStation 4 news", callback_data=read_stopgame_callback.new(
                category="PS4"
            )),
            InlineKeyboardButton(text="PlayStation 5 news", callback_data=read_stopgame_callback.new(
                category="PS5"
            ))
        ],
        [
            InlineKeyboardButton(text="MMO news", callback_data=read_stopgame_callback.new(
                category="MMO"
            )),
            InlineKeyboardButton(text="Cybersport news", callback_data=read_stopgame_callback.new(
                category="CyberSport"
            )),
            InlineKeyboardButton(text="Films news", callback_data=read_stopgame_callback.new(
                category="Films"
            ))
        ]
    ]
)

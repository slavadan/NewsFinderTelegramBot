from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.callbacks_datas import read_lenta_callback

lenta_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="World news", callback_data=read_lenta_callback.new(
                category="World"
            )),
            InlineKeyboardButton(text="Economic news", callback_data=read_lenta_callback.new(
                category="Economic"
            )),
            InlineKeyboardButton(text="Culture news", callback_data=read_lenta_callback.new(
                category="Culture"
            ))
        ],
        [
            InlineKeyboardButton(text="Science news", callback_data=read_lenta_callback.new(
                category="Science"
            )),
            InlineKeyboardButton(text="Sport news", callback_data=read_lenta_callback.new(
                category="Sport"
            )),
            InlineKeyboardButton(text="Internet news", callback_data=read_lenta_callback.new(
                category="Internet"
            ))
        ],
        [
            InlineKeyboardButton(text="Life news", callback_data=read_lenta_callback.new(
                category="Life"
            )),
            InlineKeyboardButton(text="Russian news", callback_data=read_lenta_callback.new(
                category="Russian"
            )),
            InlineKeyboardButton(text="Crime news", callback_data=read_lenta_callback.new(
                category="Crime"
            )),
        ]
    ]
)
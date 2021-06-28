from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.callbacks_datas import read_kfc_callback

kfc_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kfc coupons", callback_data=read_kfc_callback.new(
                category="coupons"
            )),
            InlineKeyboardButton(text="Kfc promotions", callback_data=read_kfc_callback.new(
                category="promotions"
            ))
        ]
    ]
)
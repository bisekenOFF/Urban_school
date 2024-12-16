from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import crud_functions
from crud_functions import *
import sqlite3

api = "api_key"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button5 = KeyboardButton(text="Купить")
kb.add(button1, button2, button5)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button4 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
ikb.add(button3, button4)

ikb1 = InlineKeyboardMarkup(resize_keyboard=True)
button6 = InlineKeyboardButton(text="Продукт 1", callback_data="product_buying")
button7 = InlineKeyboardButton(text="Продукт 2", callback_data="product_buying")
button8 = InlineKeyboardButton(text="Продукт 3", callback_data="product_buying")
button9 = InlineKeyboardButton(text="Продукт 4", callback_data="product_buying")
ikb1.add(button6, button7, button8, button9)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=ikb)

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("Формулы расчёта: (10 * вес + 6.25 * рост - 5 * возраст + 5) * 1.2")
    await call.answer()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    product = get_all_products()
    connection.close()
    for i in product:
        with open('files/product.jpg', 'rb') as product:
            await message.answer_photo(product)
            await message.answer(f"Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}" )
    await message.answer("Выберите продукт для покупки:", reply_markup=ikb1)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(state=UserState.age)
async def get_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def get_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = (10 * int(weight) + 6.25 * int(growth) - 5 * int(age) + 5) * 1.2
    await message.answer(f"Ваша суточная норма калорий: {calories}")
    await state.finish()


@dp.message_handler(text="Информация")
async def inform(message):
    await message.answer("Бот помогает рассчитать суточную норму калорий.")


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
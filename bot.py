#c3rfbot
from aiogram import Bot, types, executor, Dispatcher
from aiogram.utils.markdown import hlink
import sqlite3 as sq
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import datetime
from datetime import timedelta, datetime
import time
import asyncio
from tokenbot import TOKEN
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random
import emoji
import re
from mines import *
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import Throttled

storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=storage)
base = sq.connect('game.db')
c = base.cursor()


#menu
menu = ReplyKeyboardMarkup(resize_keyboard=True)
i1 = ['Воины 🥷', 'Рынок ⛩️', 'Играть 🕹']
i2 = ['Казино 🎲', 'Кланы 🏆', 'Профиль 🖼']
i3 = ['Инфо ⚙️', 'Скам 💸']
i4 = ['Топ игроков 🎖']
menu.add(*i1).add(*i2).add(*i3).add(*i4)
men2 = ReplyKeyboardMarkup(resize_keyboard=True)
i1 = ['Мины 🎲', 'ДжекФрукт 🎲']
i2 = ['Назад 🔙']
men2.add(*i1).add(*i2)
# stop menu
# start tasks

# stop tasks
# start inline
buyaur = InlineKeyboardMarkup(row_with=3)
b1 = InlineKeyboardButton(text='500.000 💰', callback_data='0_5_mln')
b2 = InlineKeyboardButton(text='1.000.000 💰', callback_data='1_mln')
b3 = InlineKeyboardButton(text='5.000.000 💰', callback_data='5_mln')
b4 = InlineKeyboardButton(text='10.000.000 💰', callback_data='10_mln')
b5 = InlineKeyboardButton(text='25.000.000 💰', callback_data='25_mln')
b6 = InlineKeyboardButton(text='50.000.000 💰', callback_data='50_mln')
buyaur.add(b1, b2, b3, b4, b5, b6)
# buy aurum
yes1 = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Подвердить', callback_data='yes_0_5')
p2 = InlineKeyboardButton(text='🔙 Назад', callback_data='backaurum')
yes1.add(p1, p2)
# 2
yes2 = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Подвердить', callback_data='yes_1')
p2 = InlineKeyboardButton(text='🔙 Назад', callback_data='backaurum')
yes2.add(p1, p2)
# 3
yes3 = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Подвердить', callback_data='yes_5')
p2 = InlineKeyboardButton(text='🔙 Назад', callback_data='backaurum')
yes3.add(p1, p2)
# 4
yes4 = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Подвердить', callback_data='yes_10')
p2 = InlineKeyboardButton(text='🔙 Назад', callback_data='backaurum')
yes4.add(p1, p2)
# 5
yes5 = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Подвердить', callback_data='yes_25')
p2 = InlineKeyboardButton(text='🔙 Назад', callback_data='backaurum')
yes5.add(p1, p2)
# 6
yes6 = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Подвердить', callback_data='yes_50')
p2 = InlineKeyboardButton(text='🔙 Назад', callback_data='backaurum')
yes6.add(p1, p2)
# stop aurum
pay = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Получить 💰', callback_data=f'give')
p2 = InlineKeyboardButton(text='Отправить 💰', callback_data=f'giveaway')
pay.add(p1, p2)
info = InlineKeyboardMarkup(row_with=2)
p1 = InlineKeyboardButton(text='Атрибуты 🪖', callback_data=f'atr')
p2 = InlineKeyboardButton(text='Чат ⛱', url='https://t.me/+zq5RhKKFg0s4MGY6')
info.add(p1, p2)
place = InlineKeyboardMarkup(row_with=3)
p1 = InlineKeyboardButton(text='Воины 🥷', callback_data='voinsbuy')
p2 = InlineKeyboardButton(text='Золото 💰', callback_data='aurumbuy')
p3 = InlineKeyboardButton(text='Опыт 🧩', callback_data='expbuy')
p4 = InlineKeyboardButton(text='Ящики 📦', callback_data='casebuy')
place.add(p1, p2, p3, p4)
ups = InlineKeyboardMarkup(row_with=5)
p1 = InlineKeyboardButton(text='❤', callback_data=f'hp')
p2 = InlineKeyboardButton(text='🔫', callback_data=f'attack')
p3 = InlineKeyboardButton(text='🛡', callback_data=f'shit')
p4 = InlineKeyboardButton(text='💥', callback_data=f'krit')
p5 = InlineKeyboardButton(text='🦋', callback_data=f'uklon')
p6 = InlineKeyboardButton(text='🦇', callback_data=f'vampir')
p7 = InlineKeyboardButton(text='Сменить ↔️', callback_data=f'nexstpers')
ups.add(p1, p2, p3, p4, p5, p6, p7)
                
# stop inline

interval2 = 2400


# Добавлена новая state to the FSM
class JoinClanState(StatesGroup):
    id = State()
    
class Form(StatesGroup):
    bam = State() 

async def banka():
    while True:
        minl = c.execute(f'SELECT * FROM voin WHERE voin="1"')
        for user in minl:
            voin = random.randint(2, 20)
            if user[1] != 1:
                c.execute(f'UPDATE voin SET status = {voin} WHERE voin = "1"')
                base.commit() 
            
        await asyncio.sleep(interval2)

c.execute('''CREATE TABLE IF NOT EXISTS users(user_id INTEGER, money INTEGER, voins INTEGER, play INTEGER, exp INTEGER, mmr INTEGER, skam INTEGER, voin1 INTEGER, voin2 INTEGER, voin3 INTEGER, voin4 INTEGER, voin5 INTEGER, voin6 INTEGER, nick TEXT, lose INTEGER, coin INTEGER DEFAULT 0, clan_id, role)''')
c.execute('''CREATE TABLE IF NOT EXISTS clans(clan_id INTEGER, clan_name TEXT, leader_id INTEGER, total_members INTEGER)''')
base.commit()

class CreateClanState(StatesGroup):
    name = State()

MEMBERS_PER_PAGE = 5
        
    

@dp.message_handler(commands=['delactiv'])
async def delad(msg):
    user_id = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user_id}')
    fan = c.fetchone()
    if not fan:
        return
    players.clear()
    await msg.answer('🍁 | Активные бои отменены')

@dp.callback_query_handler(text='inviteclan')
async def invite(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    cur = c.fetchone()
    if cur[16] is None:
        await call.message.answer('❕ Вы не состоите в клане')
        return
    await call.message.answer(f'🆔 <code>{cur[16]}</code> -<b> Это ID клана по которому пользователь может присоедениться к клану.</b>')

@dp.callback_query_handler(text='swape')
async def swape(call):
    user_id = call.from_user.id
    await bot.delete_message(user_id, call.message.message_id)

@dp.callback_query_handler(lambda c: c.data.startswith('kickclan:'))
async def dip(call):
    user = call.from_user.id
    user_id = int(call.data.split(':')[1])
    c.execute(f'SELECT * FROM users WHERE user_id={user}')
    min = c.fetchone()
    if min[16] is None:
        await call.answer('Вы не состоите в клане ❕')
        return
    if min[17] is None:
        await call.answer('Исключать участников могут только лидеры ❕', show_alert=True)
        return
    clan = min[16]
    c.execute(f'SELECT * FROM users WHERE user_id={user_id} AND clan_id={clan}')
    cur = c.fetchone()
    if not cur:
        await call.answer('🎈 Данный пользователь не состоит в вашем клане ❕', show_alert=True)
        return
    c.execute(f'UPDATE users SET clan_id=? WHERE user_id={user_id}',(None,))
    base.commit()
    await call.message.edit_text('<b>🎈 Пользователь исключен</b>')

@dp.callback_query_handler(text='editclan')
async def clan_edit(call, state: FSMContext):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if user[16] is None:
        await call.message.answer('<b>Вы не состоите в клане ❕</b>')
        return
    id = user[16]
    
    c.execute(f'SELECT * FROM clans WHERE clan_id={id}')
    clan = c.fetchone()
    lead = clan[2]
    if user_id != lead:
        await call.answer('🍁 Данная вкладка доступна только лидерам ❕')
        return
    await call.message.answer('🆔<b> Введите ID участника клана:</b>')

    # Сохраняем id клана в состояние
    await state.update_data(clan_id=id)
    await Form.bam.set()

@dp.message_handler(state=Form.bam)
async def getid(message: types.Message, state: FSMContext):
    user_id_to_check = message.text

    # Доступ к сохраненным данным
    data = await state.get_data()
    clan_id = data.get("clan_id")

    try:
        c.execute(f'SELECT * FROM users WHERE user_id={user_id_to_check} AND clan_id={clan_id}')
        cu = c.fetchone()
        if not cu:
            await message.answer('<b>🆔 Данный ID не состоит в вашем клане ❕</b>')
            await state.finish()
            return
        if int(user_id_to_check) == message.from_user.id:
            await message.answer('🎈 Нельзя управлять самим собой')
            await state.finish()
            return
        kb = InlineKeyboardMarkup()
        p1 = InlineKeyboardButton(text='Исключить 🎈', callback_data=f'kickclan:{user_id_to_check}')
        p2 = InlineKeyboardButton(text='Закрыть 🔻', callback_data='swape')
        kb.add(p1, p2)
        nick = cu[13]
        user_mention = f'<a href="tg://user?id={user_id_to_check}">{nick}</a>'
        role = ""
        if cu[17] == 'leader':
            role = "🏵 Лидер"
        elif cu[17] is None:
            role = "🍁 Участник"
        await message.answer(f'<b>{user_mention}\n{role}</b>\n🆔 <code>{user_id_to_check}</code>', reply_markup=kb)
        await state.finish()
    except:
        await message.answer('<b>🆔 Участник вашего клана не найден ❕</b>')
        await state.finish()
        

    
def create_members_keyboard(clan_id, page):
    keyboard = InlineKeyboardMarkup(row_width=3)
    c.execute(f'SELECT count(*) FROM users WHERE clan_id = {clan_id}')
    num_members = c.fetchone()[0]

    buttons = [InlineKeyboardButton('🏠', callback_data='mainmenuclan'), InlineKeyboardButton('☑️ Редактировать', callback_data='editclan')]

    if page > 0:
        buttons.append(InlineKeyboardButton('◀️', callback_data=f'membersclan_{clan_id}_{page - 1}'))

    if num_members > (page + 1) * MEMBERS_PER_PAGE:
        buttons.append(InlineKeyboardButton('▶️', callback_data=f'membersclan_{clan_id}_{page + 1}'))

    keyboard.add(*buttons)
    return keyboard
    
    
async def show_top_clans(page, callback_query):
    offset = page * MEMBERS_PER_PAGE

    c.execute(f'''SELECT clans.clan_id, clans.clan_name, clans.total_members, 
                SUM(users.mmr) as total_mmr FROM clans LEFT JOIN users 
                ON clans.clan_id=users.clan_id GROUP BY clans.clan_id 
                ORDER BY total_mmr DESC, clans.total_members DESC 
                LIMIT {MEMBERS_PER_PAGE} OFFSET {offset}''')
    
    clans_list = c.fetchall()
    message_out = ""
    for i, clan in enumerate(clans_list, start=offset):
        clan_id = clan[0]
        c.execute(f'SELECT count(*) FROM users WHERE clan_id = {clan_id}')
        nu = c.fetchone()[0]
        message_out += f"<b>{i+1} - {clan[1]}\n🏆 {clan[3]} MMR | 👥 {nu}</b>\n"
    
    keyboard = InlineKeyboardMarkup(row_width=3)

    buttons = [InlineKeyboardButton('🏠', callback_data='mainmenuclan')]

    if page > 0: 
        buttons.append(InlineKeyboardButton('◀️', callback_data=f'topclans_{page - 1}'))

    if len(clans_list) == MEMBERS_PER_PAGE:
        buttons.append(InlineKeyboardButton('▶️', callback_data=f'topclans_{page + 1}'))

    keyboard.add(*buttons)
    await callback_query.message.edit_caption(caption=message_out, reply_markup=keyboard)

@dp.callback_query_handler(text_contains="topclans")
async def topclans_handler(callback_query: types.CallbackQuery):
    page_str = callback_query.data.split('_')[-1]
    page = int(page_str) if page_str.isdigit() else 0
    await show_top_clans(page, callback_query)

@dp.callback_query_handler(text_contains="topclans")
async def topclans_handler(callback_query: types.CallbackQuery):
    page_str = callback_query.data.split('_')[-1]
    page = int(page_str) if page_str.isdigit() else 0
    await show_top_clans(page, callback_query)

async def send_members(clan_id, user_id, page, callback_query):
    offset = page * MEMBERS_PER_PAGE
    c.execute(f'SELECT user_id, nick, mmr, role FROM users WHERE clan_id = {clan_id} LIMIT {MEMBERS_PER_PAGE} OFFSET {offset}')
    members_list = c.fetchall()
    
    message_out = ""
    for i, member in enumerate(members_list, start=offset):
        user_mention = f'<a href="tg://user?id={member[0]}">{member[1]}</a>'
        role = ""
        if member[3] == 'leader':
            role = "🏵 Лидер"
        elif member[3] is None:
            role = "🍁 Участник"
        message_out += f"<b>{i+1} - {user_mention}\n{role} | {member[2]} MMR</b>\n 🆔 <code>{member[0]}</code>\n\n"
        
    await callback_query.message.edit_caption(caption=message_out, reply_markup=create_members_keyboard(clan_id, page))


@dp.callback_query_handler(text_contains="membersclan")
async def membersclan_handler(callback_query: types.CallbackQuery):
    _, clan_id_str, page_str = callback_query.data.split('_')
    clan_id = int(clan_id_str)
    user_id = callback_query.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await callback_query.message.reply('У вас нет личного профиля в боте, завести его можно у меня в лс ❕')
        return
    if user[16] != int(clan_id):
        await callback_query.answer('Это не ваш клан❕', show_alert=True)
        return
    page = int(page_str)
    await send_members(clan_id, callback_query.from_user.id, page, callback_query)


@dp.callback_query_handler(text_contains="mainmenuclan")
async def mainmenuclan_handler(call: types.CallbackQuery):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.reply('У вас нет личного профиля в боте, завести его можно у меня в лс ❕')
        return
    if user[16] is None:
        await call.answer('У вас нет клана ❕', show_alert=True)
        return
    try:
        if (clan_id := user[16]) is None:
            inline_kb = InlineKeyboardMarkup(row_width=2)
            buttons = [
                InlineKeyboardButton('Создать 💡', callback_data='create_clan'),
                InlineKeyboardButton('Вступить в клан 🎗', callback_data='join_clan'),
                InlineKeyboardButton('🏆 Топ кланы', callback_data='topclans')
            ]
            inline_kb.add(*buttons)
            await call.message.edii_caption(caption="<b>📓 Меню кланов:</b>", reply_markup=inline_kb)
            return
        c.execute(f'SELECT count(*) FROM users WHERE clan_id = {clan_id}')
        nu = c.fetchone()[0]
        c.execute(f'SELECT * FROM clans WHERE clan_id={clan_id}')
        clan_info = c.fetchone()
        clan_id = clan_info[0]
        clan_name = clan_info[1]
        leader_id = clan_info[2]
        
        c.execute(f'SELECT nick FROM users WHERE user_id={leader_id}')
        leader_name = c.fetchone()[0]
        leader_mention = types.User(id=leader_id, first_name=leader_name).get_mention(as_html=True)

        total_members = clan_info[3]
        c.execute(f'SELECT nick, mmr FROM users WHERE clan_id={clan_id} ORDER BY mmr DESC')
        members_list = c.fetchmany(5)
        total_mmr = c.execute(f'SELECT SUM(mmr) FROM users WHERE clan_id={clan_id}').fetchone()[0]
        message_out = f"<b>👾 {clan_name}\n🔻 Лидер: {leader_mention}\n🏆 MMR: {total_mmr}\n👥 Участников: {nu}/20\n\n</b>\n"
        lead = InlineKeyboardMarkup(row_with=2)
        p1 = InlineKeyboardButton(text='Пригласить 👥', callback_data='inviteclan')
        p3 = InlineKeyboardButton(text='👥 Участники', callback_data=f'membersclan_{clan_id}_0')
        p4 = InlineKeyboardButton('🧹 Удалить', callback_data='deleteclan')
        p2 = InlineKeyboardButton('🏆 Топ кланы', callback_data='topclans')
        lead.add(p1, p3, p4, p2)
        op = InlineKeyboardMarkup(row_with=3)
        p1 = InlineKeyboardButton(text='Пригласить 👥', callback_data='inviteclan')
        p3 = InlineKeyboardButton(text='👥 Участники', callback_data=f'membersclan_{clan_id}_0')
        p4 = InlineKeyboardButton('Покинуть 🎈', callback_data='leaveclan')
        p2 = InlineKeyboardButton('🏆 Топ кланы', callback_data='topclans')
        op.add(p1, p3, p4, p2)
        if user_id != leader_id:
            await call.message.edit_caption(caption=message_out, reply_markup=op)
        elif user_id == leader_id:
            await call.message.edit_caption(caption=message_out, reply_markup=lead)
    except Exception as e:
        print(e)
        await call.message.reply('<b>Произошла ошибка ❕</b>')

@dp.callback_query_handler(text='leaveclan')
async def del_clan(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if user[16] is None:
        await call.message.answer('<b>Вы не состоите в клане ❕</b>')
        return
    id = user[16]
    
    c.execute(f'SELECT * FROM clans WHERE clan_id={id}')
    clan = c.fetchone()
    lead = clan[2]
    if user_id == lead:
        await call.answer('🍁 Лидеры не могут выходить со своих же кланов❕')
        return
    de = InlineKeyboardMarkup()
    yes = InlineKeyboardButton(text='🎈 Выйти', callback_data='leaveyes')
    de.add(yes)
    await call.message.answer('<b>Вы собираетесь выйти из своего клана ❕</b>', reply_markup=de)

@dp.callback_query_handler(text='leaveyes')
async def del_clan(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if user[16] is None:
        await call.message.answer('<b>Вы не состоите в клане ❕</b>')
        return
    id = user[16]
    
    c.execute(f'SELECT * FROM clans WHERE clan_id={id}')
    clan = c.fetchone()
    lead = clan[2]
    if user_id == lead:
        await call.answer('🍁 Лидеры не могут выходить со своих же кланов ❕')
        return
    c.execute('UPDATE users SET clan_id=?, role=? WHERE clan_id=? AND user_id=?',(None, None, id, user_id,))
    base.commit()
    await call.message.edit_text('🎈 <b>Вы вышли из клана</b>')

@dp.callback_query_handler(text='deleteclan')
async def del_clan(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if user[16] is None:
        await call.message.answer('<b>Вы не состоите в клане ❕</b>')
        return
    id = user[16]
    
    c.execute(f'SELECT * FROM clans WHERE clan_id={id}')
    clan = c.fetchone()
    lead = clan[2]
    if user_id != lead:
        await call.answer('🍁 Данная вкладка доступна только лидерам ❕')
        return
    de = InlineKeyboardMarkup()
    yes = InlineKeyboardButton(text='🎈 Удалить', callback_data='delyes')
    de.add(yes)
    await call.message.answer('<b>Вы собираетесь удалить свой клан, это действие последует к удалению клану без его восстановления ❕</b>', reply_markup=de)

@dp.callback_query_handler(text='delyes')
async def del_clan(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if user[16] is None:
        await call.message.answer('<b>Вы не состоите в клане ❕</b>')
        return
    id = user[16]
    
    c.execute(f'SELECT * FROM clans WHERE clan_id={id}')
    clan = c.fetchone()
    lead = clan[2]
    if user_id != lead:
        await call.answer('🍁 Данная вкладка доступна только лидерам ❕')
        return
    c.execute(f'DELETE FROM clans WHERE clan_id={id}')
    c.execute('UPDATE users SET clan_id=?, role=? WHERE clan_id=?',(None, None, id,))
    base.commit()
    await call.message.edit_text('🎈 <b>Клан удален</b>')

@dp.message_handler(text='Кланы 🏆')
async def clans_handler(message: types.Message):
    user_id = message.from_user.id
    if message.chat.type == "supergroup":
        return
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await message.reply('У вас нет личного профиля в боте, завести его можно у меня в лс ❕')
        return
    try:
        if (clan_id := user[16]) is None:
            inline_kb = InlineKeyboardMarkup(row_width=2)
            buttons = [
                InlineKeyboardButton('Создать 💡', callback_data='create_clan'),
                InlineKeyboardButton('Вступить в клан 🎗', callback_data='join_clan'),
                InlineKeyboardButton('🏆 Топ кланы', callback_data='topclans')
            ]
            inline_kb.add(*buttons)
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/clan.png', 'rb'),
                              caption="<b>📓 Меню кланов:</b>", reply_markup=inline_kb)
            return
        c.execute(f'SELECT * FROM clans WHERE clan_id={clan_id}')
        clan_info = c.fetchone()
        clan_id = clan_info[0]
        clan_name = clan_info[1]
        leader_id = clan_info[2]
        
        c.execute(f'SELECT count(*) FROM users WHERE clan_id = {clan_id}')
        nu = c.fetchone()[0]

        c.execute(f'SELECT nick FROM users WHERE user_id={leader_id}')
        leader_name = c.fetchone()[0]
        leader_mention = types.User(id=leader_id, first_name=leader_name).get_mention(as_html=True)

        total_members = clan_info[3]
        c.execute(f'SELECT nick, mmr FROM users WHERE clan_id={clan_id} ORDER BY mmr DESC')
        members_list = c.fetchmany(5)

        total_mmr = c.execute(f'SELECT SUM(mmr) FROM users WHERE clan_id={clan_id}').fetchone()[0]

        message_out = f"<b>👾 {clan_name}\n🔻 Лидер: {leader_mention}\n🏆 MMR: {total_mmr}\n👥 Участников: {nu}/20\n\n</b>\n"

        lead = InlineKeyboardMarkup(row_with=2)
        p1 = InlineKeyboardButton(text='Пригласить 👥', callback_data='inviteclan')
        p3 = InlineKeyboardButton(text='👥 Участники', callback_data=f'membersclan_{clan_id}_0')
        p4 = InlineKeyboardButton('🧹 Удалить', callback_data='deleteclan')
        p2 = InlineKeyboardButton('🏆 Топ кланы', callback_data='topclans')
        lead.add(p1, p3, p4, p2)
        op = InlineKeyboardMarkup(row_with=3)
        p1 = InlineKeyboardButton(text='Пригласить 👥', callback_data='inviteclan')
        p3 = InlineKeyboardButton(text='👥 Участники', callback_data=f'membersclan_{clan_id}_0')
        p4 = InlineKeyboardButton('Покинуть 🎈', callback_data='leaveclan')
        p2 = InlineKeyboardButton('🏆 Топ кланы', callback_data='topclans')
        op.add(p1, p3, p4, p2)
        if user_id != leader_id:
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/clan.png', 'rb'),
                              caption=message_out, reply_markup=op)
        elif user_id == leader_id:
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/clan.png', 'rb'),
                              caption=message_out, reply_markup=lead)
    except Exception as e:
        print(e)
        await message.reply('<b>Произошла ошибка ❕</b>')

@dp.callback_query_handler(text_contains='join_clan')
async def join_clan_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    fu = c.fetchone()
    if fu[16] is not None:
        await callback_query.message.answer('📋 <b>Вы уже состоите в клане.</b>')
        return
    await bot.send_message(user_id, '<b>📓 Теперь нужно ввести ID клана</b>:')
    await JoinClanState.id.set()

@dp.message_handler(state=JoinClanState.id)
async def process_join_clan(message: types.Message, state: FSMContext):
    clan_id = message.text
    try:
        clan_info = c.execute(f'SELECT * FROM clans WHERE clan_id={clan_id}').fetchone()

        if not clan_info:
            await bot.send_message(message.from_user.id, '<b>📓 Данного клана с ID не существует ❕</b>')
            await state.finish()
            return

        if clan_info[3] >= 20:  # member count
            await bot.send_message(message.from_user.id, '<b>❕ Клан заполнен</b>')
            await state.finish()
            return

        total_mmr = c.execute(f'SELECT SUM(mmr) FROM users WHERE clan_id={clan_id}').fetchone()[0]
        c.execute(f'SELECT count(*) FROM users WHERE clan_id = {clan_id}')
        nu = c.fetchone()[0]
    
        msg_text = (f"👾 <b>{clan_info[1]}\n</b>"
                f"<b>👥 Участников: {nu}/20</b>\n"
                f"🏆 <b>MMR: {total_mmr}</b>\n\n"
                "<b>💡 Чтобы присоединиться в клан нажмите на кнопку «Вступить 🔰»!</b>")

        inline_kb = InlineKeyboardMarkup()
        join_button = InlineKeyboardButton('Вступить 🔰', callback_data=f'confirm_join_{clan_id}')
        inline_kb.add(join_button)
        await bot.send_message(message.from_user.id, msg_text, reply_markup=inline_kb)
        await state.finish()
    except:
        await bot.send_message(message.from_user.id, '<b>📓 Данного клана с ID не существует ❕</b>')
        await state.finish()
        return

@dp.callback_query_handler(text_contains="confirm_join_")
async def confirm_join_clan_handler(callback_data: types.CallbackQuery):
    user_id = callback_data.from_user.id
    clan_id = int(callback_data.data.split('_')[-1])
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    fu = c.fetchone()
    if fu[16] is not None:
        await callback_data.message.answer('📋 <b>Вы уже состоите в клане.</b>')
        return
    c.execute(f'UPDATE users SET clan_id={clan_id} WHERE user_id={user_id}')
    base.commit()

    clan_name = c.execute(f'SELECT clan_name FROM clans WHERE clan_id={clan_id}').fetchone()[0]
    await bot.send_message(user_id, f'<b>📋 Теперь вы состоите в клане «{clan_name}»</b>!')
        
@dp.callback_query_handler(text_contains="create_clan")
async def create_clan_handler(callback_data: types.CallbackQuery):
    user_id = callback_data.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    fu = c.fetchone()
    if fu[16] is not None:
        await callback_data.message.answer('📋 <b>Вы уже состоите в клане.</b>')
        return
    await bot.send_message(user_id, '<b>📋 Введите название для нового клана</b>:')
    await CreateClanState.name.set()
    
@dp.message_handler(state=CreateClanState.name)
async def process_create_clan(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    clan_name = message.text
    clan_id = random.randint(1, 1e6)
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    fu = c.fetchone()
    if fu[16] is not None:
        await message.answer('📋 <b>Вы уже состоите в клане.</b>')
        return
    while True:
        clan = c.execute(f'SELECT * FROM clans WHERE clan_id={clan_id}').fetchone()
        if clan is None:
            break
        clan_id = random.randint(1, 1e6)
    c.execute(f'INSERT INTO clans VALUES ({clan_id}, "{clan_name}", {user_id}, 1)')
    c.execute(f'UPDATE users SET clan_id={clan_id}, role="leader" WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f'<b>📓 Вы успешно создали клан «{clan_name}»</b>!')
    await state.finish()

# FSMContext

class GiveState(StatesGroup):
    dialog = State()
    dialog2 = State()

# stop FSMContext

'''код'''
## -*- coding: aiogram-2.19 -*-

player_queue = []
players = {}
game_data = {}
#
fruit_emojis = {"apple": "🍏", "banana": "🍌", "watermelon": "🍉", "cherry": "🍒", "pear": "🍐", "minus": "❌"}
user_games = {}

@dp.message_handler(commands=['чполе'], commands_prefix=".")
async def check(msg):
    id = msg.from_user.id
    c.execute('SELECT * FROM admin WHERE user_id=?',(id,))
    adm = c.fetchone()
    if adm:
        args = msg.text.split()
        if len(args) < 2:
            await msg.answer('❌ Введите ID')
            return
        arg = args[1]
        c.execute(f'SELECT * FROM users WHERE user_id={arg}')
        us = c.fetchone()
        if not us:
            await msg.answer('<b>Такого пользователя не существует. ❌</b>')
            return
        if us:
            if int(arg) not in user_games:
                await msg.answer('<b>У игрока нет активной игры.❌</b>')
                return
            if int(arg) in user_games:
                argf = int(arg)
                field = generate_field(argf)
                await msg.answer(field)
                return
            if not adm:
                return
    

@dp.message_handler(commands=['перевод', 'Перевод'], commands_prefix='+')
async def perevod(msg):
    if msg.chat.type == "private":
        return
    try:
        user_id = msg.from_user.id
        c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
        user = c.fetchone()
        if not user:
            await msg.reply('У вас нет личного профиля в боте, завести  его можно у меня в лс ❕')
            return
        split = msg.text.split()
        if len(split) != 2:
            await msg.reply('<b>Вы не ввели сумму 💰</b>')
            return
        amount = int(split[1])
        if not msg.reply_to_message:
            await msg.answer('<b>Ответьте на сообщение пользователя ❕</b>')
            return
        if msg.reply_to_message:
            id = msg.reply_to_message.from_user.id
            if msg.from_user.id == id:
                await msg.reply('<b>Нельзя перевести самому себе ❕</b>')
                return
            c.execute(f'SELECT * FROM users WHERE user_id={id}')
            user2 = c.fetchone()
            if not user2:
                await msg.reply('<b>У данного человека нет профиля в игре ❕</b>')
                return
            if amount <= 0:
                await msg.answer('<b>Нельзя перевести отрицательное число или равное нулю ❕</b>')
                return
            balance = int(user[1])
            if amount > balance:
                await msg.reply('<b>У вас недостаточно средств ❕</b>')
                return
            new_balance_user = balance - amount
            new_balance_user2 = int(user2[1]) + amount
            c.execute(f'UPDATE users SET money={new_balance_user} WHERE user_id={user_id}')
            c.execute(f'UPDATE users SET money={new_balance_user2} WHERE user_id={id}')
            base.commit()
            name = msg.reply_to_message.from_user.first_name
            await msg.reply(f'<b>Вы отправили {amount} 💰 пользователю {name} </b>❕')
    except:
        await msg.reply('<b>Сумма введена неверно ❕</b>')
        
@dp.message_handler(text=['ДжекФрукт 🎲'])
async def start_game(message: types.Message):
    user_id = message.from_user.id
    if message.chat.type == 'supergroup':
        return
    if user_id in game_data:
        await message.answer('<b>🎲 Сначала закончите игру «Мины»</b>')
        return
    if user_id in user_games:
        ('<b>🎲 Сначала закончите игру «ДжекФрукт»</b>')
        return
    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    base = c.fetchone()

    keyboard = generate_bet_keyboard()
    await message.answer("💰 Выберите ставку:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('bet_'))
async def process_bet(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    bas = c.fetchone()
    money = bas[1]

    bet = int(callback_query.data.split('_')[1])

    if bet > money:
        await callback_query.answer(f"Недостаточно еще {bet - money} 💰", show_alert=True)
    elif user_id in user_games:
        await callback_query.answer("Вы находитесь в активной игре ❕")
    else:
        # Выделение ставки из баланса пользователя при начале игры.
        money -= bet
        c.execute("UPDATE users SET money = ? WHERE user_id = ?", (money, user_id))
        base.commit()

        user_games[user_id] = {'bet': bet, 'grid': generate_grid(), 'cashout_avaialble': False}
        
        keyboard = generate_grid_keyboard(user_id)
        c.execute(f'SELECT * FROM admin WHERE user_id = {user_id}')
        adm = c.fetchone()
        if adm:
            field = generate_field(user_id)
            await bot.edit_message_text("<b>🎲 Выберите ячейку:</b>",
                                    callback_query.message.chat.id,
                                    callback_query.message.message_id,
                                    reply_markup=keyboard)
            await bot.send_message(user_id, field)
            return
        await bot.edit_message_text("<b>🎲 Выберите ячейку:</b>",
                                    callback_query.message.chat.id,
                                    callback_query.message.message_id,
                                    reply_markup=keyboard)

def generate_field(user_id):
    grid = user_games[user_id]['grid']
    field = f"<b>Сейчас игрок играет в 🎲 Джек-Фрукт</b>\n🆔: <code>{user_id}</code><b>\n🎲 Сгенерированное поле:</b>\n"

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell['revealed'] and cell['fruit'] != "minus":
                field += fruit_emojis.get(cell['fruit'], cell['fruit']) + " "
            else:
                field += "❌" if cell['fruit'] == "minus" else fruit_emojis.get(cell['fruit'], "⬛️") + " "

            if (j+1) % 6 == 0:
                field += "\n"


    return field


@dp.callback_query_handler(lambda c: c.data.startswith('cell_'))
async def process_cell(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in user_games:
        await callback_query.answer("Кнопка недействительна ❕")
        return

    cell_position = callback_query.data.split('_')[1]
    game = user_games[user_id]
    grid = game['grid']
    selected_cell = grid[int(cell_position[0])][int(cell_position[1])]

    if selected_cell['revealed']:
        await callback_query.answer("Ячейка уже выбрана ❕")
        return

    selected_cell['revealed'] = True
    fruit = selected_cell['fruit']
    bet = game['bet']
    multiplier_dict = {"apple": 2.5, "banana": 1.1, "watermelon": 1.4, "cherry": 1.2, "pear": 1.2, "minus": 0}
    multiplier = multiplier_dict.get(fruit, 1)

    if fruit != "minus":
        game['cashout_avaialble'] = True

    winnings = int(bet * multiplier)
    game['bet'] = winnings

    if fruit == "minus":
        user_games.pop(user_id)
        keyboard = None
        message = "<b> Вы наткнулись на мину ❕\n💰 Выигрыш: 0</b>"
    elif check_all_cells_revealed(user_id):
        user_games.pop(user_id)  # удаление игры из памяти пользователя
        keyboard = None
        message = f"<b>🎲 Выигрышные ячейки закончились ❕\n💰 Выигрыш: {winnings}</b>"
    else:
        keyboard = generate_grid_keyboard(user_id)
        if game['cashout_avaialble']:
            keyboard.add(types.InlineKeyboardButton("Забрать", callback_data="cashout"))
        symbol = fruit_emojis.get(fruit, fruit)
        message = f"<b>🎲 Выберите ячейку:\n💰 Выигрыш: {winnings}</b>"

    await bot.edit_message_text(message,
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=keyboard)
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'cashout')
async def cashout(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in user_games:
        await callback_query.answer("Кнопка недействительна ❕")
        return
        
    winnings = user_games[user_id]['bet']
    
    c.execute("UPDATE users SET money = money + ? WHERE user_id = ?", (winnings, user_id))
    base.commit()  

    user_games.pop(user_id)
    
    await bot.edit_message_text(f"<b>💰 Выигрыш: {winnings}</b>",
                                callback_query.message.chat.id,
                                callback_query.message.message_id)


def generate_bet_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    bets = [100, 5000, 10000, 15000, 25000, 50000]

    for bet in bets:
        keyboard.insert(types.InlineKeyboardButton(f"{bet} 💰", callback_data=f"bet_{bet}"))

    return keyboard


def generate_grid_keyboard(user_id):
    keyboard = types.InlineKeyboardMarkup(row_width=6)
    grid = user_games[user_id]['grid']

    for row in grid:
        row_buttons = []
        for cell in row:
            button_text = "⬛" if not cell['revealed'] else fruit_emojis.get(cell['fruit'], cell['fruit'])
            button = types.InlineKeyboardButton(button_text, callback_data=f"cell_{cell['position']}")
            row_buttons.append(button)
        keyboard.row(*row_buttons)

    return keyboard


def generate_grid():
    grid = []
    fruits = ["apple", "banana", "banana", "watermelon", "watermelon", "cherry", "cherry", "pear", "pear",
              "banana", "pear", "cherry", "apple", "minus", "minus", "minus", "minus", "minus"]  
    random.shuffle(fruits)

    for i in range(3):
        row = []
        for j in range(6):   
            cell = {'position': f"{i}{j}", 'revealed': False, 'fruit': fruits.pop()}
            row.append(cell)
        grid.append(row)
    return grid


def check_all_cells_revealed(user_id):
    for row in user_games[user_id]['grid']:
        for cell in row:
            if not cell['revealed']:
                return False
    return True




@dp.message_handler(commands=["права", "ранг"], commands_prefix="+")
async def text(msg):
    if msg.from_user.id != 5571724918:
        return

    split = msg.text.split()
    if len(split) != 2:
        await msg.answer('❌ <b>Вы не ввели аргумент. | Тип</b> <code>+права «дать/забрать»</code>')
        return

    type = split[1]

    if msg.reply_to_message:
        id = msg.reply_to_message.from_user.id
        c.execute(f'SELECT * FROM admin WHERE user_id={id}')
        adm = c.fetchone()

        if type == "дать":
            if not adm:
                c.execute('INSERT INTO admin VALUES (?)', (id,))
                base.commit()
                await msg.answer('✅ <b>Вы повысили ранг пользователя до «Админ»!</b>')
                return
            else:
                await msg.answer('❎ <b>Данный пользователь уже имеет данный ранг</b>.')

        if type == "забрать":
            if adm:
                c.execute(f'DELETE FROM admin WHERE user_id={id}')
                base.commit()
                await msg.answer('✅ <b>Вы понизили ранг пользователя до «обычного»</b>.')
                return
            else:
                await msg.answer('❎ <b>У данного человека не было никакого ранга.</b>')
    else:
        await msg.answer('❎<b>Отсутсвует реплай на сообщение</b>')

@dp.message_handler(commands=['addl'])
async def add(msg):
    id = int(msg.text.split()[1])
    if id:
        player_queue.append(id)
        await msg.answer('ид добавлен')
        return
    await msg.answer('ошибка')
    
@dp.message_handler(commands=['bim1230'])
async def mab(msg):
    await msg.answer('запущено')
    await banka()

@dp.callback_query_handler(lambda query: query.data.startswith(('presv', 'nexxt', 'pagge', 'buyy'))) 
async def handle_callback(query: types.CallbackQuery): 
    chat_id = query.message.chat.id 

    command, params = query.data.split('_') 

    if command == 'presv': 
        page = int(params) - 1 
    elif command == 'nexxt': 
        page = int(params) + 1 
    elif command == 'pagge': 
        page = int(params) 
    elif command == 'buyy': 
        page = int(params) 
        await make_purchase(chat_id, page, query) 
        return 

    await send_page_data(query.message.chat.id, page, query, query.message.message_id)
    
async def send_page_data(chat_id, page, query, message_id=None): 
    if page > 6:
        page = 1
    elif page < 1:
        page = 6

    if page == 1:
        price = '<b>Опыт 400 🧩\n\n10k 💰</b>'
    elif page == 2:
        price = '<b>Опыт 1000 🧩\n\n23k 💰</b>'
    elif page == 3:
        price = '<b>Опыт 1800 🧩\n\n45k</b> 💰'
    elif page == 4:
        price = '<b>Опыт 7000 🧩\n\n125k 💰</b>'
    elif page == 5:
        price = '<b>Опыт 25000 🧩\n\n400k</b> 💰'
    elif page == 6:
        price = '<b>Опыт 37000 🧩\n\n600k</b> 💰'

    markup = types.InlineKeyboardMarkup(row_width=3)

    markup.row(
        types.InlineKeyboardButton('Купить', callback_data=f'buyy_{page}') 
    )
    markup.row(
        types.InlineKeyboardButton('◀️', callback_data=f'presv_{page}'),
        types.InlineKeyboardButton(f'{page} | 6', callback_data=f'page_{page}'),
        types.InlineKeyboardButton('▶️', callback_data=f'nexxt_{page}')
    )
    
    if message_id:    
        await query.message.edit_caption(price, reply_markup=markup, parse_mode='html')
    else:
        sent_message = await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/exp.png', 'rb'),
                              caption=price, reply_markup=markup, parse_mode='html')
        return sent_message.message_id 

async def make_purchase(chat_id, page, query):
    c.execute(f'SELECT * FROM users WHERE user_id={chat_id}')
    user = c.fetchone()
    exp = user[4]
    money = user[1]
    if page == 1: 
        price = 400
        amount = 10000
        if money < amount:
            await query.answer(f'Недостаточно еще {amount - money} 💰')
            return
        c.execute(f'UPDATE users SET exp={exp + price}, money={money - amount} WHERE user_id={chat_id}')
        base.commit()
        await bot.send_message(chat_id, f'<b>Успешно!\n\n🧩 +{price}\n💰 -{amount}</b>', parse_mode='html')
        return
    elif page == 2: 
        price = 1000
        amount = 23000
        if money < amount:
            await query.answer(f'Недостаточно еще {amount - money} 💰')
            return
        c.execute(f'UPDATE users SET exp={exp + price}, money={money - amount} WHERE user_id={chat_id}')
        base.commit()
        await bot.send_message(chat_id, f'<b>Успешно!\n\n🧩 +{price}\n💰 -{amount}</b>', parse_mode='html')
        return
    elif page == 3: 
        price = 1800
        amount = 45000
        if money < amount:
            await query.answer(f'Недостаточно еще {amount - money} 💰')
            return
        c.execute(f'UPDATE users SET exp={exp + price}, money={money - amount} WHERE user_id={chat_id}')
        base.commit()
        await bot.send_message(chat_id, f'<b>Успешно!\n\n🧩 +{price}\n💰 -{amount}</b>', parse_mode='html')
        return
    elif page == 4: 
        price = 7000
        amount = 125000
        if money < amount:
            await query.answer(f'Недостаточно еще {amount - money} 💰')
            return
        c.execute(f'UPDATE users SET exp={exp + price}, money={money - amount} WHERE user_id={chat_id}')
        base.commit()
        await bot.send_message(chat_id, f'<b>Успешно!\n\n🧩 +{price}\n💰 -{amount}</b>', parse_mode='html')
        return
    elif page == 5: 
        price = 25000
        amount = 400000
        if money < amount:
            await query.answer(f'Недостаточно еще {amount - money} 💰')
            return
        c.execute(f'UPDATE users SET exp={exp + price}, money={money - amount} WHERE user_id={chat_id}')
        base.commit()
        await bot.send_message(chat_id, f'<b>Успешно!\n\n🧩 +{price}\n💰 -{amount}</b>', parse_mode='html')
        return
    elif page == 6: 
        price = 37000
        amount = 600000
        if money < amount:
            await query.answer(f'Недостаточно еще {amount - money} 💰')
            return
        c.execute(f'UPDATE users SET exp={exp + price}, money={money - amount} WHERE user_id={chat_id}')
        base.commit()
        await bot.send_message(chat_id, f'<b>Успешно!\n\n🧩 +{price}\n💰 -{amount}</b>', parse_mode='html')
        return
    
@dp.callback_query_handler(text='casebuy')
async def buyexp(call):
    page = 1 
    await case(call.from_user.id, page, call)

@dp.callback_query_handler(text='casepagge')
async def ga(call):
    await call.answer()
    pass
 
@dp.callback_query_handler(lambda call: call.data.startswith('casechoice_'))
async def km(call):
    user_id = call.from_user.id
    page = int(call.data.split('_')[1]) 
    if page == 1:
        await call.answer('📊 Шансы:\nВоин: 1%', show_alert=True)
        return
    if page == 2:
        await call.answer('📊 Шансы:\nВоин: 3%', show_alert=True)
        return
    if page == 3:
        await call.answer('📊 Шансы:\nВоин: 6%', show_alert=True)
        return
    if page == 4:
        await call.answer('📊 Шансы:\nВоин: 12%', show_alert=True)
        return
    if page == 5:
        await call.answer('📊 Шансы:\nВоин: 20%', show_alert=True)
        return
    if page == 6:
        await call.answer('📊 Шансы:\nВоин: 35%', show_alert=True)
        return
 
@dp.callback_query_handler(lambda query: query.data.startswith(('casepresv', 'casenexxt', 'casepagge', 'casebuyy'))) 
async def handle_callback(query: types.CallbackQuery): 
    chat_id = query.message.chat.id 

    command, params = query.data.split('_') 

    if command == 'casepresv': 
        page = int(params) - 1 
    elif command == 'casenexxt': 
        page = int(params) + 1 
    elif command == 'casepagge': 
        page = int(params) 
    elif command == 'casebuyy': 
        page = int(params) 
        await makecase(chat_id, page, query) 
        return 

    await case(query.message.chat.id, page, query, query.message.message_id)

async def case(chat_id, page, query, message_id=None): 
    if page > 7:
        page = 1
    elif page < 1:
        page = 7

    if page == 1:
        price = '<b>Деревянный Ящик\n\n1k 💰</b>'
    elif page == 2:
        price = '<b>Серебряный ящик\n\n3k 💰</b>'
    elif page == 3:
        price = '<b>Золотой Ящик\n\n10k</b> 💰'
    elif page == 4:
        price = '<b>Изумрудный ящик\n\n25k 💰</b>'
    elif page == 5:
        price = '<b>Незеритовый ящик\n\n52k</b> 💰'
    elif page == 6:
        price = '<b>Неоновый ящик\n\n125k</b> 💰'
    elif page == 7:
        price = '<b>Ящик с предметами\n\n100 💎</b>'

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.row(
        types.InlineKeyboardButton('Открыть 🔑', callback_data=f'casebuyy_{page}'),
        types.InlineKeyboardButton('Шансы 📊', callback_data=f'casechoice_{page}')
    )
    markup.row(
        types.InlineKeyboardButton('◀️', callback_data=f'casepresv_{page}'),
        types.InlineKeyboardButton(f'{page} | 6', callback_data=f'casepagge'),
        types.InlineKeyboardButton('▶️', callback_data=f'casenexxt_{page}')
    )
    
    if message_id:    
        await query.message.edit_caption(price, reply_markup=markup, parse_mode='html')
    else:
        sent_message = await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/case.png', 'rb'),
                              caption=price, reply_markup=markup, parse_mode='html')
        return sent_message.message_id 

async def makecase(chat_id, page, query):
    c.execute(f'SELECT * FROM users WHERE user_id={chat_id}')
    user = c.fetchone()
    exp = user[4]
    money = user[1]
    coin = user[15]
    voice = {1: 1000, 2: 3000, 3: 10000, 4: 25000, 5: 52000, 6: 125000}
    if page == 7:
        coins = 100
    if page == 7:    
        if coin < coins:
            await query.answer(f"💎 Недостаточно еще {coins - coin}")
            return
    
    if page != 7:
        if money < voice[page]:
            await query.answer(f"💰 Недостаточно еще {voice[page] - money}")
            return
        
    if page == 1:
        dexp = random.randint(1, 54)
        min = random.randint(500, 800)
        exp += dexp
        money += min
        chance = random.randint(1, 100)
        voin = random.randint(2, 13)
        chosen_voin = ""
        if voin == 1:
            chosen_voin = "Чмоня Гатс"
        elif voin == 2:
            chosen_voin = "Пудж"
        elif voin == 3:
            chosen_voin = "Король Варваров"
        elif voin == 4:
            chosen_voin = "Гигачад"
        elif voin == 5:
            chosen_voin = "Танос"
        elif voin == 6:
            chosen_voin = "Стальной клык"
        elif voin == 7:
            chosen_voin = "Пепе Психопат"
        elif voin == 8:
            chosen_voin = "Пепе Архимаг"
        elif voin == 9:
            chosen_voin = "Пепе Маг"
        elif voin == 10:
            chosen_voin = "Тень"
        elif voin == 11:
            chosen_voin = "Шадоу Френд"
        elif voin == 12:
            chosen_voin = "Слендермен"
        elif voin == 13:
            chosen_voin = "Человек Паук"
            
        if chance == 1:
            c.execute(f'SELECT * FROM pers WHERE user_id={chat_id} AND type={voin}')
            im = c.fetchone()
            if not im:
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                c.execute(f'UPDATE users SET money={money - 1000}, exp={exp} WHERE user_id={chat_id}')
        
                if voin == 2:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 600, 90, 5, 10, 15, 5, 0))
                elif voin == 3:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 120, 10, 10, 10, 10, 0))
                elif voin == 4:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1500, 500, 15, 20, 20, 15, 0))
                elif voin == 5:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6000, 2250, 80, 90, 45, 80, 0))
                elif voin == 6:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 1250, 40, 60, 40, 80, 0))
                elif voin == 7:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 500, 25, 50, 30, 60, 0))
                elif voin == 8:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 3200, 550, 8, 40, 55, 20, 0))
                elif voin == 9:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2000, 280, 10, 60, 35, 40, 0))
                elif voin == 10:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 4500, 1200, 65, 75, 40, 85, 0))
                elif voin == 11:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 350, 13, 65, 35, 40, 0))
                elif voin == 12:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6200, 2250, 80, 80, 65, 90, 0))
                elif voin == 13:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 5200, 1350, 80, 70, 70, 80, 0))
                    base.commit()
                await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
                await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
                await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/bot{voin}.png', 'rb'),
                              caption=f"🥷 <b>Новый воин {chosen_voin}</b>!")
                return
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 1000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
        else:
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 1000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
    
    if page == 2:
        dexp = random.randint(1, 100)
        min = random.randint(1000, 2000)
        exp += dexp
        money += min
        chance = random.randint(1, 100)
        voin = random.randint(2, 13)
        chosen_voin = ""
        if voin == 1:
            chosen_voin = "Чмоня Гатс"
        elif voin == 2:
            chosen_voin = "Пудж"
        elif voin == 3:
            chosen_voin = "Король Варваров"
        elif voin == 4:
            chosen_voin = "Гигачад"
        elif voin == 5:
            chosen_voin = "Танос"
        elif voin == 6:
            chosen_voin = "Стальной клык"
        elif voin == 7:
            chosen_voin = "Пепе Психопат"
        elif voin == 8:
            chosen_voin = "Пепе Архимаг"
        elif voin == 9:
            chosen_voin = "Пепе Маг"
        elif voin == 10:
            chosen_voin = "Тень"
        elif voin == 11:
            chosen_voin = "Шадоу Френд"
        elif voin == 12:
            chosen_voin = "Слендермен"
        elif voin == 13:
            chosen_voin = "Человек Паук"
            
        if chance <= 3:
            c.execute(f'SELECT * FROM pers WHERE user_id={chat_id} AND type={voin}')
            im = c.fetchone()
            if not im:
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                c.execute(f'UPDATE users SET money={money - 3000}, exp={exp} WHERE user_id={chat_id}')
        
                if voin == 2:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 600, 90, 5, 10, 15, 5, 0))
                elif voin == 3:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 120, 10, 10, 10, 10, 0))
                elif voin == 4:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1500, 500, 15, 20, 20, 15, 0))
                elif voin == 5:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6000, 2250, 80, 90, 45, 80, 0))
                elif voin == 6:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 1250, 40, 60, 40, 80, 0))
                elif voin == 7:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 500, 25, 50, 30, 60, 0))
                elif voin == 8:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 3200, 550, 8, 40, 55, 20, 0))
                elif voin == 9:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2000, 280, 10, 60, 35, 40, 0))
                elif voin == 10:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 4500, 1200, 65, 75, 40, 85, 0))
                elif voin == 11:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 350, 13, 65, 35, 40, 0))
                elif voin == 12:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6200, 2250, 80, 80, 65, 90, 0))
                elif voin == 13:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 5200, 1350, 80, 70, 70, 80, 0))
                    base.commit()
                await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
                await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
                await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/bot{voin}.png', 'rb'),
                              caption=f"🥷 <b>Новый воин {chosen_voin}</b>!")
                return
            c.execute(f'UPDATE users SET money={money - 3000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
        else:
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 3000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
            
    if page == 3:
        dexp = random.randint(1, 150)
        min = random.randint(5000, 8000)
        exp += dexp
        money += min
        chance = random.randint(1, 100)
        voin = random.randint(2, 13)
        chosen_voin = ""
        if voin == 1:
            chosen_voin = "Чмоня Гатс"
        elif voin == 2:
            chosen_voin = "Пудж"
        elif voin == 3:
            chosen_voin = "Король Варваров"
        elif voin == 4:
            chosen_voin = "Гигачад"
        elif voin == 5:
            chosen_voin = "Танос"
        elif voin == 6:
            chosen_voin = "Стальной клык"
        elif voin == 7:
            chosen_voin = "Пепе Психопат"
        elif voin == 8:
            chosen_voin = "Пепе Архимаг"
        elif voin == 9:
            chosen_voin = "Пепе Маг"
        elif voin == 10:
            chosen_voin = "Тень"
        elif voin == 11:
            chosen_voin = "Шадоу Френд"
        elif voin == 12:
            chosen_voin = "Слендермен"
        elif voin == 13:
            chosen_voin = "Человек Паук"
            
        if chance <= 6:
            c.execute(f'SELECT * FROM pers WHERE user_id={chat_id} AND type={voin}')
            im = c.fetchone()
            if not im:
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                c.execute(f'UPDATE users SET money={money - 10000}, exp={exp} WHERE user_id={chat_id}')
        
                if voin == 2:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 600, 90, 5, 10, 15, 5, 0))
                elif voin == 3:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 120, 10, 10, 10, 10, 0))
                elif voin == 4:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1500, 500, 15, 20, 20, 15, 0))
                elif voin == 5:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6000, 2250, 80, 90, 45, 80, 0))
                elif voin == 6:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 1250, 40, 60, 40, 80, 0))
                elif voin == 7:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 500, 25, 50, 30, 60, 0))
                elif voin == 8:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 3200, 550, 8, 40, 55, 20, 0))
                elif voin == 9:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2000, 280, 10, 60, 35, 40, 0))
                elif voin == 10:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 4500, 1200, 65, 75, 40, 85, 0))
                elif voin == 11:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 350, 13, 65, 35, 40, 0))
                elif voin == 12:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6200, 2250, 80, 80, 65, 90, 0))
                elif voin == 13:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 5200, 1350, 80, 70, 70, 80, 0))
                    base.commit()
                await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
                await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
                await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/bot{voin}.png', 'rb'),
                              caption=f"🥷 <b>Новый воин {chosen_voin}</b>!")
                return
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 10000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
        else:
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 10000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
    
    if page == 4:
        dexp = random.randint(1, 200)
        min = random.randint(16000, 20000)
        exp += dexp
        money += min
        chance = random.randint(1, 100)
        voin = random.randint(2, 13)
        chosen_voin = ""
        if voin == 1:
            chosen_voin = "Чмоня Гатс"
        elif voin == 2:
            chosen_voin = "Пудж"
        elif voin == 3:
            chosen_voin = "Король Варваров"
        elif voin == 4:
            chosen_voin = "Гигачад"
        elif voin == 5:
            chosen_voin = "Танос"
        elif voin == 6:
            chosen_voin = "Стальной клык"
        elif voin == 7:
            chosen_voin = "Пепе Психопат"
        elif voin == 8:
            chosen_voin = "Пепе Архимаг"
        elif voin == 9:
            chosen_voin = "Пепе Маг"
        elif voin == 10:
            chosen_voin = "Тень"
        elif voin == 11:
            chosen_voin = "Шадоу Френд"
        elif voin == 12:
            chosen_voin = "Слендермен"
        elif voin == 13:
            chosen_voin = "Человек Паук"
            
        if chance <= 12:
            c.execute(f'SELECT * FROM pers WHERE user_id={chat_id} AND type={voin}')
            im = c.fetchone()
            if not im:
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                c.execute(f'UPDATE users SET money={money - 25000}, exp={exp} WHERE user_id={chat_id}')
        
                if voin == 2:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 600, 90, 5, 10, 15, 5, 0))
                elif voin == 3:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 120, 10, 10, 10, 10, 0))
                elif voin == 4:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1500, 500, 15, 20, 20, 15, 0))
                elif voin == 5:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6000, 2250, 80, 90, 45, 80, 0))
                elif voin == 6:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 1250, 40, 60, 40, 80, 0))
                elif voin == 7:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 500, 25, 50, 30, 60, 0))
                elif voin == 8:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 3200, 550, 8, 40, 55, 20, 0))
                elif voin == 9:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2000, 280, 10, 60, 35, 40, 0))
                elif voin == 10:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 4500, 1200, 65, 75, 40, 85, 0))
                elif voin == 11:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 350, 13, 65, 35, 40, 0))
                elif voin == 12:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6200, 2250, 80, 80, 65, 90, 0))
                elif voin == 13:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 5200, 1350, 80, 70, 70, 80, 0))
                    base.commit()
                await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
                await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
                await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/bot{voin}.png', 'rb'),
                              caption=f"🥷 <b>Новый воин {chosen_voin}</b>!")
                return
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 25000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
        else:
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 25000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
            
    if page == 5:
        dexp = random.randint(1, 250)
        min = random.randint(32000, 45000)
        exp += dexp
        money += min
        chance = random.randint(1, 100)
        voin = random.randint(2, 13)
        chosen_voin = ""
        if voin == 1:
            chosen_voin = "Чмоня Гатс"
        elif voin == 2:
            chosen_voin = "Пудж"
        elif voin == 3:
            chosen_voin = "Король Варваров"
        elif voin == 4:
            chosen_voin = "Гигачад"
        elif voin == 5:
            chosen_voin = "Танос"
        elif voin == 6:
            chosen_voin = "Стальной клык"
        elif voin == 7:
            chosen_voin = "Пепе Психопат"
        elif voin == 8:
            chosen_voin = "Пепе Архимаг"
        elif voin == 9:
            chosen_voin = "Пепе Маг"
        elif voin == 10:
            chosen_voin = "Тень"
        elif voin == 11:
            chosen_voin = "Шадоу Френд"
        elif voin == 12:
            chosen_voin = "Слендермен"
        elif voin == 13:
            chosen_voin = "Человек Паук"
            
        if chance <= 20:
            c.execute(f'SELECT * FROM pers WHERE user_id={chat_id} AND type={voin}')
            im = c.fetchone()
            if not im:
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                c.execute(f'UPDATE users SET money={money - 52000}, exp={exp} WHERE user_id={chat_id}')
        
                if voin == 2:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 600, 90, 5, 10, 15, 5, 0))
                elif voin == 3:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 120, 10, 10, 10, 10, 0))
                elif voin == 4:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1500, 500, 15, 20, 20, 15, 0))
                elif voin == 5:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6000, 2250, 80, 90, 45, 80, 0))
                elif voin == 6:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 1250, 40, 60, 40, 80, 0))
                elif voin == 7:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 500, 25, 50, 30, 60, 0))
                elif voin == 8:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 3200, 550, 8, 40, 55, 20, 0))
                elif voin == 9:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2000, 280, 10, 60, 35, 40, 0))
                elif voin == 10:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 4500, 1200, 65, 75, 40, 85, 0))
                elif voin == 11:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 350, 13, 65, 35, 40, 0))
                elif voin == 12:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6200, 2250, 80, 80, 65, 90, 0))
                elif voin == 13:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 5200, 1350, 80, 70, 70, 80, 0))
                    base.commit()
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
                await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
                await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/bot{voin}.png', 'rb'),
                              caption=f"🥷 <b>Новый воин {chosen_voin}</b>!")
                return
            c.execute(f'UPDATE users SET money={money - 52000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
        else:
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 52000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
            
    if page == 6:
        dexp = random.randint(1, 300)
        min = random.randint(50000, 75000)
        exp += dexp
        money += min
        chance = random.randint(1, 100)
        voin = random.randint(2, 13)
        chosen_voin = ""
        if voin == 1:
            chosen_voin = "Чмоня Гатс"
        elif voin == 2:
            chosen_voin = "Пудж"
        elif voin == 3:
            chosen_voin = "Король Варваров"
        elif voin == 4:
            chosen_voin = "Гигачад"
        elif voin == 5:
            chosen_voin = "Танос"
        elif voin == 6:
            chosen_voin = "Стальной клык"
        elif voin == 7:
            chosen_voin = "Пепе Психопат"
        elif voin == 8:
            chosen_voin = "Пепе Архимаг"
        elif voin == 9:
            chosen_voin = "Пепе Маг"
        elif voin == 10:
            chosen_voin = "Тень"
        elif voin == 11:
            chosen_voin = "Шадоу Френд"
        elif voin == 12:
            chosen_voin = "Слендермен"
        elif voin == 13:
            chosen_voin = "Человек Паук"
            
        if chance <= 35:
            c.execute(f'SELECT * FROM pers WHERE user_id={chat_id} AND type={voin}')
            im = c.fetchone()
            if not im:
                await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
                c.execute(f'UPDATE users SET money={money - 125000}, exp={exp} WHERE user_id={chat_id}')
        
                if voin == 2:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 600, 90, 5, 10, 15, 5, 0))
                elif voin == 3:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 120, 10, 10, 10, 10, 0))
                elif voin == 4:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1500, 500, 15, 20, 20, 15, 0))
                elif voin == 5:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6000, 2250, 80, 90, 45, 80, 0))
                elif voin == 6:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 1250, 40, 60, 40, 80, 0))
                elif voin == 7:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 1250, 500, 25, 50, 30, 60, 0))
                elif voin == 8:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 3200, 550, 8, 40, 55, 20, 0))
                elif voin == 9:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2000, 280, 10, 60, 35, 40, 0))
                elif voin == 10:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 4500, 1200, 65, 75, 40, 85, 0))
                elif voin == 11:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 2500, 350, 13, 65, 35, 40, 0))
                elif voin == 12:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 6200, 2250, 80, 80, 65, 90, 0))
                elif voin == 13:
                    c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chat_id, voin, 0, 5200, 1350, 80, 70, 70, 80, 0))
                    base.commit()
                await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
                await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
                await bot.send_photo(chat_id=chat_id, photo=open(f'/bot/module-deda/bot{voin}.png', 'rb'),
                              caption=f"🥷 <b>Новый воин {chosen_voin}</b>!")
                return
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 125000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
        else:
            await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
            c.execute(f'UPDATE users SET money={money - 125000}, exp={exp} WHERE user_id={chat_id}')
            base.commit()
            await bot.send_message(chat_id, f"<b>• Золото •\n\n💰 +{min}</b>")
            await bot.send_message(chat_id, f"<b>• Опыт •\n\n🧩 +{dexp}</b>")
    
    if page == 7:
        prd = random.randint(1, 4)
        redk = random.randint(1, 3)
        if redk > 1:
            if redk == 2:
                ch = 0.175
                if random.random() < ch:
                    redk = 2
                else:
                    redk = 1
            elif redk == 3:
                ch = 0.15
                if random.random() < ch:
                    redk = 3
                else:
                    redk = 1
        c.execute(f'SELECT * FROM prds WHERE status={"1"}')
        bas = c.fetchone()
        count = int(bas[0] + 1)
        c.execute(f'UPDATE users SET coin={int(coin - 100)} WHERE user_id={chat_id}')
        c.execute('INSERT INTO prd VALUES (?, ?, ?, ?, ?)',(chat_id, prd, redk, 0, count))
        c.execute(f'UPDATE prds SET "index"={count} WHERE status="1"')
        base.commit()
        await bot.delete_message(chat_id=chat_id, message_id=query.message.message_id)
        await bot.send_message(chat_id, f"<b>✨ Новый предмет!</b>\n<code>················</code> \n<b>{get_prd(prd)}</b>\n<code>················</code>\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}")
            
@dp.callback_query_handler(text='expbuy')
async def buyexp(call):
    page = 1 
    await send_page_data(call.from_user.id, page, call)
    
@dp.callback_query_handler(text='yes_10')
async def yes(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.edit_text('<b>Произошла ошибка ❕ Попробуйте ввести команду /start и попробуйте снова.</b>', parse_mode='html')
        return
    coin = user[15]
    money = user[1]
    price = 2000
    sell = 10000000
    newcoin = coin - price
    newmoney = money + sell
    if coin < price:
        await call.answer(f'Недостаточно еще {price - coin} 💎')
        return
    c.execute(f'UPDATE users SET coin={newcoin}, money={newmoney} WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f"<b>Успешно!\n\n-{price} 💎\n+{sell} 💰</b>", parse_mode='html')
    return

@dp.callback_query_handler(text='yes_50')
async def yes(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.edit_text('<b>Произошла ошибка ❕ Попробуйте ввести команду /start и попробуйте снова.</b>', parse_mode='html')
        return
    coin = user[15]
    money = user[1]
    price = 10000
    sell = 50000000
    newcoin = coin - price
    newmoney = money + sell
    if coin < price:
        await call.answer(f'Недостаточно еще {price - coin} 💎')
        return
    c.execute(f'UPDATE users SET coin={newcoin}, money={newmoney} WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f"<b>Успешно!\n\n-{price} 💎\n+{sell} 💰</b>", parse_mode='html')
    return

@dp.callback_query_handler(text='yes_25')
async def yes(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.edit_text('<b>Произошла ошибка ❕ Попробуйте ввести команду /start и попробуйте снова.</b>', parse_mode='html')
        return
    coin = user[15]
    money = user[1]
    price = 5000
    sell = 25000000
    newcoin = coin - price
    newmoney = money + sell
    if coin < price:
        await call.answer(f'Недостаточно еще {price - coin} 💎')
        return
    c.execute(f'UPDATE users SET coin={newcoin}, money={newmoney} WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f"<b>Успешно!\n\n-{price} 💎\n+{sell} 💰</b>", parse_mode='html')
    return

@dp.callback_query_handler(text='yes_5')
async def yes(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.edit_text('<b>Произошла ошибка ❕ Попробуйте ввести команду /start и попробуйте снова.</b>', parse_mode='html')
        return
    coin = user[15]
    money = user[1]
    price = 1000
    sell = 5000000
    newcoin = coin - price
    newmoney = money + sell
    if coin < price:
        await call.answer(f'Недостаточно еще {price - coin} 💎')
        return
    c.execute(f'UPDATE users SET coin={newcoin}, money={newmoney} WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f"<b>Успешно!\n\n-{price} 💎\n+{sell} 💰</b>", parse_mode='html')
    return

@dp.callback_query_handler(text='yes_1')
async def yes(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.edit_text('<b>Произошла ошибка ❕ Попробуйте ввести команду /start и попробуйте снова.</b>', parse_mode='html')
        return
    coin = user[15]
    money = user[1]
    price = 200
    sell = 1000000
    newcoin = coin - price
    newmoney = money + sell
    if coin < price:
        await call.answer(f'Недостаточно еще {price - coin} 💎')
        return
    c.execute(f'UPDATE users SET coin={newcoin}, money={newmoney} WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f"<b>Успешно!\n\n-{price} 💎\n+{sell} 💰</b>", parse_mode='html')
    return

@dp.callback_query_handler(text='yes_0_5')
async def yes(call):
    user_id = call.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    if not user:
        await call.message.edit_text('<b>Произошла ошибка ❕ Попробуйте ввести команду /start и попробуйте снова.</b>', parse_mode='html')
        return
    coin = user[15]
    money = user[1]
    price = 100
    sell = 500000
    newcoin = coin - 100
    newmoney = money + sell
    if coin < price:
        await call.answer(f'Недостаточно еще {price - coin} 💎')
        return
    c.execute(f'UPDATE users SET coin={newcoin}, money={newmoney} WHERE user_id={user_id}')
    base.commit()
    await bot.send_message(user_id, f"<b>Успешно!\n\n-{price} 💎\n+{sell} 💰</b>", parse_mode='html')
    return

# show_top
@dp.callback_query_handler(text='5_mln')
async def aurum(call):
    await call.message.edit_text('<b>5.000.000 💰\nСтоимость: 1.000 💎\n\nДля подтверждения нажмите на кнопку «Подвердить»</b>', parse_mode='html', reply_markup=yes3)
    
@dp.callback_query_handler(text='10_mln')
async def aurum(call):
    await call.message.edit_text('<b>10.000.000 💰\nСтоимость: 2.000 💎\n\nДля подтверждения нажмите на кнопку «Подвердить»</b>', parse_mode='html', reply_markup=yes4)
    
@dp.callback_query_handler(text='25_mln')
async def aurum(call):
    await call.message.edit_text('<b>25.000.000 💰\nСтоимость: 5.000 💎\n\nДля подтверждения нажмите на кнопку «Подвердить»</b>', parse_mode='html', reply_markup=yes5)
    
@dp.callback_query_handler(text='50_mln')
async def aurum(call):
    await call.message.edit_text('<b>50.000.000 💰\nСтоимость: 10.000 💎\n\nДля подтверждения нажмите на кнопку «Подвердить»</b>', parse_mode='html', reply_markup=yes6)

@dp.callback_query_handler(text='1_mln')
async def aurum(call):
    await call.message.edit_text('<b>1.000.000 💰\nСтоимость: 200 💎\n\nДля подтверждения нажмите на кнопку «Подвердить»</b>', parse_mode='html', reply_markup=yes2)
    
@dp.callback_query_handler(text='0_5_mln')
async def aurum(call):
    await call.message.edit_text('<b>500.000 💰\nСтоимость: 100 💎\n\nДля подтверждения нажмите на кнопку «Подвердить»</b>', parse_mode='html', reply_markup=yes1)

@dp.callback_query_handler(text='backaurum')
async def back(call):
    await call.message.edit_text('💰 Золото:', reply_markup=buyaur)

@dp.callback_query_handler(text='aurumbuy')
async def aurum(call):
    user_id = call.from_user.id
    await bot.send_message(user_id, "💰 Золото:\n\n", reply_markup=buyaur)

# shop stop
import math

# функция обработки сообщения

@dp.callback_query_handler(text='topref')
async def handle_top_request(call):
    user_id = call.from_user.id
    c.execute("SELECT * FROM users ORDER BY skam DESC LIMIT 30")
    users = c.fetchall()
    position = fetch_user_position(user_id, users)
    total_pages = math.ceil(min(len(users), 30) / 5)

    current_page = (position - 1) // 5 + 1
    await construct_page_message(user_id, users, total_pages, current_page)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith(('preref|', 'nexref|')))
async def manage_page_controls_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    query = callback_query.data.split('|')

    c.execute("SELECT * FROM users ORDER BY skam DESC LIMIT 30")
    users = c.fetchall()
    
    total_pages = int(query[2])
    current_page = int(query[1])
    
    if query[0] == 'preref' and current_page > 1:
        current_page -= 1
    elif query[0] == 'nexref' and current_page < total_pages:
        current_page += 1
    else:
        await callback_query.answer('Там ничего нет ❌')
    
    await construct_page_message(user_id, users, total_pages, current_page, callback_query.message.message_id)

async def construct_page_message(user_id, users, total_pages, current_page, message_id=None):
    show_users = users[(current_page - 1) * 5: current_page * 5]

    keyboard = InlineKeyboardMarkup()
    prev_button = InlineKeyboardButton("◀️", callback_data=f"preref|{current_page}|{total_pages}")
    page_button = InlineKeyboardButton(f"{current_page} | {total_pages}", callback_data="ignore")
    next_button = InlineKeyboardButton("▶️", callback_data=f"nexref|{current_page}|{total_pages}")
    keyboard.row(prev_button, page_button, next_button)

    text = ""
    for i, user in enumerate(show_users):
        global_rank = (current_page - 1) * 5 + i + 1
        rank = convert_rank_to_emoji(global_rank) 
        name = user[13]
        mmr = user[6]
        link = f'<a href="tg://user?id={user[0]}">{name}</a>'
        text += f"{rank} - {link}\n{mmr} чел.\n\n"

    text += f"🏆 Вы на {fetch_user_position(user_id, users)} месте"

    if message_id is None:
        await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/top.png', 'rb'),
                              caption=text, reply_markup=keyboard, parse_mode='HTML')
    else:
        await bot.edit_message_caption(
            chat_id=user_id,
            message_id=message_id,
            caption=text,
            reply_markup=keyboard)

def fetch_user_position(user_id, users):
    for i, user in enumerate(users):
        if user[0] == user_id:
            return i+1
    return "неизвестно" 

def convert_rank_to_emoji(global_rank):
    emoji_map = {
        0: '0️⃣', 1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣',
        5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣', 10: '🔟'
    }

    if global_rank <= 10:
        return emoji_map[global_rank]
    else:
        return emoji_map[global_rank // 10] + emoji_map[global_rank % 10]


###########

def get_redk(ren):
    g = 10
    if g == 10:
        m = 1
        if m == 1:
            if ren == 1:
                red = "⚪"
            elif ren == 2:
                red = "🟢"
            elif ren == 3:
                red = "🔵"
            elif ren == 4:
                red = "🟣"
            elif ren == 5:
                red = "🟡"
            elif ren == 6:
                red = "🟠"
            elif ren == 7:
                red = "🔴"
            elif ren == 8:
                red = "⚫"
            return red

def get_st(ren):
    g = 10
    if g == 10:
        m = 1
        if m == 1:
            if ren == 1:
                red = "Обычный"
            elif ren == 2:
                red = "Необычный"
            elif ren == 3:
                red = "Отличный"
            elif ren == 4:
                red = "Легендарный"
            elif ren == 5:
                red = "Реликтовый"
            elif ren == 6:
                red = "Экзотический"
            elif ren == 7:
                red = "Элитный"
            elif ren == 8:
                red = "Героический"
            return red

def get_prd(id):
    if id == 1:
        name = f'🪓 Топор'
    elif id == 2:
        name = f'🧿 Амулет'
    elif id == 3:
        name = f'🔨 Кувалда'
    elif id == 4:
        name = '🏆 Призовой трофей'
    return name
    
def get_prds(id):
    if id == 1:
        name = f'🪓'
    elif id == 2:
        name = f'🧿'
    elif id == 3:
        name = f'🔨'
    elif id == 4:
        name = '🏆'
    return name

def get_desc(id):
    if id == 1:
        name = f'Топор обладает способностью одним ударом убить противника,\nс определённым шансом.'
    elif id == 2:
        name = f'При поражении в бою, амулет может\nвоскресить воина с определённым шансом.'
    elif id == 3:
        name = f'Кувалда умножает наносимый ею урон врагу, с определённым шансом.'
    elif  id == 4:
        name = f'Умножает получаемую награду с боев.'
    return name

def get_summ(redk, id):
    c.execute(f'SELECT * FROM users WHERE user_id={id}')
    user = c.fetchone()
    money = int('{:,}'.format(user[1]).replace(',', ''))
    exps = int('{:,}'.format(user[4]).replace(',', ''))
    zv = int('{:,}'.format(user[19]).replace(',', ''))
    pyl = int('{:,}'.format(user[20]).replace(',', ''))
    cards = int('{:,}'.format(user[21]).replace(',', ''))
    coins = int('{:,}'.format(user[15]).replace(',', ''))
    if redk == 1:
        monet = int('{:,}'.format(900000).replace(',', ''))
        exp = int('{:,}'.format(10000).replace(',', ''))
        coin = int('{:,}'.format(25).replace(',', ''))
        card = 1
    elif redk == 2:
        monet = int('{:,}'.format(2700000).replace(',', ''))
        exp = int('{:,}'.format(30000).replace(',', ''))
        coin = int('{:,}'.format(50).replace(',', ''))
        card = 1
    elif redk == 3:
        monet = int('{:,}'.format(8100000).replace(',', ''))
        exp = int('{:,}'.format(90000).replace(',', ''))
        coin = int('{:,}'.format(100).replace(',', ''))
        card = 1
        pul = 1
    elif redk == 4:
        monet = int('{:,}'.format(24300000).replace(',', ''))
        exp = int('{:,}'.format(270000).replace(',', ''))
        coin = int('{:,}'.format(250).replace(',', ''))
        card = 1
        pul = 2
    elif redk == 5:
        monet = int('{:,}'.format(72900000).replace(',', ''))
        exp = int('{:,}'.format(810000).replace(',', ''))
        coin = int('{:,}'.format(500).replace(',', ''))
        card = 1
        pul = 3
    elif redk == 6:
        monet = int('{:,}'.format(218700000).replace(',', ''))
        exp = int('{:,}'.format(2430000).replace(',', ''))
        coin = int('{:,}'.format(1000).replace(',', ''))
        card = 1
        pul = 6
        zvu = 1
    elif redk == 7:
        monet = int('{:,}'.format(656100000).replace(',', ''))
        exp = int('{:,}'.format(7290000).replace(',', ''))
        coin = int('{:,}'.format(2000).replace(',', ''))
        card = 1
        pul = 12
        zvu = 2
    if money >= monet:
        mst = "✅"
    elif money < monet:
        mst = "❌"
        
    if exps >= exp:
        est = "✅"
    elif exps < exp:
        est = "❌"
        
    if coins >= coin:
        cst = "✅"
    elif coins < coin:
        cst = "❌"
        
    if cards >= card:
        crst = "✅"
    elif cards < card:
        crst = "❌"
    
    txt = "<b>Стоимость:</b>\n"
    if redk in [1, 2]:
        txt += f"{mst} | <b>💰 Золото:</b> {money:,} / {monet:,}\n"
        txt += f"{est} | <b>🧩 Опыт:</b> {exps:,} / {exp:,}\n"
        txt += f"{cst} | <b>💎 Коины:</b> {coins:,} / {coin:,}\n"
        txt += f"{crst} | <b>🃏 Карта редкости:</b> {cards} / {card}\n"
        
    elif redk in [3, 4, 5]:
        if isinstance(pul, str):
            pul = int(pul.replace(',', ''))
        if pyl >= pul:
            pst = "✅"
        elif pyl < pul:
            pst = "❌"
        txt += f"{pst} | <b>✨ Магическая пыль:</b> {pyl:,} / {pul:,}\n"
        txt += f"{mst} | <b>💰 Золото:</b> {money:,} / {monet:,}\n"
        txt += f"{est} | <b>🧩 Опыт:</b> {exps:,} / {exp:,}\n"
        txt += f"{cst} | <b>💎 Коины:</b> {coins:,} / {coin:,}\n"
        txt += f"{crst} | <b>🃏 Карта редкости:</b> {cards} / {card}\n"
        
    elif redk in [6, 7]:
        if isinstance(pul, str):
            pul = int(pul.replace(',', ''))
        if isinstance(zvu, str):
            zvu = int(zvu.replace(',', ''))
        if pyl >= pul:
            pst = "✅"
        elif pyl < pul:
            pst = "❌"
        if zv >= zvu:
            zst = "✅"
        elif zv < zvu:
            zst = "❌"
        txt += f"{zst} | <b>🌌 Звездный осколок:</b> {zv:,} / {zvu:,}\n"
        txt += f"{pst} | <b>✨ Магическая пыль:</b> {pyl:,} / {pul:,}\n"
        txt += f"{mst} | <b>💰 Золото:</b> {money:,} / {monet:,}\n"
        txt += f"{est} | <b>🧩 Опыт:</b> {exps:,} / {exp:,}\n"
        txt += f"{cst} | <b>💎 Коины:</b> {coins:,} / {coin:,}\n"
        txt += f"{crst} | <b>🃏 Карта редкости:</b> {cards} / {card}\n"
    return txt
    
        

def upgrade_prd(id, redk, user_id):
    #1
    if id == 1:
        if redk == 1:
            chance = "0.25"
        elif redk == 2:
            chance = "0.5"
        elif redk == 3:
            chance = "0.75"
        elif redk == 4:
            chance = "1.0"
        elif redk == 5:
            chance = "1.5"
        elif redk == 6:
            chance = "2.0"
        elif redk == 7:
            chance = "3.0"
        elif redk == 8:
            chance = "5.0"
        reu = redk + 1
        if reu == 1:
            ch = "0.25"
        elif reu == 2:
            ch = "0.5"
        elif reu == 3:
            ch = "0.75"
        elif reu == 4:
            ch = "1.0"
        elif reu == 5:
            ch = "1.5"
        elif reu == 6:
            ch = "2.0"
        elif reu == 7:
            ch = "3.0"
        elif reu == 8:
            ch = "5.0"
        txt = ""  
        txt += "<b>✨ Улучшение предмета</b>\n<code>···············</code>\n"
        txt += f"<b>{get_prd(id)}</b>\n"
        txt += "<code>···············</code>\n"
        txt += "Текущий уровень:\n"
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {chance}%\n"
        txt += "<code>···············</code>\n"
        if redk >= 8:
            txt += "<b>💥 Максимальный уровень!</b>"
            return txt
        txt += "После улучшения:\n"
        redk += 1
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {ch}%\n"
        txt += "<code>···············</code>\n"
        redk -= 1
        txt += f"{get_summ(redk, user_id)}"
        return txt
        
    #2
    elif id == 2:
        if redk == 1:
            chance = "2.5"
        elif redk == 2:
            chance = "5.0"
        elif redk == 3:
            chance = "7.5"
        elif redk == 4:
            chance = "10.0"
        elif redk == 5:
            chance = "12.5"
        elif redk == 6:
            chance = "15.0"
        elif redk == 7:
            chance = "20.0"
        elif redk == 8:
            chance = "35.0"
        reu = redk + 1
        if reu == 1:
            ch = "2.5"
        elif reu == 2:
            ch = "5.0"
        elif reu == 3:
            ch = "7.5"
        elif reu == 4:
            ch = "10.0"
        elif reu == 5:
            ch = "12.5"
        elif reu == 6:
            ch = "15.0"
        elif reu == 7:
            ch = "20.0"
        elif reu == 8:
            ch = "35.0"   
        txt = ""  
        txt += "<b>✨ Улучшение предмета</b>\n<code>···············</code>\n"
        txt += f"<b>{get_prd(id)}</b>\n"
        txt += "<code>···············</code>\n"
        txt += "Текущий уровень:\n"
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {chance}%\n"
        txt += "<code>···············</code>\n"
        if redk >= 8:
            txt += "<b>💥 Максимальный уровень!</b>"
            return txt
        txt += "После улучшения:\n"
        redk += 1
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {ch}%\n"
        txt += "<code>···············</code>\n"
        redk -= 1
        txt += f"{get_summ(redk, user_id)}"
        return txt
    
    
    #3
    elif id == 3:
        if redk == 1:
            chance = "2.5"
            x = "1.5"
        elif redk == 2:
            chance = "5.0"
            x = "2.0"
        elif redk == 3:
            x = "3.0"
            chance = "7.5"
        elif redk == 4:
            x = "3.0"
            chance = "10.0"
        elif redk == 5:
            x = "3.0"
            chance = "12.5"
        elif redk == 6:
            x = "3.0"
            chance = "15.0"
        elif redk == 7:
            x = "4.0"
            chance = "30.0"
        elif redk == 8:
            x = "5.0"
            chance = "40.0"
            
        reu = redk + 1
        if reu == 1:
            ch = "2.5"
            xe = "1.5"
        elif reu == 2:
            ch = "5.0"
            xe = "2.0"
        elif reu == 3:
            xe = "3.0"
            ch = "7.5"
        elif reu == 4:
            xe = "3.0"
            ch = "10.0"
        elif reu == 5:
            xe = "3.0"
            ch = "12.5"
        elif reu == 6:
            xe = "3.0"
            ch = "15.0"
        elif reu == 7:
            xe = "4.0"
            ch = "30.0"
        elif reu == 8:
            xe = "5.0"
            ch = "40.0"
        txt = ""  
        txt += "<b>✨ Улучшение предмета</b>\n<code>···············</code>\n"
        txt += f"<b>{get_prd(id)}</b>\n"
        txt += "<code>···············</code>\n"
        txt += "Текущий уровень:\n"
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {chance}%\n🔥<b> Множитель:</b> {x}×\n"
        txt += "<code>···············</code>\n"
        if redk >= 8:
            txt += "<b>💥 Максимальный уровень!</b>"
            return txt
        txt += "После улучшения:\n"
        redk += 1
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {ch}%\n🔥<b> Множитель:</b> {xe}×\n"
        txt += "<code>···············</code>\n"
        redk -= 1
        txt += f"{get_summ(redk, user_id)}"
        
        return txt
   
    elif id == 4:
        if redk == 1:
            chance = "2.5"
            x = "1.1"
            max = "💰 Золото"
        elif redk == 2:
            chance = "3.0"
            x = "1.3"
            max = "💰 Золото"
        elif redk == 3:
            x = "1.6"
            chance = "5.0"
            max = "🧩 Опыт"
        elif redk == 4:
            x = "2.0"
            chance = "7.5"
            max = "🧩 Опыт"
        elif redk == 5:
            max = "💎 Коины"
            x = "2.5"
            chance = "10.0"
        elif redk == 6:
            max = "💎 Коины"
            x = "3.5"
            chance = "15.0"
        elif redk == 7:
            max = "🏆 MMR"
            x = "5.5"
            chance = "30.0"
        elif redk == 8:
            max = "🏆 MMR"
            x = "9.5"
            chance = "60.0"
        
        reu = redk + 1    
        if reu == 1:
            ch = "2.5"
            xe = "1.1"
            maxe = "💰 Золото"
        elif reu == 2:
            ch = "3.0"
            xe = "1.3"
            maxe = "💰 Золото"
        elif reu == 3:
            xe = "1.6"
            ch = "5.0"
            maxe = "🧩 Опыт"
        elif reu == 4:
            xe = "2.0"
            ch = "7.5"
            maxe = "🧩 Опыт"
        elif reu == 5:
            maxe = "💎 Коины"
            xe = "2.5"
            ch = "10.0"
        elif reu == 6:
            maxe = "💎 Коины"
            xe = "3.5"
            ch = "15.0"
        elif reu == 7:
            maxe = "🏆 MMR"
            xe = "5.5"
            ch = "30.0"
        elif reu == 8:
            maxe = "🏆 MMR"
            xe = "9.5"
            ch = "60.0"
            
        txt = ""  
        txt += "<b>✨ Улучшение предмета</b>\n<code>···············</code>\n"
        txt += f"<b>{get_prd(id)}</b>\n"
        txt += "<code>···············</code>\n"
        txt += "Текущий уровень:\n"
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {chance}%\n🔥<b> Множитель:</b> {x}×\n🪄 <b>Максимум:</b> {max}\n"
        txt += "<code>···············</code>\n"
        if redk >= 8:
            txt += "<b>💥 Максимальный уровень!</b>"
            return txt
        txt += "После улучшения:\n"
        redk += 1
        txt += f"<b>✨ Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n🍀 <b>Шанс:</b> {ch}%\n🔥<b> Множитель:</b> {xe}×\n🪄 <b>Максимум:</b> {maxe}\n"
        txt += "<code>···············</code>\n"
        redk -= 1
        txt += f"{get_summ(redk, user_id)}"
        
        return txt
    

def get_stats(redk, id, user_id, count):
    if id == 1:
        if redk == 1:
            chance = "0.25"
        elif redk == 2:
            chance = "0.5"
        elif redk == 3:
            chance = "0.75"
        elif redk == 4:
            chance = "1.0"
        elif redk == 5:
            chance = "1.5"
        elif redk == 6:
            chance = "2.0"
        elif redk == 7:
            chance = "3.0"
        elif redk == 8:
            chance = "5.0"
            
        txt = f"<b>{get_prd(id)}</b>\n<code>···············</code>\n✨ <b>Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n···············\n<b>🍀 Шанс:</b> {chance}%\n<code>···············</code>\n{get_desc(id)}"
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND redk={redk} AND type={id} AND count={count}')
        g = c.fetchone()
        if g:
            use = g[3]
            if use > 0:
                txt += f"\n<code>···············</code>\n🖐 Установлен в слот <b>{use}</b>"
        return txt
    elif id == 2:
        if redk == 1:
            chance = "2.5"
        elif redk == 2:
            chance = "5.0"
        elif redk == 3:
            chance = "7.5"
        elif redk == 4:
            chance = "10.0"
        elif redk == 5:
            chance = "12.5"
        elif redk == 6:
            chance = "15.0"
        elif redk == 7:
            chance = "20.0"
        elif redk == 8:
            chance = "35.0"
            
        txt = f"<b>{get_prd(id)}</b>\n<code>···············</code>\n✨ <b>Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n···············\n<b>🍀 Шанс:</b> {chance}%\n<code>···············</code>\n{get_desc(id)}"
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND redk={redk} AND type={id} AND count={count}')
        g = c.fetchone()
        if g:
            use = g[3]
            if use > 0:
                txt += f"\n<code>···············</code>\n🖐 Установлен в слот <b>{use}</b>"
        return txt
    elif id == 3:
        if redk == 1:
            chance = "2.5"
            x = "1.5"
        elif redk == 2:
            chance = "5.0"
            x = "2.0"
        elif redk == 3:
            x = "3.0"
            chance = "7.5"
        elif redk == 4:
            x = "3.0"
            chance = "10.0"
        elif redk == 5:
            x = "3.0"
            chance = "12.5"
        elif redk == 6:
            x = "3.0"
            chance = "15.0"
        elif redk == 7:
            x = "4.0"
            chance = "30.0"
        elif redk == 8:
            x = "5.0"
            chance = "40.0"
            
        txt = f"<b>{get_prd(id)}</b>\n<code>···············</code>\n✨ <b>Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n···············\n<b>🍀 Шанс:</b> {chance}%\n🔥 <b>Множитель</b>: {x}×\n<code>···············</code>\n{get_desc(id)}"
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND redk={redk} AND type={id} AND count={count}')
        g = c.fetchone()
        if g:
            use = g[3]
            if use > 0:
                txt += f"\n<code>···············</code>\n🖐 Установлен в слот <b>{use}</b>"
        return txt
    elif id == 4:
        if redk == 1:
            chance = "2.5"
            x = "1.1"
            max = "💰 Золото"
        elif redk == 2:
            chance = "3.0"
            x = "1.3"
            max = "💰 Золото"
        elif redk == 3:
            x = "1.6"
            chance = "5.0"
            max = "🧩 Опыт"
        elif redk == 4:
            x = "2.0"
            chance = "7.5"
            max = "🧩 Опыт"
        elif redk == 5:
            max = "💎 Коины"
            x = "2.5"
            chance = "10.0"
        elif redk == 6:
            max = "💎 Коины"
            x = "3.5"
            chance = "15.0"
        elif redk == 7:
            max = "🏆 MMR"
            x = "5.5"
            chance = "30.0"
        elif redk == 8:
            max = "🏆 MMR"
            x = "9.5"
            chance = "60.0"
        
         
        txt = f"<b>{get_prd(id)}</b>\n<code>···············</code>\n✨ <b>Уровень:</b> {redk}\n{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n···············\n<b>🍀 Шанс:</b> {chance}%\n🔥 <b>Множитель</b>: {x}×\n🪄 <b>Максимум</b>: {max}\n<code>···············</code>\n{get_desc(id)}"
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND redk={redk} AND type={id} AND count={count}')
        g = c.fetchone()
        if g:
            use = g[3]
            if use > 0:
                txt += f"\n<code>···············</code>\n🖐 Установлен в слот <b>{use}</b>"
        return txt

@dp.callback_query_handler(lambda call: call.data.startswith('prdytil_'))
async def sell_prd(call):
    user_id = call.from_user.id
    type, count, redk, page, id= map(int, call.data.split('_')[1:])
    
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return

    rewards = {
        1: (100_000, 1_500, 5),
        2: (300_000, 3_000, 15),
        3: (900_000, 10_000, 15),
        4: (2_700_000, 30_000, 35),
        5: (8_100_000, 90_000, 85, 1, 0),
        6: (24_300_000, 270_000, 200, 2, 0),
        7: (72_900_000, 810_000, 350, 4, 0),
        8: (218_700_000, 2_430_000, 700, 8, 1)
    }

    reward_data = rewards.get(redk, None)
    if reward_data is None:
        await call.answer('Ошибка: невозможно определить награду за этот предмет.')
        return

    card = 1
    
    txt = "<b>♻ Предмет утилизирован!</b>\n"
    txt += "<code>···············</code>\n"
    txt += f"<b>{get_prd(type)}</b>\n"
    txt += f"{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n"
    txt += "<code>···············</code>\n"
    txt += "<b>Получено:</b>\n"
    if len(reward_data) > 4 and reward_data[4] > 0:
        txt += f"🌌 <b>Звездный осколок:</b> {'{:,}'.format(int(reward_data[4]))}\n"
    if len(reward_data) > 3 and reward_data[3] > 0:
        txt += f"✨ <b>Магическая пыль:</b> {'{:,}'.format(int(reward_data[3]))}\n"
    txt += f"💰 <b>Золото:</b> {'{:,}'.format(int(reward_data[0]))}\n"
    txt += f"🧩 <b>Опыт:</b> {'{:,}'.format(int(reward_data[1]))}\n"
    txt += f"💎 <b>Коины:</b> {'{:,}'.format(int(reward_data[2]))}\n"
    txt += f"🃏 <b>Карта редкости:</b> {card}\n"

    if redk in [1, 2, 3, 4]:
        c.execute(f'UPDATE users SET money=money+{int(reward_data[0])}, exp=exp+{int(reward_data[1])}, coin=coin+{int(reward_data[2])}, cards=cards+{card} WHERE user_id={user_id}')
    elif redk in [5, 6, 7]:
        c.execute(f'UPDATE users SET money=money+{int(reward_data[0])}, exp=exp+{int(reward_data[1])}, coin=coin+{int(reward_data[2])}, cards=cards+{card}, magp=magp+{int(reward_data[3])} WHERE user_id={user_id}')
    elif redk == 8:
        c.execute(f'UPDATE users SET money=money+{int(reward_data[0])}, exp=exp+{int(reward_data[1])}, coin=coin+{int(reward_data[2])}, cards=cards+{card}, magp=magp+{int(reward_data[3])}, zvo=zvo+{int(reward_data[4])} WHERE user_id={user_id}')
    c.execute(f'DELETE FROM prd WHERE user_id={user_id} AND type={type} AND redk={redk} AND count={count}')
    base.commit()
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdcancel_1_{user_id}")
    markup.add(b1)
    await call.message.edit_text(txt, reply_markup=markup)

@dp.callback_query_handler(lambda call: call.data.startswith('sellprd_'))
async def sell_prd(call):
    user_id = call.from_user.id
    type, count, redk, page, id = map(int, call.data.split('_')[1:])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return

    rewards = {
        1: (100_000, 1_500, 5),
        2: (300_000, 3_000, 15),
        3: (900_000, 10_000, 15),
        4: (2_700_000, 30_000, 35),
        5: (8_100_000, 90_000, 85, 1),
        6: (24_300_000, 270_000, 200, 2),
        7: (72_900_000, 810_000, 350, 4),
        8: (218_700_000, 2_430_000, 700, 8, 1)
    }

    reward_data = rewards.get(redk, None)
    if reward_data is None:
        await call.answer('Ошибка: невозможно определить награду за этот предмет.')
        return

    card = 1
    
    txt = "<b>♻ Утилизация предмета</b>\n"
    txt += "<code>···············</code>\n"
    txt += f"<b>{get_prd(type)}</b>\n"
    txt += f"{get_redk(redk)} <b>Редкость:</b> {get_st(redk)}\n"
    txt += "<code>···············</code>\n"
    txt += "<b>Получишь:</b>\n"
    if len(reward_data) > 4:
        txt += f"🌌 <b>Звездный осколок:</b> {'{:,}'.format(int(reward_data[4]))}\n"
        
    if len(reward_data) > 3:
        txt += f"✨ <b>Магическая пыль:</b> {'{:,}'.format(int(reward_data[3]))}\n"
    txt += f"💰 <b>Золото:</b> {'{:,}'.format(int(reward_data[0]))}\n"
    txt += f"🧩 <b>Опыт:</b> {'{:,}'.format(int(reward_data[1]))}\n"
    txt += f"💎 <b>Коины:</b> {'{:,}'.format(int(reward_data[2]))}\n"
    
    

    txt += f"🃏 <b>Карта редкости:</b> {card}\n"
    txt += "<code>···············</code>\n"
    txt += "Утилизируй предмет и\nполучи часть ресурсов\nобратно!"

    markup = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text="♻️ Утилизировать", callback_data=f"prdytil_{type}_{count}_{redk}_{page}_{user_id}")
    b2 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}")
    markup.add(b1, b2)

    await call.message.edit_text(txt, reply_markup=markup)
            

@dp.callback_query_handler(lambda call: call.data.startswith('prd_'))
async def choose_prd(call):
    user_id = call.from_user.id
    type = int(call.data.split('_')[1])
    count = int(call.data.split('_')[2])
    redk = int(call.data.split('_')[3])
    page = int(call.data.split('_')[4])
    id = int(call.data.split('_')[5])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    if user_id in players:
        await call.answer('Во время игры нельзя выбрать предмет ❕')
        return
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    text = get_stats(redk, type, user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    b1 = InlineKeyboardButton(text="🖐", callback_data=f"setslot_{type}_{count}_{redk}_{page}_{user_id}")
    b2 = InlineKeyboardButton(text="✨", callback_data=f"upgrade_{type}_{count}_{redk}_{page}_{user_id}")
    b3 = InlineKeyboardButton(text="♻️", callback_data=f"sellprd_{type}_{count}_{redk}_{page}_{user_id}")
    b5 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdcancel_{page}_{user_id}")
    markup.add(b1,b2,b3)
    markup.add(b5)
    await call.message.edit_text(text, reply_markup=markup)
#
@dp.callback_query_handler(lambda call: call.data.startswith('setslot_'))
async def slots(call):
    user_id = call.from_user.id
    type = int(call.data.split('_')[1])
    count = int(call.data.split('_')[2])
    redk = int(call.data.split('_')[3])
    page = int(call.data.split('_')[4])
    id = int(call.data.split('_')[5])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    g1 = 1
    g2 = 2
    g3 = 3
    g4 = 4
    g5 = 5
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    markup = InlineKeyboardMarkup(row_width=5)
    #1
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g1}')
    slot1 = c.fetchone()
    if slot1:
        b1 = InlineKeyboardButton(text=f"{get_prds(slot1[1])}{get_redk(slot1[2])}", callback_data=f"slotaked_1_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b1 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_1_{type}_{count}_{redk}_{page}_{user_id}")
    if user[22] >= 2:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g2}')
        slot2 = c.fetchone()
        if slot2:
            b2 = InlineKeyboardButton(text=f"{get_prds(slot2[1])}{get_redk(slot2[2])}", callback_data=f"slotaked_2_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b2 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_2_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b2 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_2_{page}_{user_id}")
     #3
    if user[22] >= 3:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g3}')
        slot3 = c.fetchone()
        if slot3:
            b3 = InlineKeyboardButton(text=f"{get_prds(slot3[1])}{get_redk(slot3[2])}", callback_data=f"slotaked_3_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b3 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_3_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b3 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_3_{page}_{user_id}")
    #4
    if user[22] >= 4:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g4}')
        slot4 = c.fetchone()
        if slot4:
            b4 = InlineKeyboardButton(text=f"{get_prds(slot4[1])}{get_redk(slot4[2])}", callback_data=f"slotaked_4_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b4 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_4_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b4 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_4_{page}_{user_id}")
    #5
    if user[22] >= 5:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g5}')
        slot5 = c.fetchone()
        if slot5:
            b5 = InlineKeyboardButton(text=f"{get_prds(slot5[1])}{get_redk(slot5[2])}", callback_data=f"slotaked_5_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b5 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_5_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b5 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_5_{page}_{user_id}")
    
    markup.add(b1, b2, b3, b4, b5)
    markup.add(InlineKeyboardButton(text="Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}"))
    await call.message.edit_text(f"<b>Выбери слот, в который\nхочешь поместить предмет:</b>", reply_markup=markup)

#
@dp.callback_query_handler(lambda call: call.data.startswith('slotaked_'))
async def slots(call):
    user_id = call.from_user.id
    slot = int(call.data.split('_')[1])
    type = int(call.data.split('_')[2])
    count = int(call.data.split('_')[3])
    redk = int(call.data.split('_')[4])
    page = int(call.data.split('_')[5])
    id = int(call.data.split('_')[6])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND type={type} AND count!={count} AND use!={0} AND use!={slot}')
    existing_items = c.fetchall()

    if existing_items:
        await call.answer('😥 Нельзя устанавливать два одинаковых предмета!')
        return
    g1 = 1
    g2 = 2
    g3 = 3
    g4 = 4
    g5 = 5
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={slot}')
    hh = c.fetchone()
    if hh:
        c.execute(f'UPDATE prd SET use={"0"} WHERE user_id={user_id} AND use={slot}')
    c.execute(f'UPDATE prd SET use={slot} WHERE user_id={user_id} AND type={type} AND count={count} AND redk={redk}')
    base.commit()
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    markup = InlineKeyboardMarkup(row_width=5)
    #1
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g1}')
    slot1 = c.fetchone()
    if slot1:
        b1 = InlineKeyboardButton(text=f"{get_prds(slot1[1])}{get_redk(slot1[2])}", callback_data=f"slotaked_1_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b1 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_1_{type}_{count}_{redk}_{page}_{user_id}")
    if user[22] >= 2:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g2}')
        slot2 = c.fetchone()
        if slot2:
            b2 = InlineKeyboardButton(text=f"{get_prds(slot2[1])}{get_redk(slot2[2])}", callback_data=f"slotaked_2_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b2 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_2_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b2 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_2_{page}_{user_id}")
     #3
    if user[22] >= 3:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g3}')
        slot3 = c.fetchone()
        if slot3:
            b3 = InlineKeyboardButton(text=f"{get_prds(slot3[1])}{get_redk(slot3[2])}", callback_data=f"slotaked_3_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b3 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_3_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b3 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_3_{page}_{user_id}")
    #4
    if user[22] >= 4:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g4}')
        slot4 = c.fetchone()
        if slot4:
            b4 = InlineKeyboardButton(text=f"{get_prds(slot4[1])}{get_redk(slot4[2])}", callback_data=f"slotaked_4_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b4 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_4_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b4 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_4_{page}_{user_id}")
    #5
    if user[22] >= 5:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g5}')
        slot5 = c.fetchone()
        if slot5:
            b5 = InlineKeyboardButton(text=f"{get_prds(slot5[1])}{get_redk(slot5[2])}", callback_data=f"slotaked_5_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b5 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_5_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b5 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_5_{page}_{user_id}")
    
    markup.add(b1, b2, b3, b4, b5)
    markup.add(InlineKeyboardButton(text="Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}"))
    await call.answer(f"{get_redk(redk)} {get_prd(type)} установлен в {slot} слот.")
    await call.message.edit_text(f"<b>Выбери слот, в который\nхочешь поместить предмет:</b>", reply_markup=markup)
#
@dp.callback_query_handler(lambda call: call.data.startswith('slotempty_'))
async def slots(call):
    user_id = call.from_user.id
    slot = int(call.data.split('_')[1])
    type = int(call.data.split('_')[2])
    count = int(call.data.split('_')[3])
    redk = int(call.data.split('_')[4])
    page = int(call.data.split('_')[5])
    id = int(call.data.split('_')[6])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND type={type} AND count!={count} AND use!={0} AND use!={slot}')
    existing_items = c.fetchall()

    if existing_items:
        await call.answer('😥 Нельзя устанавливать два одинаковых предмета!')
        return
    g1 = 1
    g2 = 2
    g3 = 3
    g4 = 4
    g5 = 5
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={slot}')
    hh = c.fetchone()
    if hh:
        c.execute(f'UPDATE prd SET use={"0"} WHERE user_id={user_id} AND use={slot}')
    c.execute(f'UPDATE prd SET use={slot} WHERE user_id={user_id} AND type={type} AND count={count} AND redk={redk}')
    base.commit()
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    markup = InlineKeyboardMarkup(row_width=5)
    #1
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g1}')
    slot1 = c.fetchone()
    if slot1:
        b1 = InlineKeyboardButton(text=f"{get_prds(slot1[1])}{get_redk(slot1[2])}", callback_data=f"slotaked_1_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b1 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_1_{type}_{count}_{redk}_{page}_{user_id}")
    if user[22] >= 2:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g2}')
        slot2 = c.fetchone()
        if slot2:
            b2 = InlineKeyboardButton(text=f"{get_prds(slot2[1])}{get_redk(slot2[2])}", callback_data=f"slotaked_2_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b2 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_2_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b2 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_2_{page}_{user_id}")
     #3
    if user[22] >= 3:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g3}')
        slot3 = c.fetchone()
        if slot3:
            b3 = InlineKeyboardButton(text=f"{get_prds(slot3[1])}{get_redk(slot3[2])}", callback_data=f"slotaked_3_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b3 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_3_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b3 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_3_{page}_{user_id}")
    #4
    if user[22] >= 4:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g4}')
        slot4 = c.fetchone()
        if slot4:
            b4 = InlineKeyboardButton(text=f"{get_prds(slot4[1])}{get_redk(slot4[2])}", callback_data=f"slotaked_4_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b4 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_4_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b4 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_4_{page}_{user_id}")
    #5
    if user[22] >= 5:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g5}')
        slot5 = c.fetchone()
        if slot5:
            b5 = InlineKeyboardButton(text=f"{get_prds(slot5[1])}{get_redk(slot5[2])}", callback_data=f"slotaked_5_{type}_{count}_{redk}_{page}_{user_id}")
        else:
            b5 = InlineKeyboardButton(text=" ", callback_data=f"slotempty_5_{type}_{count}_{redk}_{page}_{user_id}")
    else:
        b5 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_5_{page}_{user_id}")
    
    markup.add(b1, b2, b3, b4, b5)
    markup.add(InlineKeyboardButton(text="Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}"))
    await call.answer(f"{get_redk(redk)} {get_prd(type)} установлен в {slot} слот.")
    await call.message.edit_text(f"<b>Выбери слот, в который\nхочешь поместить предмет:</b>", reply_markup=markup)
#
@dp.callback_query_handler(lambda call: call.data.startswith('slots_'))
async def slots(call):
    user_id = call.from_user.id
    page = int(call.data.split('_')[1])
    id = int(call.data.split('_')[2])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    g1 = 1
    g2 = 2
    g3 = 3
    g4 = 4
    g5 = 5
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    markup = InlineKeyboardMarkup(row_width=5)
    #1
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g1}')
    slot1 = c.fetchone()
    if slot1:
        b1 = InlineKeyboardButton(text=f"{get_prds(slot1[1])}{get_redk(slot1[2])}", callback_data=f"slotclear_1_{page}_{user_id}")
    else:
        b1 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_1_{page}_{user_id}")
    if user[22] >= 2:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g2}')
        slot2 = c.fetchone()
        if slot2:
            b2 = InlineKeyboardButton(text=f"{get_prds(slot2[1])}{get_redk(slot2[2])}", callback_data=f"slotclear_2_{page}_{user_id}")
        else:
            b2 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_2_{page}_{user_id}")
    else:
        b2 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_2_{page}_{user_id}")
     #3
    if user[22] >= 3:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g3}')
        slot3 = c.fetchone()
        if slot3:
            b3 = InlineKeyboardButton(text=f"{get_prds(slot3[1])}{get_redk(slot3[2])}", callback_data=f"slotclear_3_{page}_{user_id}")
        else:
            b3 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_3_{page}_{user_id}")
    else:
        b3 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_3_{page}_{user_id}")
    #4
    if user[22] >= 4:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g4}')
        slot4 = c.fetchone()
        if slot4:
            b4 = InlineKeyboardButton(text=f"{get_prds(slot4[1])}{get_redk(slot4[2])}", callback_data=f"slotclear_4_{page}_{user_id}")
        else:
            b4 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_4_{page}_{user_id}")
    else:
        b4 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_4_{page}_{user_id}")
    #5
    if user[22] >= 5:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g5}')
        slot5 = c.fetchone()
        if slot5:
            b5 = InlineKeyboardButton(text=f"{get_prds(slot5[1])}{get_redk(slot5[2])}", callback_data=f"slotclear_5_{page}_{user_id}")
        else:
            b5 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_5_{page}_{user_id}")
    else:
        b5 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_5_{page}_{user_id}")
    
    markup.add(b1, b2, b3, b4, b5)
    markup.add(InlineKeyboardButton(text="Назад", callback_data=f"prdcancel_{page}_{user_id}"))
    await call.message.edit_text(f"<b>Это твои активные\nпредметы.</b>\n<code>···············</code>\nКликни на предмет,\nчтобы очистить слот.", reply_markup=markup)
    
@dp.callback_query_handler(lambda call: call.data.startswith('slotclear_'))
async def clesrslot(call):
    user_id = call.from_user.id
    slot = int(call.data.split('_')[1])
    page = int(call.data.split('_')[2])
    id = int(call.data.split('_')[3])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    g1 = 1
    g2 = 2
    g3 = 3
    g4 = 4
    g5 = 5
    j = c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={slot}').fetchone()
    if not j:
        await call.answer("🫤 Нечего освобождать, слот и так пустой!")
        return
    if j:
        c.execute(f'UPDATE prd SET use={"0"} WHERE user_id={user_id} AND use={slot}')
        base.commit()
     
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    markup = InlineKeyboardMarkup(row_width=5)
    #1
    c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g1}')
    slot1 = c.fetchone()
    if slot1:
        b1 = InlineKeyboardButton(text=f"{get_prds(slot1[1])}{get_redk(slot1[2])}", callback_data=f"slotclear_1_{page}_{user_id}")
    else:
        b1 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_1_{page}_{user_id}")
    if user[22] >= 2:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g2}')
        slot2 = c.fetchone()
        if slot2:
            b2 = InlineKeyboardButton(text=f"{get_prds(slot2[1])}{get_redk(slot2[2])}", callback_data=f"slotclear_2_{page}_{user_id}")
        else:
            b2 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_2_{page}_{user_id}")
    else:
        b2 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_2_{page}_{user_id}")
     #3
    if user[22] >= 3:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g3}')
        slot3 = c.fetchone()
        if slot3:
            b3 = InlineKeyboardButton(text=f"{get_prds(slot3[1])}{get_redk(slot3[2])}", callback_data=f"slotclear_3_{page}_{user_id}")
        else:
            b3 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_3_{page}_{user_id}")
    else:
        b3 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_3_{page}_{user_id}")
    #4
    if user[22] >= 4:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g4}')
        slot4 = c.fetchone()
        if slot4:
            b4 = InlineKeyboardButton(text=f"{get_prds(slot4[1])}{get_redk(slot4[2])}", callback_data=f"slotclear_4_{page}_{user_id}")
        else:
            b4 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_4_{page}_{user_id}")
    else:
        b4 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_4_{page}_{user_id}")
    #5
    if user[22] >= 5:
        c.execute(f'SELECT * FROM prd WHERE user_id={user_id} AND use={g5}')
        slot5 = c.fetchone()
        if slot5:
            b5 = InlineKeyboardButton(text=f"{get_prds(slot5[1])}{get_redk(slot5[2])}", callback_data=f"slotclear_5_{page}_{user_id}")
        else:
            b5 = InlineKeyboardButton(text=" ", callback_data=f"slotclear_5_{page}_{user_id}")
    else:
        b5 = InlineKeyboardButton(text="🔒", callback_data=f"slotblocked_5_{page}_{user_id}")
    
    markup.add(b1, b2, b3, b4, b5)
    markup.add(InlineKeyboardButton(text="Назад", callback_data=f"prdcancel_{page}_{user_id}"))
    await call.answer('😊 Слот освобождён!')
    await call.message.edit_text(f"<b>Это твои активные\nпредметы.</b>\n<code>···············</code>\nКликни на предмет,\nчтобы очистить слот.", reply_markup=markup)
    
@dp.callback_query_handler(lambda call: call.data.startswith('slotblocked_'))
async def clesrslot(call):
    user_id = call.from_user.id
    id = int(call.data.split('_')[3])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    slot = int(call.data.split('_')[1])
    if slot >= 2:
        await call.answer("🔒 Слот недоступен.\nПриобрести можно в магазине.", show_alert=True)

@dp.callback_query_handler(lambda call: call.data.startswith('upgrade_'))
async def chooe_prd(call):
    user_id = call.from_user.id
    type = int(call.data.split('_')[1])
    count = int(call.data.split('_')[2])
    redk = int(call.data.split('_')[3]) 
    page = int(call.data.split('_')[4]) 
    id = int(call.data.split('_')[5])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    if user_id in players:
        await query.answer('Во время игры нельзя улучшить предмет ❕')
        return
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    text = upgrade_prd(type, redk, user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    b2 = InlineKeyboardButton(text="✨ Улучшить", callback_data=f"prdupgrade_{type}_{count}_{redk}_{page}_{user_id}")
    b1 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}")
    if redk != 8:
        markup.add(b2)
    markup.add(b1)
    await call.message.edit_text(text, reply_markup=markup)

@dp.callback_query_handler(lambda call: call.data.startswith('prdexit_'))
async def prd_upgr(call):
    user_id = call.from_user.id
    type = int(call.data.split('_')[1])
    count = int(call.data.split('_')[2])
    redk = int(call.data.split('_')[3]) 
    page = int(call.data.split('_')[4])
    id = int(call.data.split('_')[5])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    
    text = get_stats(redk, type, user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    b1 = InlineKeyboardButton(text="🖐", callback_data=f"setslot_{type}_{count}_{redk}_{page}_{user_id}")
    b2 = InlineKeyboardButton(text="✨", callback_data=f"upgrade_{type}_{count}_{redk}_{page}_{user_id}")
    b3 = InlineKeyboardButton(text="♻️", callback_data=f"sellprd_{type}_{count}_{redk}_{page}_{user_id}")
    b5 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdcancel_{page}_{user_id}")
    markup.add(b1,b2,b3)
    markup.add(b5)
    await call.message.edit_text(text, reply_markup=markup)



@dp.callback_query_handler(lambda call: call.data.startswith('prdupgrade_'))
async def prd_upgr(call):
    user_id = call.from_user.id
    type = int(call.data.split('_')[1])
    count = int(call.data.split('_')[2])
    redk = int(call.data.split('_')[3]) 
    page = int(call.data.split('_')[4]) 
    id = int(call.data.split('_')[5])
    if user_id != id:
        await call.answer('❗ Это не твоя кнопка!')
        return
    if user_id in players:
        await query.answer('Во время игры нельзя улучшить предмет ❕')
        return
    c.execute(f'SELECT * FROM prd WHERE count={count} AND type={type} AND redk={redk} AND user_id={user_id}')
    prd = c.fetchone()
    if not prd:
        await call.answer('😥 У тебя нет этого предмета!')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    money = int('{:,}'.format(user[1]).replace(',', ''))
    exps = int('{:,}'.format(user[4]).replace(',', ''))
    zv = int('{:,}'.format(user[19]).replace(',', ''))
    pyl = int('{:,}'.format(user[20]).replace(',', ''))
    cards = int('{:,}'.format(user[21]).replace(',', ''))
    coins = int('{:,}'.format(user[15]).replace(',', ''))
    if redk == 1:
        monet = int('{:,}'.format(900000).replace(',', ''))
        exp = int('{:,}'.format(10000).replace(',', ''))
        coin = int('{:,}'.format(25).replace(',', ''))
        card = 1
    elif redk == 2:
        monet = int('{:,}'.format(2700000).replace(',', ''))
        exp = int('{:,}'.format(30000).replace(',', ''))
        coin = int('{:,}'.format(50).replace(',', ''))
        card = 1
    elif redk == 3:
        monet = int('{:,}'.format(8100000).replace(',', ''))
        exp = int('{:,}'.format(90000).replace(',', ''))
        coin = int('{:,}'.format(100).replace(',', ''))
        card = 1
        pul = 1
    elif redk == 4:
        monet = int('{:,}'.format(24300000).replace(',', ''))
        exp = int('{:,}'.format(270000).replace(',', ''))
        coin = int('{:,}'.format(250).replace(',', ''))
        card = 1
        pul = 2
    elif redk == 5:
        monet = int('{:,}'.format(72900000).replace(',', ''))
        exp = int('{:,}'.format(810000).replace(',', ''))
        coin = int('{:,}'.format(500).replace(',', ''))
        card = 1
        pul = 3
    elif redk == 6:
        monet = int('{:,}'.format(218700000).replace(',', ''))
        exp = int('{:,}'.format(2430000).replace(',', ''))
        coin = int('{:,}'.format(1000).replace(',', ''))
        card = 1
        pul = 6
        zvu = 1
    elif redk == 7:
        monet = int('{:,}'.format(656100000).replace(',', ''))
        exp = int('{:,}'.format(7290000).replace(',', ''))
        coin = int('{:,}'.format(2000).replace(',', ''))
        card = 1
        pul = 12
        zvu = 2
    
    if redk in [1, 2]:
        if money < monet:
            await call.answer('💰 | Недостаточно золота.')
            return
            
        elif exps < exp:
            await call.answer('🧩 | Недостаточно опыта.')
            return
      
        elif coins < coin:
            await call.answer('💎 | Недостаточно коинов.')
            return
        
        elif cards < card:
            await call.answer('🃏 | Недостаточно карты редкости.')
            return
        redk += 1
        money -= monet
        exps -= exp
        coins -= coin
        cards -= card
        c.execute(f'UPDATE prd SET redk={redk} WHERE user_id={user_id} AND count={count} AND type={type}')
        c.execute(f'UPDATE users SET money={money}, exp={exps}, coin={coins}, cards={cards} WHERE user_id={user_id}')
        base.commit()
        markup = InlineKeyboardMarkup(row_width=3)
        b2 = InlineKeyboardButton(text="✨ Улучшить", callback_data=f"prdupgrade_{type}_{count}_{redk}_{page}_{user_id}")
        b1 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}")
        markup.add(b2)
        markup.add(b1)
        text = upgrade_prd(type, redk, user_id)
        await call.message.edit_text(text, reply_markup=markup)
        
        
    elif redk in [3, 4, 5]:
        if isinstance(pul, str):
            pul = int(pul.replace(',', ''))
        if pyl < pul:
            await call.answer('✨ | Недостаточно магической пыли.')
            return
            
        elif money < monet:
            await call.answer('💰 | Недостаточно золота.')
            return
            
        elif exps < exp:
            await call.answer('🧩 | Недостаточно опыта.')
            return
      
        elif coins < coin:
            await call.answer('💎 | Недостаточно коинов.')
            return
        
        elif cards < card:
            await call.answer('🃏 | Недостаточно карты редкости.')
            return
        redk += 1
        money -= monet
        exps -= exp
        coins -= coin
        cards -= card
        pyl -= pul
        c.execute(f'UPDATE prd SET redk={redk} WHERE user_id={user_id} AND count={count} AND type={type}')
        c.execute(f'UPDATE users SET money={money}, exp={exps}, coin={coins}, cards={cards}, magp={pyl} WHERE user_id={user_id}')
        base.commit()
        markup = InlineKeyboardMarkup(row_width=3)
        b2 = InlineKeyboardButton(text="✨ Улучшить", callback_data=f"prdupgrade_{type}_{count}_{redk}_{page}_{user_id}")
        b1 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}")
        markup.add(b2)
        markup.add(b1)
        text = upgrade_prd(type, redk, user_id)
        await call.message.edit_text(text, reply_markup=markup)
        
    elif redk in [6, 7]:
        if isinstance(pul, str):
            pul = int(pul.replace(',', ''))
        if isinstance(zvu, str):
            zvu = int(zvu.replace(',', ''))

        if zv < zvu:
            await call.answer('🌌 | Недостаточно звездных осколков.')
            return
        
        elif pyl < pul:
            await call.answer('✨ | Недостаточно магической пыли.')
            return
            
        elif money < monet:
            await call.answer('💰 | Недостаточно золота.')
            return
            
        elif exps < exp:
            await call.answer('🧩 | Недостаточно опыта.')
            return
      
        elif coins < coin:
            await call.answer('💎 | Недостаточно коинов.')
            return
        
        elif cards < card:
            await call.answer('🃏 | Недостаточно карты редкости.')
            return
        redk += 1
        money -= monet
        exps -= exp
        coins -= coin
        cards -= card
        pyl -= pul
        zv -= zvu
        c.execute(f'UPDATE prd SET redk={redk} WHERE user_id={user_id} AND count={count} AND type={type}')
        c.execute(f'UPDATE users SET money={money}, exp={exps}, coin={coins}, cards={cards}, magp={pyl}, zvo={zv} WHERE user_id={user_id}')
        base.commit()
        markup = InlineKeyboardMarkup(row_width=3)
        b2 = InlineKeyboardButton(text="✨ Улучшить", callback_data=f"prdupgrade_{type}_{count}_{redk}_{page}_{user_id}")
        b1 = InlineKeyboardButton(text="◀️ Назад", callback_data=f"prdexit_{type}_{count}_{redk}_{page}_{user_id}")
        if redk != 8:
            markup.add(b2)
        markup.add(b1)
        text = upgrade_prd(type, redk, user_id)
        await call.message.edit_text(text, reply_markup=markup)
    

@dp.callback_query_handler(lambda call: call.data.startswith('prdcancel_'))
async def callh(call):
    pag = int(call.data.split('_')[1])
    id = int(call.data.split('_')[2])
    m = 1
    if m == 1:
        user_id = call.from_user.id
        if user_id != id:
            await call.answer('❗ Это не твоя кнопка!')
            return
        c.execute('SELECT * FROM prd WHERE user_id=?', (user_id,))
        fighters = c.fetchall()

        change_kb = InlineKeyboardMarkup()

        fighters = sorted(fighters, key=lambda x: x[2], reverse=True)
        row = []
        start = (pag - 1) * 12
        end = start + 12
        for fighter in fighters[start:end]:
            fighter_id = fighter[1]
            reg = fighter[2]

            name = get_prds(fighter_id)
            redk = get_redk(reg)
            if fighter[3] != 0:
                fighter_name = f"🖐{name}{redk}"
            else:
                fighter_name = f"{name}{redk}"

            button = InlineKeyboardButton(text=fighter_name, callback_data=f'prd_{fighter_id}_{fighter[4]}_{reg}_{pag}_{user_id}')
            row.append(button)

            if len(row) == 3:
                change_kb.row(*row)
                row = []

        if row:
            change_kb.row(*row)

        total_pages = (len(fighters) + 11) // 12
        if len(fighters) > 12:
            change_kb.row(
                InlineKeyboardButton(text="Назад", callback_data=f'prdprev_{total_pages if pag == 1 else pag-1}_{user_id}'),
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_{pag}_{user_id}'),
                InlineKeyboardButton(text="Вперед", callback_data=f'prdnext_{"1" if pag >= total_pages else pag+1}_{user_id}')
            )
        else:
            change_kb.row(InlineKeyboardButton(text="Слоты", callback_data=f'slots_{pag}_{user_id}'))

        await call.message.edit_text('<b>Твои предметы ❕</b>', reply_markup=change_kb, parse_mode='html')
        
@dp.callback_query_handler(lambda query: query.data.startswith('choose_'))
async def handle_choose_fighter(query):
    user_id = query.from_user.id
    fighter_id = int(query.data.split('_')[1])
    if user_id in players:
        await query.answer('Во время игры нельзя сменить персонажа ❕')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    vo = c.fetchone()
    hp1 = vo[7]
    attack1 = vo[8]
    armor1 = vo[9]
    crit1 = vo[10]
    uklon1 = vo[11]
    vampir1 = vo[12]
    mmr = vo[9]
    #
    c.execute('UPDATE pers SET hp=?, uron=?, armor=?, crit=?, uklon=?, vampir=? WHERE status="1" AND user_id=?',(hp1, attack1, armor1, crit1, uklon1, vampir1, user_id,))
    c.execute('UPDATE pers SET status="0" WHERE status="1" AND user_id=?',(user_id,))
    c.execute('UPDATE pers SET status=? WHERE user_id=? AND type=?', (1, user_id, fighter_id))
    c.execute('UPDATE users SET voins=? WHERE user_id=?', (fighter_id, user_id))
    base.commit()
    c.execute('SELECT * FROM pers WHERE status="1" AND user_id=?',(user_id,))
    pers = c.fetchone()
    #
    hp2 = pers[3]
    uron2 = pers[4]
    armor2 = pers[5]
    crit2 = pers[6]
    uklon2 = pers[7]
    vampir2 = pers[8]
    c.execute(f'UPDATE users SET voin1={hp2}, voin2={uron2}, voin3={armor2}, voin4={crit2}, voin5={uklon2}, voin6={vampir2} WHERE user_id={user_id}')
    base.commit()

    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = c.fetchone()
    hp = user[7]
    phot = user[2]
    attack = user[8]
    shit = user[9]
    krit = user[10]
    uklon = user[11]
    vampirism = user[12]
    op = user[4]
    chosen_voin = ""
    if user[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif user[2] == 2:
        chosen_voin = "Пудж"
    elif user[2] == 3:
        chosen_voin = "Король Варваров"
    elif user[2] == 4:
        chosen_voin = "Гигачад"
    elif user[2] == 5:
        chosen_voin = "Танос"
    elif user[2] == 6:
        chosen_voin = "Стальной клык"
    elif user[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif user[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif user[2] == 9:
        chosen_voin = "Пепе Маг"
    elif user[2] == 10:
        chosen_voin = "Тень"
    elif user[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif user[2] == 12:
        chosen_voin = "Слендермен"
    elif user[2] == 13:
        chosen_voin = "Человек Паук"
    elif user[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif user[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif user[2] == 16:
        chosen_voin = "Паймон"
    elif user[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif user[2] == 18:
        chosen_voin = "Стальной Гром"
    elif user[2] == 19:
        chosen_voin = "Аста"
    elif user[2] == 20:
        chosen_voin = "Шрек"

    await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    await bot.send_photo(chat_id=query.message.chat.id, photo=open(f'/bot/module-deda/bot{phot}.png', 'rb'),
                              caption=f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hp}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)

########
@dp.message_handler(text=['Топ игроков 🎖'])
async def show_top(msg):
    if msg.chat.type == "supergroup":
        return
    user_id = msg.from_user.id
    c.execute("SELECT * FROM users ORDER BY mmr DESC") 
    users = c.fetchall()
    place = get_user_place(user_id, users)
    total_pages = math.ceil(min(len(users), 30) / 5) 

    if place > 30:
        current_page = 1
    else:
        current_page = (place - 1) // 5 + 1

    await construct_message(user_id, users, total_pages, current_page)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith(('prev|', 'next|')))
async def process_callback_pagination(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    query = callback_query.data.split('|')

    c.execute("SELECT * FROM users ORDER BY mmr DESC")
    users = c.fetchall()

    total_pages = int(query[2])
    current_page = int(query[1])

    if query[0] == 'prev' and current_page > 1:
        current_page -= 1
    elif query[0] == 'next' and current_page < total_pages:
        current_page += 1
    else:
        await callback_query.answer('Там ничего нет ❌')

    await construct_message(user_id, users, total_pages, current_page, callback_query.message.message_id)

async def construct_message(user_id, users, total_pages, current_page, message_id=None):
    show_users = users[(current_page - 1) * 5: current_page * 5]

    keyboard = InlineKeyboardMarkup()
    prev_button = InlineKeyboardButton("◀️", callback_data=f"prev|{current_page}|{total_pages}")
    page_button = InlineKeyboardButton(f"{current_page} | {total_pages}", callback_data="ignore")
    next_button = InlineKeyboardButton("▶️", callback_data=f"next|{current_page}|{total_pages}")
    keyboard.row(prev_button, page_button, next_button)

    text = ""
    for i, user in enumerate(show_users):
        global_rank = (current_page - 1) * 5 + i + 1
        rank = get_user_emoji_rank(global_rank) 
        name = user[13]
        mmr = user[5]
        link = f'<a href="tg://user?id={user[0]}">{name}</a>'
        text += f"{rank} - {link}\n{mmr} MMR\n\n"

    user_place = get_user_place(user_id, users)
    text += f"🏆 Вы на {user_place} месте"

    if message_id is None:
        await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/top.png', 'rb'),
                              caption=text, reply_markup=keyboard, parse_mode='HTML')
    else:
        await bot.edit_message_caption(
            chat_id=user_id,
            message_id=message_id,
            caption=text,
            reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'ignore')
async def process_callback_swipe(callback_query: types.CallbackQuery):
    await callback_query.answer()

def get_user_place(user_id, users):
    for i, user in enumerate(users):
        if user[0] == user_id:
            return i+1
    return "неизвестно" 

def get_user_emoji_rank(global_rank):
    emoji_map = {
        0: '0️⃣', 1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣',
        5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣', 10: '🔟'
    }

    if global_rank <= 10:
        return emoji_map[global_rank]
    else:
        return emoji_map[global_rank // 10] + emoji_map[global_rank % 10]

@dp.message_handler(commands=['setexp'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setexp «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🧩')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[4]
        c.execute(f'UPDATE users SET exp={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🧩 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[4]
        c.execute(f'UPDATE users SET exp={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🧩 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось') 
        
@dp.message_handler(commands=['sethp'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /sethp «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите ❤')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[7]
        c.execute(f'UPDATE users SET voin1={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n❤ +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[7]
        c.execute(f'UPDATE users SET voin1={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n❤ -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')   
        
@dp.message_handler(commands=['setattack'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setattack «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🔫')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[8]
        c.execute(f'UPDATE users SET voin2={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🔫 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[8]
        c.execute(f'UPDATE users SET voin2={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🔫 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')
        
@dp.message_handler(commands=['setarmor'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setarmor «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🛡')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[9]
        c.execute(f'UPDATE users SET voin3={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🛡 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[9]
        c.execute(f'UPDATE users SET voin3={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🛡 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')   
       
@dp.message_handler(commands=['setc'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setc «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 💥')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[10]
        c.execute(f'UPDATE users SET voin4={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n💥 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[10]
        c.execute(f'UPDATE users SET voin4={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n💥 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')   
        
@dp.message_handler(commands=['setevade'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setevade «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🦋')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[11]
        c.execute(f'UPDATE users SET voin5={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🦋 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[11]
        c.execute(f'UPDATE users SET voin5={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🦋-{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')
        
@dp.message_handler(commands=['setv'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setv «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🦇')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[12]
        c.execute(f'UPDATE users SET voin6={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🦇 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[12]
        c.execute(f'UPDATE users SET voin6={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🦇 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')    

@dp.message_handler(commands=['setmoney'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setmoney «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 💰')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[1]
        c.execute(f'UPDATE users SET money={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n💰 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[1]
        c.execute(f'UPDATE users SET money={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n💰 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')

@dp.message_handler(commands=['setskam'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setskam «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🏆')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[6]
        c.execute(f'UPDATE users SET skam={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n👨‍💻 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[6]
        c.execute(f'UPDATE users SET skam={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n👨‍💻 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось') 
        
@dp.message_handler(commands=['setplay'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setplay «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🕹')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[3]
        c.execute(f'UPDATE users SET play={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🕹 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[3]
        c.execute(f'UPDATE users SET play={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🕹 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось') 

@dp.message_handler(commands=['setmmr'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setmmr «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 🏆')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[5]
        c.execute(f'UPDATE users SET mmr={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🏆 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[5]
        c.execute(f'UPDATE users SET mmr={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n🏆 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось') 
        
@dp.message_handler(commands=['setcoin'])
async def set(msg: types.Message):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    split = msg.text.split()
    if len(split) < 4:
        await msg.answer('❕ Использование | /setcoin «id» «+/-» «amount»')
        return
    arg = int(split[1])
    arg2 = split[2]
    arg3 = int(split[3])
    if not arg:
        await msg.answer('❕ Введите ID')
        return
    if not arg2 or arg2 not in ["+", "-", "минус", "плюс"]:
        await msg.answer('❕ Введите значение + | -')
        return
    if not arg3:
        await msg.answer('Введите 💎')
        return
    c.execute(f'SELECT * FROM users WHERE user_id={arg}')
    user = c.fetchone()
    if not user:
        await msg.answer('❕ Игрок не найден')
        return
    if arg3 <= 0:
        await msg.answer('❕ Ошибка в числе')
        return
    if arg2 == "+" or arg2 == "плюс":
        money = user[15]
        c.execute(f'UPDATE users SET coin={money + arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n💎 +{arg3}</b>', parse_mode='html')
    elif arg2 == "-" or arg2 == "минус":
        money = user[15]
        c.execute(f'UPDATE users SET coin={money - arg3} WHERE user_id={arg}')
        base.commit()
        await msg.answer(f'<b>Баланс пользователя обновлен.\n\n💎 -{arg3}</b>', parse_mode='html')
    else:
        await msg.answer('❕ Обновить баланс не удалось')
    
@dp.message_handler(commands=['och'])
async def send_queue(message: types.Message):
   user = message.from_user.id
   c.execute(f'SELECT * FROM admin WHERE user_id={user}')
   id = c.fetchone()
   if not id:
       return
   if not player_queue:
       await message.reply('❗️ Очередь пуста')
   else:
       text = "🕹 Очередь на игру\n\n"

       for idx, user_id in enumerate(player_queue, start=1):
           text += '{}. <a href="tg://user?id={}">Игрок</a>\n'.format(idx, user_id)

           if len(text) > 4000:
               await message.reply(text, parse_mode='HTML')
               text = ""

       if text.strip():
           await message.reply(text, parse_mode='HTML')

@dp.callback_query_handler(text='nexstpers')
async def pers(call):
    user_id = call.from_user.id
    if user_id in players:
        await call.answer('Во время игры нельзя сменить персонажа ❕')
        return
    c.execute('SELECT COUNT(*) FROM pers WHERE user_id=?', (user_id,))
    num_fighters = c.fetchone()[0]

    c.execute('SELECT * FROM pers WHERE user_id=?', (user_id,))
    fighters = c.fetchall()

    change_kb = InlineKeyboardMarkup(row_width=2)

    for fighter in fighters:
        fighter_id = fighter[1]

        if fighter_id == 1:
            fighter_name = 'Чмоня Гатс'
        elif fighter_id == 2:
            fighter_name = 'Пудж'
        elif fighter_id == 3:
            fighter_name = 'Король Варваров'
        elif fighter_id == 4:
            fighter_name = 'Гигачад'
        elif fighter_id == 5:
            fighter_name = 'Танос'
        elif fighter_id == 6:
            fighter_name = 'Стальной клык'
        elif fighter_id == 7:
            fighter_name = "Пепе Психопат"
        elif fighter_id == 8:
            fighter_name = "Пепе Архимаг"
        elif fighter_id == 9:
            fighter_name = "Пепе Маг"
        elif fighter_id == 10:
            fighter_name = "Тень"
        elif fighter_id == 11:
            fighter_name = "Шадоу Френд"
        elif fighter_id == 12:
            fighter_name = "Слендермен"
        elif fighter_id == 13:
            fighter_name = "Человек Паук"
        elif fighter_id == 14:
            fighter_name = "Кот в Сапогах"
        elif fighter_id == 15:
            fighter_name = "Грозная Паймон"
        elif fighter_id == 16:
            fighter_name = "Паймон"
        elif fighter_id == 17:
            fighter_name = "Пепе Бандит"
        elif fighter_id == 18:
            fighter_name = "Стальной Гром"
        elif fighter_id == 19:
            fighter_name = "Аста"
        elif fighter_id == 20:
            fighter_name = "Шрек"


        if fighter[2] == 1:
            fighter_name += ' ✔️'
                
        change_kb.add(InlineKeyboardButton(text=fighter_name, callback_data=f'choose_{fighter_id}'))

    await call.message.edit_caption('<b>Ваши воины ❕</b>', reply_markup=change_kb, parse_mode='html')


@dp.message_handler(commands=['edit'], commands_prefix='!./+')
async def setbd(msg):
    user = msg.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    try:
        split = msg.text.split()
        id = int(split[1])
        c.execute('SELECT * FROM users WHERE user_id=?',(id,))
        user = c.fetchone()
        
        #
        kb = InlineKeyboardMarkup()
        p1 = InlineKeyboardButton(text='Воины 🥷', callback_data=f'getvoin_{id}')
        p2 = InlineKeyboardButton(text='Выдать 🥷', callback_data=f'givevoin_{id}')
        p3 = InlineKeyboardButton(text='Забрать 🥷', callback_data=f'takevoin_{id}')
        kb.add(p1, p2, p3)
        #
        c.execute("SELECT * FROM users ORDER BY mmr DESC LIMIT 30")
        users = c.fetchall()
        money = user[1]
        c.execute(f'SELECT COUNT(*) FROM pers WHERE user_id={id}')
        voins = c.fetchone()[0]
        name = user[13]
        play = user[3]
        exp = user[4]
        mmr = user[5]
        skam = user[6]
        lose = user[14]
        coin = user[15]
        wins = play - lose
        
        if play != 0:
            win = (wins / play) * 100
        else:
            win = 0
        
        stats = (
            f'Профиль игрока {name}\n\n'
            f'🔰 {get_user_place(id, users)} ранг\n'
            f'🏆 {mmr} MMR\n\n'
            f'🔷 Сыграно боев: {play}\n'
            f'🔶 Доля побед: {win:.1f}%\n\n'
            f'🥷 Воины {voins} / 15\n'
            f'💰 Золото {money}\n'
            f'💎 Коины: {coin} шт.\n'
            f'🧩 Опыт {exp}\n\n'
            f'🧑‍💻 Заскамлено людей {skam}'
            )
             
        await msg.answer(stats, parse_mode='html', reply_markup=kb)
    except:
        await msg.answer('❕ Профиль игрока не найден') 

@dp.callback_query_handler(lambda c: c.data.startswith('takevoin_'))
async def dip(call):
    user = call.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    user_id = int(call.data.split('_')[1])
    c.execute('SELECT COUNT(*) FROM pers WHERE user_id=?', (user_id,))
    num_fighters = c.fetchone()[0]

    c.execute('SELECT * FROM pers WHERE user_id=?', (user_id,))
    fighters = c.fetchall()

    change_kb = InlineKeyboardMarkup(row_width=2)

    for fighter in fighters:
        fighter_id = fighter[1]

        if fighter_id == 1:
            fighter_name = 'Чмоня Гатс'
        elif fighter_id == 2:
            fighter_name = 'Пудж'
        elif fighter_id == 3:
            fighter_name = 'Король Варваров'
        elif fighter_id == 4:
            fighter_name = 'Гигачад'
        elif fighter_id == 5:
            fighter_name = 'Танос'
        elif fighter_id == 6:
            fighter_name = 'Стальной клык'
        elif fighter_id == 7:
            fighter_name = "Пепе Психопат"
        elif fighter_id == 8:
            fighter_name = "Пепе Архимаг"
        elif fighter_id == 9:
            fighter_name = "Пепе Маг"
        elif fighter_id == 10:
            fighter_name = "Тень"
        elif fighter_id == 11:
            fighter_name = "Шадоу Френд"
        elif fighter_id == 12:
            fighter_name = "Слендермен"
        elif fighter_id == 13:
            fighter_name = "Человек Паук"


        if fighter[2] == 1:
            fighter_name += ' ✔️'
                
        change_kb.add(InlineKeyboardButton(text=fighter_name, callback_data=f'take_{fighter_id}_{user_id}'))

    await call.message.edit_text('<b>Какого воина забрать ❕</b>', reply_markup=change_kb, parse_mode='html')
        
@dp.callback_query_handler(lambda c: c.data.startswith('getvoin_'))
async def dip(call):
    user = call.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    user_id = int(call.data.split('_')[1])
    c.execute('SELECT COUNT(*) FROM pers WHERE user_id=?', (user_id,))
    num_fighters = c.fetchone()[0]

    c.execute('SELECT * FROM pers WHERE user_id=?', (user_id,))
    fighters = c.fetchall()

    change_kb = InlineKeyboardMarkup(row_width=2)

    for fighter in fighters:
        fighter_id = fighter[1]

        if fighter_id == 1:
            fighter_name = 'Чмоня Гатс'
        elif fighter_id == 2:
            fighter_name = 'Пудж'
        elif fighter_id == 3:
            fighter_name = 'Король Варваров'
        elif fighter_id == 4:
            fighter_name = 'Гигачад'
        elif fighter_id == 5:
            fighter_name = 'Танос'
        elif fighter_id == 6:
            fighter_name = 'Стальной клык'
        elif fighter_id == 7:
            fighter_name = "Пепе Психопат"
        elif fighter_id == 8:
            fighter_name = "Пепе Архимаг"
        elif fighter_id == 9:
            fighter_name = "Пепе Маг"
        elif fighter_id == 10:
            fighter_name = "Тень"
        elif fighter_id == 11:
            fighter_name = "Шадоу Френд"
        elif fighter_id == 12:
            fighter_name = "Слендермен"
        elif fighter_id == 13:
            fighter_name = "Человек Паук"


        if fighter[2] == 1:
            fighter_name += ' ✔️'
                
        change_kb.add(InlineKeyboardButton(text=fighter_name, callback_data=f'kenplr_{fighter_id}'))

    await call.message.edit_text('<b>Воины игрока ❕</b>', reply_markup=change_kb, parse_mode='html')

@dp.callback_query_handler(lambda c: c.data.startswith('take_'))
async def dip(call):
    try:
        user_id = int(call.data.split('_')[2])
        type = int(call.data.split('_')[1])
        user = call.from_user.id
        c.execute(f'SELECT * FROM admin WHERE user_id={user}')
        id = c.fetchone()
        if not id:
            return
        c.execute(f'DELETE FROM pers WHERE user_id={user_id} AND type={type}')
        base.commit()
        await call.answer('Успешно ❕', show_alert=True)
    except:
        await call.answer('У данного человека уже нет данного воина ❕', show_alert=True)
        
@dp.callback_query_handler(lambda c: c.data.startswith('givevoin_'))
async def dip(call):
    user = call.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    user_id = int(call.data.split('_')[1])
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    #
    c.execute(f'SELECT * FROM pers WHERE user_id={user_id}')
    pers = c.fetchone()
    #
    givevoin = InlineKeyboardMarkup()
    p1 = InlineKeyboardButton(text='Чмоня гатс', callback_data=f'give:1:{user_id}')
    p2 = InlineKeyboardButton(text='Пудж', callback_data=f'give:2:{user_id}')
    p3 = InlineKeyboardButton(text='Король Варваров', callback_data=f'give:3:{user_id}')
    p4 = InlineKeyboardButton(text='Гигачад', callback_data=f'give:4:{user_id}')
    p5 = InlineKeyboardButton(text='Танос', callback_data=f'give:5:{user_id}')
    p6 = InlineKeyboardButton(text='Стальной клык', callback_data=f'give:6:{user_id}')
    p7 = InlineKeyboardButton(text='Пепе Психопат', callback_data=f'give:7:{user_id}')
    p8 = InlineKeyboardButton(text='Пепе Архимаг', callback_data=f'give:8:{user_id}')
    p9 = InlineKeyboardButton(text='Пепе Маг', callback_data=f'give:9:{user_id}')
    p10 = InlineKeyboardButton(text='Тень', callback_data=f'give:10:{user_id}')
    p11 = InlineKeyboardButton(text='Шадоу Френд', callback_data=f'give:11:{user_id}')
    p12 = InlineKeyboardButton(text='Слендермен', callback_data=f'give:12:{user_id}')
    p13 = InlineKeyboardButton(text='Человек Паук', callback_data=f'give:13:{user_id}')
    givevoin.add(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
    await call.message.answer('🥷 Какого воина выдать:', reply_markup=givevoin)

@dp.callback_query_handler(lambda c: c.data.startswith('kenplr_'))
async def dip(call):
    user = call.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    await call.answer('❕ Это воины игрока которого вы выбрали в панели', show_alert=True)

@dp.callback_query_handler(lambda c: c.data.startswith('give:'))
async def dip(call):
    user_id = int(call.data.split(':')[2])
    type = int(call.data.split(':')[1])
    user = call.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    if type == 1:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="1"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 1, 1, 550, 55, 1, 5, 1, 1, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 2:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="2"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 2, 0, 600, 90, 5, 10, 15, 5, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 3:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="3"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 3, 0, 1250, 120, 10, 10, 10, 10, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 4:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="4"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 4, 0, 1500, 500, 15, 20, 20, 15, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 5:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="5"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 5, 0, 6000, 2250, 80, 90, 45, 80, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 6:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="6"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 6, 0, 2500, 1250, 40, 60, 40, 80, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 7:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="7"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 7, 0, 1250, 500, 25, 50, 30, 60, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 8:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="8"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 8, 0, 3200, 550, 8, 40, 55, 20, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 9:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="9"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 9, 0, 2000, 280, 10, 60, 35, 40, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 10:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="10"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 10, 0, 4500, 1200, 65, 75, 40, 85, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 11:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="11"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 11, 0, 2500, 350, 13, 65, 35, 40, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 12:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="12"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 12, 0, 6200, 2250, 80, 80, 65, 90, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)
    elif type == 13:
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type="13"')
        voin = c.fetchone()
        if not voin:
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 13, 0, 5200, 1350, 80, 70, 70, 80, 0))
            base.commit()
            await call.answer('Готово ❕', show_alert=True)
            return
        await call.answer('❕ Данный воин присутсвует', show_alert=True)

@dp.message_handler(commands=['boy'])
async def chec_battles(message: types.Message):
    user = message.from_user.id
    c.execute(f'SELECT * FROM admin WHERE user_id={user}')
    id = c.fetchone()
    if not id:
        return
    if not players:
        await message.reply('❗️ Нет активных боев')
    else:
        text = ""
        battle_number = 1

        for player_id, player_stats in players.items():
            c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
            player_info = c.fetchone()
            user = c.fetchone()
            player_name = player_info[13]
            chosen_voin = ""
            if player_info[2] == 1:
                chosen_voin = "Чмоня Гатс"
            elif player_info[2] == 2:
                chosen_voin = "Пудж"
            elif player_info[2] == 3:
                chosen_voin = "Король Варваров"
            elif player_info[2] == 4:
                chosen_voin = "Гигачад"
            elif player_info[2] == 5:
                chosen_voin = "Танос"
            elif player_info[2] == 6:
                chosen_voin = "Стальной клык"
            elif player_info[2] == 7:
                chosen_voin = "Пепе Психопат"
            elif player_info[2] == 8:
                chosen_voin = "Пепе Архимаг"
            elif player_info[2] == 9:
                chosen_voin = "Пепе Маг"
            elif player_info[2] == 10:
                chosen_voin = "Тень"
            elif player_info[2] == 11:
                chosen_voin = "Шадоу Френд"
            elif player_info[2] == 12:
                chosen_voin = "Слендермен"
            elif player_info[2] == 13:
                chosen_voin = "Человек Паук"
            elif player_info[2] == 14:
                chosen_voin = "Кот в Сапогах"
            elif player_info[2] == 15:
                chosen_voin = "Грозная Паймон"
            elif player_info[2] == 16:
                chosen_voin = "Паймон"
            elif player_info[2] == 17:
                chosen_voin = "Пепе Бандит"
            elif player_info[2] == 18:
                chosen_voin = "Стальной Гром"
            elif player_info[2] == 19:
                chosen_voin = "Аста"
            elif player_info[2] == 20:
                chosen_voin = "Шрек"
           
            text += f"〰️\n{battle_number}️⃣ Бой\n\n"
            text += f"👤 <a href='tg://user?id={player_id}'>{player_name}</a>\n"
            text += f"🎭 {chosen_voin} ❤️  {player_stats['health']}\n"
            text += f"🔫 {player_stats['attack']} "
            text += f"🛡 {player_stats['armor']} "
            text += f"💥 {player_stats['crit_chance']}% "
            text += f"🦋 {player_stats['evade_chance']}% "
            text += f"🦇 {player_stats['vampirism_chance']}%\n\n"

            if len(text) > 4000:
                await message.reply(text, parse_mode='HTML')
                text = ""
                
            battle_number += 1

        if text.strip():
           await message.reply(text, parse_mode='HTML')

@dp.message_handler(text=['Играть 🕹'])
async def duel_command_handler(message: types.Message):
    if message.chat.type == "supergroup":
        return
    user_id = message.from_user.id
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    play = c.fetchone()
    if not play:
        await message.answer('❗ Введите  /start и попробуйте снова.')
        return
    if play[23] != 0:
        c.execute(f'UPDATE users SET attacks={"0"} WHERE user_id={user_id}')
        base.commit()
        
    if int(user_id) in player_queue:
        await message.reply("❗ <b>Вы уже в ожидании противника</b>", reply_markup=get_cancel_keyboard(user_id), parse_mode='html')
        return

    if int(user_id) in players:
        await message.reply("<b>Вы находитесь в бою ❕</b>", parse_mode='html')
        return
    player_queue.append(user_id)
    await message.answer_sticker(sticker='CAACAgEAAxkBAAEXUmNlKo4N6ASs2cJlzOZmkVpsGrLxOQACxQIAAkeAGUTTk7G7rIZ7GjAE')
    await message.answer('♻️ <b>Поиск противника...</b>', reply_markup=get_cancel_keyboard(user_id), parse_mode='html')

    if len(player_queue) >= 2:
        await start_duel()

async def afkst(msg1, msg2, user1, user2):
    c.execute(f'SELECT * FROM users WHERE user_id={user1}')
    us = c.fetchone()
    attack = us[23]
    count = 0
    seconds = 20
    destv = 0

    while True:
        c.execute(f'SELECT * FROM users WHERE user_id={user1}')
        new = c.fetchone()

        
        if user1 not in players:
            break

        if new[23] != attack:
            break

        if count >= seconds:
            if user1 in players:
                if destv == 0:
                    await bot.send_message(user1, '<b>❕ Атакуйте</b>')
                    seconds += 10
                    destv = 1
                else:
                    await win_players(msg1, msg2, user1, user2)
                    destv = 0
                    break
            else:
                break

        await asyncio.sleep(1)
        count += 1
        

def get_cancel_keyboard(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Отменить поиск ❌", callback_data=f"cancel:{user_id}"))
    return keyboard

async def start_duel():
    player1_id = player_queue.pop(0)
    player2_id = player_queue.pop(0)
    global opponent_id
    global player_id
    player_id = player1_id
    opponent_id = player2_id
    c.execute(f'SELECT * FROM users WHERE user_id={player1_id}')
    p1 = c.fetchone()
    
    c.execute(f'SELECT * FROM users WHERE user_id={player2_id}')
    p2 = c.fetchone()
    
    # player 1
    hp = p1[7]
    attack = p1[8]
    armor = p1[9]
    crit = p1[10]
    uklon = p1[11]
    vamp = p1[12]
    phot2 = p1[2]
    # player 2
    hp2 = p2[7]
    attack2 = p2[8]
    armor2 = p2[9]
    crit2 = p2[10]
    uklon2 = p2[11]
    vamp2 = p2[12]
    phot1 = p2[2]

    players[player1_id] = {
        'health': hp,
        'attack': attack,
        'armor': armor,
        'crit_chance': crit,
        'evade_chance': uklon,
        'vampirism_chance': vamp,
        'turn': True,  # player1 starts
        'message_id': None
    }

    players[player2_id] = {
        'health': hp2,
        'attack': attack2,
        'armor': armor2,
        'crit_chance': crit2,
        'evade_chance': uklon2,
        'vampirism_chance': vamp2,
        'turn': False,  # player2 waits
        'message_id': None
    }
    chosen_voin = ""
    if p1[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif p1[2] == 2:
        chosen_voin = "Пудж"
    elif p1[2] == 3:
        chosen_voin = "Король Варваров"
    elif p1[2] == 4:
        chosen_voin = "Гигачад"
    elif p1[2] == 5:
        chosen_voin = "Танос"
    elif p1[2] == 6:
        chosen_voin = "Стальной клык"
    elif p1[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif p1[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif p1[2] == 9:
        chosen_voin = "Пепе Маг"
    elif p1[2] == 10:
        chosen_voin = "Тень"
    elif p1[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif p1[2] == 12:
        chosen_voin = "Слендермен"
    elif p1[2] == 13:
        chosen_voin = "Человек Паук"
    elif p1[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif p1[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif p1[2] == 16:
        chosen_voin = "Паймон"
    elif p1[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif p1[2] == 18:
        chosen_voin = "Стальной Гром"
    elif p1[2] == 19:
        chosen_voin = "Аста"
    elif p1[2] == 20:
        chosen_voin = "Шрек"
    
    chosen_voin2 = ""
    if p2[2] == 1:
        chosen_voin2 = "Чмоня Гатс"
    elif p2[2] == 2:
        chosen_voin2 = "Пудж"
    elif p2[2] == 3:
        chosen_voin2 = "Король Варваров"
    elif p2[2] == 4:
        chosen_voin2 = "Гигачад"
    elif p2[2] == 5:
        chosen_voin2 = "Танос"
    elif p2[2] == 6:
        chosen_voin2 = "Стальной клык"  
    if p2[2] == 7:
        chosen_voin2 = "Чмоня Гатс"
    elif p2[2] == 2:
        chosen_voin2 = "Пудж"
    elif p2[2] == 3:
        chosen_voin2 = "Король Варваров"
    elif p2[2] == 4:
        chosen_voin2 = "Гигачад"
    elif p2[2] == 5:
        chosen_voin2 = "Танос"
    elif p2[2] == 6:
        chosen_voin2 = "Стальной клык"
    elif p2[2] == 7:
        chosen_voin2 = "Пепе Психопат"
    elif p2[2] == 8:
        chosen_voin2 = "Пепе Архимаг"
    elif p2[2] == 9:
        chosen_voin2 = "Пепе Маг"
    elif p2[2] == 10:
        chosen_voin2 = "Тень"
    elif p2[2] == 11:
        chosen_voin2 = "Шадоу Френд"
    elif p2[2] == 12:
        chosen_voin2 = "Слендермен"
    elif p2[2] == 13:
        chosen_voin2 = "Человек Паук"
    elif p2[2] == 14:
        chosen_voin2 = "Кот в Сапогах"
    elif p2[2] == 15:
        chosen_voin2 = "Грозная Паймон"
    elif p2[2] == 16:
        chosen_voin2 = "Паймон"
    elif p2[2] == 17:
        chosen_voin2 = "Пепе Бандит"
    elif p2[2] == 18:
        chosen_voin2 = "Стальной Гром"
    elif p2[2] == 19:
        chosen_voin2 = "Аста"
    elif p2[2] == 20:
        chosen_voin2 = "Шрек"

    await bot.send_message(player1_id, "<b>Противник найден!</b>", parse_mode='html')

    with open(f'/bot/module-deda/bot{phot1}.png', 'rb') as photo1:
        msg1 = await bot.send_photo(
            chat_id=player1_id,
            photo=photo1,
            caption=f"<b>{get_stats_message(player1_id, player2_id)}</b>", 
            parse_mode='html',
            reply_markup=get_attack_keyboard(player1_id, player2_id)
        )
        players[player1_id]['message_id'] = msg1.message_id
        


    await bot.send_message(player2_id, "<b>Противник найден!</b>", parse_mode='html')
    with open(f'/bot/module-deda/bot{phot2}.png', 'rb') as photo2:
        msg2 = await bot.send_photo(
            chat_id=player2_id,
            photo=photo2,
            caption=f"<b>{get_stats_message2(player2_id, player1_id)}</b>", 
            parse_mode='html',
            reply_markup=get_attack_keyboard(player2_id, player1_id)  # передайте идентификаторы обоих игроков
        )
        players[player2_id]['message_id'] = msg2.message_id
        
    await afkst(msg1, msg2, player1_id, player2_id)

def get_stats_message(player_id, opponent_id):
    player_stats = players[player_id]
    opponent_stats = players[opponent_id]
    c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
    p1 = c.fetchone()
    c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
    p2 = c.fetchone()
    nick = p2[13]
    mmr2 = p2[5]
    mmr1 = p1[5]
    voin = ""
    if p1[2] == 1:
        voin = "Чмоня Гатс"
    elif p1[2] == 2:
        voin = "Пудж"
    elif p1[2] == 3:
        voin = "Король Варваров"
    elif p1[2] == 4:
        voin = "Гигачад"
    elif p1[2] == 5:
        voin = "Танос"
    elif p1[2] == 6:
        voin = "Стальной клык"
    elif p1[2] == 7:
        voin = "Пепе Психопат"
    elif p1[2] == 8:
        voin = "Пепе Архимаг"
    elif p1[2] == 9:
        voin = "Пепе Маг"
    elif p1[2] == 10:
        voin = "Тень"
    elif p1[2] == 11:
        voin = "Шадоу Френд"
    elif p1[2] == 12:
        voin = "Слендермен"
    elif p1[2] == 13:
        voin = "Человек Паук"
    elif p1[2] == 14:
        voin = "Кот в Сапогах"
    elif p1[2] == 15:
        voin = "Грозная Паймон"
    elif p1[2] == 16:
        voin = "Паймон"
    elif p1[2] == 17:
        voin = "Пепе Бандит"
    elif p1[2] == 18:
        voin = "Стальной Гром"
    elif p1[2] == 19:
        voin = "Аста"
    elif p1[2] == 20:
        voin = "Шрек"
    
    voin2 = ""
    if p2[2] == 1:
        voin2 = "Чмоня Гатс"
    elif p2[2] == 2:
        voin2 = "Пудж"
    elif p2[2] == 3:
        voin2 = "Король Варваров"
    elif p2[2] == 4:
        voin2 = "Гигачад"
    elif p2[2] == 5:
        voin2 = "Танос"
    elif p2[2] == 6:
        voin2 = "Стальной клык"
    elif p2[2] == 7:
        voin2 = "Пепе Психопат"
    elif p2[2] == 8:
        voin2 = "Пепе Архимаг"
    elif p2[2] == 9:
        voin2 = "Пепе Маг"
    elif p2[2] == 10:
        voin2 = "Тень"
    elif p2[2] == 11:
        voin2 = "Шадоу Френд"
    elif p2[2] == 12:
        voin2 = "Слендермен"
    elif p2[2] == 13:
        voin2 = "Человек Паук"
    elif p2[2] == 14:
        voin2 = "Кот в Сапогах"
    elif p2[2] == 15:
        voin2 = "Грозная Паймон"
    elif p2[2] == 16:
        voin2 = "Паймон"
    elif p2[2] == 17:
        voin2 = "Пепе Бандит"
    elif p2[2] == 18:
        voin2 = "Стальной Гром"
    elif p2[2] == 19:
        voin2 = "Аста"
    elif p2[2] == 20:
        voin2 = "Шрек"
    
    message = f"{nick} | {mmr2} MMR\n" \
              f"🎭 {voin2} ❤️ {opponent_stats['health']}\n" \
              f"🔫 {opponent_stats['attack']} " \
              f"🛡 {opponent_stats['armor']} " \
              f"💥 {opponent_stats['crit_chance']}%\n" \
              f"🦋 {opponent_stats['evade_chance']}% " \
              f"🦇 {opponent_stats['vampirism_chance']}%\n\n" \
              f"Вы | {mmr1} MMR\n" \
              f"🎭 {voin} ❤️  {player_stats['health']}\n" \
              f"🔫 {player_stats['attack']} " \
              f"<b>🛡 {player_stats['armor']} </b>" \
              f"<b>💥 {player_stats['crit_chance']}%\n</b>" \
              f"<b>🦋 {player_stats['evade_chance']}%</b>" \
              f"<b> 🦇 {player_stats['vampirism_chance']}%\n\n☀️ Ваша очередь атаковать!</b>"

    return message
    
def get_stats_message2(player_id, opponent_id):
    player_stats = players[player_id]
    opponent_stats = players[opponent_id]
    c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
    p1 = c.fetchone()
    c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
    p2 = c.fetchone()
    nick = p2[13]
    mmr2 = p2[5]
    mmr1 = p1[5]
    voin = ""
    if p1[2] == 1:
        voin = "Чмоня Гатс"
    elif p1[2] == 2:
        voin = "Пудж"
    elif p1[2] == 3:
        voin = "Король Варваров"
    elif p1[2] == 4:
        voin = "Гигачад"
    elif p1[2] == 5:
        voin = "Танос"
    elif p1[2] == 6:
        voin = "Стальной клык"
    elif p1[2] == 7:
        voin = "Пепе Психопат"
    elif p1[2] == 8:
        voin = "Пепе Архимаг"
    elif p1[2] == 9:
        voin = "Пепе Маг"
    elif p1[2] == 10:
        voin = "Тень"
    elif p1[2] == 11:
        voin = "Шадоу Френд"
    elif p1[2] == 12:
        voin = "Слендермен"
    elif p1[2] == 13:
        voin = "Человек Паук"
    elif p1[2] == 14:
        voin = "Кот в Сапогах"
    elif p1[2] == 15:
        voin = "Грозная Паймон"
    elif p1[2] == 16:
        voin = "Паймон"
    elif p1[2] == 17:
        voin = "Пепе Бандит"
    elif p1[2] == 18:
        voin = "Стальной Гром"
    elif p1[2] == 19:
        voin = "Аста"
    elif p1[2] == 20:
        voin = "Шрек"
    
    voin2 = ""
    if p2[2] == 1:
        voin2 = "Чмоня Гатс"
    elif p2[2] == 2:
        voin2 = "Пудж"
    elif p2[2] == 3:
        voin2 = "Король Варваров"
    elif p2[2] == 4:
        voin2 = "Гигачад"
    elif p2[2] == 5:
        voin2 = "Танос"
    elif p2[2] == 6:
        voin2 = "Стальной клык"
    elif p2[2] == 7:
        voin2 = "Пепе Психопат"
    elif p2[2] == 8:
        voin2 = "Пепе Архимаг"
    elif p2[2] == 9:
        voin2 = "Пепе Маг"
    elif p2[2] == 10:
        voin2 = "Тень"
    elif p2[2] == 11:
        voin2 = "Шадоу Френд"
    elif p2[2] == 12:
        voin2 = "Слендермен"
    elif p2[2] == 13:
        voin2 = "Человек Паук"
    elif p1[2] == 14:
        voin = "Кот в Сапогах"
    elif p1[2] == 15:
        voin = "Грозная Паймон"
    elif p1[2] == 16:
        voin = "Паймон"
    elif p1[2] == 17:
        voin = "Пепе Бандит"
    elif p1[2] == 18:
        voin = "Стальной Гром"
    elif p1[2] == 19:
        voin = "Аста"
    elif p1[2] == 20:
        voin = "Шрек"

    message = f"{nick} | {mmr2} MMR\n" \
              f"🎭 {voin2} ❤️ {opponent_stats['health']}\n" \
              f"🔫 {opponent_stats['attack']} " \
              f"🛡 {opponent_stats['armor']} " \
              f"💥 {opponent_stats['crit_chance']}%\n" \
              f"🦋 {opponent_stats['evade_chance']}% " \
              f"🦇 {opponent_stats['vampirism_chance']}%\n\n" \
              f"Вы | {mmr1} MMR\n" \
              f"🎭 {voin} ❤️  {player_stats['health']}\n" \
              f"🔫 {player_stats['attack']} " \
              f"<b>🛡 {player_stats['armor']} </b>" \
              f"<b>💥 {player_stats['crit_chance']}%\n</b>" \
              f"<b>🦋 {player_stats['evade_chance']}%</b>" \
              f"<b> 🦇 {player_stats['vampirism_chance']}%\n\n🌑 {nick} атакует...</b>"

    return message
    

def get_attack_keyboard(player_id, opponent_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Удар 🥊", callback_data=f"attack:{player_id}:{opponent_id}"))
    keyboard.add(types.InlineKeyboardButton("Сдаться 🎈", callback_data=f"notcanc:{player_id}:{opponent_id}"))
    opponent_id = opponent_id
    return keyboard

@dp.callback_query_handler(lambda c: c.data.startswith('attack:'))
async def handle_attack_callback(call: types.CallbackQuery):
    data = call.data.split()
    player_id = call.from_user.id
    playe = call.from_user.id
    opponent_id = int(call.data.split(':')[2])
    
    
    if playe not in players:
        await call.message.edit_caption(caption='❕ Кнопка недействительна')
        return
    
    if players[playe]['turn'] == False:
        await call.answer("Сейчас не ваш ход ❕")
        return
    
    player_stats = players[player_id]
    opponent_stats = players[opponent_id]
    
    old_player_health = player_stats['health']
    old_opponent_health = opponent_stats['health']
    
    old_player_attack = player_stats['attack']
    old_opponent_attack = opponent_stats['attack']
    
    old_player_armor = player_stats['armor']
    old_opponent_armor = opponent_stats['armor']
    
    old_player_crit_chance = player_stats['crit_chance']
    old_opponent_crit_chance = opponent_stats['crit_chance']
    
    old_player_evade_chance = player_stats['evade_chance']
    old_opponent_evade_chance = opponent_stats['evade_chance']
    
    old_player_vampirism_chance = player_stats['vampirism_chance']
    old_opponent_vampirism_chance = opponent_stats['vampirism_chance']
    
    attack_damage = player_stats['attack']
    c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
    p1 = c.fetchone()
    c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
    p2 = c.fetchone()
    nick = p2[13]
    nick2 = p1[13]
    mmr2 = p2[5]
    mmr1 = p1[5]
    voin = ""
    if p1[2] == 1:
        voin = "Чмоня Гатс"
    elif p1[2] == 2:
        voin = "Пудж"
    elif p1[2] == 3:
        voin = "Король Варваров"
    elif p1[2] == 4:
        voin = "Гигачад"
    elif p1[2] == 5:
        voin = "Танос"
    elif p1[2] == 6:
        voin = "Стальной клык"
    elif p1[2] == 7:
        voin = "Пепе Психопат"
    elif p1[2] == 8:
        voin = "Пепе Архимаг"
    elif p1[2] == 9:
        voin = "Пепе Маг"
    elif p1[2] == 10:
        voin = "Тень"
    elif p1[2] == 11:
        voin = "Шадоу Френд"
    elif p1[2] == 12:
        voin = "Слендермен"
    elif p1[2] == 13:
        voin = "Человек Паук"
    elif p1[2] == 14:
        voin = "Кот в Сапогах"
    elif p1[2] == 15:
        voin = "Грозная Паймон"
    elif p1[2] == 16:
        voin = "Паймон"
    elif p1[2] == 17:
        voin = "Пепе Бандит"
    elif p1[2] == 18:
        voin = "Стальной Гром"
    elif p1[2] == 19:
        voin = "Аста"
    elif p1[2] == 20:
        voin = "Шрек"
    
    voin2 = ""
    if p2[2] == 1:
        voin2 = "Чмоня Гатс"
    elif p2[2] == 2:
        voin2 = "Пудж"
    elif p2[2] == 3:
        voin2 = "Король Варваров"
    elif p2[2] == 4:
        voin2 = "Гигачад"
    elif p2[2] == 5:
        voin2 = "Танос"
    elif p2[2] == 6:
        voin2 = "Стальной клык"
    elif p2[2] == 7:
        voin2 = "Пепе Психопат"
    elif p2[2] == 8:
        voin2 = "Пепе Архимаг"
    elif p2[2] == 9:
        voin2 = "Пепе Маг"
    elif p2[2] == 10:
        voin2 = "Тень"
    elif p2[2] == 11:
        voin2 = "Шадоу Френд"
    elif p2[2] == 12:
        voin2 = "Слендермен"
    elif p2[2] == 13:
        voin2 = "Человек Паук"
    elif p2[2] == 14:
        voin2 = "Кот в Сапогах"
    elif p2[2] == 15:
        voin2 = "Грозная Паймон"
    elif p2[2] == 16:
        voin2 = "Паймон"
    elif p2[2] == 17:
        voin2 = "Пепе Бандит"
    elif p2[2] == 18:
        voin2 = "Стальной Гром"
    elif p2[2] == 19:
        voin2 = "Аста"
    elif p2[2] == 20:
        voin2 = "Шрек"
    if random.randint(1, 100) <= player_stats['crit_chance']:
        attack_damage *= random.randint(2, 5)

    if random.randint(1, 100) <= opponent_stats['evade_chance']:
        player_stats['turn'] = False
        opponent_stats['turn'] = True
        c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
        atm = c.fetchone()
        ata = int(atm[23])
        ata += 1
        c.execute(f'UPDATE users SET attacks={ata} WHERE user_id={player_id}')
        base.commit()
        ka = 1
        ju = 2
        
        await bot.edit_message_caption(chat_id=player_id, 
                               message_id=player_stats['message_id'], 
                               caption=f"<b>{nick} | {mmr2} MMR\n🎭 {voin2} ❤ {old_opponent_health}\n🔫 {old_opponent_attack} 🛡 {old_opponent_armor} 💥\n{old_opponent_crit_chance}% 🦋 {old_opponent_evade_chance}% 🦇 {old_opponent_vampirism_chance}%\n\nВы | {mmr1} MMR\n🎭 {voin} ❤ {old_player_health}\n🔫 {old_player_attack} 🛡 {old_player_armor} 💥\n{old_player_crit_chance}% 🦋 {old_player_evade_chance}% 🦇 {old_player_vampirism_chance}%\n\nВы промахнулись 🌷\n\n🌑 {nick} атакует...\n\n</b>", 
                               reply_markup=get_attack_keyboard(player_id, opponent_id), parse_mode='html')
        await bot.edit_message_caption(chat_id=opponent_id, 
                                    message_id=opponent_stats['message_id'], 
                                    caption=f"<b>{nick2} | {mmr1} MMR\n🎭 {voin} ❤ {old_player_health}\n🔫 {old_player_attack} 🛡 {old_player_armor} 💥\n{old_player_crit_chance}% 🦋 {old_player_evade_chance}% 🦇 {old_player_vampirism_chance}%\n\nВы | {mmr2} MMR\n🎭 {voin2} ❤ {old_opponent_health}\n🔫 {old_opponent_attack} 🛡 {old_opponent_armor} 💥\n{old_opponent_crit_chance}% 🦋 {old_opponent_evade_chance}% 🦇 {old_opponent_vampirism_chance}%\n\nВраг промахнулся 🌷\n\n☀️ Ваша очередь атаковать!\n</b>",
                                    reply_markup=get_attack_keyboard(opponent_id, player_id), parse_mode='html')
        await afkst(ka, ju, opponent_id, player_id)
        return
    c.execute(f'SELECT * FROM prd WHERE user_id={player_id} AND use!={"0"} AND type={"3"}')
    prd = c.fetchone()
    if prd:
        redk = prd[2]
        if redk == 1:
            chance = 0.025
            x = 1.5
        elif redk == 2:
            chance = 0.050
            x = 2
        elif redk == 3:
            x = 3
            chance = 0.075
        elif redk == 4:
            x = 3
            chance = 0.1
        elif redk == 5:
            x = 3
            chance = 0.125
        elif redk == 6:
            x = 3
            chance = 0.150
        elif redk == 7:
            x = 4
            chance = 0.3
        elif redk == 8:
            x = 5
            chance = 0.4
        if random.random() <= chance:
            sto = 1
            attack_damage *= x
        else:
            sto = 0
            pass
    else:
        sto = 0
        pass
    attack_damage -= int(attack_damage * (opponent_stats['armor'] / 100))
    if attack_damage <= 0:
        attack_damage = 1

    
    c.execute(f'SELECT * FROM prd WHERE user_id={player_id} AND use!={"0"} AND type={"1"}')
    prd = c.fetchone()
    if prd:
        redk = prd[2]
        if redk == 1:
            chance = 0.0025
        elif redk == 2:
            chance = 0.005
        elif redk == 3:
            chance = 0.0075
        elif redk == 4:
            chance = 0.01
        elif redk == 5:
            chance = 0.015
        elif redk == 6:
            chance = 0.02
        elif redk == 7:
            chance = 0.03
        elif redk == 8:
            chance = 0.05
        if random.random() <= chance:
            toper = 1
            attack_damage = opponent_stats['health']
        else:
            toper = 0
            pass
    else:
        toper = 0
        pass
    
    player_stats['health'] += int(attack_damage * (player_stats['vampirism_chance'] / 100))
    opponent_stats['health'] -= int(attack_damage)


    if opponent_stats['health'] <= 0:
        c.execute(f'SELECT * FROM prd WHERE user_id={opponent_id} AND use!={"0"} AND type={"2"}')
        prd = c.fetchone()
        if prd:
            redk = prd[2]
            if redk == 1:
                chance = 0.25
            elif redk == 2:
                chance = 0.05
            elif redk == 3:
                chance = 0.075
            elif redk == 4:
                chance = 0.1
            elif redk == 5:
                chance = 0.125
            elif redk == 6:
                chance = 0.150
            elif redk == 7:
                chance = 0.2
            elif redk == 8:
                chance = 0.35
            if random.random() <= chance:
                amyl = 1
                c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
                p2 = c.fetchone()
                hp2 = p2[7]
                attack2 = p2[8]
                armor2 = p2[9]
                crit2 = p2[10]
                uklon2 = p2[11]
                vamp2 = p2[12]
                opponent_stats['health'] = hp2
                opponent_stats['attack'] = attack2
                opponent_stats['armor'] = armor2
                opponent_stats['crit_chance'] = crit2
                opponent_stats['evade_chance'] = uklon2
                opponent_stats['vampirism_chance'] = vamp2
                opponent_stats['turn'] = True
                player_stats['turn'] = False
            else:
                amyl = 0
                pass
        else:
            amyl = 0
            pass
        
        if amyl == 1:
            t = 1
            if t == 1:
                if toper == 0:
                    getg = "🔨" if sto == 1 else ""
                    kuv = "Кувалдой!" if sto == 1 else ""
                elif toper == 1:
                    getg = "🪓"
                    kuv = "Топором!"

                c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
                atm = c.fetchone()
                ata = int(atm[23])
                ata += 1
                c.execute(f'UPDATE users SET attacks={ata} WHERE user_id={player_id}')
                base.commit()
                ka = 1
                ju = 2
                
                await bot.edit_message_caption(chat_id=player_id,
                                message_id=player_stats['message_id'],
                                caption=f"<b>{nick} | {mmr2}  MMR\n🎭 {voin2} ❤ {opponent_stats['health']}\n🔫 {old_opponent_attack} 🛡 {old_opponent_armor} 💥\n{old_opponent_crit_chance}% 🦋 {old_opponent_evade_chance}% 🦇 {old_opponent_vampirism_chance}%\n\nВы | {mmr1} MMR\n🎭 {voin} ❤ {old_player_health + int(attack_damage * (player_stats['vampirism_chance'] / 100))}\n🔫 {old_player_attack} 🛡 {old_player_armor} 💥\n {old_player_crit_chance}% 🦋 {old_player_evade_chance}% 🦇 {old_player_vampirism_chance}%\n\n{getg} Вы нанесли {attack_damage} урона 🩸 {kuv}\n🧿 Амулет спас жизнь врагу!\n\n🌑 {nick} атакует...</b>",
                                parse_mode='html', 
                                reply_markup=get_attack_keyboard(player_id, opponent_id))
                await bot.edit_message_caption(chat_id=opponent_id,
                               message_id=opponent_stats['message_id'],
                               caption=f"<b>{nick2} | {mmr1} MMR\n🎭 {voin} ❤ {old_player_health + int(attack_damage * (player_stats['vampirism_chance'] / 100))}\n🔫 {old_player_attack} 🛡 {old_player_armor} 💥\n{old_player_crit_chance}% 🦋 {old_player_evade_chance}% 🦇 {old_player_vampirism_chance}%\n\nВы | {mmr2} MMR\n🎭 {voin2} ❤ {opponent_stats['health']}\n🔫 {old_opponent_attack} 🛡 {old_opponent_armor} 💥\n{old_opponent_crit_chance}% 🦋 {old_opponent_evade_chance}% 🦇 {old_opponent_vampirism_chance}%\n\n{getg} Вам нанесли {attack_damage} урона 🩸 {kuv}\n🧿 Амулет спас вам жизнь!\n\n☀️ Ваша очередь атаковать!</b>",
                               parse_mode='html', 
                               reply_markup=get_attack_keyboard(opponent_id, player_id))
                await afkst(ka, ju, opponent_id, player_id)
            return
        elif amyl == 0:
            pass
        m = players[opponent_id]['message_id']
        players.pop(player_id)
        players.pop(opponent_id)
        c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
        p1 = c.fetchone()
        c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
        p2 = c.fetchone()
        win = random.randint(5000, 25000)
        loser = random.randint(1000, 3600)
        opyt1 = random.randint(50, 400) 
        opyt2 = random.randint(50, 150)
        up1 = opyt1 + p1[4]
        up2 = opyt2 + p2[4]
        play = p1[3]
        play2 = p2[3]
        lo = p2[14]
        pla1 = play + 1
        pla2 = play2 + 1
        lo2 = lo + 1
        phot = p1[2]
        phot2 = p2[2]
        coin = p1[15]
        coinwin = random.randint(1, 5)
        wincoin = coin + coinwin
        wi1 = win + p1[1]
        wi2 = loser + p2[1]
        mmr = max(0, p1[5] + 30)
        mmr3 = max(0, p2[5] - 30)
        c.execute('UPDATE users SET money=?, exp=?, mmr=?, coin=?, play=? WHERE user_id=?',(wi1, up1, mmr, wincoin, pla1, player_id,))
        c.execute('UPDATE users SET money=?, exp=?, mmr=?, lose=?, play=? WHERE user_id=?',(wi2, up2, mmr3, lo2, pla2, opponent_id,))
        base.commit()
        
        
        await bot.delete_message(chat_id=opponent_id, message_id=m)
        await call.message.delete()
        await bot.send_photo(chat_id=player_id, photo=open(f'/bot/module-deda/bot{phot}.png', 'rb'),
                              caption=f"<b>Победа 🎃\n\n🥷 Воин {voin}\n🧩 Опыт +{opyt1}\n💰 Золото +{win}\n💎 Коины +{coinwin}\n\n+30 MMR</b>", parse_mode='html')
        await bot.send_photo(chat_id=opponent_id, photo=open(f'/bot/module-deda/bot{phot2}.png', 'rb'),
                              caption=f"<b>Поражение 💀\n\n🥷 Воин {voin2}\n🧩 Опыт +{opyt2}\n💰 Золото +{loser}\n\n-30 MMR</b>", parse_mode='html')
        
    else:
        player_stats['turn'] = False
        opponent_stats['turn'] = True
        getg = "🔨" if sto == 1 else ""
        kuv = "Кувалдой!" if sto == 1 else ""

        # update stats for both players
        ka = 1
        ju = 2
        c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
        atm = c.fetchone()
        ata = int(atm[23])
        ata += 1
        c.execute(f'UPDATE users SET attacks={ata} WHERE user_id={player_id}')
        base.commit()
        await bot.edit_message_caption(chat_id=player_id,
                                message_id=player_stats['message_id'],
                                caption=f"<b>{nick} | {mmr2}  MMR\n🎭 {voin2} ❤‍🩹 {old_opponent_health - attack_damage}\n🔫 {old_opponent_attack} 🛡 {old_opponent_armor} 💥\n{old_opponent_crit_chance}% 🦋 {old_opponent_evade_chance}% 🦇 {old_opponent_vampirism_chance}%\n\nВы | {mmr1} MMR\n🎭 {voin} ❤ {old_player_health + int(attack_damage * (player_stats['vampirism_chance'] / 100))}\n🔫 {old_player_attack} 🛡 {old_player_armor} 💥\n{old_player_crit_chance}% 🦋 {old_player_evade_chance}% 🦇 {old_player_vampirism_chance}%\n\n{getg} Вы нанесли {attack_damage} урона 🩸 {kuv}\n\n🌑 {nick} атакует...</b>",
                                parse_mode='html', 
                                reply_markup=get_attack_keyboard(player_id, opponent_id))
        await bot.edit_message_caption(chat_id=opponent_id,
                               message_id=opponent_stats['message_id'],
                               caption=f"<b>{nick2} | {mmr1} MMR\n🎭 {voin} ❤ {old_player_health + int(attack_damage * (player_stats['vampirism_chance'] / 100))}\n🔫 {old_player_attack} 🛡 {old_player_armor} 💥\n{old_player_crit_chance}% 🦋 {old_player_evade_chance}% 🦇 {old_player_vampirism_chance}%\n\nВы | {mmr2} MMR\n🎭 {voin2} ❤‍🩹 {old_opponent_health - attack_damage}\n🔫 {old_opponent_attack} 🛡 {old_opponent_armor} 💥\n{old_opponent_crit_chance}% 🦋 {old_opponent_evade_chance}% 🦇 {old_opponent_vampirism_chance}%\n\n{getg} Вам нанесли {attack_damage} урона 🩸 {kuv}\n\n☀️ Ваша очередь атаковать!\n</b>",
                               parse_mode='html', 
                               reply_markup=get_attack_keyboard(opponent_id, player_id))
        await afkst(1, 2, opponent_id, player_id)

@dp.callback_query_handler(lambda c: c.data.startswith('cancel:'))
async def handle_cancel_callback(call: types.CallbackQuery):
    user_id = int(call.data.split(':')[1])

    if user_id in player_queue:
        player_queue.remove(user_id)
        await call.message.edit_text("🕹 <b>Вы вышли из очереди</b>", parse_mode='html')
    else:
        await call.message.edit_text("❗ В<b>ы не находитесь в очереди</b>", parse_mode='html')
        return
    
@dp.callback_query_handler(lambda c: c.data.startswith('notcanc:'))
async def handle_cancel_callback(call: types.CallbackQuery):
    user_id = int(call.data.split(':')[1])
    opponent_id = int(call.data.split(':')[2])
    
    if user_id not in players:
        await call.message.edit_caption(caption='❕ Кнопка недействительна')
    else:
        m = players[opponent_id]['message_id']
        await bot.delete_message(chat_id=opponent_id, message_id=m)
        await call.message.delete()
        await win_player(user_id, opponent_id)

async def win_players(msg1, msg2, opponent_id, player_id):
    if player_id in players or opponent_id in players:
        msg1 = players[opponent_id]['message_id']
        msg2 = players[player_id]['message_id']
        players.pop(player_id)
        players.pop(opponent_id)
        c.execute(f'SELECT * FROM users WHERE user_id={player_id}')
        p1 = c.fetchone()
        c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
        p2 = c.fetchone()
        
        voin = ""
        if p1[2] == 1:
            voin = "Чмоня Гатс"
        elif p1[2] == 2:
            voin = "Пудж"
        elif p1[2] == 3:
            voin = "Король Варваров"
        elif p1[2] == 4:
            voin = "Гигачад"
        elif p1[2] == 5:
            voin = "Танос"
        elif p1[2] == 6:
            voin = "Стальной клык"
        elif p1[2] == 7:
            voin = "Пепе Психопат"
        elif p1[2] == 8:
            voin = "Пепе Архимаг"
        elif p1[2] == 9:
            voin = "Пепе Маг"
        elif p1[2] == 10:
            voin = "Тень"
        elif p1[2] == 11:
            voin = "Шадоу Френд"
        elif p1[2] == 12:
            voin = "Слендермен"
        elif p1[2] == 13:
            voin = "Человек Паук"
        elif p1[2] == 14:
            voin = "Кот в Сапогах"
        elif p1[2] == 15:
            voin = "Грозная Паймон"
        elif p1[2] == 16:
            voin = "Паймон"
        elif p1[2] == 17:
            voin = "Пепе Бандит"
        elif p1[2] == 18:
            voin = "Стальной Гром"
        elif p1[2] == 19:
            voin = "Аста"
        elif p1[2] == 20:
            voin = "Шрек"
    
        voin2 = ""
        if p2[2] == 1:
            voin2 = "Чмоня Гатс"
        elif p2[2] == 2:
            voin2 = "Пудж"
        elif p2[2] == 3:
            voin2 = "Король Варваров"
        elif p2[2] == 4:
            voin2 = "Гигачад"
        elif p2[2] == 5:
            voin2 = "Танос"
        elif p2[2] == 6:
            voin2 = "Стальной клык"
        elif p2[2] == 7:
            voin2 = "Пепе Психопат"
        elif p2[2] == 8:
            voin2 = "Пепе Архимаг"
        elif p2[2] == 9:
            voin2 = "Пепе Маг"
        elif p2[2] == 10:
            voin2 = "Тень"
        elif p2[2] == 11:
            voin2 = "Шадоу Френд"
        elif p2[2] == 12:
            voin2 = "Слендермен"
        elif p2[2] == 13:
            voin2 = "Человек Паук"
        elif p2[2] == 14:
            voin2 = "Кот в Сапогах"
        elif p2[2] == 15:
            voin2 = "Грозная Паймон"
        elif p2[2] == 16:
            voin2 = "Паймон"
        elif p2[2] == 17:
            voin2 = "Пепе Бандит"
        elif p2[2] == 18:
            voin2 = "Стальной Гром"
        elif p2[2] == 19:
            voin2 = "Аста"
        elif p2[2] == 20:
            voin2 = "Шрек"
        
        win = random.randint(5000, 25000)
        loser = random.randint(1000, 3600)
        opyt1 = random.randint(50, 400) 
        opyt2 = random.randint(50, 150)
        up1 = opyt1 + p1[4]
        up2 = opyt2 + p2[4]
        play = p1[3]
        play2 = p2[3]
        lo = p2[14]
        pla1 = play + 1
        pla2 = play2 + 1
        lo2 = lo + 1
        phot = p1[2]
        phot2 = p2[2]
        coin = p1[15]
        coinwin = random.randint(1, 5)
        wincoin = coin + coinwin
        wi1 = win + p1[1]
        wi2 = loser + p2[1]
        mmr = max(0, p1[5] + 33)
        mmr3 = max(0, p2[5] - 33)
        c.execute('UPDATE users SET money=?, exp=?, mmr=?, coin=?, play=?, attacks=? WHERE user_id=?',(wi1, up1, mmr, wincoin, pla1, 0, player_id,))
        c.execute('UPDATE users SET mmr=?, lose=?, play=?, attacks=? WHERE user_id=?',(mmr3, lo2, pla2, 0, opponent_id,))
        base.commit()
        
        
        await bot.delete_message(chat_id=opponent_id, message_id=msg1)
        await bot.delete_message(chat_id=player_id, message_id=msg2)
        await bot.send_photo(chat_id=player_id, photo=open(f'/bot/module-deda/bot{phot}.png', 'rb'),
                              caption=f"<b>Враг спит 🎃\n\n🥷 Воин {voin}\n🧩 Опыт +{opyt1}\n💰 Золото +{win}\n💎 Коины +{coinwin}\n\n+33 MMR</b>", parse_mode='html')
        await bot.send_photo(chat_id=opponent_id, photo=open(f'/bot/module-deda/bot{phot2}.png', 'rb'),
                              caption=f"<b>Нефиг спать 💀\n\n🥷 Воин {voin2}\n🧩 Опыт +0\n💰 Золото +0\n\n-33 MMR</b>", parse_mode='html')
    else:
        return
        
        
async def win_player(user_id, opponent_id):
    players.pop(user_id)
    players.pop(opponent_id)
        
    c.execute(f'SELECT * FROM users WHERE user_id={opponent_id}')
    p1 = c.fetchone()
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    p2 = c.fetchone()    
    win = random.randint(2500, 5000)
    opyt1 = random.randint(50, 150) 
    up1 = opyt1 + p1[4]
    wi1 = win + p1[1]
    play = p1[3]
    play2 = p2[3]
    lo = p2[14]
    pla1 = play + 1
    pla2 = play2 + 1
    lo2 = lo + 1
    phot = p1[2]
    phot2 = p2[2]
    coin = p1[15]
    coinwin = random.randint(1, 2)
    wincoin = coin + coinwin
    voin = ""
    if p1[2] == 1:
        voin = "Чмоня Гатс"
    elif p1[2] == 2:
        voin = "Пудж"
    elif p1[2] == 3:
        voin = "Король Варваров"
    elif p1[2] == 4:
        voin = "Гигачад"
    elif p1[2] == 5:
        voin = "Танос"
    elif p1[2] == 6:
        voin = "Стальной клык"
    elif p1[2] == 7:
        voin = "Пепе Психопат"
    elif p1[2] == 8:
        voin = "Пепе Архимаг"
    elif p1[2] == 9:
        voin = "Пепе Маг"
    elif p1[2] == 10:
        voin = "Тень"
    elif p1[2] == 11:
        voin = "Шадоу Френд"
    elif p1[2] == 12:
        voin = "Слендермен"
    elif p1[2] == 13:
        voin = "Человек Паук"
    elif p1[2] == 14:
        voin = "Кот в Сапогах"
    elif p1[2] == 15:
        voin = "Грозная Паймон"
    elif p1[2] == 16:
        voin = "Паймон"
    elif p1[2] == 17:
        voin = "Пепе Бандит"
    elif p1[2] == 18:
        voin = "Стальной Гром"
    elif p1[2] == 19:
        voin = "Аста"
    elif p1[2] == 20:
        voin = "Шрек"
    
    voin2 = ""
    if p2[2] == 1:
        voin2 = "Чмоня Гатс"
    elif p2[2] == 2:
        voin2 = "Пудж"
    elif p2[2] == 3:
        voin2 = "Король Варваров"
    elif p2[2] == 4:
        voin2 = "Гигачад"
    elif p2[2] == 5:
        voin2 = "Танос"
    elif p2[2] == 6:
        voin2 = "Стальной клык"
    elif p2[2] == 7:
        voin2 = "Пепе Психопат"
    elif p2[2] == 8:
        voin2 = "Пепе Архимаг"
    elif p2[2] == 9:
        voin2 = "Пепе Маг"
    elif p2[2] == 10:
        voin2 = "Тень"
    elif p2[2] == 11:
        voin2 = "Шадоу Френд"
    elif p2[2] == 12:
        voin2 = "Слендермен"
    elif p2[2] == 13:
        voin2 = "Человек Паук"
    elif p2[2] == 14:
        voin2 = "Кот в Сапогах"
    elif p2[2] == 15:
        voin2 = "Грозная Паймон"
    elif p2[2] == 16:
        voin2 = "Паймон"
    elif p2[2] == 17:
        voin2 = "Пепе Бандит"
    elif p2[2] == 18:
        voin2 = "Стальной Гром"
    elif p2[2] == 19:
        voin2 = "Аста"
    elif p2[2] == 20:
        voin2 = "Шрек"
    
        
    if p2[5] > 30:
        mmr = max(0, p1[5] + 30)
        mmr3 = max(0, p2[5] - 30)
    else:
        mmr = max(0, p1[5])
        mmr3 = max(0, p2[5])
            
    c.execute('UPDATE users SET money=?, exp=?, mmr=?, coin=?, play=? WHERE user_id=?',(wi1, up1, mmr, wincoin, pla1, opponent_id,))
    c.execute('UPDATE users SET mmr=?, play=?, lose=? WHERE user_id=?',(mmr3, pla2, lo2, user_id,))
    base.commit()
        
    await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{phot2}.png', 'rb'),
                              caption=f"<b>Вы сдались 💀\n\n🥷 Воин {voin2}\n🧩 Опыт +0\n💰 Золото +0\n\n-{30 if p2[5] >= 30 else 0} MMR</b>", parse_mode='html')
    await bot.send_photo(chat_id=opponent_id, photo=open(f'/bot/module-deda/bot{phot}.png', 'rb'),
                              caption=f"<b>Враг сдался 🎃\n\n🥷 Воин {voin}\n🧩 Опыт +{opyt1}\n💰 Золото +{win}\n💎 Коины +{coinwin}\n\n+{30 if p2[5] > 30 else 0} MMR</b>", parse_mode='html')
       
        
@dp.message_handler(commands=['start', 'play'])
async def start(msg):
    if msg.chat.type == "supergroup":
        return
    user_id = msg.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    user = c.fetchone()
    if user:
        await msg.answer('Жми <b>Играть</b> 🕹', parse_mode='html', reply_markup=menu)
        return
    
    if not user:
        ref = msg.get_args()
        if ref:
            low = InlineKeyboardMarkup()
            yes = InlineKeyboardButton(text='✔️ Подвердить', callback_data=f'confirm:{ref}')
            low.add(yes)
            c.execute(f'SELECT * FROM users WHERE user_id={ref}')
            minka = c.fetchone()
            if not minka:
                await msg.answer('❕ Произошла ошибка введите команду ручным вводом /start - или нажммте сюда.')
                return
            await msg.answer("<b>Подвердите что вы не робот! 🤖</b>", reply_markup=low)
        else:
            money = 5000
            voins = 1 
            play = 0
            exp = 500
            mmr = 0
            skam = 0
            voin1 = 550
            voin2 = 55
            voin3 = 1
            voin4 = 5
            voin5 = 1
            voin6 = 1
            nick = msg.from_user.first_name
            lose = 0
            coin = 0
            
            c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, money, voins, play, exp, mmr, skam, voin1, voin2, voin3, voin4, voin5, voin6, nick, lose, coin, None, None, None, 0, 0, 0, 1, 0))
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 1, 1, 550, 55, 1, 5, 1, 1, 0))
            base.commit()
            await msg.answer(f'<b>Добро пожаловать!</b>\nЗдесь ты можешь сражаться в поединках с другими игроками', reply_markup=menu, parse_mode='html')
            await msg.answer('Нажимай на кнопку Инфо ⚙️ если есть вопросы')
            await msg.answer('Жми Играть 🕹, чтобы найти врага!')
        

@dp.callback_query_handler(text='voinsbuy')
async def voin(call: types.CallbackQuery):
    c.execute("SELECT * FROM users WHERE user_id=?",(call.from_user.id,))
    user = c.fetchone()
    if not user:
        await call.answer("Перезапустите бота и попробуйте снова")
        return
    #
    c.execute("SELECT * FROM voin WHERE voin='1'")
    cur = c.fetchone() 
    voin = ""
    am = 0
    if cur[1] == 2:
        voin = "Пудж"
        am = 90000
        h = 600
        at = 90
        s = 5
        k = 10
        u = 15
        v = 5 
    elif cur[1] == 3:
        voin = "Король Варваров"
        am = 150000
        h = 1250
        at = 120
        s = 10
        k = 10
        u = 10
        v = 10
    elif cur[1] == 4:
        voin = "Гигачад"
        am = 200000
        h = 1500
        at = 500
        s = 15
        k = 20
        u = 20
        v = 15 
    elif cur[1] == 5:
        voin = "Танос"
        am = 2000000
        h = 6000
        at = 2250
        s = 80
        k = 90
        u = 45
        v = 80 
    elif cur[1] == 6:
        voin = "Стальной клык"
        am = 1200000
        h = 2500
        at = 1250
        s = 40
        k = 60
        u = 40
        v = 80 
    elif cur[1] == 7:
        voin = "Пепе Психопат"
        am = 400000
        h = 1250
        at = 500
        s = 25
        k = 50
        u = 30
        v = 60
    elif cur[1] == 8:
        voin = "Пепе Архимаг"
        am = 600000
        h = 3200
        at = 550
        s = 8
        k = 40
        u = 55
        v = 20
    elif cur[1] == 9:
        voin = "Пепе Маг"
        am = 200000
        h = 2000
        at = 280
        s = 10
        k = 60
        u = 35
        v = 40
    elif cur[1] == 10:
        voin = "Тень"
        am = 1000000
        h = 4500
        at = 1200
        s = 65
        k = 75
        u = 40
        v = 85
    elif cur[1] == 11:
        voin = "Шадоу Френд"
        am = 300000
        h = 2500
        at = 350
        s = 13
        k = 65
        u = 35
        v = 40
    elif cur[1] == 12:
        voin = "Слендермен"
        am = 1250000
        h = 6200
        at = 2250
        s = 80
        k = 80
        u = 65
        v = 90
    elif cur[1] == 13:
        voin = "Человек Паук"
        am = 1100000
        h = 5200
        at = 1350
        s = 80
        k = 70
        u = 70
        v = 80
    elif cur[1] == 14:
        voin = "Кот в Сапогах"
        am = 1560000
        h = 4200
        at = 2600
        s = 44
        k = 70
        u = 30
        v = 80
    elif cur[1] == 15:
        voin = "Грозная Паймон"
        am = 1420000
        h = 4200
        at = 2200
        s = 80
        k = 70
        u = 40
        v = 60
    elif cur[1] == 16:
        voin = "Паймон"
        am = 1200000
        h = 3200
        at = 1660
        s = 80
        v = 80
        u = 45
        k = 65
    elif cur[1] == 17:
        voin = "Пепе Бандит"
        am = 700000
        h = 3000
        at = 900
        s = 80
        u = 30
        k = 60
        v = 80
    elif cur[1] == 18:
        voin = "Стальной Гром"
        am = 4200000
        h = 9200
        at = 4200
        s = 80
        v = 80
        u = 45
        k = 80
    elif cur[1] == 19:
        voin = "Аста"
        am = 1900000
        h = 3400
        at = 1200
        k = 60
        u = 50
        v = 90
    elif cur[1] == 20:
        voin = "Шрек"
        am = 2200000
        h = 5600
        at = 2560
        k = 60
        s = 80
        u = 30
        v = 100
        #
    inline = InlineKeyboardMarkup(row_with=2)
    buy = InlineKeyboardButton(text='Купить 🥷', callback_data=f'pbuy:{cur[1]}')
    info = InlineKeyboardButton(text='Инфо ⚙️', callback_data=f'infor')
    inline.add(info, buy)
      
    await bot.send_photo(chat_id=call.from_user.id, photo=open(f'/bot/module-deda/bot{cur[1]}.png', 'rb'),
                              caption=f'<b>{voin} | {am} 💰\n\n❤️ Здоровье {h}\n🔫 Урон {at}\n🛡 Броня {s}\n💥 Шанс крита {k}%\n🦋 Уклонение {u}%\n🦇 Вампиризм {v}%</b>', reply_markup=inline, parse_mode='html')
 
@dp.callback_query_handler(text='infor')
async def cal(call):
    await call.answer('⚙️ Инфо: Рынок воинов обновляется каждые 40 минут', show_alert=True)

@dp.callback_query_handler(lambda call: call.data.startswith('confirm:'))
async def confirm(call):
    id = int(call.data.split(':')[1])
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    user = c.fetchone()
    
    if user:
        await call.message.edit_text('❕ Кнопка недействительна')
        return
    
    if not user:
        c.execute(f'SELECT * FROM users WHERE user_id={id}')
        up = c.fetchone()
        ref = up[6]
        ref += 1
        m = up[1]
        m += 100000
        money = 5000
        voins = 1 
        play = 0
        exp = 500
        mmr = 0
        skam = 0
        voin1 = 550
        voin2 = 55
        voin3 = 1
        voin4 = 5
        voin5 = 1
        voin6 = 1
        nick = call.from_user.first_name
        lose = 0
        coin = 0
        c.execute(f'UPDATE users SET money={m}, skam={ref} WHERE user_id={id}')
        c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, money, voins, play, exp, mmr, skam, voin1, voin2, voin3, voin4, voin5, voin6, nick, lose, coin, None, None, None, 0, 0, 0, 1, 0))
        c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 1, 1, 550, 55, 1, 5, 1, 1, 0))
        base.commit()
        await call.message.answer(f'<b>Добро пожаловать!</b>\nЗдесь ты можешь сражаться в поединках с другими игроками', reply_markup=menu, parse_mode='html')
        await call.message.answer('Нажимай на кнопку Инфо ⚙️ если есть вопросы')
        await call.message.answer('Жми Играть 🕹, чтобы найти врага!')
        await bot.send_message(id, f"<b>Вы заскамили {nick}</b>")
        await bot.send_message(id, f"<b>Награда за {ref} чел. получена!</b>")
    
@dp.callback_query_handler(lambda query: query.data.startswith('pbuy:'))
async def shop(query):
    user_id = query.from_user.id
    id = int(query.data.split(':')[1])
    c.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = c.fetchone()
    money = user[1]
    if id == 2:
        summ = 90000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 2, 0, 600, 90, 5, 10, 15, 5, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Пудж')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
    if id == 3:
        summ = 150000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 3, 0, 1250, 120, 10, 10, 10, 10, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Король Варваров')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
    
    if id == 4:
        summ = 200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 4, 0, 1500, 500, 15, 20, 20, 15, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Гигачад')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 5:
        summ = 2000000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 5, 0, 6000, 2250, 80, 90, 45, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Танос')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)

    if id == 6:
        summ = 1200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 6, 0, 2500, 1250, 40, 60, 40, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Стальной клык')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)

    if id == 7:
        summ = 400000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 7, 0, 1250, 500, 25, 50, 30, 60, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Пепе Психопат')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)

    if id == 8:
        summ = 600000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 8, 0, 3200, 550, 8, 40, 55, 20, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Пепе Архимаг')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
 
    if id == 9:
        summ = 200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 9, 0, 2000, 280, 10, 60, 35, 40, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Пепе Маг')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 10:
        summ = 1000000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 10, 0, 4500, 1200, 65, 75, 40, 85, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Тень')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 11:
        summ = 300000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 11, 0, 2500, 350, 13, 65, 35, 40, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Шадоу Френд')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 12:
        summ = 1200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 12, 0, 6200, 2250, 80, 80, 65, 90, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Слендермен')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 13:
        summ = 1100000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 13, 0, 5200, 1350, 80, 70, 70, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Человек Паук')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 14:
        summ = 1560000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 14, 0, 4200, 2605, 44, 70, 35, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Кот в Сапогах')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
    
    if id == 15:
        summ = 1420000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 15, 0, 4200, 2220, 80, 70, 40, 60, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Грозная Паймон')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 16:
        summ = 1200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 16, 0, 3200, 1660, 80, 65, 45, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Паймон')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
    
    if id == 17:
        summ = 700000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 17, 0, 3000, 900, 80, 60, 30, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Пепе Бандит')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
    
    if id == 18:
        summ = 4200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 18, 0, 9200, 4200, 80, 80, 45, 80, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Стальной Гром')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
        
    if id == 19:
        summ = 1900000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 19, 0, 3400, 1200, 80, 60, 50, 90, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Аста')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)
    
    if id == 20:
        summ = 2200000
        c.execute(f'SELECT * FROM voin WHERE voin="1" AND status={id}')
        st = c.fetchone()
        if not st:
            await query.answer('Кнопка устарела ❕')
            return
        
        c.execute(f'SELECT * FROM pers WHERE user_id={user_id} AND type={id}')
        cut = c.fetchone()
        if not cut:
            if money <  summ:
                await query.answer(f'Недостаточно еще {summ - money} 💰', show_alert=True)
                return
            c.execute(f'UPDATE users SET money={money - summ} WHERE user_id={user_id}')
            c.execute('INSERT INTO pers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(user_id, 20, 0, 5600, 2560, 80, 60, 30, 100, 0))
            base.commit()
            await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{id}.png', 'rb'),
                              caption='Новый воин! Шрек')
            return
        await query.answer('Данный воин уже есть ❕', show_alert=True)

    
@dp.callback_query_handler(text='vampir')
async def hp(call: types.CallbackQuery):
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    voin = cur[2]
    hp = int(cur[12])
    bal = cur[4]
    level = 1
    max_levels = {1: 80, 2: 80, 3: 80, 4: 80, 5: 80, 6: 85, 7: 80, 8: 80, 9: 80, 10: 80, 11: 80, 12: 90, 13: 80, 14: 80, 15: 80, 16: 80, 17: 80, 18: 80, 19: 80, 20: 80}
    
    if hp >= max_levels[voin]:
        await call.answer('Вы достигли макс. уровня 🦇')
        return

    resurs = hp * 20
    if bal < resurs:
        await call.answer(f'Недостаточно еще {resurs - bal} 🧩')
        return

    summ = int(bal - resurs)
    hpn = cur[12]
    newhp = int(hpn + 1)

    c.execute('UPDATE users SET exp =? WHERE user_id=?',(summ, user_id,))
    c.execute('UPDATE users SET voin6 =? WHERE user_id=?',(newhp, user_id,))
    base.commit()

    ## Обновление данных после изменения
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    attack = cur[8]
    shit = cur[9]
    krit = cur[10]
    uklon = cur[11]
    vampirism = cur[12]
    op = cur[4]
    chosen_voin = ""

    if cur[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif cur[2] == 2:
        chosen_voin = "Пудж"
    elif cur[2] == 3:
        chosen_voin = "Король Варваров"
    elif cur[2] == 4:
        chosen_voin = "Гигачад"
    elif cur[2] == 5:
        chosen_voin = "Танос"
    elif cur[2] == 6:
        chosen_voin = "Стальной клык"
    elif cur[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif cur[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif cur[2] == 9:
        chosen_voin = "Пепе Маг"
    elif cur[2] == 10:
        chosen_voin = "Тень"
    elif cur[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif cur[2] == 12:
        chosen_voin = "Слендермен"
    elif cur[2] == 13:
        chosen_voin = "Человек Паук"
    elif cur[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif cur[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif cur[2] == 16:
        chosen_voin = "Паймон"
    elif cur[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif cur[2] == 18:
        chosen_voin = "Стальной Гром"
    elif cur[2] == 19:
        chosen_voin = "Аста"
    elif cur[2] == 20:
        chosen_voin = "Шрек"

    await call.answer(f'Успешно! -{resurs} 🧩')

    hps = cur[7]
    await call.message.edit_caption(f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hps}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)
    return

@dp.callback_query_handler(text='uklon')
async def hp(call: types.CallbackQuery):
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    voin = cur[2]
    hp = int(cur[11])
    bal = cur[4]
    level = 1
    max_levels = {1: 30, 2: 30, 3: 30, 4: 40, 5: 40, 6: 60, 7: 45, 8: 50, 9: 40, 10: 45, 11: 35, 12: 55, 13: 65, 14: 35, 15: 40, 16: 45, 17: 30, 18: 45, 19: 50, 20: 30}
    
    if hp >= max_levels[voin]:
        await call.answer('Вы достигли макс. уровня 🦋')
        return

    resurs = hp * 20
    if bal < resurs:
        await call.answer(f'Недостаточно еще {resurs - bal} 🧩')
        return

    summ = int(bal - resurs)
    hpn = cur[11]
    newhp = int(hpn + 1)

    c.execute('UPDATE users SET exp =? WHERE user_id=?',(summ, user_id,))
    c.execute('UPDATE users SET voin5 =? WHERE user_id=?',(newhp, user_id,))
    base.commit()

    ## Обновление данных после изменения
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    attack = cur[8]
    shit = cur[9]
    krit = cur[10]
    uklon = cur[11]
    vampirism = cur[12]
    op = cur[4]
    chosen_voin = ""

    if cur[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif cur[2] == 2:
        chosen_voin = "Пудж"
    elif cur[2] == 3:
        chosen_voin = "Король Варваров"
    elif cur[2] == 4:
        chosen_voin = "Гигачад"
    elif cur[2] == 5:
        chosen_voin = "Танос"
    elif cur[2] == 6:
        chosen_voin = "Стальной клык"
    elif cur[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif cur[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif cur[2] == 9:
        chosen_voin = "Пепе Маг"
    elif cur[2] == 10:
        chosen_voin = "Тень"
    elif cur[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif cur[2] == 12:
        chosen_voin = "Слендермен"
    elif cur[2] == 13:
        chosen_voin = "Человек Паук"
    elif cur[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif cur[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif cur[2] == 16:
        chosen_voin = "Паймон"
    elif cur[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif cur[2] == 18:
        chosen_voin = "Стальной Гром"
    elif cur[2] == 19:
        chosen_voin = "Аста"
    elif cur[2] == 20:
        chosen_voin = "Шрек"

    await call.answer(f'Успешно! -{resurs} 🧩')

    hps = cur[7]
    await call.message.edit_caption(f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hps}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)
    return

@dp.callback_query_handler(text='krit')
async def hp(call):
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    hp = int(cur[10])
    bal = cur[4]
    voin = cur[2]
    level = 1
    max_levels = {1: 60, 2: 60, 3: 60, 4: 65, 5: 90, 6: 80, 7: 60, 8: 65, 9: 70, 10: 60, 11: 60, 12: 80, 13: 75, 14: 75, 15: 75, 16: 70, 17: 65, 18: 80, 19: 80, 20: 80}
    
    if hp >= max_levels[voin]:
        await call.answer('Вы достигли макс. уровня 💥')
        return
    
    resurs = hp * 20
    
    if bal < resurs:
        await call.answer(f'Недостаточно еще {resurs - bal} 🧩')
        return
    
    summ = int(bal - resurs)
    hpn = cur[10]
    newhp = int(hpn + 1)
    c.execute('UPDATE users SET exp =? WHERE user_id=?',(summ, user_id,))
    c.execute('UPDATE users SET voin4 =? WHERE user_id=?',(newhp, user_id,))
    base.commit()
    
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    attack = cur[8]
    shit = cur[9]
    krit = cur[10]
    uklon = cur[11]
    vampirism = cur[12]
    op = cur[4]
    chosen_voin = ""

    if cur[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif cur[2] == 2:
        chosen_voin = "Пудж"
    elif cur[2] == 3:
        chosen_voin = "Король Варваров"
    elif cur[2] == 4:
        chosen_voin = "Гигачад"
    elif cur[2] == 5:
        chosen_voin = "Танос"
    elif cur[2] == 6:
        chosen_voin = "Стальной клык"
    elif cur[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif cur[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif cur[2] == 9:
        chosen_voin = "Пепе Маг"
    elif cur[2] == 10:
        chosen_voin = "Тень"
    elif cur[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif cur[2] == 12:
        chosen_voin = "Слендермен"
    elif cur[2] == 13:
        chosen_voin = "Человек Паук"
    elif cur[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif cur[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif cur[2] == 16:
        chosen_voin = "Паймон"
    elif cur[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif cur[2] == 18:
        chosen_voin = "Стальной Гром"
    elif cur[2] == 19:
        chosen_voin = "Аста"
    elif cur[2] == 20:
        chosen_voin = "Шрек"
    
    await call.answer(f'Успешно! -{resurs} 🧩')
    
    
    hps = cur[7]
    await call.message.edit_caption(f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hps}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)
    return

@dp.callback_query_handler(text='shit')
async def hp(call):
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    hp = int(cur[9])
    bal = cur[4]
    level = 1
    voin = cur[2]
    max_levels = {1: 80, 2: 80, 3: 80, 4: 80, 5: 80, 6: 80, 7: 80, 8: 80, 9: 80, 10: 80, 11: 80, 12: 80, 13: 80, 14: 80, 15: 80, 16: 80, 17: 80, 18: 80, 19: 80, 20: 80}
    
    if hp >= max_levels[voin]:
        await call.answer('Вы достигли макс. уровня 🛡')
        return
    
    resurs = hp * 20
    if bal < resurs:
        await call.answer(f'Недостаточно еще {resurs - bal} 🧩')
        return
    
    summ = int(bal - resurs)
    hpn = cur[9]
    newhp = int(hpn + 1)
    
    c.execute('UPDATE users SET exp =? WHERE user_id=?',(summ, user_id,))
    c.execute('UPDATE users SET voin3 =? WHERE user_id=?',(newhp, user_id,))
    base.commit()
    
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    attack = cur[8]
    shit = cur[9]
    krit = cur[10]
    uklon = cur[11]
    vampirism = cur[12]
    op = cur[4]
    chosen_voin = ""

    if cur[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif cur[2] == 2:
        chosen_voin = "Пудж"
    elif cur[2] == 3:
        chosen_voin = "Король Варваров"
    elif cur[2] == 4:
        chosen_voin = "Гигачад"
    elif cur[2] == 5:
        chosen_voin = "Танос"
    elif cur[2] == 6:
        chosen_voin = "Стальной клык"
    elif cur[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif cur[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif cur[2] == 9:
        chosen_voin = "Пепе Маг"
    elif cur[2] == 10:
        chosen_voin = "Тень"
    elif cur[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif cur[2] == 12:
        chosen_voin = "Слендермен"
    elif cur[2] == 13:
        chosen_voin = "Человек Паук"
    elif cur[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif cur[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif cur[2] == 16:
        chosen_voin = "Паймон"
    elif cur[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif cur[2] == 18:
        chosen_voin = "Стальной Гром"
    elif cur[2] == 19:
        chosen_voin = "Аста"
    elif cur[2] == 20:
        chosen_voin = "Шрек"
    
    await call.answer(f'Успешно! -{resurs} 🧩')
    
    hps = cur[7]
    await call.message.edit_caption(f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hps}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)
    return

@dp.callback_query_handler(text='attack')
async def hp(call):
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    hp = int(cur[8] // 1.5)
    bal = cur[4]
    level = 5
    resurs = 0
    
    for i in range(int(hp) - int(level)):
        resurs += int((int(hp) + i + 1) ** 0.25)
        
    if bal < resurs:
        await call.answer(f'Недостаточно еще {resurs - bal} 🧩')
        return
    
    summ = int(bal - resurs)
    hpn = cur[8]
    newhp = int(hpn + 5)
    
    c.execute('UPDATE users SET exp =? WHERE user_id=?',(summ, user_id,))
    c.execute('UPDATE users SET voin2 =? WHERE user_id=?',(newhp, user_id,))
    base.commit()
    
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    attack = cur[8]
    shit = cur[9]
    krit = cur[10]
    uklon = cur[11]
    vampirism = cur[12]
    op = cur[4]
    chosen_voin = ""

    if cur[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif cur[2] == 2:
        chosen_voin = "Пудж"
    elif cur[2] == 3:
        chosen_voin = "Король Варваров"
    elif cur[2] == 4:
        chosen_voin = "Гигачад"
    elif cur[2] == 5:
        chosen_voin = "Танос"
    elif cur[2] == 6:
        chosen_voin = "Стальной клык"
    elif cur[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif cur[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif cur[2] == 9:
        chosen_voin = "Пепе Маг"
    elif cur[2] == 10:
        chosen_voin = "Тень"
    elif cur[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif cur[2] == 12:
        chosen_voin = "Слендермен"
    elif cur[2] == 13:
        chosen_voin = "Человек Паук"
    elif cur[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif cur[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif cur[2] == 16:
        chosen_voin = "Паймон"
    elif cur[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif cur[2] == 18:
        chosen_voin = "Стальной Гром"
    elif cur[2] == 19:
        chosen_voin = "Аста"
    elif cur[2] == 20:
        chosen_voin = "Шрек"
    
    await call.answer(f'Успешно! -{resurs} 🧩')
    
    hps = cur[7]
    await call.message.edit_caption(f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hps}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)
    return resurs

@dp.callback_query_handler(text='hp')
async def hp(call):
    user_id = call.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    hp = int(cur[7] // 10)
    bal = cur[4]
    level = 50
    resurs = 0
    
    for i in range(int(hp) - int(level)):
        resurs += int((int(hp) + i + 1) ** 0.25)
        
    if bal < resurs:
        await call.answer(f'Недостаточно еще {resurs - bal} 🧩')
        return
    
    summ = int(bal - resurs)
    hpn = cur[7]
    newhp = int(hpn + 50)
    
    c.execute('UPDATE users SET exp =? WHERE user_id=?',(summ, user_id,))
    c.execute('UPDATE users SET voin1 =? WHERE user_id=?',(newhp, user_id,))
    base.commit()
    
    c.execute('SELECT * FROM users WHERE user_id=?',(user_id,))
    cur = c.fetchone()
    
    attack = cur[8]
    shit = cur[9]
    krit = cur[10]
    uklon = cur[11]
    vampirism = cur[12]
    op = cur[4]
    chosen_voin = ""

    if cur[2] == 1:
        chosen_voin = "Чмоня Гатс"
    elif cur[2] == 2:
        chosen_voin = "Пудж"
    elif cur[2] == 3:
        chosen_voin = "Король Варваров"
    elif cur[2] == 4:
        chosen_voin = "Гигачад"
    elif cur[2] == 5:
        chosen_voin = "Танос"
    elif cur[2] == 6:
        chosen_voin = "Стальной клык"
    elif cur[2] == 7:
        chosen_voin = "Пепе Психопат"
    elif cur[2] == 8:
        chosen_voin = "Пепе Архимаг"
    elif cur[2] == 9:
        chosen_voin = "Пепе Маг"
    elif cur[2] == 10:
        chosen_voin = "Тень"
    elif cur[2] == 11:
        chosen_voin = "Шадоу Френд"
    elif cur[2] == 12:
        chosen_voin = "Слендермен"
    elif cur[2] == 13:
        chosen_voin = "Человек Паук"
    elif cur[2] == 14:
        chosen_voin = "Кот в Сапогах"
    elif cur[2] == 15:
        chosen_voin = "Грозная Паймон"
    elif cur[2] == 16:
        chosen_voin = "Паймон"
    elif cur[2] == 17:
        chosen_voin = "Пепе Бандит"
    elif cur[2] == 18:
        chosen_voin = "Стальной Гром"
    elif cur[2] == 19:
        chosen_voin = "Аста"
    elif cur[2] == 20:
        chosen_voin = "Шрек"
    
    await call.answer(f'Успешно! -{resurs} 🧩')
    
    hps = cur[7]
    mmr = cur[18]
    await call.message.edit_caption(f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hps}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%</b>', reply_markup=ups)
    return

@dp.callback_query_handler(text='atr')
async def atr(call):
    await call.message.edit_text('Информация ⚙️\n\n▫️ Здоровье ❤️\nпри прокачке прибаляется 50 единиц, макс. значение не ограничено\n\n▫️ Урон 🔫\nпри прокачке прибавляется 5 единиц, макс. значение не ограничено\n\n▫️ Броня 🛡\nпри прокачке прибалется 1 единица, чем больше новых единиц брони тем меньше она блокирует урон, к примеру 20 брони блокируют 50 процентов урона, а 60 только 75%, макс. значение 80, но у некоторых воинов может быть выше\n\n▫️ Шанс крита 💥\nпри прокачке прибаляется 1 процент, если критический урон проходит, то он умножает ваш урон на случайное число от 1 до 5, макс. значение 60, но у некоторых воинов может быть выше\n\n▫️ Уклонение 🦋\nпри прокачке прибавляется 1 процент, если шанс прокает, то враг не нанесёт урон вашему воину, макс. значение 30, но у некоторых воинов может быть выше\n\n▫️ Вампиризм 🦇\nпри прокачке прибавляется 1 процент, при атаке процент от нанесённого урона превращается в Здоровье, макс. значение 80, но у некоторых воинов может быть выше')

@dp.callback_query_handler(text='give')
async def give(call):
    user_id = call.from_user.id
    await bot.send_message(user_id, f"{user_id}")
    await bot.send_message(user_id, f"Вот ваш айди, по которому вам можно отправить золото, скопируйте и отправьте его")

@dp.callback_query_handler(text='giveaway')
async def pay_callback_handler(query: types.CallbackQuery, state: FSMContext):
    await query.answer()

    user_id = query.from_user.id
    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = c.fetchone()
    if not user:
        await query.message.answer('❗ Произошла ошибка введите команду /start и попробуйте снова.')
        return

    await query.message.answer('Введите айди на который нужно отправить золото, '
                               'айди можно узнать нажав на кнопку Получить 💰')
    await GiveState.dialog.set()

@dp.message_handler(state=GiveState.dialog)
async def process_user_id(message: types.Message, state: FSMContext):
    global user2
    user2 = message.text
    c.execute('SELECT * FROM users WHERE user_id=?', (user2,))
    user = c.fetchone()
    if not user:
        await message.answer('<b>Перевод отменен, айди не найден!</b>', parse_mode='html')
        await state.finish()
        return
    user_id = message.from_user.id
    if int(message.text) == user_id:
        await message.answer('<b>Перевод отменен, нельзя перевести самому себе!</b>', parse_mode='html')
        await state.finish()
        return 

    await message.answer('<b>Айди найден!</b>\nВведите количество золота которое хотите отдать:', parse_mode='html')
    await GiveState.dialog2.set()

@dp.message_handler(state=GiveState.dialog2)
async def process_amount(message: types.Message, state: FSMContext):
    use = message.from_user.id
    try:
        c.execute('SELECT * FROM users WHERE user_id=?',(use,))
        us = c.fetchone()
        money = us[1]
        amount = int(message.text)
    except ValueError:
        await message.answer('<b>💰 Сумма введена неверна, перевод отменëн.</b>', parse_mode='html')
        await state.finish()
        return
    if amount <= 0:
        await message.answer('<b>💰 Сумма введена неверна, перевод отменëн.</b>', parse_mode='html')
        await state.finish()
        return
    if money < amount:
        await message.answer('💰 Перевод отменëн, недостаточно золота!')
        await state.finish()
        return
    global user2
    c.execute('SELECT * FROM users WHERE user_id =?',(user2,))
    unicod = c.fetchone()
    money2 = unicod[1]
    summ2 = money2 + amount
    summ = money - amount
    
    c.execute('UPDATE users SET money =? WHERE user_id=?',(summ, use,))
    c.execute('UPDATE users SET money =? WHERE user_id=?',(summ2, user2,))
    base.commit()

    await message.answer(f'<b>Успешно!</b>\n-{amount} 💰', parse_mode='html')
    await state.finish()
    await bot.send_message(user2, f" Вам отправили {amount} 💰")

# mines    

def get_new_field():
    field = [[HIDDEN] * COLS for _ in range(ROWS)]
    mines_positions = random.sample([(i,j) for i in range(ROWS) for j in range(COLS)], MINES)
    return (field, mines_positions)

def render_field(field):
    game_field = InlineKeyboardMarkup()
    for i, row in enumerate(field):
        game_field.row(*[InlineKeyboardButton(text=cell, callback_data=f'{i}_{j}') for j, cell in enumerate(row)])
    return game_field

@dp.message_handler(lambda message: message.text == 'Мины 🎲')
async def casino(message: types.Message):
    if message.chat.type == "supergroup":
        return
    user_id = message.from_user.id
    if user_id in game_data:
        await message.answer('<b>🎲 Сначала закончите игру «Мины»</b>')
        return
    if user_id in user_games:
        ('<b>🎲 Сначала закончите игру «ДжекФрукт»</b>')
        return
    keyboard = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(text=f'{amount} 💰', callback_data=f'amnt_{amount}') for amount in CASINO_OPTIONS]
    keyboard.add(*buttons)
    await message.answer('Выберите ставку 💰:', reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data.split('_')[0] == 'amnt')
async def bet(call: types.CallbackQuery):
    user_id = call.from_user.id
    c.execute('SELECT money FROM users WHERE user_id=?', (user_id,))
    user_money = c.fetchone()[0]
    bet_amount = int(call.data.split('_')[1])
    if user_id in game_data:
        await message.answer('<b>🎲 Сначала закончите игру «Мины»</b>')
        return
    if user_id in user_games:
        ('<b>🎲 Сначала закончите игру «ДжекФрукт»</b>')
        return
    if bet_amount > user_money:
        await call.answer(f"Недостаточно еще {bet_amount - user_money} 💰", show_alert=True)
    else:
        c.execute('UPDATE users SET money = money - ? WHERE user_id = ?', (bet_amount, user_id,))
        base.commit()
        game_field, mines_positions = get_new_field()
        game_data[user_id] = {'field': game_field, 'mines': mines_positions, 'bet': bet_amount, 'hits': 0, 'last_click': None}
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(user_id, '<b>Нажимай на минное поле!</b>', reply_markup=render_field(game_data[user_id]['field']), parse_mode='html')

#callback_query_handle

@dp.callback_query_handler(lambda c: c.data.startswith('prdnext_'))
async def prdnext_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data.split('_')
    page = int(data[1])
    id = int(data[2])
    if user_id != id:
        await callback_query.answer('❗ Это не твоя кнопка!')
        return

    c.execute('SELECT * FROM prd WHERE user_id=?', (user_id,))
    fighters = c.fetchall()

    change_kb = InlineKeyboardMarkup()

    fighters = sorted(fighters, key=lambda x: x[2], reverse=True)
    row = []
    start = (page - 1) * 12
    end = start + 12
    for fighter in fighters[start:end]:
        fighter_id = fighter[1]
        reg = fighter[2]

        name = get_prds(fighter_id)
        redk = get_redk(reg)
        if fighter[3] != 0:
                fighter_name = f"🖐{name}{redk}"
        else:
            fighter_name = f"{name}{redk}"

        button = InlineKeyboardButton(text=fighter_name, callback_data=f'prd_{fighter_id}_{fighter[4]}_{reg}_{page}_{user_id}')
        row.append(button)

        if len(row) == 3:
            change_kb.row(*row)
            row = []

    if row:
        change_kb.row(*row)

    total_pages = (len(fighters) + 11) // 12
    if len(fighters) > 12:
        if page > 1:
            change_kb.row(
                InlineKeyboardButton(text="Назад", callback_data=f'prdprev_{page-1}_{user_id}'),
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_{page}_{user_id}'),
                InlineKeyboardButton(text="Вперед", callback_data=f'prdnext_{"1" if page >= total_pages else page+1}_{user_id}')
            )
        else:
            change_kb.row(
                InlineKeyboardButton(text="Назад", callback_data=f'prdprev_{total_pages}_{user_id}'),
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_{page}_{user_id}'),
                InlineKeyboardButton(text="Вперед", callback_data=f'prdnext_2_{user_id}')
            )
    else:
        change_kb.row(InlineKeyboardButton(text="Слоты", callback_data=f'slots_{page}_{user_id}'))

    await callback_query.message.edit_text('<b>Твои предметы ❕</b>', reply_markup=change_kb, parse_mode='html')

@dp.callback_query_handler(lambda c: c.data.startswith('prdprev_'))
async def prdprev_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data.split('_')
    page = int(data[1])
    id = int(data[2])
    if user_id != id:
        await callback_query.answer('❗ Это не твоя кнопка!')
        return

    c.execute('SELECT * FROM prd WHERE user_id=?', (user_id,))
    fighters = c.fetchall()

    change_kb = InlineKeyboardMarkup()

    fighters = sorted(fighters, key=lambda x: x[2], reverse=True)
    row = []
    start = (page - 1) * 12
    end = start + 12
    for fighter in fighters[start:end]:
        fighter_id = fighter[1]
        reg = fighter[2]

        name = get_prds(fighter_id)
        redk = get_redk(reg)
        if fighter[3] != 0:
                fighter_name = f"🖐{name}{redk}"
        else:
            fighter_name = f"{name}{redk}"

        button = InlineKeyboardButton(text=fighter_name, callback_data=f'prd_{fighter_id}_{fighter[4]}_{reg}_{page}_{user_id}')
        row.append(button)

        if len(row) == 3:
            change_kb.row(*row)
            row = []

    if row:
        change_kb.row(*row)

    total_pages = (len(fighters) + 11) // 12
    if len(fighters) > 12:
        if page > 1:
            change_kb.row(
                InlineKeyboardButton(text="Назад", callback_data=f'prdprev_{page-1}_{user_id}'),
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_{page}_{user_id}'),
                InlineKeyboardButton(text="Вперед", callback_data=f'prdnext_{"1" if page >= total_pages else page+1}_{user_id}')
            )
        else:
            change_kb.row(
                InlineKeyboardButton(text="Назад", callback_data=f'prdprev_{total_pages}_{user_id}'),
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_{page}_{user_id}'),
                InlineKeyboardButton(text="Вперед", callback_data=f'prdnext_{page+1}_{user_id}')
            )
    else:
        change_kb.row(InlineKeyboardButton(text="Слоты", callback_data=f'slots_{page}_{user_id}'))

    await callback_query.message.edit_text('<b>Твои предметы ❕</b>', reply_markup=change_kb, parse_mode='html')

@dp.callback_query_handler(lambda call: call.data.split('_')[0] not in 'amnt')
async def casino(call: types.CallbackQuery):
    user_id = call.from_user.id
    if user_id not in game_data:
        await call.message.edit_text('<b>Кнопка недействительна ❕</b>', parse_mode='html')
        return

    row, col = map(int, call.data.split('_'))

    last_click = game_data[user_id].get('last_click', None)
    if last_click:
        l_row, l_col = last_click
        game_data[user_id]['field'][l_row][l_col] = HIDDEN

    if (row, col) == last_click:
        return
    else:
        game_data[user_id]['last_click'] = (row, col)
        game_field, mines_positions = get_new_field() 
        game_data[user_id]['field'] = game_field
        game_data[user_id]['mines'] = mines_positions
        if (row, col) in game_data[user_id]['mines']:
            reward = int(0.50* game_data[user_id]['bet'] * game_data[user_id]['hits'])
            c.execute('UPDATE users SET money = money + ? WHERE user_id = ?', (reward, user_id,))
            base.commit()
            await call.message.edit_text(f"<b>Вы подорвались</b> 💥\nПопаданий: {game_data[user_id]['hits']}\n\n+{reward} 💰", parse_mode='html')
            del game_data[user_id]  
        else:
            game_data[user_id]['field'][row][col] = SAFE 
            game_data[user_id]['hits'] += 1
            await call.message.edit_text(f'<b>Нажимай на минное поле!</b>\nПопаданий: {game_data[user_id]["hits"]}', reply_markup=render_field(game_data[user_id]['field']), parse_mode='html')


@dp.message_handler(content_types=['text'])
async def text(msg):
    m = msg.text.lower()
    if m == "Витрина ❄":
        user_id = msg.from_user.id
        if msg.chat.type == "supergroup":
            return
        c.execute('SELECT * FROM users WHERE user_id =?',(user_id,))
        user = c.fetchone()
        if not user:
            await msg.answer('❗ Произошла ошибка введите команду /start и попробуйте снова.')
            return
        await msg.answer()
        
        
    if m == 'профиль 🖼':
        user_id = msg.from_user.id
        name = msg.from_user.first_name
        if msg.chat.type == "supergroup":
            return
        c.execute('SELECT * FROM users WHERE user_id =?',(user_id,))
        user = c.fetchone()
        if not user:
            await msg.answer('❗ Произошла ошибка введите команду /start и попробуйте снова.')
            return
        c.execute("SELECT * FROM users ORDER BY mmr DESC LIMIT 30")
        users = c.fetchall()
        money = user[1]
        c.execute(f'SELECT COUNT(*) FROM pers WHERE user_id={user_id}')
        voins = c.fetchone()[0]
        play = user[3]
        exp = user[4]
        mmr = user[5]
        skam = user[6]
        lose = user[14]
        coin = user[15]
        wins = play - lose
        
        if play != 0:
            win = (wins / play) * 100
        else:
            win = 0
        
        stats = (
            f'{name}\n\n'
            f'🔰 {get_user_place(user_id, users)} ранг\n'
            f'🏆 {mmr} MMR\n\n'
            f'🔷 Сыграно боев: {play}\n'
            f'🔶 Доля побед: {win:.1f}%\n\n'
            f'🥷 Воины {voins} / 20\n'
            f'💰 Золото {money}\n'
            f'💎 Коины: {coin} шт.\n'
            f'🧩 Опыт {exp}\n\n'
            f'🧑‍💻 Заскамлено людей {skam}'
            )
            
        await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/profile.png', 'rb'),
                              caption=stats, parse_mode='html', reply_markup=pay)
    if m == "инфо ⚙️":
        user_id = msg.from_user.id
        name = msg.from_user.first_name
        if msg.chat.type == "supergroup":
            return 
        await msg.answer('<b>Информация</b> ⚙️\n\n▫️ <b>Играть</b> 🕹\nТут враги подбираются по твоему значению рейтинга MMR.\n\n▫️ <b>Дуэль</b> ⚔️\nВы можете позвать в бой с собой любого человека или друга.\n\n▫️ <b>Воины</b> 🥷\nВы можете выбрать любого воина, который у вас есть и прокачивать его атрибуты.\n\n▫️ <b>Атрибуты 🪖</b>\nВключают в себя Здоровье, урон, броню, шанс крита, уклонение, вампиризм. Узнать больше о них можно в кнопке ниже.', parse_mode='html', reply_markup=info)
    if m == "воины 🥷":
        user_id = msg.from_user.id
        if msg.chat.type == "supergroup":
            return
        c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
        user = c.fetchone()
        hp = user[7]
        attack = user[8]
        shit = user[9]
        krit = user[10]
        phot = user[2]
        uklon = user[11]
        vampirism = user[12]
        op = user[4]
        chosen_voin = ""
        if user[2] == 1:
            chosen_voin = "Чмоня Гатс"
        elif user[2] == 2:
            chosen_voin = "Пудж"
        elif user[2] == 3:
            chosen_voin = "Король Варваров"
        elif user[2] == 4:
            chosen_voin = "Гигачад"
        elif user[2] == 5:
            chosen_voin = "Танос"
        elif user[2] == 6:
            chosen_voin = "Стальной клык"
        elif user[2] == 7:
            chosen_voin = "Пепе Психопат"
        elif user[2] == 8:
            chosen_voin = "Пепе Архимаг"
        elif user[2] == 9:
            chosen_voin = "Пепе Маг"
        elif user[2] == 10:
            chosen_voin = "Тень"
        elif user[2] == 11:
            chosen_voin = "Шадоу Френд"
        elif user[2] == 12:
            chosen_voin = "Слендермен"
        elif user[2] == 13:
            chosen_voin = "Человек Паук"
        elif user[2] == 14:
            chosen_voin = "Кот в Сапогах"
        elif user[2] == 15:
            chosen_voin = "Грозная Паймон"
        elif user[2] == 16:
            chosen_voin = "Паймон"
        elif user[2] == 17:
            chosen_voin = "Пепе Бандит"
        elif user[2] == 18:
            chosen_voin = "Стальной Гром"
        elif user[2] == 19:
            chosen_voin = "Аста"
        elif user[2] == 20:
            chosen_voin = "Шрек"
        

        await bot.send_photo(chat_id=user_id, photo=open(f'/bot/module-deda/bot{phot}.png', 'rb'),
                              caption=f'<b>{chosen_voin} | 🧩 Опыт {op}\n\n❤️ Здоровье {hp}\n🔫 Урон {attack}\n🛡 Броня {shit}\n💥 Шанс крита {krit}%\n🦋 Уклонение {uklon}%\n🦇 Вампиризм {vampirism}%\n</b>',
                                reply_markup=ups)
    
    if m == "скам 💸":
        if msg.chat.type == "supergroup":
            return
        id = msg.from_user.id
        keb = InlineKeyboardMarkup()
        ik = InlineKeyboardButton(text='👨‍💻 Топ скамеров', callback_data='topref')
        keb.add(ik)
        await bot.send_photo(chat_id=id, photo=open(f'/bot/module-deda/skam.png', 'rb'),
                              caption=f'<b>Если по вашей ссылке зайдет человек, который не использовал бота, то вы получите награды!\n\n🟢 Cсылка -</b> <code>https://t.me/c3rfbbot?start={id}</code>\n\n💰 <b>За каждого человека вы будете получать по 100k золота.</b>', reply_markup=keb)
        return
    #
    if m == "рынок ⛩️":
        if msg.chat.type == 'supergroup':
            return
        user_id = msg.from_user.id
        await msg.answer('<b>Рынок ⛩</b>', parse_mode='html', reply_markup=place)
    if m == ".ид":
        if msg.reply_to_message:
            id = msg.reply_to_message.from_user.id
            await msg.reply(f'<b>🆔 Ид пользователя:</b> <code>{id}</code>')
            return
        else:
            id = msg.from_user.id
            await msg.reply(f'<b>🆔 Ваш ид:</b> <code>{id}</code>')
            return
    if m == "казино 🎲":
        if msg.chat.type == "supergroup":
            return
        await msg.answer('<b>Казино 🎲</b>:', reply_markup=men2)
    
    if m == "назад 🔙":
        if msg.chat.type == 'supergroup':
            return
        await msg.answer('<b>🕹 Меню:</b>', reply_markup=menu)
        
    if m == "прд":
        user_id = msg.from_user.id
        c.execute('SELECT * FROM prd WHERE user_id=?', (user_id,))
        fighters = c.fetchall()

        change_kb = InlineKeyboardMarkup()

        fighters = sorted(fighters, key=lambda x: x[2], reverse=True)
        row = []
        for fighter in fighters[:12]:
            fighter_id = fighter[1]
            reg = fighter[2]

            name = get_prds(fighter_id)
            redk = get_redk(reg)
            if fighter[3] != 0:
                fighter_name = f"🖐{name}{redk}"
            else:
                fighter_name = f"{name}{redk}"
                
            button = InlineKeyboardButton(text=fighter_name, callback_data=f'prd_{fighter_id}_{fighter[4]}_{reg}_1_{user_id}')
            row.append(button)

            if len(row) == 3:
                change_kb.row(*row)
                row = []

        if row:
            change_kb.row(*row)

        total_pages = (len(fighters) + 11) // 12
        if len(fighters) > 12:
            change_kb.row(
                InlineKeyboardButton(text="Назад", callback_data=f'prdprev_{total_pages}_{user_id}'),
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_1_{user_id}'),
                InlineKeyboardButton(text="Вперед", callback_data=f'prdnext_2_{user_id}')
            )
        else:
            change_kb.row(
                InlineKeyboardButton(text="Слоты", callback_data=f'slots_1_{user_id}')
                )

        await msg.reply('<b>Твои предметы ❕</b>', reply_markup=change_kb, parse_mode='html')
        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
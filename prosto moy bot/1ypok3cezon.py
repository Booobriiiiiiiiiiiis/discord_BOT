#ypok3cezon
#MTE0MDk4NjA5MzQ3MTI3Mjk4MA.Gej1CN.vzjrDC5rw_ckA4z2IpEEADdPxEV-cFjQ1LeNhk
import json
import string
import sqlite3
import discord
from discord.ext import commands
import os
bot = commands.Bot(command_prefix = '/', intents = discord.Intents.all())
@bot.event
async def on_member_join(member):
    await member.send('приветствую вас на сервере')
    talk = discord.utils.get(member.guild.roles, name='talk')
    no_talk = discord.utils.get(member.guild.roles, name='no talk')
    base.execute(f'CREATE TABLE IF NOT EXISTS "{member.guild.name}"(user_id INT, count INT, mute INT)')
    Mute = cur.execute(f'SELECT * FROM "{member.guild.name}" WHERE user_id == ?', (member.id, )).fetchone()
    if Mute == None:
        cur.execute(f'INSERT INTO "{member.guild.name}" VALUES(?, ?, ?)', (member.id, 0, 0))
        base.commit()
        await member.add_roles(talk)
    elif Mute [2] == 0:
        await member.add_roles(talk)
    else:
        await member.add_roles(no_talk)
    await member.add_roles(talk)
    for Mr_beast in bot.get_guild(member.guild.id).channels:
        if Mr_beast.name == 'основной':
            await bot.get_channel(Mr_beast.id).send(f'приветствуем {member} на нашем сервере ')
@bot.event
async def on_member_remove(member):
    for Mr_beast in bot.get_guild(member.guild.id).channels:
        if Mr_beast.name == 'основной':
            await bot.get_channel(Mr_beast.id).send(f'Пользователь  {member} покинул сервер пока :("очень жалко то что Мистор Бист сбросит на него 250000 тонн тротила со словами "Я сброшу на вас 250000 тонн тротила"":(')
@bot.event
async def on_ready():
    print('я на старте')
    global base, cur
    base = sqlite3.connect('data.db')
    cur = base.cursor()
    if base:
        print('База готова')
    else:
        print('стоп ошибка стоп 0000000000')

@bot.event
async def on_message(message):
    if {in_message_content_split.lower().translate(str.maketrans('', '', string.punctuation)) for in_message_content_split in message.content.split(' ')}.intersection(set(json.load(open('`.json')))) != set():
        await message.channel.send(f'ай-ай-ай {message.author.mention} так писать нельзя"cfgj;ybr" ещё раз так напишешь то я тебя по айпи вычеслю и скажу Мистору Бисту и он сбросит на тебя 250000 тонн тротила со словами "Я сброшу на вас 250000 тонн тротила"')
        await message.delete()
        mess = message.guild.name
        base.execute('CREATE TABLE IF NOT EXISTS Tablitsa_s_PREDUPREZHDENIYAMI(user_id INT, count INT)')
        base.commit()
        peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy = cur.execute('SELECT * FROM Tablitsa_s_PREDUPREZHDENIYAMI WHERE user_id == ?', (message.author.id, )).fetchone()
        if peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy == None:
            cur.execute('INSERT INTO Tablitsa_s_PREDUPREZHDENIYAMI VALUES(?, ?)', (message.author.id, 1))
            base.commit()
            await message.channel.send(f'{message.author.mention} у тебя первое предупреждение')
        elif peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy[1] == 1:
            cur.execute('UPDATE Tablitsa_s_PREDUPREZHDENIYAMI SET count == ? WHERE user_id == ?', (2, message.author.id ))
            base.commit()
            await message.channel.send(f'{message.author.mention} у тебя второе предупреждение')
        elif peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy[1] >= 2:
            cur.execute('UPDATE Tablitsa_s_PREDUPREZHDENIYAMI SET count == ? WHERE user_id == ?', (3, message.author.id ))
            base.commit()
            await message.channel.send(f'{message.author.mention} получает бан и на него летят 250000 тонн тротила от мистора Биста')
            await message.author.ban(reason='cfgj;ybr А теперь расшифруй что написано')
    if 'mr_beast' in message.content.lower():
        await message.channel.send('Я сброшу на вас 250000 тонн тротила')
    if 'сколько у меня предупреждений' in message.content.lower():
        base.execute('CREATE TABLE IF NOT EXISTS Tablitsa_s_PREDUPREZHDENIYAMI(user_id INT, count INT)')
        base.commit()
        peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy = cur.execute('SELECT * FROM Tablitsa_s_PREDUPREZHDENIYAMI WHERE user_id == ?', (message.author.id,)).fetchone()
        if peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy == None:
            await message.author.send('У вас нет предупреждений')
        else:
            await message.author.send(f'у вас {peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy[1]} предупреждение(ия)')

    await bot.process_commands(message)
#@bot.event
#async def on_message(message):
#    if 'Mauster_Beast' in message.content.lower():
#        await message.channel.send('Я сброшу на вас 250000 тонн тротила')
@bot.command()
@commands.has_permissions(manage_messages=True)
async def no_Talk(ctx, member:discord.Member):
    no_talk = discord.utils.get(member.guild.roles, name='no talk')
    talk = discord.utils.get(member.guild.roles, name='talk')
    await member.add_roles(no_talk)
    await member.remove_roles(talk)
    cur.execute(f'UPDATE "{member.guild.name}" SET mute == ? WHERE user_id == ?', (1, member.id))
    base.commit()
    await member.send('вы потеряли дар речи за плохое поведение посидите и подумайте над своим повидением')
    await ctx.send(f'{member.mention} потерял дар речи за плохое поведение пусть посидит и подумает над своим поведением')
@bot.command()
@commands.has_permissions(manage_messages=True)
async def noyes_Talk(ctx, member:discord.Member):
    talk = discord.utils.get(member.guild.roles, name='talk')
    no_talk = discord.utils.get(member.guild.roles, name='no talk')
    await member.add_roles(talk)
    await member.remove_roles(no_talk)
    await member.send('вы вернули дар речи за хорошее поведение')
    await ctx.send(f'{member.mention} вернул дар речи за хорошее поведение')
@bot.command()
async def proverka_statusa(ctx, member:discord.Member):
    base.execute('CREATE TABLE IF NOT EXISTS Tablitsa_s_PREDUPREZHDENIYAMI(user_id INT, count INT)')
    base.commit()
    peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy = cur.execute('SELECT * FROM Tablitsa_s_PREDUPREZHDENIYAMI WHERE user_id == ?', (member.id,)).fetchone()
    if peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy == None:
        await ctx.author.send('У пользователеля введённого вами нет предупреждений')
    else:
       await ctx.autor.send(f'У пользователеля введённого вами {peremennaya_kotoroya_budet_proveryat_kolichestvo_preduprezhdeniy[1]} предупреждение(ия)')
@bot.command()
async def send_bot(ctx, member:discord.Member):
    await member.send(f'{member.name} пhиdеn')
@bot.command()
async def delete2(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
@bot.command()
async def ne_laaadnooo(ctx):
    await ctx.send('ладно')
@bot.command()
async def comanda1(ctx, *, arg):
    await ctx.send(arg)
@bot.command()
async def comanda2(ctx, arg=None):
    await ctx.send(f'{ctx.message.author}')
bot.run('MTE0MDk4NjA5MzQ3MTI3Mjk4MA.G4HNfV.rSNW78qQBL3jDOM-PRrKrRowClCFGqj5p6WX6w')










    











































































































































































































































































































































































































































































































































































































































































































































































































































































































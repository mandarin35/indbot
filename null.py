import discord
import random
import os
import asyncio
import time
import requests
from discord.ext import commands
from discord.utils import get

# settings
PREFIX = '/'
client = commands.Bot(command_prefix = PREFIX, intents = discord.Intents.all())

client.remove_command('help')

@client.event
async def on_ready():
	print('BOT connected.')
	await client.change_presence(status = discord.Status.online, activity = discord.Game('SimpleMinecraft.Ru'))

# /help
@client.command()
async def help(ctx, member = discord.Member):
	await ctx.message.channel.purge(limit = 1)
	emb = discord.Embed(title = '**Команды**', description = 'Эти команды доступны на сервере:', colour = 0xCC99FF)
	emb.add_field(name = '**/help**', value = 'Выводит сообщение, показывающее все команды на сервере. \nДоступна всем.', inline = False)
	emb.add_field(name = '**/av**', value = 'Выводит сообщение, показывающее аватарку участника. \nДоступна всем.', inline = False)
	emb.add_field(name = '**/vio**', value = 'Выводит специальное сообщение для <#765056351357370388>. \nДоступна всем.', inline = False)
	emb.add_field(name = '**/forum**', value = 'Выводит специальное сообщение для <#754421356078301290>. \nДоступна всем.', inline = False)
	emb.add_field(name = '**/leave**', value = 'Выводит специальное сообщение для <#754653288611315742>. \nДоступна всем.', inline = False)
	emb.add_field(name = '**/clear**', value = 'Удаляет указанное количество сообщений. \nДоступна администраторам.', inline = False)
	emb.add_field(name = '**/chatinf**', value = 'Специальные сообщения для каждого чата. \nДоступна администраторам.', inline = False)
	emb.add_field(name = '**/qq и /bb**', value = 'Уведомляет о новом модере или о том, что модер ушел соответственно. \nДоступна администраторам.', inline = False)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /clear
@client.command()
@commands.has_permissions(view_audit_log = True)
async def clear(ctx, amount : int, member = discord.Member):
	if amount == int('1'):
		deleted = await ctx.message.channel.purge(limit = amount + 1)
		emb = discord.Embed(title = '**Было удалено ' + str(amount) + ' сообщение!**', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
		time.sleep(3)
		await ctx.message.channel.purge(limit = 1)
	elif amount == int('2'):
		deleted = await ctx.message.channel.purge(limit = amount + 1)
		emb = discord.Embed(title = '**Было удалено ' + str(amount) + ' сообщения!**', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
		time.sleep(3)
		await ctx.message.channel.purge(limit = 1)
	elif amount == int('3'):
		deleted = await ctx.message.channel.purge(limit = amount + 1)
		emb = discord.Embed(title = '**Было удалено ' + str(amount) + ' сообщения!**', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
		time.sleep(3)
	elif amount == int('4'):
		deleted = await ctx.message.channel.purge(limit = amount + 1)
		emb = discord.Embed(title = '**Было удалено ' + str(amount) + ' сообщения!**', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
		time.sleep(3)
		await ctx.message.channel.purge(limit = 1)
	elif amount >= int('5'):
		deleted = await ctx.message.channel.purge(limit = amount + 1)
		emb = discord.Embed(title = '**Было удалено ' + str(amount) + ' сообщений!**', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
		time.sleep(3)
		await ctx.message.channel.purge(limit = 1)

# /av
@client.command()
async def av(ctx, *, member: discord.Member = None):
	await ctx.message.channel.purge(limit = 1)
	member = ctx.author if not member else member
	emb = discord.Embed(title = f'**Аватар пользователя {member.nick}**', colour = 0xCC99FF)
	emb.set_image(url = member.avatar_url)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /qq
@client.command()
@commands.has_permissions(view_audit_log = True)
async def qq(ctx, arg, member = discord.Member):
	await ctx.message.channel.purge(limit = 1)
	chat = '<#754421356275171482>'
	chat2 = '<#754421356275171483>'
	user = 'Приветствуем нового модератора ' + str(arg) + '.'
	emb = discord.Embed(title = '**Уведомление**', colour = 0xCC99FF)
	emb.add_field(name = user, value = 'Рекомендум заглянуть в ' + str(chat) + ' и ' + str(chat2) + ' .', inline = False)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /bb
@client.command()
@commands.has_permissions(view_audit_log = True)
async def bb(ctx, arg, member = discord.Member):
	await ctx.message.channel.purge(limit = 1)
	user = 'Наш состав покидает ' + str(arg) + '.'
	emb = discord.Embed(title = '**Уведомление**', colour = 0xCC99FF)
	emb.add_field(name = user, value = 'Может еще увидимся!', inline = False)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /vio
@client.command()
async def vio(ctx, x, y, z, rule, member = discord.Member):
	await ctx.message.channel.purge(limit = 1)
	emb = discord.Embed(title = '**Нарушение**', colour = 0xCC99FF)
	emb.add_field(name = '**Координаты: **', value = '/tppos ' + str(x) + ' ' + str(y) + ' ' + str(z), inline = False)
	emb.add_field(name = '**Правило: **', value = str(rule), inline = False)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /forum
@client.command()
async def forum(ctx, vid, time, reason, ssilka, member = discord.Member):
	await ctx.message.channel.purge(limit = 1)
	vidat = str('/') + str(vid) + ' ' + str(time) + ' ' + str(reason)
	emb = discord.Embed(title = '**Форум**', colour = 0xCC99FF)
	emb.add_field(name = '**Выдать:**', value = vidat, inline = False)
	emb.add_field(name = '**Ссылка:**', value = ssilka, inline = False)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /leave
@client.command()
async def leave(ctx, date, member = discord.Member):
	await ctx.message.channel.purge(limit = 1)
	emb = discord.Embed(title = '**Отгул/отпуск**', colour = 0xCC99FF)
	emb.add_field(name = '**Дни отсутствия:**', value = date, inline = False)
	emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
	await ctx.send(embed = emb)

# /chatinf
@client.command()
@commands.has_permissions(view_audit_log = True)
async def chatinf(ctx, arg, member = discord.Member):
	if arg == 'online':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Онлайн**', description = 'В этом канале Вы можете найти таблицу с онлайном и актуальный онлайн за неделю.', colour = 0xCC99FF)
		emb.add_field(name = '**Таблица:**', value = 'https://clck.ru/P6yBG', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'news':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Новости**', description = 'В этом канале Вы сможете мониторить последние новости нашего сервера и проекта.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'ivent':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Ивенты**', description = 'В этом канале Вы сможете найти всю информацию по проведению ивентов.', colour = 0xCC99FF)
		emb.add_field(name = '**Инструкция**', value = 'Инструкция по проведению:', inline = False)
		emb.add_field(name = '**Первое:**', value = 'За 20-25 минут пишем уведомление в <#282991046185451532>.', inline = False)
		emb.add_field(name = '**Пример:**', value = '/event Industrial Напоминаем, что через 20 минут будет проходить ивент "Гора"! Ждём всех желающих принять участие на /warp hill!', inline = False)
		emb.add_field(name = '**Второе:**', value = 'Информируем игроков на сервере через команду /say. Информируем за 10, 5, 3 и 1 минуту до ивента.', inline = False)
		emb.add_field(name = '**Пример:**', value = '/say Через 10 минут будет проходить ивент "Гора"! Ждём всех желающих принять участие на /warp hill!', inline = False)
		emb.add_field(name = '**Третье:**', value = 'Проверяем, все ли соблюдают правила ивента, указанные на информационной панельке (/whois; /invsee). Далее информируем игроков, что ивент начнется через 3, 2, 1 в локальном чате.', inline = False)
		emb.add_field(name = '**Пример:**', value = 'Ивент начинается через: \n3... \n2... \n1...', inline = False)
		emb.add_field(name = '**Четвертое:**', value = 'По мере того, как появляются победители ивента, объявляем их от имени сервера (команда /say), переводим им эконы (количество эконов за каждое место указано в лобби ивента), дублируем команду перевода эконов в глобальный чат.', inline = False)
		emb.add_field(name = '**Пример:**', value = '/say Первый раунд выигрывает KobraDM! Поздравляем! \n/money pay KobraDM 35000 \n!/money pay KobraDM 35000 \n/say Следующий раунд через минуту!', inline = False)
		emb.add_field(name = '**Пятое:**', value = 'После того, как объявили всех победителей, сообщите, что ивент окончен.', inline = False)
		emb.add_field(name = '**Пример:**', value = '/say Всем спасибо за участие, ивент окончен!', inline = False)
		emb.add_field(name = '**Шестое:**', value = ' Сразу после проведения ивента заходим в <#361435659988238336>. \nПишем /ivent и получаем инструкцию.', inline = False)
		emb.add_field(name = '**Пример:**', value = '/ivent Hill Bird,sun2night xb1tnatorV yarikDOTA Goodvise', inline = False)
		emb.add_field(name = '**Информация**', value = 'Полезная информация:', inline = False)
		emb.add_field(name = '**Модератор "проспал" свой ивент:**', value = 'Если модератор "проспал" свой ивент, то проведите ивент вместо него. Можете провести любой ивент, который хотят игроки.', inline = False)
		emb.add_field(name = '**Модератор не может провести свой ивент:**', value = 'Если модератор не может провести ивент, он должен договориться с другим модератором, чтобы тот провёл ивент вместо него.', inline = False)
		emb.add_field(name = '**Расписание:**', value = 'Ивенты должны быть проведены строго по расписанию, ибо на форуме есть тема, в которой есть расписание. \nТакже Вы можете найти расписание здесь - https://clck.ru/RLdf6', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'links':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Ссылки**', description = 'В этом Вы можете найти полезные ссылки:', colour = 0xCC99FF)
		emb.add_field(name = '**Руководство для модераторов:**', value = 'https://clck.ru/QpDsT', inline = False)
		emb.add_field(name = '**Утвержденные администрацией слова:**', value = 'https://clck.ru/MwP9u')
		emb.add_field(name = '**Список спорных выражений. \nИспользовать только для ознакомления, не является утвержденным администрацией документом:**', value = 'https://clck.ru/MzU7H', inline = False)
		emb.add_field(name = '**Таблица состава:**', value = 'https://clck.ru/P6yBG', inline = False)
		emb.add_field(name = '**Таблица с чисткой карты:**', value = 'https://clck.ru/R4y5J', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'cmdslm':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**LowModer:**', description = 'Команды, доступные LowModer\'ам:', colour = 0xCC99FF)	
		emb.add_field(name = '**/authkey**', value = 'Команда для авторизации на сервере.', inline = False)
		emb.add_field(name = '**/tpa**', value = 'Запрос на телепортацию к игроку.', inline = False)
		emb.add_field(name = '**/near**', value = 'Узнать кто рядом.', inline = False)
		emb.add_field(name = '**/tpahere**', value = 'Запрос на телепортацию игрока к себе.', inline = False)
		emb.add_field(name = '**/fly**', value = 'Полёт.', inline = False)
		emb.add_field(name = '**/god**', value = 'Бессмертие.', inline = False)
		emb.add_field(name = '**/feed**', value = 'Восполнение еды.', inline = False)
		emb.add_field(name = '**/heal**', value = 'Восполнение здоровья.', inline = False)
		emb.add_field(name = '**/c**', value = 'Написать в модераторский чат.', inline = False)
		emb.add_field(name = '**/kit**', value = 'Получить набор ресурсов.', inline = False)
		emb.add_field(name = '**/back**', value = 'Возвращает к предыдущей точке телепортации или смерти.', inline = False)
		emb.add_field(name = '**/warn**', value = 'Проверить, снять или выдать предупреждение.', inline = False)
		emb.add_field(name = '**/mute**', value = 'Выдать блокировку чата игроку.', inline = False)
		emb.add_field(name = '**/jail**', value = 'Посадить игрока в тюрьму.', inline = False)
		emb.add_field(name = '**/invsee**', value = 'Проверить инвентарь игрока.', inline = False)
		emb.add_field(name = '**/cban**', value = 'Проверить наличие блокировки.', inline = False)
		emb.add_field(name = '**/seen**', value = 'Посмотреть, когда заходил игрок и наличие мультиаккаунта через ip.', inline = False)
		emb.add_field(name = '**/whois**', value = 'Посмотреть всю информацию об игроке.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'cmdsm':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Moder:**', description = 'Команды, доступные Moder\'ам:', colour = 0xCC99FF)
		emb.add_field(name = '**Команды LowModer\'ов**', value = 'Все команды, доступные LowModer\'ам.', inline = False)
		emb.add_field(name = '**/hat**', value = 'Одеть предмет на голову.', inline = False)
		emb.add_field(name = '**/craft**', value = 'Открыть верстак.', inline = False)
		emb.add_field(name = '**/tban**', value = 'Выдать временную блокировку.', inline = False)
		emb.add_field(name = '**/pban**', value = 'Выдать вечную блокировку.', inline = False)
		emb.add_field(name = '**/unban**', value = 'Снять блокировку.', inline = False)
		emb.add_field(name = '**/lag или /mem**', value = 'Проверить TPS и аптаймна сервере..', inline = False)
		emb.add_field(name = '**/say**', value = 'Сообщение от лица сервера.', inline = False)
		emb.add_field(name = '**/endersee**', value = 'Посмотреть эндер-сундук игрока.', inline = False)
		emb.add_field(name = '**/speed**', value = 'Установить скорость полета/бега.', inline = False)
		emb.add_field(name = '**/tp**', value = 'Мгновенная телепортация к игроку.', inline = False)
		emb.add_field(name = '**/s**', value = 'Мгновенная телепортация игрока к себе.', inline = False)
		emb.add_field(name = '**/tppos**', value = 'Телепортироваться на координаты.', inline = False)
		emb.add_field(name = '**/setwarp**', value = 'Установить точку варпа.', inline = False)
		emb.add_field(name = '**/delwarp**', value = 'Удалить точку варпа.', inline = False)
		emb.add_field(name = '**/cban**', value = 'Проверить наличие блокировки.', inline = False)
		emb.add_field(name = '**/seen**', value = 'Посмотреть, когда заходил игрок и наличие мультиаккаунта через ip.', inline = False)
		emb.add_field(name = '**//drain**', value = 'Осушить ванильную жидкость.', inline = False)
		emb.add_field(name = '**//undo**', value = 'Отменить последнее действие.', inline = False)
		emb.add_field(name = '**/rg i**', value = 'Посмотреть информацию о регионе.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'cmdsdop':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Дополнительные права:**', description = 'Дополнительные права, выдающиеся старшим модератором:', colour = 0xCC99FF)
		emb.add_field(name = '**Команды LowModer\'ов и Moder\'ов**', value = 'Все команды, доступные LowModer\'ам и Moder\'ам.', inline = False)
		emb.add_field(name = '**/v**', value = 'Стать невидимым.', inline = False)
		emb.add_field(name = '**//set**', value = 'Заполнить выделенную территорию.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'cmdsinfo':
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команды**', description = 'В этом канале Вы сможете найти все доступные команды на сервере.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'help':
		await ctx.message.channel.purge(limit = 1)	
		emb = discord.Embed(title = '**Команды**', description = 'Аргументы для команды /chatinf:', colour = 0xCC99FF)
		emb.add_field(name = '**/chatinf online**', value = 'Специальное сообщение для чата <#754421356078301292>.', inline = False)
		emb.add_field(name = '**/chatinf news**', value = 'Специальное сообщение для чата <#754421356078301293>.', inline = False)
		emb.add_field(name = '**/chatinf ivent**', value = 'Специальные сообщения для чата <#754421356078301293>.', inline = False)
		emb.add_field(name = '**/chatinf cmds[lm/m/dop/info]**', value = 'Специальные сообщения для чата <#754421356275171482>.', inline = False)
		emb.add_field(name = '**/chatinf forum**', value = 'Специальное сообщение для чата <#754421356078301290>.', inline = False)
		emb.add_field(name = '**/chatinf vio**', value = 'Специальное сообщение для чата <#765056351357370388>.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'vio':
		await ctx.message.channel.purge(limit = 1)	
		emb = discord.Embed(title = '**Отгулы и отпуски**', description = 'В этом текстовом канале Вы можете отправлять нарушения, найденные в мире.', colour = 0xCC99FF)
		emb.add_field(name = '**Пример:**', value = '/vio -8949 66 10243 5.0')
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'forum':
		await ctx.message.channel.purge(limit = 1)	
		emb = discord.Embed(title = '**Форум**', description = 'В этом текстовом канале Вы можете найти нарушения, указанные на форуме.', colour = 0xCC99FF)
		emb.add_field(name = '**Пример:**', value = '/forum mute 30m 1.9 https://clck.ru/RZXtc')
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	elif arg == 'leave':
		await ctx.message.channel.purge(limit = 1)	
		emb = discord.Embed(title = '**Отгулы и отпуски**', description = 'В этом текстовом канале Вы можете отправлять дату отгула/отпуска.', colour = 0xCC99FF)
		emb.add_field(name = '**Пример:**', value = '/leave 24.10.2020-28.10.2020')
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

# errors
@client.event
async def on_command_error(ctx, error):
	pass

@chatinf.error
async def chatinf_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/chatinf help', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@leave.error
async def leave_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/leave [D]', colour = 0xCC99FF)
		emb.add_field(name = '**[D]:**', value = 'Даты отсутствия: 23.10.2020-27.10.2020, например.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@forum.error
async def forum_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/forum [V] [T] [R] [S]', colour = 0xCC99FF)
		emb.add_field(name = '**[V]:**', value = 'Вид наказания (mute, jail, tban или pban).', inline = False)
		emb.add_field(name = '**[T]:**', value = 'Время, на которое надо наказать игрока.', inline = False)
		emb.add_field(name = '**[R]:**', value = 'Причина, по которой мы наказываем игрока.', inline = False)
		emb.add_field(name = '**[S]:**', value = 'Ссылка на нарушение на форуме.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@vio.error
async def vio_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/vio [X] [Y] [Z] [R]', colour = 0xCC99FF)
		emb.add_field(name = '**[X]; [Y]; [Z]:**', value = 'Координаты, где находится нарушение.', inline = False)
		emb.add_field(name = '**[R]:**', value = 'Правило, нарушенное игроком.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@qq.error
async def qq_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/bb [M]', colour = 0xCC99FF)
		emb.add_field(name = '**[M]:**', value = 'Никнейм пользователя, которого Вы хотите поприветствовать.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@bb.error
async def bb_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/bb [M]', colour = 0xCC99FF)
		emb.add_field(name = '**[M]:**', value = 'Никнейм пользователя, с которым Вы хотите попрощаться.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@av.error
async def av_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/av [M]', colour = 0xCC99FF)
		emb.add_field(name = '**[M]:**', value = 'Упоминание участника, чью аватарку Вы хотите посмотреть.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

@clear.error
async def clear_error(ctx, error, member = discord.Member):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Недостаточно аргументов!**', description = '/clear [A]', colour = 0xCC99FF)
		emb.add_field(name = '**[A]:**', value = 'Количество сообщений, которое Вы хотите удалить.', inline = False)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**У Вас недостаточно прав!**', description = 'Вы не являетесь администратором.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.channel.purge(limit = 1)
		emb = discord.Embed(title = '**Команда не найдена!**', description = 'Проверьте, правильно ли Вы ввели команду.', colour = 0xCC99FF)
		emb.set_footer(text = f'{ctx.message.author.nick}', icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emb)

# token
token = os.environ.get('BOT_TOKEN')
client.run(str(token))

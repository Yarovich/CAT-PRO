# import
import asyncio
import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix=".")
client.remove_command('help')


@client.event
async def on_ready():
    print("CAT PRO Bot#0694 started.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Brawl Stars'))


# help
@client.command()
@commands.has_any_role('💚Помощник модератора', '💙Модератор', '💛HELPER', 'Мл.Админ', 'сам cat pro')
async def help(ctx):
    await ctx.send(
        f'**.help** - это сообщение\n'
        f'**.lol** - крутая команда\n'
        f'**.news** - новости о багах/фиксах/добавлениях чего-то нового\n'
        f'**.mute [участник] [время в минутах] [причина]** - мут участника\n'
        f'**.unmute [участник]** - размут участника\n'
        f'**.acter [участник]** - выдать роль актёр участнику\n')
    print('Used .help')


# lol
@client.command()
@commands.has_any_role('💚Помощник модератора', '💙Модератор', '💛HELPER', 'Мл.Админ', 'сам cat pro')  # РОЛЬ
async def lol(ctx):
    await ctx.send(f'https://youtu.be/dQw4w9WgXcQ')
    print('Used .lol')


@client.command()
@commands.has_any_role('💙Модератор', '💛HELPER', 'Мл.Админ', 'сам cat pro')  # РОЛЬ
async def news(ctx):
    await ctx.send(f'**-----01.05.22-----**\n'
                   f'Добавлен бот на cat pro.\n'
                   f'Обнаружен баг на выдачу мута самому себе и боту, баг будет пофикшен.\n'
                   f'Добавлена команда .news.\n')
    print('Used .news')


# mute
@client.command()
@commands.has_any_role('💙Модератор', '💛HELPER', 'Мл.Админ', 'сам cat pro')  # РОЛЬ
async def mute(ctx, user: discord.Member, time: int, *, reason='None'):
    role = discord.utils.get(ctx.message.guild.roles, name='мут')  # РОЛЬ
    await user.add_roles(role)
    await ctx.send(f'{user.mention} получил мут на {time} минут по причине: {reason}.')
    print('Used .mute')
    await asyncio.sleep(time * 60)
    await user.remove_roles(role)
    await ctx.send(f'{user.mention} больше не в муте.')


# unmute
@client.command()
@commands.has_any_role('💙Модератор', '💛HELPER', 'Мл.Админ', 'сам cat pro')  # РОЛЬ
async def unmute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name='мут')  # РОЛЬ
    await member.remove_roles(mute_role)
    await ctx.send(f'{member.mention} размучен.')
    print('Used .unmute')


# acter
@client.command()
@commands.has_any_role('💚Помощник модератора', '💙Модератор', '💛HELPER', 'Мл.Админ', 'сам cat pro')  # РОЛЬ
async def acter(ctx, member: discord.Member):
    # await ctx.channel.purge(limit=1)
    role = discord.utils.get(ctx.message.guild.roles, name='📷Актёр')  # РОЛЬ
    await member.add_roles(role)
    await ctx.send(f'Игрок {member.name} теперь Актёр!')
    print('Used .acter')


# errors
@client.event
async def on_command_error(ctx, error):
    pass


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, обязательно укажите аргумент!')
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send(f'{ctx.author.name}, у вас недостаточно прав!')


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, обязательно укажите аргумент!')
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send(f'{ctx.author.name}, у вас недостаточно прав!')

@acter.error
async def acter_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, обязательно укажите аргумент!')
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send(f'{ctx.author.name}, у вас недостаточно прав!')


client.run("OTY5MTY1ODg2MzQ0ODEwNTA2.YmpcEQ.nwWzVwo1CvtWsg3rQxd5MSRNizk")  # CAT PRO Bot

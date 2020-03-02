from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
   async def on_message(message):
    if message.author.id == 159985870458322944: # MEE6からのメッセージかどうかを判別
        if message.content.startswith("!levelup"):
            await message.delete() # メッセージを消去

            level = int(message.content.split()[-2]) # メッセージを分解
            t_name = message.content.split()[-1] # メッセージを分解
            target = discord.utils.get(message.server.members, mention=t_name) # レベルアップしたユーザーのIDを取得

            replys = f"{t_name}さん、が{str(level)}レべになりました。" # レベルアップメッセージ
            await message.channel.send(replys)

            if level == 1: # レベル1になった時の処理
                levelrole1 = discord.utils.get(message.server.roles, name="初心者")
                await target.add_roles(levelrole1)

            elif level == '5': # レベル5になった時の処理
                levelrole1 = discord.utils.get(message.server.roles, name="初心者")
                levelrole5 = discord.utils.get(message.server.roles, name="アマチュア")
                await target.add_roles(levelrole5)
                await target.remove_roles(levelrole1)

client.run(token) # Botのトークン


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)

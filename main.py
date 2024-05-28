import discord
import os 
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

# prefix for commands
# contoh : !help
intents = discord.Intents.default()
intents.typing = True
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
members = bot.get_all_members()

# event
@bot.event
async def on_ready():
    print('Bot is ready')

# command
# contoh : !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# command 
# command ini untuk menyapa user yang menggunakan command !hai-bot
@bot.command()
async def hai_bot(ctx):
    for member in members:
        if member.id == ctx.author.id:
            await ctx.send(f'Hai {member.mention}, ada yang bisa saya bantu?')
            break

# run bot
# pasang token bot 
bot.run(os.getenv('TOKEN'))

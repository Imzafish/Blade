import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.slash_command(
    name="buy",
    description="Buy a product"
)
async def buy(ctx):
    await ctx.send("Buy command executed")

bot.run('YOUR_BOT_TOKEN')


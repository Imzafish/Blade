import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True  # Enable message content intent

bot = commands.Bot(command_prefix='/', intents=intents)

bounties = {}  # Dictionary to store bounties

@bot.command(description='Accept a bounty')
async def bounty(ctx, name: str):
    # Handle bounty command here
    bounties[name] = True
    await ctx.send(f'Bounty accepted for {name}!')

@bot.command(description='Perform a task')
@commands.has_role('Blade')  # Only users with the role "Blade" can execute this command
async def task(ctx, name: str):
    # Perform the task here
    if name in bounties and bounties[name]:
        bounties[name] = False
        await ctx.send(f'Task finished, {name} is dead!')
    else:
        await ctx.send(f'{name} does not have an active bounty.')

@bot.command(description='List active bounties')
@commands.has_role('Blade')  # Only users with the role "Blade" can execute this command
async def bountylist(ctx):
    active_bounties = [name for name, status in bounties.items() if status]
    if active_bounties:
        await ctx.send(f'Active bounties: {", ".join(active_bounties)}')
    else:
        await ctx.send('No active bounties.')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run('MTA5NjQwNzQ4ODAxNTg5MjQ5MA.GYWdl5.SNshzvb9vy3Q9jQrD-_CiDHNQEAde1z2RkrwYY')

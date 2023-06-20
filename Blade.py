import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bounties = {}  # Dictionary to store bounties

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def bounty(ctx, name: str):
    # Handle bounty command here
    bounties[name] = True
    await ctx.send(f'Bounty accepted for {name}!')

@bot.command()
@commands.has_role('Blade')  # Only users with the role "Blade" can execute this command
async def task(ctx, name: str):
    # Perform the task here
    if name in bounties and bounties[name]:
        bounties[name] = False
        await ctx.send(f'Task finished, {name} is dead!')
    else:
        await ctx.send(f'{name} does not have an active bounty.')

@task.error
async def task_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the required role to execute this command.")

@bot.command()
@commands.has_role('Blade')  # Only users with the role "Blade" can execute this command
async def bountylist(ctx):
    active_bounties = [name for name, status in bounties.items() if status]
    if active_bounties:
        await ctx.send(f'Active bounties: {", ".join(active_bounties)}')
    else:
        await ctx.send('No active bounties.')

@bountylist.error
async def bountylist_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the required role to execute this command.")

bot.run('YOUR_BOT_TOKEN')


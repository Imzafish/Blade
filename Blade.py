import discord
import discord_slash
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType

# Create a new bot instance
bot = commands.Bot(command_prefix='/')  # Set the command prefix to '/'

# Create a new SlashCommand instance
slash = SlashCommand(bot, sync_commands=True)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

# Command: Buy a product
@slash.slash(
    name="buy",
    description="Buy a product",
    options=[
        {
            "name": "product",
            "description": "Product to buy",
            "type": SlashCommandOptionType.STRING,
            "required": True
        },
        {
            "name": "quantity",
            "description": "Quantity to buy",
            "type": SlashCommandOptionType.INTEGER,
            "required": True
        }
    ]
)
async def buy(ctx: SlashContext, product: str, quantity: int):
    # Replace this code with your desired implementation
    await ctx.send(f"You want to buy {quantity} {product}(s).")

# Run the bot
bot.run('YOUR_BOT_TOKEN')

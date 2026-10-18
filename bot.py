import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='simplify', help='Simplifies a question')
async def simplify(ctx, *, question: str):
    # Simplify the question logic here
    simplified_answer = f"Simplified answer for: {question}"
    await ctx.send(simplified_answer)

bot.run(TOKEN)
import discord
from discord.ext import commands
from Module.Translate.translate import TranslateCommand
from Module import Config
app = commands.Bot(command_prefix="!",intents=discord.Intents.default())


@app.event
async def on_ready():
    await app.add_cog(TranslateCommand(app=app))
    await app.tree.sync()
    print('Bot is ready')

app.run(Config.Discord.Token())
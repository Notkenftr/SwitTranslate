# MIT License
# Copyright (c) 2025 kenftr


import discord
import io
import os
import asyncio
from Module import Model
from Module.Translate.Utils import EmbedJson
from discord import app_commands
from discord.ext import commands
from Module.Translate.Utils import Config
from Module.cooldown import CoolDown
class TranslateCommand(commands.Cog):
    def __init__(self,app):
        self.app = app
    @app_commands.command(name=Config.TranslateCommand.Name(),
                          description=Config.TranslateCommand.Description())
    @app_commands.describe(translate_to=Config.TranslateCommand.Describe.Translate_to_description(),config_file=Config.TranslateCommand.Describe.Config_file_description())

    async def Translate(self,interaction: discord.Interaction,translate_to:str,config_file: discord.Attachment) -> None:
        await interaction.response.defer(thinking=True,ephemeral=True)

        if Config.TranslateCommand.Enabled() == False:
            await interaction.followup.send("This command is disabled.",ephemeral=True)
            return

        if "@everyone" not in Config.TranslateCommand.RolesAllowed():
            user_role_ids = [role.id for role in interaction.user.roles]

            has_role = any(int(role_id) in user_role_ids for role_id in Config.TranslateCommand.RolesAllowed())

            if not has_role:
                return

        if Config.TranslateCommand.UsersAllowed() is not None:
            if interaction.user.id not in Config.TranslateCommand.UsersAllowed():
                return

        cooldown = CoolDown.check(interaction.user.id)

        if cooldown == 1:
            await interaction.followup.send(
                'Please wait a moment before you can use it!',
                ephemeral=True
            )
            return

        elif cooldown == 2:
            CoolDown.remove(interaction.user.id)
            CoolDown.add(interaction.user.id)

        elif cooldown == 0:
            CoolDown.add(interaction.user.id)


        config_file_name, config_file_ext = os.path.splitext(config_file.filename)
        config_file = await config_file.read()

        config_file_data = config_file.decode('utf-8')

        Embed = EmbedJson.get('before_start_translate')

        EmbedStructure = discord.Embed(
            title=Embed['title'],
            description=Embed['description'],
            color=discord.Color.from_str(Embed['color'])
        )
        message = await interaction.followup.send(embed=EmbedStructure)
        model = Model(target=translate_to,
                      config_data=config_file_data)

        Embed = EmbedJson.get('after_start_translate')
        EmbedStructure = discord.Embed(
            title=Embed['title'],
            description=Embed['description'],
            color=discord.Color.from_str(Embed['color'])
        )
        await message.edit(embed=EmbedStructure)

        #Because waiting for the result takes around 20 seconds, it causes a heartbeat block, so I added this :3
        for i in range(3):
            EmbedStructure = discord.Embed(
                title=Embed['title'],
                description=Embed['description'] + '.'*i,
                color=discord.Color.from_str(Embed['color'])
            )
            await message.edit(embed=EmbedStructure)
            await asyncio.sleep(4)

        result = model.StartTranslate()
        file_name = f"{config_file_name}-translate{config_file_ext}"


        discord_file = discord.File(io.BytesIO(result.encode('utf-8')), filename=file_name)


        Embed = EmbedJson.get('after_translate')
        EmbedStructure = discord.Embed(
            title=Embed['title'],
            description=Embed['description'],
            color=discord.Color.from_str(Embed['color'])
        )
        await message.edit(embed=EmbedStructure)
        await interaction.followup.send(file=discord_file)




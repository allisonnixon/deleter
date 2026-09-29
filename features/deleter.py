"""Deletes the bot's own messages a fixed time after they are sent."""

import discord

from discord.ext import commands


class AutoDelete(commands.Cog):
    def __init__(self, bot: commands.Bot, delete_after: float) -> None:
        self.bot = bot
        self.delete_after = delete_after

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.id != self.bot.user.id:
            return

        # discord.py schedules the deletion in the background and
        # silently ignores it if the message is already gone.
        await message.delete(delay=self.delete_after)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutoDelete(bot, bot.config.delete_after))
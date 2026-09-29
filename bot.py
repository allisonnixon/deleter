from discord.ext import commands

import logging

from config import Config, load_config #type: ignore

FEATURES = ("features.deleter",)


class Bot(commands.Bot):
    def __init__(self, config: Config) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned,
            chunk_guilds_at_startup=False,
            guild_subscriptions=False,
        )
        self.config = config

    async def setup_hook(self) -> None:
        for extension in FEATURES:
            await self.load_extension(extension)

    async def on_ready(self) -> None:
        logging.info("Logged in as %s (%s)", self.user, self.user.id)


def main() -> None:
    config = load_config()
    Bot(config).run(config.token)


if __name__ == "__main__":
    main()
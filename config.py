"""Loads and validates configuration from the environment / .env file."""

from dataclasses import dataclass

from dotenv import load_dotenv

import os


@dataclass(frozen=True)
class Config:
    token: str
    delete_after: float = 60.0


def load_config() -> Config:
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set. Copy .env.example to .env and fill it in.")

    return Config(
        token=token,
        delete_after=float(os.getenv("DELETE_AFTER_SECONDS", Config.delete_after)),
    )